import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class GameCentralServer(QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setGeometry(200, 200, 500, 200)
        self.statusBar()
        menubar = self.menuBar()
#--------------------------------------------------------------
        newAction = QAction('&New', self)
        newAction.setShortcut('Ctrl+N')
        newAction.setStatusTip('Create a new server')
        newAction.triggered.connect(self.newServer)

        loadAction = QAction('&Load', self)
        loadAction.setShortcut('Ctrl+L')
        loadAction.setStatusTip('Load an existing server')
        loadAction.triggered.connect(self.loadServer)

        exitAction = QAction('&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(newAction)
        fileMenu.addAction(loadAction)
        fileMenu.addSeparator()
        fileMenu.addAction(exitAction)
#--------------------------------------------------------------
        startServerAction = QAction('&Start Server', self)
        startServerAction.setShortcut('Ctrl+S')
        startServerAction.setStatusTip('Start Current Server')
        startServerAction.triggered.connect(self.startServer)

        stopServerAction = QAction('S&top Server', self)
        stopServerAction.setShortcut('Ctrl+T')
        stopServerAction.setStatusTip('Stop Current Server')
        stopServerAction.triggered.connect(self.stopServer)

        editServerAction = QAction('&Modify Server', self)
        editServerAction.setShortcut('Ctrl+M')
        editServerAction.setStatusTip('Edit Current Server Configuration')
        editServerAction.triggered.connect(self.modifyServer)

        editMenu = menubar.addMenu('&Server')
        editMenu.addAction(startServerAction)
        editMenu.addAction(stopServerAction)
        editMenu.addSeparator()
        editMenu.addAction(editServerAction)
#        editMenu.setEnabled(False)
#--------------------------------------------------------------
        aboutAction = QAction('&About', self)
        aboutAction.setShortcut('Ctrl+A')
        aboutAction.setStatusTip('About Game Central Server')
        aboutAction.triggered.connect(self.about)

        helpMenu = menubar.addMenu('&Help')
        helpMenu.addAction(aboutAction)
#--------------------------------------------------------------
        self.setWindowTitle('Game Central Server')
        self.show()
#--------------------------------------------------------------

    def newServer(self):
        print("New Server")

    def loadServer(self):
        print("Load Server")

    def startServer(self):
        print("Start Server")

    def stopServer(self):
        print("Stop Server")

    def modifyServer(self):
        print("Modify Server")

    def about(self):
        print("About")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GameCentralServer()
    sys.exit(app.exec_())