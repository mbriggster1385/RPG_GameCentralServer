#!/usr/bin/python3
from xml.dom.minidom import parse
import xml.dom.minidom
from GameClass import GameClass

class ParseGameFile():
   def loadgame(self, game_file_name):
      DOMTree = xml.dom.minidom.parse(game_file_name)
      collection = DOMTree.documentElement
      games = collection.getElementsByTagName("game")

      game_class = GameClass()
      for game in games:
         element = game.getElementsByTagName('name')[0]
         game_class.set_game_name(element.childNodes[0].data)
         element = game.getElementsByTagName('gametype')[0]
         game_class.set_game_type(element.childNodes[0].data)
         element = game.getElementsByTagName('isconfigured')[0]
         game_class.set_is_configured_from_string(element.childNodes[0].data)

      return game_class

#<GameCentralDB version = "0.01">
#	<game>
#		<name>Briggs</name>
#		<gametype>1</gametype>
#		<isconfigured>False</isconfigured>
#	</game>
#</GameCentralDB>

   def savegame(self, game_file_name, game_class):
      if game_file_name != "":
         with open(game_file_name,'w') as output_file:
            print("\nOutput file --->> " + game_file_name + "\n")
            output_file.write('<GameCentralDB version = "0.01">\n')
            output_file.write('\t<game>\n')
            output_file.write('\t\t<name>' + game_class.get_game_name() + '</name>\n')
            output_file.write('\t\t<gametype>' + game_class.get_game_type() + '</gametype>\n')
            output_file.write('\t\t<isconfigured>' + str(game_class.isconfigured()) + '</isconfigured>\n')
            output_file.write('\t</game>\n')
            output_file.write('</GameCentralDB>')
            output_file.close()


if __name__ == "__main__":
   app = ParseGameFile()
   game = app.loadgame("GamesFile.xml")
   print(game.get_game_name(), " ", game.get_game_type())
   if game.isconfigured() == True:
      print("True")
   else:
      print("False")

   game.set_is_configured_from_string("True")
   app.savegame("GamesFileCheck.xml", game)
