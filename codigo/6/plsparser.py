# -*- coding: utf-8 -*-

"""Módulo de parsing de playlists PLS."""

import urllib
from ConfigParser import RawConfigParser

def parse_pls(url):
    u"""
    Dada una URL, baja el contenido, y devuelve una lista de [título,url]
    obtenida del PLS al que la URL apunta.

    Devuelve [] si el archivo no se puede parsear o si hubo
    cualquier problema.

    >>> parse_pls('http://207.200.96.225:8020/listen.pls')
    [['', 'http://207.200.96.225:8020/']]

    """
    try:
        # Si es un stream directo, entonces lo devolvemos
        # sin parsear.
        
        if url[-4].lower() in ['.ogg','.mp3']:
            return [['',url]]

        # Si no, suponemos que es un .pls
        parser = RawConfigParser()
        parser.readfp(urllib.urlopen(url))

        # Hacemos las cosas de acuerdo a la descripción de Wikipedia:
        # http://en.wikipedia.org/wiki/PLS_(file_format)

        if not parser.has_section('playlist'):
            return []
        if not parser.has_option('playlist', 'NumberOfEntries'):
            return []

        result=[]
        for i in range(1, parser.getint('playlist', 'NumberOfEntries')+1):

            if parser.has_option('playlist', 'Title%s'%i):
                title=parser.get('playlist', 'Title%s'%i)
            else:
                title=''
            result.append([
                    title,
                    parser.get('playlist', 'File%s'%i)
                    ])
        return result
    except:
        # FIXME: reportar el error en log
        return []