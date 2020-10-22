#!/usr/bin/python3
import sys, uuid
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from ServerClass import *

class ServerDialog(QDialog):

    def __init__(self, server):
        super(ServerDialog, self).__init__()

        self.setWindowTitle("Server Configuration")
        self.server = ServerClass()
        self.server.set_server_name(server.get_server_name())
        self.server.set_server_type(server.get_server_type())

        self.server_name_label = QLabel('Server Name : ') 
        self.server_name = QLineEdit()
        self.server_name.setText(server.get_server_name())

        separator1 = QFrame()
        separator1.setFrameShape(QFrame.HLine)
        separator1.setLineWidth(1)

        self.serverTypeLabel = QLabel('Server Type:')
        self.rbtn1 = QRadioButton('Undefined')
        self.rbtn2 = QRadioButton('D&D 5th Ed')

        self.rbtn1.toggled.connect(self.onRbtnClicked1)
        self.rbtn2.toggled.connect(self.onRbtnClicked2)

        if int(UNDEFINED) == int(self.server.get_server_type()):
            self.rbtn1.setChecked(True)
            self.rbtn2.setChecked(False)
        elif int(DND_5TH_ED) == int(self.server.get_server_type()):
            self.rbtn1.setChecked(False)
            self.rbtn2.setChecked(True)
        self.rbtn1.setDisabled(True)

        separator2 = QFrame()
        separator2.setFrameShape(QFrame.HLine)
        separator2.setLineWidth(1)

        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.server_name_label, 0)
        self.layout.addWidget(self.server_name, 1)
        self.layout.addWidget(separator1, 2)
        self.layout.addWidget(self.serverTypeLabel, 3)
        self.layout.addWidget(self.rbtn1, 4)
        self.layout.addWidget(self.rbtn2, 5)
        self.layout.addWidget(separator2, 6)
        self.layout.addWidget(self.buttonBox, 7)
        self.setLayout(self.layout)

    def get_server_info(self):
        return self.server

    def accept(self):
        if self.server_name.text() == '':
            QMessageBox.critical(self, 'Error!', 'Server Name Cannot Be Blank')
        elif self.server_name.text().lower() == 'blank':
            QMessageBox.warning(self, 'Lol!', 'SmartAss')
            return QDialog.accept(self)
        else:
            return QDialog.accept(self)

    def onRbtnClicked1(self):
        radioBtn = self.sender()
        if radioBtn.isChecked():
            self.server_type = UNDEFINED

    def onRbtnClicked2(self):
        radioBtn = self.sender()
        if radioBtn.isChecked():
            self.server_type = DND_5TH_ED
