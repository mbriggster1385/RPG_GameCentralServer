#!/usr/bin/python3
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from ServerClass import *

class ServerDialog(QDialog):

    def __init__(self, *args, **kwargs):
        super(ServerDialog, self).__init__(*args, **kwargs)

        self.setWindowTitle("Server Configuration")
        self.server = ServerClass()

        self.server_name_label = QLabel('Server Name : ') 
        self.server_name = QLineEdit() 

        separator1 = QFrame()
        separator1.setFrameShape(QFrame.HLine)
        separator1.setLineWidth(1)

        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.server_name_label, 0)
        self.layout.addWidget(self.server_name, 1)
        self.layout.addWidget(separator1, 2)
        self.layout.addWidget(self.buttonBox, 3)
        self.setLayout(self.layout)

    def set_server_info(self, server):
        self.server_name.setText(server.get_server_name())

    def get_server_info(self):
        self.server.set_server_name(self.server_name.text())
        return self.server

    def accept(self):
        if self.server_name.text() == '':
            QMessageBox.critical(self, 'Error!', 'Server Name Cannot Be Blank')
        elif self.server_name.text().lower() == 'blank':
            QMessageBox.warning(self, 'Lol!', 'SmartAss')
            return QDialog.accept(self)
        else:
            return QDialog.accept(self)