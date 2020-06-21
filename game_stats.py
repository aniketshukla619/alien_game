import pygame

class GameStats():

	def __init__(self,all_settings):
		self.all_settings = all_settings
		self.reset_stats()
		self.game_active = True

	def reset_stats(self):
		self.ship_left  = self.all_settings.ship_limit
