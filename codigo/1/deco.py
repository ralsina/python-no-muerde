# -*- coding: utf-8 -*-

def memo(f):
    cache={}
    def memof(arg):
        if not arg in cache:
            cache[arg]=f(arg)
        return cache[arg]
    return memof
    
@memo
def factorial(n):
    print 'Calculando, n = ',n
    if n > 2:
        return n * factorial(n-1)
    else:
        return n

print factorial(4)
print factorial(4)
print factorial(5)
print factorial(3)
