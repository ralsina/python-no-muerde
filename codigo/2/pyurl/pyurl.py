# -*- coding: utf-8 -*-

'''Un 'acortador de URLs pero que permite:

* Editar adonde apunta el atajo más tarde
* Definir tests para saber si el atajo es válido

'''

# Usamos storm para almacenar los datos
from storm.locals import *

# Usamos bottle para hacer el sitio
from bottle import route, run, request, response, send_file, abort, view, debug, redirect, static_file

# Caracteres válidos en un atajo de URL
from string import letters, digits
validos = letters + digits

def id_to_slug(n):
    '''Dado un entero n, devuelve un "slug", un string
    con letras y números.

    Básicamente un contador devuelve el número
    codificado en base 62 usando a-zA-Z09 como dígitos, y
    dado vuelta (más significativo a la derecha)

    >>> id_to_slug(100000)
    '4aA'
    >>> id_to_slug(100001)
    '5aA'
    '''

    s = ''
    while n:
        s+=validos[n%62]
        n=n//62
    return s

def slug_to_id(slug):
    '''Dado un slug, devuelve un id entero.

    La recíproca de id_to_slug()
    
    >>> slug_to_id('4aA')
    100000
    
    '''

    i=0
    for p,l in enumerate(slug):
        i+=62**p*validos.index(l)
    return i

# Creamos una base SQLite
database = create_database("sqlite:///pyurl.sqlite")
store = Store (database)
try:
    # Creamos la tabla
    store.execute ('''
    CREATE TABLE atajo (
        id INTEGER PRIMARY KEY,
        url VARCHAR,
        test VARCHAR
    )
    '''
    )
except:
    pass

class Atajo(object):
    '''Un atajo de URL, que se almacena en una base
    de datos via storm.

    Miembros:

    id    = Único, creciente, entero (primary key)
    url   = la URL original
    test  = un test de validez de la URL
    '''

    __storm_table__ = "atajo"
    id    = Int(primary=True)
    url   = Unicode()
    test  = Unicode()

    def __init__(self, url):
        '''Exigimos la URL, lo demás es opcional.'''
        self.url = url
    
#Estático
@route('/css/:filename')
def static_file(filename):
    send_file(filename, root='./static/css/')

# Alta de URL
@route('/')
@view('add')
def alta():
    resp = {
        'baseurl':'http://127.0.0.1:8080/',
        'url':'',
        'short':'',
        }
    if 'url' in request.GET:
        u=request.GET['url']
        resp['url']=u
        atajo=Atajo(unicode(u))
        store.add(atajo)
        store.flush()
        resp['short']=id_to_slug(atajo.id)
        store.commit()
    return resp


#Redirigir
@route('/:slug')
def redir(slug):
    atajo=store.find(Atajo, id=slug_to_id(slug)).one()
    if atajo:
        redirect(atajo.url)
    else:
        redirect('/')



if __name__=='__main__':
    # Correr server de prueba
    debug(True)
    run(reloader=False, host='127.0.0.1', port=8080)
