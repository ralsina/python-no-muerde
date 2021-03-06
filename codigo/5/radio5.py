# -*- coding: utf-8 -*-

"""La interfaz de nuestra aplicación."""

import os,sys

# Importamos los módulos de Qt
from PyQt4 import QtCore, QtGui, uic

# Cargamos los iconos
import icons_rc

# JSON para guardar la lista de radios a disco
import json

# Soporte de sonido
from PyQt4.phonon import Phonon

# Parser de playlists
from plsparser import parse_pls

def _loadRadios(self):
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

    loadRadios = _loadRadios

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

    # XXX1
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
            self.radioList.setCurrentRow(curIdx)

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
        if curIdx > 0:
            self.radios=self.radios[:curIdx-1]+\
                [self.radios[curIdx], self.radios[curIdx-1]]+\
                self.radios[curIdx+1:]
            self.saveRadios()
            self.listRadios()
            self.radioList.setCurrentRow(curIdx-1)

    @QtCore.pyqtSlot()
    def on_down_clicked(self):
        "Baja la radio seleccionada una posicion."
        curIdx = self.radioList.currentRow()
        if curIdx < len(self.radios):
            self.radios=self.radios[:curIdx]+\
                [self.radios[curIdx+1], self.radios[curIdx]]+\
                self.radios[curIdx+2:]
            self.saveRadios()
            self.listRadios()
            self.radioList.setCurrentRow(curIdx+1)
    # XXX2

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

class TrayIcon(QtGui.QSystemTrayIcon):
    "Icono en area de notificación"

    loadRadios = _loadRadios
    
    def __init__(self):
        QtGui.QSystemTrayIcon.__init__ (self,
            QtGui.QIcon(":/antenna.svg"))

        ## Acciones del menú de botón derecho
        self.configAction = QtGui.QAction(
            QtGui.QIcon(":/configure.svg"),
            "&Configure...",self )
        self.aboutAction = QtGui.QAction(
            "&About...",self )
        self.quitAction = QtGui.QAction(
            QtGui.QIcon(":/exit.svg"),
            "&Quit",self )

        # Armamos el menú con las acciones
        self.rmbMenu=QtGui.QMenu()
        self.rmbMenu.addActions([
            self.configAction,
            self.aboutAction,
            self.quitAction
            ])
        # Ponemos este menú como menú de contexto
        self.setContextMenu(self.rmbMenu)

        # Conectamos las acciones
        self.configAction.triggered.connect(self.showConfig)
        self.aboutAction.triggered.connect(self.showAbout)
        self.quitAction.triggered.connect(
            QtCore.QCoreApplication.instance().quit)

        # XXX5
        # Conectamos el botón izquierdo
        self.activated.connect(self.activatedSlot)
        self.player = None

    def activatedSlot(self, reason):
        """El usuario activó este icono"""
        if reason == QtGui.QSystemTrayIcon.Trigger:
            # El menú del botón izquierdo
            self.stopAction=QtGui.QAction(
                QtGui.QIcon(":/stop.svg"),
                "&Turn Off Radio",self )

            self.lmbMenu=QtGui.QMenu()
            self.lmbMenu.addAction(self.stopAction)
            self.lmbMenu.addSeparator()

            self.loadRadios()
            self.radioActions = []
            for r in self.radios:
                receiver = lambda url=r[1]: self.playURL(url)
                self.lmbMenu.addAction(
                    r[0], receiver)

            # Mostramos el menú en la posición del cursor
            self.lmbMenu.exec_(QtGui.QCursor.pos())

    # XXX9
    def playURL(self, url):
        """Toma la URL de un playlist, y empieza a hacer ruido"""
        data = parse_pls(url)
        if data: # Tengo una URL
            # Sí, tomamos el primer stream y listo.
            url = data[0][1]

            self.player = Phonon.createPlayer(Phonon.MusicCategory,
                Phonon.MediaSource(url))
            self.player.play()
            
        else: # Pasó algo malo
            QtGui.QMessageBox.information(None,
                "Radio - Error reading playlist",
                "Sorry, error starting this radio.")
    # XXX10
    # XXX3
    @QtCore.pyqtSlot()
    def showConfig(self):
        "Muestra diálogo de configuración"
        self.confDlg = Main()
        self.confDlg.exec_()
    
    @QtCore.pyqtSlot()
    def showAbout(self):
        QtGui.QMessageBox.about(None, u"Radio",
            u"Example app from 'Python No Muerde'<br>"\
            u"© 2010 Roberto Alsina<br>"\
            u"More information: http://nomuerde.netmanagers.com.ar"
         )
    # XXX4

def main():
    app = QtGui.QApplication(sys.argv)
    # Como corre en tray, no debe salir cuando cierra
    # la última ventana.
    app.setQuitOnLastWindowClosed ( False )
    tray = TrayIcon()
    tray.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
    
