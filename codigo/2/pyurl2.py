# -*- coding: utf-8 -*-
'''Un acortador de URLs pero que permite:

* Editar adonde apunta el atajo más tarde
* Eliminar atajos
* Definir tests para saber si el atajo es válido

'''

import os

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
    return "Editar el slug=%s"%slug

@bottle.route('/:slug/del')
def borrar(slug):
    """Elimina un slug"""
    if not 'REMOTE_USER' in bottle.request.environ:
        bottle.abort(401, "Sorry, access denied.")
    return "Borrar el slug=%s"%slug

# Un slug está formado sólo por estos caracteres
@bottle.route('/:slug#[a-zA-Z0-9]+#')
def redir(slug):
    """Redirigir un slug"""
    # Buscamos el atajo correspondiente
    a = Atajo.get(slug=slug)
    if not a:
        bottle.abort(404, 'El atajo no existe')
    bottle.redirect(a.url)

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

    app = middleware(app,
                 enable=True,
                 setup_method='openid',
                 openid_store_type='file',
                 openid_store_config=os.getcwd(),
                 openid_path_signedin='/')

    app = AuthTKTMiddleware(SessionMiddleware(app),
                        'some auth ticket secret');

    # Ejecutar aplicación
    bottle.run(app)
