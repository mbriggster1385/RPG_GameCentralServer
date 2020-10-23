#!/usr/bin/python3
import sys, uuid

DND_5TH_ED = 1
UNDEFINED = 9999

class ServerClass():
	def __init__(self):
		self.server_name = "Default Server Name"
		self.server_type = UNDEFINED
		self.server_uuid = uuid.uuid4()

	def reset(self):
		self.server_name = "Default Server Name"
		self.server_type = UNDEFINED
		self.server_uuid = uuid.uuid4()

	def set_server_name(self, server_name):
		self.server_name = server_name
	def get_server_name(self):
		return self.server_name

	def set_server_type(self, server_type):
		self.server_type = server_type
	def get_server_type(self):
		return self.server_type

	def set_server_uuid(self, server_uuid):
		self.server_uuid = server_uuid
	def get_server_uuid(self):
		return self.server_uuid