# -*- coding: utf-8 -*-

import urllib

def largo_de_pagina(url):
    '''Dada una URL, devuelve el número de caracteres que la página tiene.
    Basado en código de Paul Prescod:
    http://code.activestate.com/recipes/65127-count-tags-in-a-document/
    '''

    return len(urllib.URLopener().open(url).read())

from mock import Mock, patch

def test_largo_de_pagina():
    """Test usando mock, para no requerir internet."""

    # Este "with" crea un bloque en el cual urllib.URLopener
    # es reemplazado con un objeto Mock.
    with patch('urllib.URLopener') as mock:
        # En Mock, todos los atributos de un Mock
        # son Mock. Y todos los Mock son "llamables" como funciones que
        # devuelven su propio return_value. Entonces solo necesito
        # especificar el resultado de la última de la cadena
        url = 'http://www.netmanagers.com.ar'
        mock.return_value.open.return_value.read.return_value = '<h1>Hola mundo!</h1>'
        l = largo_de_pagina(url)
        assert l == 20
        # Se debería haber llamado una vez, sin argumentos
        mock.assert_called_once_with()
        # Se llama una vez, con la URL
        mock.return_value.open.assert_called_once_with(url)
        # Se llama una vez, sin argumentos
        mock.return_value.open.return_value.read.assert_called_once_with()
