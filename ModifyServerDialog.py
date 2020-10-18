#!/usr/bin/python3
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from ServerClass import *

class ModifyServerDialog(QDialog):

    def __init__(self, *args, **kwargs):
        super(ModifyServerDialog, self).__init__(*args, **kwargs)
        
        self.setWindowTitle("Modify Server Configuration")
        
        self.server_name_label = QLabel('Server Name') 
        self.server_name = QLineEdit() 

        separator1 = QFrame()
        separator1.setFrameShape(QFrame.HLine)
        separator1.setLineWidth(1)

        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.server_name_label)
        self.layout.addWidget(self.server_name)
        self.layout.addWidget(separator1)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

    def set_text(self, initial_text):
        self.server_name.setText(initial_text)