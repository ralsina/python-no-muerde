# -*- coding: utf-8 -*-

import string

def es_numero(x):
    '''Verifica que x sea convertible a número'''
    s = str(x)
    for c in s:
        if c not in string.digits+'.'
            return False
        return True

s=raw_input()
if es_numero(s):
    print "El doble es ", float(s)*2
else:
    print "No es un numero"
