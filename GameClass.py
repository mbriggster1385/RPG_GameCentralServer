#!/usr/bin/python3
import sys
from enum import Enum

class GS(Enum):
	DND_5TH_ED = 1
	UNDEFINED = 9999

class GameClass():
	def __init__(self):
		self.game_name = ""
		self.game_type = GS.UNDEFINED

	def reset(self):
		self.game_name = ""
		self.game_type = GS.UNDEFINED

	def set_game_name(self, name):
		self.game_name = name
	def get_game_name(self):
		return self.game_name

	def set_game_type(self, type):
		self.game_type = type
	def get_game_type(self):
		return self.game_type
