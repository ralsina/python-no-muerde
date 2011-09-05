#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def selecciona_lineas(lineas, desde=0, hasta=sys.maxint):
    u"""Filtra el texto dejando sólo las lineas [desde:hasta].

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
    u"""Filtra el texto dejando sólo las columnas [desde:hasta].

    Soporta índices positivos y negativos con la misma semántica
    de los slices de python.

    >>> list(selecciona_columnas(("ornitorrinco",) * 5, 5, 10))
    ['orrin', 'orrin', 'orrin', 'orrin', 'orrin']
    >>> list(selecciona_columnas(("ornitorrinco",) * 5, 5, 99999))
    ['orrinco', 'orrinco', 'orrinco', 'orrinco', 'orrinco']
    """

    for l in lineas:
        yield(l[desde:hasta])


def selecciona_fragmento(lineas, fila1=0, fila2=sys.maxint, col1=None, col2=None):
    u"""Filtra el texto dejando solo lo seleccionado.

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

def procesa_archivo(archivo, fila1=0, fila2=sys.maxint, col1=None, col2=None):
    u"""Abre un archivo y lo corta según se pida."""

    selecciona_fragmento(open(archivo), fila1, fila2, col1, col2)


if __name__ == "__main__":
   import commandline
   commandline.run_as_main(procesa_archivo)   