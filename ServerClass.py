#!/usr/bin/python3
import sys
from enum import Enum

class GS(Enum):
	DND_5TH_ED = 1
	UNDEFINED = 9999

class ServerClass():
	def __init__(self):
		self.server_name = "Default Server Name"
		self.server_type = GS.UNDEFINED.value
		self.configured_flag = False

	def reset(self):
		self.server_name = ""
		self.server_type = GS.UNDEFINED.value
		self.configured_flag = False

	def set_server_name(self, server_name):
		self.server_name = server_name
	def get_server_name(self):
		return self.server_name

	def set_server_type(self, server_type):
		self.server_type = server_type
	def get_server_type(self):
		return self.server_type

	def set_is_configured_from_string(self, configuration_value):
		if configuration_value == "True":
			self.configured_flag = True
		else:
			self.configured_flag = False
	def set_is_configured(self, configuration_value):
		self.configured_flag = configured_flag
	def isconfigured(self):
		return self.configured_flag
