#!/usr/bin/python3
from xml.dom.minidom import parse
import xml.dom.minidom
from GameClass import GameClass

class ParseGameFile():
   def loadgame(self, game_file):
      DOMTree = xml.dom.minidom.parse(game_file)
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

if __name__ == "__main__":
   app = ParseGameFile()
   game = app.loadgame("GamesFile.xml")
   print(game.get_game_name(), " ", game.get_game_type())
   if game.isconfigured() == True:
      print("True")
   else:
      print("False")
