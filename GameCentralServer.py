#!/usr/bin/python3
import pygame, sys, os, time
from pygame.locals import *

class GameCentralServer:
	def __init__(self):
		pygame.init()
		self.infoObject = None
		self.main_option_index = 0
		self.main_screen_background = None
		self.myfont = pygame.font.SysFont("comicsansms", 64)
		self.splashScreen = "GameCentralStartupScreen.jpg"
		self.main_options = [0, " New Server "], \
							[1, " Load Server "], \
							[2, " Start Server "], \
							[3, " Save Server "]

		self.pygameInit()

	def pygameInit(self):
		pygame.init()
		pygame.mouse.set_visible(False)

		self.myMainWindow = pygame.display.set_mode((0, 0), pygame.FULLSCREEN | pygame.HWSURFACE)
		self.infoObject = pygame.display.Info()

		self.main_screen_background = pygame.image.load(self.splashScreen)
		self.main_screen_background = pygame.transform.scale(self.main_screen_background, (self.infoObject.current_w, self.infoObject.current_h))
		rect = self.main_screen_background.get_rect()
		rect.center = self.infoObject.current_w//2, self.infoObject.current_h//2
		self.myMainWindow.blit(self.main_screen_background, rect)

		pygame.display.update()
		time.sleep(2)

		self.draw_main_options()

	def draw_main_options(self):
		rect = self.main_screen_background.get_rect()
		rect.center = self.infoObject.current_w//2, self.infoObject.current_h//2
		self.myMainWindow.blit(self.main_screen_background, rect)

		for [index, option] in self.main_options:
			option_string = self.myfont.render(option, True, (255,255,255))
			option_string2 = self.myfont.render(option, True, (0,0,0), (128,128,128))
			option_string2.set_alpha(128)

			myTextRect = option_string.get_rect()
			myTextRect.center = (self.infoObject.current_w//2, 250+(100*index))

			if index == self.main_option_index:
				myTextRect2 = option_string2.get_rect()
				myTextRect2.center = (self.infoObject.current_w//2, 250+(100*index))
				self.myMainWindow.blit(option_string2, myTextRect2)

			self.myMainWindow.blit(option_string, myTextRect)

		pygame.display.update()

	def run(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				elif event.type == pygame.KEYDOWN:
					if event.mod == pygame.KMOD_NONE:
						if event.key == pygame.K_ESCAPE:
							pygame.quit()
							quit()
						elif event.key == pygame.K_DOWN:
							self.main_option_index += 1
							if self.main_option_index >= len(self.main_options):
								self.main_option_index = len(self.main_options)-1
							self.draw_main_options()
						elif event.key == pygame.K_UP:
							self.main_option_index -= 1
							if self.main_option_index < 0:
								self.main_option_index = 0
							self.draw_main_options()
						elif event.key == pygame.K_RETURN:
							[index, option] = self.main_options[self.main_option_index]
							if option == " New Server ":
								self.new_server()
							elif option == " Load Server ":
								self.load_server()
							elif option == " Start Server ":
								self.start_server()
							elif option == " Save Server ":
								self.save_server()

			pygame.display.update()

	def new_server(self):
		print("New Server")

	def load_server(self):
		print("Load Server")

	def start_server(self):
		print("Start Server")

	def save_server(self):
		print("Save Server")

#----------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
	app = GameCentralServer()
	app.run()
