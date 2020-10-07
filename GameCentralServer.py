#!/usr/bin/python3
import pygame, sys, os, time
from pygame.locals import *

class GameCentralServer:
	def __init__(self):
		pygame.init()
		self.myfont = pygame.font.SysFont("comicsansms", 72)
		self.splashScreen = "GameCentralStartupScreen.jpg"

		self.pygameInit()

	def pygameInit(self):
		pygame.init()
		pygame.mouse.set_visible(True)

		self.myMainWindow = pygame.display.set_mode((0, 0), pygame.FULLSCREEN | pygame.HWSURFACE)
		infoObject = pygame.display.Info()

		image_s = pygame.image.load(self.splashScreen)
		image_s = pygame.transform.scale(image_s, (infoObject.current_w, infoObject.current_h))
		rect = image_s.get_rect()
		rect.center = infoObject.current_w//2, infoObject.current_h//2
		self.myMainWindow.blit(image_s, rect)

		pygame.display.update()
		time.sleep(2)

		server_string = self.myfont.render(" Configure Server ", True, (255,255,255))
		server_string2 = self.myfont.render(" Configure Server ", True, (0,0,0), (64,64,64))
		server_string2.set_alpha(128)
		myTextRect = server_string.get_rect()
		myTextRect.center = ((infoObject.current_w//2, infoObject.current_h//2))
		myTextRect2 = server_string2.get_rect()
		myTextRect2.center = ((infoObject.current_w//2, infoObject.current_h//2))
		self.myMainWindow.blit(server_string2, myTextRect2)
		self.myMainWindow.blit(server_string, myTextRect)

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
#						elif event.key == pygame.K_DOWN:
#						elif event.key == pygame.K_UP:
#						elif event.key == pygame.K_LCTRL:
#					elif event.mod & pygame.KMOD_LALT:
#						if event.key == pygame.K_DOWN:
#						elif event.key == pygame.K_UP:

			pygame.display.update()

'----------------------------------------------------------------------------------------------------------'

if __name__ == "__main__":
	app = GameCentralServer()
	app.run()
