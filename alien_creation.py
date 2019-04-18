import sys
from time import sleep
from random import randint

import pygame

from bullet import Bullet
from alien import *

def create_alien(ai_settings, screen, stats, aliens_of_color, color):
	if ai_settings.timer > 0:
		ai_settings.timer -= 1
	else:
		create_alien_random(ai_settings, screen, stats, aliens_of_color, color)
		ai_settings.timer = ai_settings.interval

def create_alien_random(ai_settings, screen, stats, aliens_of_color, color):
	"""Create an alien and place it randomly on the top of the screen."""
	if color == 'green':
		alien = AlienGreen(ai_settings, screen)
	elif color == 'yellow':
		alien = AlienYellow(ai_settings, screen)
	elif color == 'red':
		alien = AlienRed(ai_settings, screen)
	alien_width = alien.rect.width
	x = randint(0, ai_settings.screen_width - alien_width)
	place_alien(screen, aliens_of_color, x, alien)

def create_alien_x(ai_settings, screen, stats, aliens_of_color, color, x=0):
	"""Create an alien and place it in a given coordinate."""
	if color == 'green':
		alien = AlienGreen(ai_settings, screen)
	elif color == 'yellow':
		alien = AlienYellow(ai_settings, screen)
	elif color == 'red':
		alien = AlienRed(ai_settings, screen)
	stats.aliens_count += 1
	place_alien(screen, aliens_of_color, x, alien)

def place_alien(screen, aliens_of_color, x, alien):
	"""Place an alien in a given coordinate if possible."""
	alien.x = x
	alien.rect.x = alien.x
	alien.rect.y = 0
	aliens_of_color.add(alien)

