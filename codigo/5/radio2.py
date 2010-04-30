# -*- coding: utf-8 -*-

"""La interfaz de nuestra aplicación."""

import os,sys

# Importamos los módulos de Qt
from PyQt4 import QtCore, QtGui, uic

# Cargamos los iconos
import icons_rc

class Main(QtGui.QDialog):
    """La ventana principal de la aplicación."""
    def __init__(self):
        QtGui.QDialog.__init__(self)
        
        # Cargamos la interfaz desde el archivo .ui
        uifile = os.path.join(
            os.path.abspath(
                os.path.dirname(__file__)),'radio.ui')
        uic.loadUi(uifile, self)


class AddRadio(QtGui.QDialog):
    """El diálogo de agregar una radio"""
    def __init__(self, parent):
        QtGui.QDialog.__init__(self, parent)

        # Cargamos la interfaz desde el archivo .ui
        uifile = os.path.join(
            os.path.abspath(
                os.path.dirname(__file__)),'addradio.ui')
        uic.loadUi(uifile, self)


def main():
    app = QtGui.QApplication(sys.argv)
    window=Main()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
    
