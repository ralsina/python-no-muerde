# -*- coding: utf-8 -*-

import urllib

def largo_de_pagina(url):
    '''Dada una URL, devuelve el número de caracteres que la página tiene.
    Basado en código de Paul Prescod:
    http://code.activestate.com/recipes/65127-count-tags-in-a-document/

    Como las páginas cambian su contenido periódicamente,
    usamos mock para simular el acceso a Internet en el test.

    >>> from minimock import Mock, mock
    
    Creamos un falso URLOpener
    
    >>> opener = Mock ('opener')
    
    Creamos un falso archivo

    >>> _file = Mock ('file')

    El metodo open del URLopener devuelve un falso archivo

    >>> opener.open = Mock('open', returns = _file)

    urllib.URLopener devuelve un falso URLopener

    >>> mock('urllib.URLopener', returns = opener)

    El falso archivo devuelve lo que yo quiero:
    
    >>> _file.read = Mock('read', returns = '<h1>Hola mundo!</h1>')
    
    >>> largo_de_pagina ('http://www.netmanagers.com.ar')
    Called urllib.URLopener()
    Called open('http://www.netmanagers.com.ar')
    Called read()
    20
    '''

    return len(urllib.URLopener().open(url).read())
