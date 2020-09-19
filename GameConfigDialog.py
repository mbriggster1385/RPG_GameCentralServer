#!/usr/bin/python3
import tkinter as tk
from tkinter import ttk

class GameConfigDialog:
    def __init__(self, root):
        self.root = root

    def Create_Toplevel(self):
        self.root.wm_attributes("-disabled", True)
        self.root.toplevel_dialog = tk.Toplevel(self.root)
        self.root.toplevel_dialog.minsize(300, 100)
        self.root.toplevel_dialog.transient(self.root)
        self.root.toplevel_dialog.protocol("WM_DELETE_WINDOW", self.Close_Toplevel)


        self.root.toplevel_dialog_label = ttk.Label(self.root.toplevel_dialog, text='Do you want to enable my parent window again?')
        self.root.toplevel_dialog_label.pack(side='top')

        self.root.toplevel_dialog_yes_button = ttk.Button(self.root.toplevel_dialog, text='Yes', command=self.Close_Toplevel)
        self.root.toplevel_dialog_yes_button.pack(side='left', fill='x', expand=True)

        self.root.toplevel_dialog_no_button = ttk.Button(self.root.toplevel_dialog, text='No')
        self.root.toplevel_dialog_no_button.pack(side='right', fill='x', expand=True)

    def Close_Toplevel(self):
        self.root.wm_attributes("-disabled", False) # IMPORTANT!
        self.root.toplevel_dialog.destroy()
        self.root.deiconify() 
