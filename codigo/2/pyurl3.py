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

class Atajo(object):
    '''Representa una relación slug <=> URL
    
    Miembros:

    id   = Único, creciente, entero (primary key)
    url   = la URL original
    test  = un test de validez de la URL
    user  = el dueño del atajo
    '''

    # Hacer que los datos se guarden via Storm
    __storm_table__ = "atajo"
    id    = Int(primary=True)
    url   = Unicode()
    test  = Unicode()
    user  = Unicode()

    def __init__(self, url, user):
        '''Exigimos la URL y el usuario, test es opcional,
        _id es automático.'''
        
        self.url = url
        self.user = user

        # Autosave/flush/commit a la base de datos
        self.store.add(self)
        self.store.flush()
        self.store.commit()

    @classmethod
    def initDB(cls):
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
                    user VARCHAR
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
    def get(cls, slug = None, user = None):
        ''' Dado un slug, devuelve el atajo correspondiente.
        Dado un usuario, devuelve la lista de sus atajos
        '''
        
        if slug is not None:
            i = 0
            for p,l in enumerate(slug):
                i += 62 ** p * cls.validos.index(l)
            return cls.store.find(cls, id = i).one()
            
        if user is not None:
            return cls.store.find(cls, user = user)


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
def alta():
    """Crea un nuevo slug"""
    if not 'REMOTE_USER' in bottle.request.environ:
        bottle.abort(401, "Sorry, access denied.")
    return "Pagina: /"

@bottle.route('/:slug/edit')
def editar(slug):
    """Edita un slug"""
    if not 'REMOTE_USER' in bottle.request.environ:
        bottle.abort(401, "Sorry, access denied.")
    return "Borrar el slug=%s"%slug

@bottle.route('/:slug/del')
def borrar(slug):
    """Elimina un slug"""
    if not 'REMOTE_USER' in bottle.request.environ:
        bottle.abort(401, "Sorry, access denied.")
    return "Borrar el slug=%s"%slug

@bottle.route('/:slug')
def redir(slug):
    """Redirigir un slug"""
    return "Redirigir con slug=%s"%slug

@bottle.route('/static/:filename')
def static_file(filename):
    """Archivos estáticos (CSS etc)"""
    send_file(filename, root='./static/')



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

    # Ejecutar aplicación
    bottle.run(app)
