#!/usr/bin/python3
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from ServerDialog import *
from ServerClass import *
from ServerFileParser import *

class GameCentralServer(QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.server = ServerClass()
        self.server_file_parser = ServerFileParser()
        self.server_filename = None
        self.initUI()

    def initUI(self):
        self.setGeometry(200, 200, 500, 400)
        self.statusBar()
        self.menubar = self.menuBar()
#--------------------------------------------------------------
        self.newAction = QAction('&New Server', self)
        self.newAction.setShortcut('Ctrl+N')
        self.newAction.setStatusTip('Create a new server')
        self.newAction.triggered.connect(self.newServer)

        self.loadAction = QAction('&Load Server', self)
        self.loadAction.setShortcut('Ctrl+L')
        self.loadAction.setStatusTip('Load an existing server')
        self.loadAction.triggered.connect(self.loadServer)

        self.saveAction = QAction('&Save Server', self)
        self.saveAction.setShortcut('Ctrl+S')
        self.saveAction.setStatusTip('Save current server')
        self.saveAction.triggered.connect(self.saveServer)
        self.saveAction.setEnabled(False)

        self.saveAsAction = QAction('Save Server &As', self)
        self.saveAsAction.setShortcut('Ctrl+A')
        self.saveAsAction.setStatusTip('Save server as new filename')
        self.saveAsAction.triggered.connect(self.saveAsServer)
        self.saveAsAction.setEnabled(False)

        self.closeAction = QAction('&Close Server', self)
        self.closeAction.setShortcut('Ctrl+C')
        self.closeAction.setStatusTip('Close current server')
        self.closeAction.triggered.connect(self.closeServer)
        self.closeAction.setEnabled(False)

        self.startServerAction = QAction('Start Server', self)
        self.startServerAction.setShortcut('Ctrl+B')
        self.startServerAction.setStatusTip('Start Current Server')
        self.startServerAction.triggered.connect(self.startServer)
        self.startServerAction.setEnabled(False)

        self.stopServerAction = QAction('S&top Server', self)
        self.stopServerAction.setShortcut('Ctrl+T')
        self.stopServerAction.setStatusTip('Stop Current Server')
        self.stopServerAction.triggered.connect(self.stopServer)
        self.stopServerAction.setEnabled(False)

        self.exitAction = QAction('&Exit', self)
        self.exitAction.setShortcut('Ctrl+Q')
        self.exitAction.setStatusTip('Exit application')
        self.exitAction.triggered.connect(qApp.quit)

        self.fileMenu = self.menubar.addMenu('&File')
        self.fileMenu.addAction(self.newAction)
        self.fileMenu.addAction(self.loadAction)
        self.fileMenu.addAction(self.saveAction)
        self.fileMenu.addAction(self.saveAsAction)
        self.fileMenu.addAction(self.closeAction)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.startServerAction)
        self.fileMenu.addAction(self.stopServerAction)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.exitAction)
#--------------------------------------------------------------
        self.editServerAction = QAction('&Edit Server', self)
        self.editServerAction.setShortcut('Ctrl+E')
        self.editServerAction.setStatusTip('Edit Current Server Configuration')
        self.editServerAction.triggered.connect(self.modifyServer)
        self.editServerAction.setEnabled(False)

        self.editMenu = self.menubar.addMenu('Edit')
        self.editMenu.addAction(self.editServerAction)
#--------------------------------------------------------------
        self.aboutAction = QAction('&About', self)
        self.aboutAction.setShortcut('?')
        self.aboutAction.setStatusTip('About Game Central Server')
        self.aboutAction.triggered.connect(self.about)

        self.helpMenu = self.menubar.addMenu('&Help')
        self.helpMenu.addAction(self.aboutAction)
#--------------------------------------------------------------
        self.setWindowTitle('Game Central Server')
        self.show()
#--------------------------------------------------------------

    def newServer(self):
        print("New Server")
        dlg = ServerDialog()
        self.server = ServerClass()
        dlg.set_server_info(self.server)
        if dlg.exec_():
            self.server = dlg.get_server_info()
            self.server.set_is_configured_from_string("True")
            self.saveAction.setEnabled(True)
            self.saveAsAction.setEnabled(True)
            self.closeAction.setEnabled(True)
            self.editServerAction.setEnabled(True)
            self.startServerAction.setEnabled(True)

    def loadServer(self):
        print("Load Server")
        self.server_filename = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\',filter=("Server file (*.xml);;Any file (*.*)"))
        if self.server_filename[0] != '':
            self.server = self.server_file_parser.loadServer(self.server_filename[0])
            self.saveAction.setEnabled(True)
            self.saveAsAction.setEnabled(True)
            self.closeAction.setEnabled(True)
            self.editServerAction.setEnabled(True)
            self.startServerAction.setEnabled(True)

    def saveServer(self):
        print("Save Server")

    def saveAsServer(self):
        print("Save As Server")

    def closeServer(self):
        print("Close Server")
        self.server.reset()
        self.editServerAction.setEnabled(False)
        self.saveAction.setEnabled(False)
        self.saveAsAction.setEnabled(False)
        self.closeAction.setEnabled(False)
        self.startServerAction.setEnabled(False)
        self.stopServerAction.setEnabled(False)

    def startServer(self):
        print("Start Server")
        self.editServerAction.setEnabled(False)
        self.startServerAction.setEnabled(False)
        self.stopServerAction.setEnabled(True)

    def stopServer(self):
        print("Stop Server")
        self.editServerAction.setEnabled(True)
        self.startServerAction.setEnabled(True)
        self.stopServerAction.setEnabled(False)

    def modifyServer(self):
        dlg = ServerDialog()
        dlg.set_server_info(self.server)
        if dlg.exec_():
            self.server = dlg.get_server_info()

    def about(self):
        QMessageBox.about(self, 'About',
                    'Game Central Server - version 0.01\n'
                    '\n'
                    'Copyright(c) 2020 - Mike Briggs')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GameCentralServer()
    sys.exit(app.exec_())