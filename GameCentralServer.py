import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication

class basicMenubar(QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.initUI()

    def initUI(self):
        self.setGeometry(200, 200, 200, 200)

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

        self.statusBar()
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(newAction)
        fileMenu.addAction(loadAction)
        fileMenu.addAction(exitAction)

        self.setWindowTitle('Game Central Server')
        self.show()

    def newServer(self):
        print("New Server")

    def loadServer(self):
        print("Load Server")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = basicMenubar()
    sys.exit(app.exec_())
