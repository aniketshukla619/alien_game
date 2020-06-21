import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	
	def __init__(self, all_settings, screen):
		#initializing alien and set its starting postion
		super(Alien, self).__init__()
		self.screen = screen
		self.all_settings = all_settings
		
		#load the alien image and set its rect attribute
		self.image = pygame.image.load('images/alien.bmp')
		self.rect = self.image.get_rect()
		
		#start each new alien near the top left of the screen
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		
		#store the alien's exact position
		self.x = float(self.rect.x)
		

	def blitme(self):
		self.screen.blit(self.image, self.rect)

	def update(self):
		self.x += (self.all_settings.alien_speed * self.all_settings.fleet_direction)
		self.rect.x = self.x

	def check_edges(self): 
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right:
			return True
		elif self.rect.left <= 0:
			return True

		
