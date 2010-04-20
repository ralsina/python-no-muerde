# -*- coding: utf-8 -*-
import random

def logger(nombre):
    def wrapper(f):
        def f2(*args):
            print '===> Entrando a',nombre
            r=f(*args)
            print '<=== Saliendo de',nombre
            return r
        return f2
    return wrapper

@logger('F1')
def f1():
    print 'Estoy haciendo algo importante'

@logger('F2')
def f2():
    print 'Estoy haciendo algo no tan importante'

@logger('Master')
def f3():
    print 'Hago varias cosas'
    for f in range(1,5):
        random.choice([f1,f2])()

f3()