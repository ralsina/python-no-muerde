# -*- coding: utf-8 -*-
import re
import unicodedata
from buscaacento1 import busca_acento

def gas(letra):
    '''Dada una letra X devuelve XgasX excepto si X es una vocal acentuada,
    en cuyo caso devuelve la primera X sin acento.

    El uso de normalize lo saqué de google.

    \xe1 y \\xe1 son "a con tilde", los doctests son un poco
    quisquillosos con los acentos.

    >>> gas(u'\xe1')
    u'agas\\xe1'
    
    >>> gas(u'a')
    u'agasa'

    '''
    return u'%sgas%s'%(unicodedata.normalize('NFKD', letra).\
    encode('ASCII', 'ignore'), letra)


def gasear(palabra):
    '''Dada una palabra, la convierte al rosarino

    \xe1 y \\xe1 son "a con tilde", los doctests son un poco
    quisquillosos con los acentos.

    >>> gasear(u'c\xe1mara')
    u'cagas\\xe1mara'

    >>> gasear(u'rosarino')
    u'rosarigasino'

    '''

    # El caso obvio: acentos.
    # Lo resolvemos con una regexp

    # Uso \xe1 etc, porque así se puede copiar y pegar en un
    # archivo sin importar el encoding.
 
    if re.search(u'[\xe1\xe9\xed\xf3\xfa]',palabra):
        return re.sub(u'([\xe1\xe9\xed\xf3\xfa])',
            lambda x: gas(x.group(0)),palabra,1)
    # No tiene acento ortográfico
    pos = busca_acento(palabra)
    return palabra[:pos]+gas(palabra[pos])+palabra[pos+1:]

