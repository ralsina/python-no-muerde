# -*- coding: utf-8 -*-

def selecciona_lineas(lineas, desde=0, hasta=-1):
    """Filtra el texto dejando sólo las lineas [desde:hasta].

    A diferencia de los iterables en python, no soporta índices
    negativos.
    """

    for i, l in enumerate(lineas):
        if desde <= i < hasta:
            yield(l)
