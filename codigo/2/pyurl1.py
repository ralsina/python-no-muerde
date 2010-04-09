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
    return "Borrar el slug=%s"%slug

@bottle.route('/:slug/del')
def borrar(slug):
    """Elimina un slug"""
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

    # Ejecutar aplicación
    bottle.run(app)
