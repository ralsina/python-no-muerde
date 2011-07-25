# -*- coding: utf-8 -*-
'''Un acortador de URLs pero que permite:

* Editar adonde apunta el atajo más tarde
* Eliminar atajos
* Definir tests para saber si el atajo es válido

'''

# Usamos bottle para hacer el sitio
import bottle

@bottle.route('/')
def alta():
    """Crea un nuevo slug"""
    return "Pagina: /"

@bottle.route('/:slug/edit')
def editar(slug):
    """Edita un slug"""
    return "Editar el slug=%s"%slug

@bottle.route('/:slug/del')
def borrar(slug):
    """Elimina un slug"""
    return "Borrar el slug=%s"%slug

# Un slug está formado sólo por estos caracteres
@bottle.route('/:slug#[a-zA-Z0-9]+#')
def redir(slug):
    """Redirigir un slug"""
    return "Redirigir con slug=%s"%slug

@bottle.route('/static/:filename#.*#')
@bottle.route('/:filename#favicon.*#')
def static_file(filename):
    """Archivos estáticos (CSS etc)"""
    # No permitir volver para atras
    filename.replace("..",".")
    # bottle.static_file parece no funcionar en esta version de bottle
    return open(os.path.join("static", *filename.split("/")))

if __name__=='__main__':
    """Ejecutar con el server de debug de bottle"""
    bottle.debug(True)
    app = bottle.default_app()

    # Mostrar excepciones mientras desarrollamos
    app.catchall = False

    # Ejecutar aplicación
    bottle.run(app)
