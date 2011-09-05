# -*- coding: utf-8 -*-

def selecciona_lineas(lineas, desde=0, hasta=-1):
    """Filtra el texto dejando sólo las lineas [desde:hasta].

    A diferencia de los iterables en python, no soporta índices
    negativos.

    >>> list(selecciona_lineas(range(10), 5, 10))
    [5, 6, 7, 8, 9]
    >>> list(selecciona_lineas(range(10), -5, 1))
    [0]
    >>> list(selecciona_lineas(range(10), 5, 100))
    [5, 6, 7, 8, 9]
    >>> list(selecciona_lineas(range(10), 5, -1))
    []
    """

    for i, l in enumerate(lineas):
        if desde <= i < hasta:
            yield(l)


def selecciona_columnas(lineas, desde=None, hasta=None):
    """Filtra el texto dejando sólo las columnas [desde:hasta].

    Soporta índices positivos y negativos con la misma semántica
    de los slices de python.

    >>> list(selecciona_columnas(("ornitorrinco",) * 5, 5, 10))
    ['orrin', 'orrin', 'orrin', 'orrin', 'orrin']
    >>> list(selecciona_columnas(("ornitorrinco",) * 5, 5, 99999))
    ['orrinco', 'orrinco', 'orrinco', 'orrinco', 'orrinco']
    """

    for l in lineas:
        yield(l[desde:hasta])


def selecciona_fragmento(lineas, fila1, fila2, col1, col2):
    """Filtra el texto dejando solo lo seleccionado.

    La selección es un "rectángulo" marcado por las filas
    y columnas especificadas.

    >>> datos = ("ornitorrinco",) * 10
    >>> list(selecciona_fragmento(datos, 0, 5, 5, 10))
    ['orrin', 'orrin', 'orrin', 'orrin', 'orrin']
    >>> list(selecciona_fragmento(datos, 0, 5, 0, None))
    ['ornitorrinco', 'ornitorrinco', 'ornitorrinco', 'ornitorrinco', 'ornitorrinco']
    """

    lineas = selecciona_lineas(lineas, fila1, fila2)
    resultado = selecciona_columnas(lineas, col1, col2)
    return resultado
