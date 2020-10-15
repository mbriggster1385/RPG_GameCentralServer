#!/usr/bin/python3
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class ModifyServerDialog(QDialog):

    def __init__(self, *args, **kwargs):
        super(ModifyServerDialog, self).__init__(*args, **kwargs)
        
        self.setWindowTitle("HELLO!")
        
        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)