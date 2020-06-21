import pygame

from settings import Settings
from ship import Ship
from alien import Alien
from game_stats import GameStats
import game_functions as gf
from pygame.sprite import Group


def run_game():
	#initialize game and create the screen
	pygame.init()
	#import settings from settings.py
	all_settings = Settings()
	#make a group to store bullets in
	bullets = Group()
	aliens = Group()
	
	
	

	#initializing the screen settings
	screen=pygame.display.set_mode((all_settings.screen_width,all_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	pygame.display.toggle_fullscreen()
	stats = GameStats(all_settings)
	#make a ship
	ship = Ship(all_settings,screen)
	
	#make  a alien
	alien = Alien(all_settings,screen)
	#create the fleet of aliens
	gf.create_fleet(all_settings, screen , ship, aliens)
	#main loop
	while True:
		#keyboard and mouse events
		gf.check_events(all_settings, screen, ship, bullets)
		if stats.game_active:
			
			ship.update()
			gf.update_bullets(all_settings,screen,ship,aliens ,bullets)
			gf.update_aliens(all_settings,stats,screen,ship,aliens,bullets)
			#update_settings
			gf.update_settings(all_settings,screen,ship,aliens,bullets)
		
		

run_game()
