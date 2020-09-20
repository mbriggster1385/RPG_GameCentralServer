#!/usr/bin/python3
import sys
import socket
import threading
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox, font
from tkinter.filedialog import askopenfilename, asksaveasfilename

from ParseGamesFile import *
from GameClass import *
from GameConfigDialog import *

class GameCentralServer:
	def __init__(self):
		self.server_address = ''
		self.server_port = 0

		self.root_window = None
		self.root_window = tk.Tk()
		self.root_window.title("Game Central Server")
		self.root_window.minsize(640, 480)
		self.root_window.geometry("900x600") #Width x Height

		self.game_class = GameClass()

	def clearGame(self):
		self.game_class.reset()

	def aboutDialog(self):
		messagebox.showinfo("About", "Game Central Server : v:0.1\nFor the Game Mastering an RPG session")

	def run(self):
		self.clearGame()

		menubar = tk.Menu(self.root_window)
		filemenu = tk.Menu(menubar, tearoff=0)
		filemenu.add_command(label="New Game", command=self.newGame)
		filemenu.add_command(label="Load Game", command=self.loadGame)
		filemenu.add_separator()
		filemenu.add_command(label="Exit", command=self.root_window.quit)
		menubar.add_cascade(label="File", menu=filemenu)
		helpmenu = tk.Menu(menubar, tearoff=0)
		helpmenu.add_command(label="About...", command=self.aboutDialog)
		menubar.add_cascade(label="Help", menu=helpmenu)

		self.root_window.config(menu=menubar)
		self.root_window.mainloop()

	def newGame(self):
		self.clearGame()
		dlg = GameConfigDialog(self.root_window)
		dlg.Create_Toplevel()

	def loadGame(self):
		self.clearGame()
		name = askopenfilename(initialdir=".", filetypes =(("Game XML",".xml"),("All Files","*.*")), title = "Choose a game file to load.")
		if name != "":
			with open(name,'r') as gameFile:
				parser = ParseGameFile()
				self.game_class = parser.loadgame(name)
				print(self.game_class.get_game_name(), " ", self.game_class.get_game_type())
				gameFile.close()

'----------------------------------------------------------------------------------------------------------'

if __name__ == "__main__":
	app = GameCentralServer()
	app.run()
