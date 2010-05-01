# -*- coding: utf-8 -*-

"""La interfaz de nuestra aplicación."""

import os,sys

# Importamos los módulos de Qt
from PyQt4 import QtCore, QtGui, uic

# Cargamos los iconos
import icons_rc

# JSON para guardar la lista de radios a disco
import json

class Main(QtGui.QDialog):
    """La ventana principal de la aplicación."""
    def __init__(self):
        QtGui.QDialog.__init__(self)
        
        # Cargamos la interfaz desde el archivo .ui
        uifile = os.path.join(
            os.path.abspath(
                os.path.dirname(__file__)),'radio.ui')
        uic.loadUi(uifile, self)

        self.loadRadios()
        self.listRadios()

    def loadRadios(self):
        "Carga la lista de radios de disco"
        try:
            f = open(os.path.expanduser('~/.radios'))
            data = f.read()
            f.close()
            self.radios = json.loads(data)
        except:
            self.radios = []

        if self.radios is None:
            # El archivo estaba vacío
            self.radios = []

    def saveRadios(self):
        "Guarda las radios a disco"
        f = open(os.path.expanduser('~/.radios'),'w')
        f.write(json.dumps(self.radios))
        f.close()

    def listRadios(self):
        "Muestra las radios en la lista"
        self.radioList.clear()
        for nombre,url in self.radios:
            self.radioList.addItem(nombre)

    @QtCore.pyqtSlot()
    def on_add_clicked(self):
        addDlg = AddRadio(self)
        r = addDlg.exec_()
        if r: # O sea, apretaron "Add"
            self.radios.append ((unicode(addDlg.name.text()),
                                 unicode(addDlg.url.text())))
            self.saveRadios()
            self.listRadios()
            
    @QtCore.pyqtSlot()
    def on_edit_clicked(self):
        "Edita la radio actualmente seleccionada"
        curIdx = self.radioList.currentRow()
        name, url = self.radios[curIdx]
        editDlg = EditRadio(self)
        editDlg.name.setText(name)
        editDlg.url.setText(url)
        r = editDlg.exec_()
        if r: # O sea, apretaron "Save"
            self.radios[curIdx]= [unicode(editDlg.name.text()),
                                 unicode(editDlg.url.text())]
            self.saveRadios()
            self.listRadios()

    @QtCore.pyqtSlot()
    def on_remove_clicked(self):
        "Borra la radio actualmente seleccionada"
        curIdx = self.radioList.currentRow()
        del (self.radios[curIdx])
        self.saveRadios()
        self.listRadios()
        
    @QtCore.pyqtSlot()
    def on_up_clicked(self):
        "Sube la radio seleccionada una posicion."
        curIdx = self.radioList.currentRow()
        self.saveRadios()
        self.listRadios()

    @QtCore.pyqtSlot()
    def on_down_clicked(self):
        "Baja la radio seleccionada una posicion."
        curIdx = self.radioList.currentRow()
        self.saveRadios()
        self.listRadios()

class AddRadio(QtGui.QDialog):
    """El diálogo de agregar una radio"""
    def __init__(self, parent):
        QtGui.QDialog.__init__(self, parent)

        # Cargamos la interfaz desde el archivo .ui
        uifile = os.path.join(
            os.path.abspath(
                os.path.dirname(__file__)),'addradio.ui')
        uic.loadUi(uifile, self)

class EditRadio(AddRadio):
    """El diálogo de editar una radio.
    Es exactamente igual a AddRadio, excepto
    que cambia el texto de un botón."""
    def __init__(self, parent):
        AddRadio.__init__(self, parent)
        self.addButton.setText("&Save")


def main():
    app = QtGui.QApplication(sys.argv)
    window=Main()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
    
