# -*- coding: utf-8 -*-

import zope.interface

# Definiciones de interfaces


class IFieldType(zope.interface.Interface):

    """La definición de un tipo de campo."""

    name = zope.interface.Attribute("Nombre del tipo de campo")

    def set_value(v):
        """Almacenar valor "v" en la instancia del campo."""

    def get_value(v):
        """Obtener valor de la instancia del campo."""


class IElement(zope.interface.Interface):
    
    """Un elemento a almacenar, una tarea, etc."""
    
    def fields():
        """Una lista de los campos de este elemento."""

    def save():
        """Guarda este elemento en storage persistente."""

    def remove():
        """Elimina este elemento del storage."""

# Fin de definicion de interfaces