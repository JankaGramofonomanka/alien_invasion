import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from menu import Menu
from ship import Ship
import game_functions as gf

def run_game():
	#Initialize game and create screen object.
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height)
		)
	pygame.display.set_caption("Alien Invasion")
	
	#Make buttons.
	menu = Menu(screen)
	play_button = Button(screen, 'New Game')
	exit_button = Button(screen, 'Exit')
	menu.add(play_button)
	menu.add(exit_button)
	menu.select(0)
	
	#Make a group of pop up messages.
	pop_ups = []
	
	#Create an instance to store game statistics and create a scoreboard.
	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings, screen, stats)
	
	#Make a ship, a group of bullets, and a group of aliens
	ship = Ship(ai_settings, screen)
	bullets = Group()
	green_aliens = Group()
	yellow_aliens = Group()
	red_aliens = Group()
	aliens = {'green': green_aliens, 'yellow':  yellow_aliens, 'red': red_aliens}
	
	#Start the main loop for the game.
	while True:
		
		gf.check_events(ai_settings, screen, stats, sb, menu, ship,
			aliens, bullets)
		
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings, screen, stats, sb, ship,
				aliens, bullets, pop_ups)
			gf.update_aliens(ai_settings, screen, stats, sb, menu, ship,
				aliens, bullets)
		
		gf.update_screen(ai_settings, screen, stats, sb, ship, aliens,
			bullets, pop_ups, menu)

run_game()
