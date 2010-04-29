# -*- coding: utf-8 -*-

"""La interfaz de nuestra aplicación."""

import os,sys

# Importamos los módulos de Qt
from PyQt4 import QtCore,QtGui

def main():
    app = QtGui.QApplication(sys.argv)
    window=Main()
    window.show()
    sys.exit(app.exec_())
    

if __name__ == "__main__":
    main()
    
