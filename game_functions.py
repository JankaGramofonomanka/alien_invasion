import sys
from time import sleep
from random import randint

import pygame

from button import Button
from bullet import Bullet
from alien import Alien
from collisions import *
from alien_creation import *

def check_keydown_events(event, ai_settings, screen, stats, sb, menu,
		ship, aliens, bullets):
	"""Respond to keypresses"""
	if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
		ship.moving_left = True
	elif event.key == pygame.K_UP or event.key == pygame.K_w:
		if not stats.game_active:
			n = menu.selected - 1
			menu.select(n % len(menu.buttons))
	elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
		if not stats.game_active:
			n = menu.selected + 1
			menu.select(n % len(menu.buttons))
	elif event.key == pygame.K_LSHIFT:
		ai_settings.slow_mo = True
	elif event.key == pygame.K_SPACE:
		if stats.game_active:
			fire_bullet(ai_settings, screen, stats, sb, ship, bullets)
	elif event.key == pygame.K_ESCAPE:
		if stats.game_active:
			stats.game_active = False
			stats.game_paused = True
			pygame.mouse.set_visible(True)
			menu.select(0)
		elif menu.buttons[0].msg == 'Continue':
			menu.buttons[0].execute(ai_settings, screen, stats, sb, menu, ship, aliens, bullets)
	elif event.key == pygame.K_RETURN and not stats.game_active:
		menu.buttons[menu.selected].execute(ai_settings, screen, stats, sb, menu, ship, aliens, bullets)

def check_keyup_events(event, ai_settings, ship):
	"""Respond to key releases"""
	if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
		ship.moving_left = False
	elif event.key == pygame.K_LSHIFT:
		ai_settings.slow_mo = False

def check_events(ai_settings, screen, stats, sb, menu, ship,
		aliens, bullets):
	"""Respond to keypresses and mouse events."""
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				stats.check_high_score(sb, 1)
				sys.exit()
			
			elif event.type == pygame.KEYDOWN:
				check_keydown_events(event, ai_settings, screen, stats,
					sb, menu, ship, aliens, bullets)
			
			elif event.type == pygame.KEYUP:
				check_keyup_events(event, ai_settings, ship)
			
			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_x, mouse_y = pygame.mouse.get_pos()
				check_button(ai_settings, screen, stats, sb,
					menu, ship, aliens, bullets, mouse_x, mouse_y)
			elif event.type == pygame.MOUSEMOTION:
				mouse_x, mouse_y = pygame.mouse.get_pos()
				for n in range(len(menu.buttons)):
					if menu.buttons[n].rect.collidepoint(mouse_x, mouse_y):
						menu.select(n)

def check_button(ai_settings, screen, stats, sb, menu, ship,
		aliens,	bullets, mouse_x, mouse_y):
	"""Start a new game when the player clicks Play."""
	for button in menu.buttons:
		button_clicked = button.rect.collidepoint(mouse_x, mouse_y)
		if button_clicked and not stats.game_active:
			button.execute(ai_settings, screen, stats, sb, menu, ship, aliens, bullets)

def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, pop_ups, menu):
	"""Update images on the screen and flip to the new screen."""
	#Redraw the screen during each pass through the loop.
	screen.fill(ai_settings.bg_color)
	
	#Redraw all bullets bahind ship and aliens.
	if stats.game_active or stats.game_paused:
		for bullet in bullets.sprites():
			bullet.draw_bullet()
		ship.blitme()
		for aliens_of_color in aliens.values():
			aliens_of_color.draw(screen)
		
		for message in pop_ups.copy():
			message.draw()
			message.update()
			if message.time <= 0:
				pop_ups.remove(message)
				
		#Draw the score information.

		sb.show_stats()
	if not stats.first_game or stats.game_active or stats.game_paused:
		sb.show_score()
	
	sb.show_high_score()	
	
	#Draw the play button if the game is inactive.
	if not stats.game_active:
		menu.draw_buttons()
	
	#Make the most recently drawn screen visible.
	pygame.display.flip()

def update_bullets(ai_settings, screen, stats, sb, ship, aliens,
		bullets, pop_ups):
	"""Update position of bullets and get rid of old bullets"""
	#Update positions.
	bullets.update()
	#Check for any bullets that have hit aliens.
	#If so, get rid of the bullet and the alien.
		
	#Get rid of bullets that have disappeared.
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 9:
			bullets.remove(bullet)
	#for aliens_of_color in aliens.values():
	check_bullet_alien_collisions(ai_settings, screen, stats, sb,
		ship, aliens, bullets, pop_ups)

def fire_bullet(ai_settings, screen, stats, sb, ship, bullets):
	"""Fire a bullet if limit not reached yes."""
	#Create a new bullet and add it to the bullets group.
	if stats.number_bullets > 0:
		new_bullet = Bullet(ai_settings, screen, ship)
		bullets.add(new_bullet)
		stats.number_bullets -= 1
		sb.prep_number_bullets()

def update_aliens(ai_settings, screen, stats, sb, menu, ship, aliens, bullets):
	"""
	Check if the fleet is at an edge, 
	and then update the positions of all aliens in the fleet.
	"""
	x = randint(1, 100)
	if x < ai_settings.yellow_prob and stats.aliens_shot > ai_settings.yellow_start:
		color = 'yellow'
	elif (x < ai_settings.yellow_prob + ai_settings.red_prob and 
			stats.aliens_shot > ai_settings.red_start):
		color = 'red'
	else:
		color = 'green'
	create_alien(ai_settings, screen, stats, aliens[color], color)
	for aliens_of_color in aliens.values():
		aliens_of_color.update()
	
	#Look for alien-ship collisions.
	for aliens_of_color in aliens.values():
		if pygame.sprite.spritecollideany(ship, aliens_of_color):
			ship_hit(ai_settings, screen, stats, sb, menu, ship, aliens, bullets)
	
	#Look for aliens hitting the  bottom of the screen.
	for aliens_of_color in aliens.values():
		if check_aliens_bottom(ai_settings, screen, stats, sb, menu, ship, aliens, bullets):
			break
