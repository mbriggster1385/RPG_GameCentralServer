#!/usr/bin/python3
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
from GameClass import *

class GameConfigDialog:
	def __init__(self, root):
		self.root = root
		self.game = GameClass()
		self.v = StringVar()

	def Create_Toplevel(self):
		self.root.wm_attributes("-disabled", True)
		self.root.toplevel_dialog = tk.Toplevel(self.root)
		self.root.toplevel_dialog.minsize(600, 300)
		self.root.toplevel_dialog.title("Configure Game")
		self.root.toplevel_dialog.transient(self.root)
		self.root.toplevel_dialog.protocol("WM_DELETE_WINDOW", self.cancel_clicked)

		self.root.toplevel_dialog_label = ttk.Label(self.root.toplevel_dialog, text="\n         New Game Name:   \n")
		self.root.toplevel_dialog_label.grid(column=0, row=1)
		self.root.toplevel_dialog_entry = ttk.Entry(self.root.toplevel_dialog,width=60, textvariable=self.v)
		self.root.toplevel_dialog_entry.grid(column=1, row=1)

		self.root.toplevel_dialog_rad1 = ttk.Radiobutton(self.root.toplevel_dialog,text='\nD&D 5th ed\n', value=GS.UNDEFINED)
		self.root.toplevel_dialog_rad1.grid(column=0, row=3)

		self.root.toplevel_dialog_yes_button = ttk.Button(self.root.toplevel_dialog, text='Accept', command=self.accept_clicked)
		self.root.toplevel_dialog_yes_button.grid(column=0, row=5)

		self.root.toplevel_dialog_no_button = ttk.Button(self.root.toplevel_dialog, text='Cancel', command=self.cancel_clicked)
		self.root.toplevel_dialog_no_button.grid(column=1, row=5)

	def accept_clicked(self):
		self.game.set_is_configured_from_string("True")
#		self.game.set_game_type(self.root.toplevel_dialog.rad1.get())
		self.game.set_game_name(self.v)
		print(self.v)

		self.root.wm_attributes("-disabled", False) # IMPORTANT!
		self.root.toplevel_dialog.destroy()
		self.root.deiconify() 

	def cancel_clicked(self):
		self.root.wm_attributes("-disabled", False) # IMPORTANT!
		self.root.toplevel_dialog.destroy()
		self.root.deiconify() 

	def Get_Game(self):
		return self.game