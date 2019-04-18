import sys
import pygame
import pygame.font

class Button():
	
	def __init__(self, screen, msg):
		"""Initialize button attributes."""
		self.screen = screen
		self.screen_rect = screen.get_rect()
		
		self.msg = msg
		
		#Set the dimensions and properties of the button.
		self.width, self.height = 200, 50
		
		self.selected_color = (200, 0, 0)
		self.not_selected_color = (0, 200, 0)

		self.text_color = (255, 255, 255)
		self.font = pygame.font.SysFont(None, 48)
		
		#Build the button's rect object and center it.
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.center = self.screen_rect.center
		
		self.selected = False
		
		#The button needs to be prepped only once.
		self.prep_msg()
	
	def prep_msg(self):
		"""Turn msg into a rendered image and center text on the button."""
		"""if self.selected:
			self.button_color = self.selected_color
		else:
			self.button_color = self.not_selected_color
		"""
		self.msg_image = self.font.render(self.msg, True, self.text_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center
	
	def draw_button(self):
		#Draw blank button and the n draw message.
		if self.selected:
			button_color = self.selected_color
		else:
			button_color = self.not_selected_color
		self.screen.fill(button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)
		
	def execute(self, ai_settings, screen, stats, sb, menu, ship, aliens, bullets):
		"""Start an action according to buttons message."""
		if self.msg == 'New Game':
			if stats.game_paused:
				stats.first_game = False
			play(ai_settings, screen, stats, sb, menu, ship, aliens, bullets)
		elif self.msg == 'Continue':
			stats.game_active = True
			stats.game_paused = False
			pygame.mouse.set_visible(False)
		elif self.msg == 'Exit':
			stats.check_high_score(sb, 1)
			sys.exit()
		
		
def play(ai_settings, screen, stats, sb, menu, ship, aliens, bullets):
	"""Start a new game."""
	#Save high score if needed.
	if stats.game_paused:
		stats.check_high_score(sb, 1)
	
	#Reset the game settings.
	ai_settings.initialize_dynamic_settings()
	
	#Hide the mouse cursor.
	pygame.mouse.set_visible(False)
	
	#Reset the game statistics.
	stats.reset_stats()
	stats.game_active = True
	
	#Reset the scoreboard images.
	sb.prep_score()
	sb.prep_high_score()
	sb.prep_aliens_shot()
	sb.prep_ships()
	sb.prep_number_bullets()
	
	#Empty the list of aliens and bullets.
	for aliens_of_color in aliens.values():
		aliens_of_color.empty()
	bullets.empty()
	
	#Center the ship.
	ship.center_ship()
	
	if menu.buttons[0].msg != 'Continue':
		continue_button = Button(screen, 'Continue')
		menu.add(continue_button, 0)
	menu.select()

