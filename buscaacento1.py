# -*- coding: utf-8 -*-
import re

def busca_acento(palabra):
    '''Dada una palabra (sin acento ortográfico),
    devuelve la posición de la vocal acentuada.

    Sabiendo que la palabra no tiene acento ortográfico,
    sólo puede ser grave o aguda. Y sólo es grave si termina
    en 'nsaeiou'.

    Ignorando diptongos, hay siempre una vocal por sílaba.
    Ergo, si termina en 'nsaeiou' es la penúltima vocal, si no,
    es la última.

    >>> busca_acento('casa')
    1

    >>> busca_acento('impresor')
    6
    
    '''

    if palabra[-1] in 'nsaeiou':
        # Palabra grave, acento en la penúltima vocal
        # Posición de la penúltima vocal:
        pos=list(re.finditer('[aeiou]',palabra))[-2].start()
    else:
        # Palabra aguda, acento en la última vocal
        # Posición de la última vocal:
        pos=list(re.finditer('[aeiou]',palabra))[-1].start()

    return pos