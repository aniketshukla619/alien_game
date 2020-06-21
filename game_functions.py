import sys
from alien import Alien
import pygame
from bullet import Bullet
from time import sleep
def check_keydown_events(event,all_settings,screen,ship,bullets):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(all_settings, screen , ship, bullets)
	elif event.key == pygame.K_q:
		sys.exit()
		
def check_keyup_events(event,ship):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False

def check_events(all_settings,screen,ship,bullets):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event,all_settings,screen,ship,bullets)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event,ship)
			

def update_settings(all_settings,screen,ship,aliens,bullets):
	#fill screen
	screen.fill(all_settings.bg_color)

	for bullet in bullets.sprites():
		bullet.draw_bullet()

	ship.blitme()
	aliens.draw(screen)

	#recent screen visible
	pygame.display.flip()

def update_bullets(all_settings,screen,ship,aliens,bullets):
	bullets.update()
		
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
	
	check_alien_bullet_collision(all_settings,screen,ship,aliens,bullets)
	
def fire_bullet(all_settings, screen, ship, bullets):
	if len(bullets) < all_settings.bullet_allowed:		
		new_bullet = Bullet(all_settings, screen , ship)
		bullets.add(new_bullet)	


def create_fleet(all_settings, screen,ship, aliens):
	alien = Alien(all_settings, screen)
	alien_width = alien.rect.width
	number_alien_x = get_alien_x(all_settings, alien.rect.width)
	number_rows = get_num_rows(all_settings, ship.rect.height, alien.rect.height)
	
	for row_num in range(number_rows):
		for alien_num in range(number_alien_x):
			create_alien(all_settings,screen,aliens,alien_num,row_num)


def get_alien_x(all_settings, alien_width):
	available_space_x = all_settings.screen_width - 2* alien_width
	number_alien_x = int(available_space_x / (2 * alien_width))
	return number_alien_x

def create_alien(all_settings, screen, aliens, alien_num,row_num):
	alien = Alien(all_settings, screen)
	alien_width = alien.rect.width
	alien.x = alien_width + 2*alien_width*alien_num
	alien.rect.x = alien.x
	alien.rect.y = alien.rect.height + 2*alien.rect.height*row_num
	aliens.add(alien)

def get_num_rows(all_settings, ship_height, alien_height):
	available_space_y = (all_settings.screen_height - (3*alien_height) - ship_height)
	number_rows = int(available_space_y / (2*alien_height))
	return number_rows


def update_aliens(all_settings,stats,screen,ship,aliens,bullets):
	check_fleet_edges(all_settings,aliens)
	aliens.update()
	if pygame.sprite.spritecollideany(ship,aliens):
		ship_hit(all_settings,stats,screen,ship,aliens,bullets)
	check_bottom_pass(all_settings,stats, screen, ship, aliens,bullets)	

def check_fleet_edges(all_settings, aliens):
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(all_settings, aliens)
			break	

def change_fleet_direction(all_settings, aliens):
	for alien in aliens.sprites():
		alien.rect.y += all_settings.fleet_drop_speed
	all_settings.fleet_direction *= -1 

def check_alien_bullet_collision(all_settings,screen,ship,aliens,bullets):
	collisions = pygame.sprite.groupcollide(aliens,bullets,True,True)

	if len(aliens) == 0:
		bullets.empty()
		create_fleet(all_settings,screen,ship,aliens)

def ship_hit(all_settings,stats,screen,ship,aliens,bullets):
	
	if stats.ship_left > 0:
		stats.ship_left -= 1
		aliens.empty()
		bullets.empty()
		create_fleet(all_settings, screen,ship, aliens)
		ship.center_ship()
		sleep(0.5)
	else:
		stats.game_active = False
		pygame.display.set_palette("Game Over!!!")
def check_bottom_pass(all_settings,stats, screen, ship, aliens,bullets):
	screen_rect = screen.get_rect()
	for alien in aliens.sprites():
		if alien.rect.bottom >= screen_rect.bottom:
			ship_hit(all_settings,stats,screen,ship,aliens,bullets)
			break
