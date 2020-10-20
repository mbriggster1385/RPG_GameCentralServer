#!/usr/bin/python3
from xml.dom.minidom import parse
import xml.dom.minidom
from ServerClass import *

class ServerFileParser():
   def loadServer(self, server_file_name):
      DOMTree = xml.dom.minidom.parse(server_file_name)
      collection = DOMTree.documentElement
      servers = collection.getElementsByTagName("server")

      server_class = ServerClass()
      for server in servers:
         element = server.getElementsByTagName('name')[0]
         server_class.set_server_name(element.childNodes[0].data)
         element = server.getElementsByTagName('servertype')[0]
         server_class.set_server_type(element.childNodes[0].data)
         element = server.getElementsByTagName('isconfigured')[0]
         server_class.set_is_configured_from_string(element.childNodes[0].data)

      return server_class

#<GameCentralDB version = "0.01">
#	<server>
#		<name>Briggs</name>
#		<servertype>1</servertype>
#		<isconfigured>False</isconfigured>
#	</server>
#</GameCentralDB>

   def saveServer(self, server_file_name, server_class):
      if server_file_name != "":
         with open(server_file_name,'w') as output_file:
            output_file.write('<GameCentralDB version = "0.01">\n')
            output_file.write('\t<server>\n')
            output_file.write('\t\t<name>' + server_class.get_server_name() + '</name>\n')
            output_file.write('\t\t<servertype>' + str(server_class.get_server_type()) + '</servertype>\n')
            output_file.write('\t\t<isconfigured>' + str(server_class.isconfigured()) + '</isconfigured>\n')
            output_file.write('\t</server>\n')
            output_file.write('</GameCentralDB>')
            output_file.close()


if __name__ == "__main__":
   app = ServerFileParser()
   server = app.loadServer("ServerFile.xml")
   print(server.get_server_name(), " ", server.get_server_type())
   if server.isconfigured() == True:
      print("True")
   else:
      print("False")

   server.set_is_configured_from_string("True")
   app.saveServer("ServerFileCheck.xml", server)
