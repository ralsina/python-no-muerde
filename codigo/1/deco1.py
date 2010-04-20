# -*- coding: utf-8 -*-
import random

def f1():
    print 'Estoy haciendo algo importante'

def f2():
    print 'Estoy haciendo algo no tan importante'

def f3():
    print 'Hago varias cosas'
    for f in range(1,5):
        random.choice([f1,f2])()

f3()