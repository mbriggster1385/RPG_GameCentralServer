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
		self.configured_flag = False

	def reset(self):
		self.game_name = ""
		self.game_type = GS.UNDEFINED
		self.configured_flag = False

	def set_game_name(self, game_name):
		self.game_name = game_name
	def get_game_name(self):
		return self.game_name

	def set_game_type(self, game_type):
		self.game_type = game_type
	def get_game_type(self):
		return self.game_type

	def set_is_configured_from_string(self, configuration_value):
		if configuration_value == "True":
			self.configured_flag = True
		else:
			self.configured_flag = False
	def set_is_configured(self, configuration_value):
		self.configured_flag = configured_flag
	def isconfigured(self):
		return self.configured_flag
