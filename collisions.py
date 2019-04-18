import sys
from time import sleep
from random import randint

import pygame

from bullet import Bullet
from alien import *

def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship,
		aliens, bullets, pop_ups):
	"""Respond to bullet-alien collisions."""
	#Remove any bullets and aliens that have collided.
	for color in aliens.keys():
		if color == 'green':
			alien_points = int(ai_settings.green_points)
			new_bullets = int(ai_settings.green_bullets)
		elif color == 'yellow':
			alien_points = int(ai_settings.yellow_points)
			new_bullets = int(ai_settings.yellow_bullets)
		elif color == 'red':
			alien_points = int(ai_settings.red_points)
			new_bullets = int(ai_settings.red_bullets)
		collisions = pygame.sprite.groupcollide(bullets, aliens[color], True, True)
		if collisions:
			for aliens_shot in collisions.values():
				n = len(aliens_shot)
				stats.score += alien_points * n
				stats.aliens_shot += n
				ai_settings.increase_speed(n)
				stats.number_bullets += new_bullets * n
				for alien in aliens_shot:
					alien.pop_up(pop_ups, alien_points, new_bullets)
		sb.prep_number_bullets()
		sb.prep_score()
		sb.prep_aliens_shot()
		stats.check_high_score(sb)

def check_aliens_bottom(ai_settings, screen, stats, sb, menu, ship, aliens,
		bullets):
	"""Check if any aliens have reached the bottom of the screen."""
	screen_rect = screen.get_rect()
	ret = False
	for aliens_of_color in aliens.values():
		for alien in aliens_of_color.sprites():
			if alien.rect.bottom >= screen_rect.bottom:
				#Treat this the same as if the ship got hit.
				ship_hit(ai_settings, screen, stats, sb, menu, ship,
					aliens, bullets)
				ret = True
				break
	return ret

def ship_hit(ai_settings, screen, stats, sb, menu, ship, aliens, bullets):
	"""Respond to ship being hit by alien."""
	if stats.ships_left > 0:
		#Decrement ships_left.
		stats.ships_left -= 1
		
		#Update scoreboard.
		sb.prep_ships()
		
		#Empty the list of aliens and bullets.
		for aliens_of_color in aliens.values():
			aliens_of_color.empty()
		bullets.empty()
		if stats.number_bullets < int(ai_settings.first_number_bullets):
			stats.number_bullets = int(ai_settings.first_number_bullets)
		sb.prep_number_bullets()
		
		#Create a new fleet and center the ship.
		ship.center_ship()
		
		#Pause.
		sleep(0.5)
	else:
		stats.game_active = False
		stats.first_game = False
		pygame.mouse.set_visible(True)
		menu.remove(0)
		stats.check_high_score(sb, 1)
