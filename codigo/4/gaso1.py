# -*- coding: utf-8 -*-
import re
import unicodedata

def gas(letra):
    u'''Dada una letra X devuelve XgasX excepto si X es una vocal acentuada,
    en cuyo caso devuelve la primera X sin acento.

    El uso de normalize lo saqué de google.
    '''
    return u'%sgas%s'%(unicodedata.normalize('NFKD', letra).\
    encode('ASCII', 'ignore'), letra)


def gasear(palabra):
    u'''Dada una palabra, la convierte al rosarino'''

    # El caso obvio: acentos.
    # Lo resolvemos con una regexp

    # Uso \xe1 etc, porque así se puede copiar y pegar en un
    # archivo sin importar el encoding.

    if re.search(u'[\xe1\xe9\xed\xf3\xfa]',palabra):
        return re.sub(u'([\xe1\xe9\xed\xf3\xfa])',
            lambda x: gas(x.group(0)),palabra,1)
    return palabra

