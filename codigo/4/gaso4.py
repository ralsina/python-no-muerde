# -*- coding: utf-8 -*-
import re
import unicodedata


def gas(letra):
    u"""Dada una letra X devuelve XgasX excepto si
    X es una vocal acentuada, en cuyo caso devuelve
    la primera X sin acento.

    El uso de normalize lo saqué de google.

    \xe1 y \\xe1 son "a con tilde", los doctests son
    un poco quisquillosos con los acentos.

    >>> gas(u'\xe1')
    u'agas\\xe1'

    >>> gas(u'a')
    u'agasa'
    """
    return u'%sgas%s' % (unicodedata.normalize('NFKD', letra).\
    encode('ASCII', 'ignore'), letra)


def gasear(palabra):
    u'''Dada una palabra, la convierte al rosarino

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

    if re.search(u'[\xe1\xe9\xed\xf3\xfa]', palabra):
        return re.sub(u'([\xe1\xe9\xed\xf3\xfa])',
            lambda x: gas(x.group(0)), palabra, 1)
    # No tiene acento ortográfico
    pos = busca_acento(palabra)
    return palabra[:pos] + gas(palabra[pos]) + palabra[pos + 1:]


def busca_acento(palabra):
    """Dada una palabra (sin acento ortográfico),
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
    """

    if palabra[-1] in 'nsaeiou':
        # Palabra grave, acento en la penúltima vocal
        # Posición de la penúltima vocal:
        pos = list(re.finditer('[aeiou]', palabra))[-2].start()
    else:
        # Palabra aguda, acento en la última vocal
        # Posición de la última vocal:
        pos = list(re.finditer('[aeiou]', palabra))[-1].start()
    return pos


# Test Suite

class TestBuscaAcento(object):

    """Test case de la función busca_acento.

    En este test case estamos agrupando los tests de esa función.
    """

    def test_grave(self):
        """Test de palabra grave."""
        resultado = busca_acento("casa")
        assert resultado == 1

    def test_aguda(self):
        """Test de palabra aguda."""
        resultado = busca_acento("impresor")
        assert resultado == 6


class TestGasear(object):

    """Test case de la función gasear.

    En este test case estamos agrupando los tests de esa función.
    """

    def test_acento_ortografico(self):
        """Test palabra con acento ortográfico."""
        assert gasear(u'c\xe1mara') == u'cagas\xe1mara'

    def test_grave_prosodico(self):
        """Test palabra grave con acento prosódico."""
        assert gasear(u'rosarino') == u'rosarigasino'
