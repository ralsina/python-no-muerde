# -*- coding: utf-8 -*-
'''Un acortador de URLs pero que permite:

* Editar adonde apunta el atajo más tarde
* Eliminar atajos
* Definir tests para saber si el atajo es válido

'''

import os

import string

# Usamos storm para almacenar los datos
from storm.locals import *

# FIXME: tengo que hacer más consistentes los nombres
# de los métodos.

class Atajo(object):
    '''Representa una relación slug <=> URL
    
    Miembros:

    id     = Único, creciente, entero (primary key)
    url    = la URL original
    test   = un test de validez de la URL
    user   = el dueño del atajo
    activo = Si este atajo está activo o no.
             Nunca hay que borrarlos, sino el ID puede volver
             atrás y se "recicla" una URL. ¡Malo, malo, malo!
    '''

    # Hacer que los datos se guarden via Storm
    __storm_table__ = "atajo"
    id     = Int(primary=True)
    url    = Unicode()
    test   = Unicode()
    user   = Unicode()
    activo = Bool()

    def __init__(self, url, user):
        '''Exigimos la URL y el usuario, test es opcional,
        _id es automático.'''

        # Hace falta crear esto?
        r = self.store.find(Atajo, user = user, url = url) 
        self.url = url
        self.user = user
        self.activo = True
        if r.count():
            # FIXME: esto creo que es una race condition
            # Existe la misma URL para el mismo usuario,
            # reciclamos el id y el test, pero activa.
            viejo = r.one()
            Atajo.store.remove(viejo)
            self.id = viejo.id
            self.test = viejo.test
        self.store.add(self)
        # Autosave/flush/commit a la base de datos
        self.save()

    def save(self):
        '''Método de conveniencia'''
        Atajo.store.flush()
        Atajo.store.commit()

    @classmethod
    def init_db(cls):
        # Creamos una base SQLite
        if not os.path.exists('pyurl.sqlite'):
            cls.database = create_database("sqlite:///pyurl.sqlite")
            cls.store = Store (cls.database)
            try:
                # Creamos la tabla
                cls.store.execute ('''
                CREATE TABLE atajo (
                    id INTEGER PRIMARY KEY,
                    url VARCHAR,
                    test VARCHAR,
                    user VARCHAR,
                    activo TINYINT
                ) ''' )
            except:
                pass
        else:
            cls.database = create_database("sqlite:///pyurl.sqlite")
            cls.store = Store (cls.database)

    # Caracteres válidos en un atajo de URL
    validos = string.letters + string.digits

    def slug(self):
        '''Devuelve el slug correspondiente al
        ID de este atajo

        Básicamente un slug es un número en base 62, representado usando
        a-zA-Z0-9 como "dígitos", y dado vuelta (más significativo
        a la derecha.

        >>> Atajo.slug(100000)
        '4aA'
        >>> Atajo.slug(100001)
        '5aA'

        '''
        s = ''
        n = self.id
        while n:
            s += self.validos[n%62]
            n = n // 62
        return s

    @classmethod
    # FIXME: no estoy feliz con esta API
    def get(cls, slug = None, user = None, url = None):
        ''' Dado un slug, devuelve el atajo correspondiente.
        Dado un usuario:
            Si url es None, devuelve la lista de sus atajos
            Si url no es None , devuelve *ese* atajo
        '''
        
        if slug is not None:
            i = 0
            for p,l in enumerate(slug):
                i += 62 ** p * cls.validos.index(l)
            return cls.store.find(cls, id = i, activo = True).one()
            
        if user is not None:
            if url is None:
                return cls.store.find(cls, user = user, activo = True)
            else:
                return cls.store.find(cls, user = user,
                    url = url, activo = True).one()

    def delete(self):
        '''Eliminar este objeto de la base de datos'''
        self.activo=False
        self.save()

# Usamos bottle para hacer el sitio
import bottle

# Middlewares
from beaker.middleware import SessionMiddleware
from authkit.authenticate import middleware
from paste.auth.auth_tkt import AuthTKTMiddleware

@bottle.route('/logout')
def logout():
    bottle.request.environ['paste.auth_tkt.logout_user']()
    if 'REMOTE_USER' in bottle.request.environ:
        del bottle.request.environ['REMOTE_USER']
    bottle.redirect('/')

@bottle.route('/')
@bottle.view('usuario.tpl')
def alta():
    """Crea un nuevo slug"""

    # Requerimos que el usuario esté autenticado.
    if not 'REMOTE_USER' in bottle.request.environ:
        bottle.abort(401, "Sorry, access denied.")
    usuario = bottle.request.environ['REMOTE_USER'].decode('utf8')

    # Data va a contener todo lo que el template
    # requiere para hacer la página
    data ={}

    # Esto probablemente debería obtenerse de una
    # configuración
    data['baseurl'] = 'http://localhost:8080/'

    # Si tenemos un parámetro URL, estamos en esta
    # funcion porque el usuario envió una URL a acortar.
    
    if 'url' in bottle.request.GET:
        # La acortamos
        url = bottle.request.GET['url'].decode('utf8')
        a = Atajo(url=url, user=usuario)    
        data['short'] = a.slug()
        data['url'] = url

        # Mensaje para el usuario de que el acortamiento
        # tuvo éxito.
        data['mensaje'] = u'''La URL <a href="%(url)s">%(url)s</a>
        se convirtió en:
        <a href="%(baseurl)s%(short)s">%(baseurl)s%(short)s</a>'''%data

        # Clase CSS que muestra las cosas como buenas
        data['clasemensaje']='success'
    else:
        # No se acortó nada, no hay nada para mostrar.
        data['url']=None
        data['short']=None
        data['mensaje']=None

    # Lista de atajos, usuario.
    data ['atajos'] = Atajo.get (user = usuario)

    # Crear la página con esos datos.
    return data

@bottle.route('/:slug/edit')
@bottle.view('atajo.tpl')
def editar(slug):
    """Edita un slug"""
    if not 'REMOTE_USER' in bottle.request.environ:
        bottle.abort(401, "Sorry, access denied.")
    return "Editar el slug=%s"%slug

@bottle.route('/:slug/del')
def borrar(slug):
    """Elimina un slug"""
    if not 'REMOTE_USER' in bottle.request.environ:
        bottle.abort(401, "Sorry, access denied.")
    usuario = bottle.request.environ['REMOTE_USER'].decode('utf8')
    
    # Solo el dueño de un atajo puede borrarlo
    a = Atajo.get(slug)
    if a.user == usuario:
        a.delete()
    # FIXME: pasar un mensaje en la sesión
    bottle.redirect('/')

@bottle.route('/:slug')
def redir(slug):
    """Redirigir un slug"""
    return "Redirigir con slug=%s"%slug

@bottle.route('/static/:filename')
def static_file(filename):
    """Archivos estáticos (CSS etc)"""
    bottle.send_file(filename, root='./static/')



if __name__=='__main__':
    """Ejecutar con el server de debug de bottle"""
    bottle.debug(True)
    app = bottle.default_app()

    # Mostrar excepciones mientras desarrollamos
    app.catchall = False

    app = middleware(app,
                 enable=True,
                 setup_method='openid',
                 openid_store_type='file',
                 openid_store_config=os.getcwd(),
                 openid_path_signedin='/private')

    app = AuthTKTMiddleware(SessionMiddleware(app),
                        'some auth ticket secret');

    # Inicializar DB
    Atajo.init_db()

    # Ejecutar aplicación
    bottle.run(app)
