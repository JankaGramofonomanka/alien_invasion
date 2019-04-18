import pygame.font
from pygame.sprite import Group

from ship import Ship

class Scoreboard():
	"""A class to report scoring information."""
	
	def __init__(self, ai_settings, screen, stats):
		"""Initialize scorekeeping attributes."""
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.ai_settings = ai_settings
		self.stats = stats
		
		self.space = ai_settings.sb_space
		
		#Font settings for scoring information.
		self.font = pygame.font.SysFont(None, 36)
		self.description_font = pygame.font.SysFont(None, 24)
		
		#Prepare the initial score images.
		self.prep_score()
		self.prep_high_score()
		self.prep_aliens_shot()
		self.prep_ships()
		self.prep_number_bullets()
	
	def prep_score(self):
		"""Turn the score into a rendered image."""
		#rounded_score = int(round(self.stats.score, -1))
		score_str = "{:,}".format(self.stats.score)
		
		self.score_description_image = self.description_font.render('score:', True,
			self.ai_settings.score_color)
		self.score_image = self.font.render(score_str, True,
			self.ai_settings.score_color)
		
		#Display the score description at the top right of the screen.
		self.score_description_rect = self.score_description_image.get_rect()
		self.score_description_rect.right = self.screen_rect.right - self.space
		self.score_description_rect.top = self.space
		
		#Display the score below score description.
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.score_description_rect.right
		self.score_rect.top = self.score_description_rect.bottom
	
	def prep_high_score(self):
		"""Turn the high score into a rendered image."""
		#high_score = int(round(self.stats.high_score, -1))
		high_score_str = "{:,}".format(self.stats.high_score)
		
		self.high_score_description_image = ( 
			self.description_font.render('high score:', True,
				self.ai_settings.high_score_color)
			)
		self.high_score_image = self.font.render(high_score_str, True,
			self.ai_settings.high_score_color)
		
		#Center the score description at the top of the screen.
		self.high_score_description_rect = self.high_score_description_image.get_rect()
		self.high_score_description_rect.centerx = self.screen_rect.centerx
		self.high_score_description_rect.top = self.score_description_rect.top
		
		#Center the high score below high score description.
		self.high_score_rect = self.high_score_image.get_rect()
		self.high_score_rect.centerx = self.screen_rect.centerx
		self.high_score_rect.top = self.high_score_description_rect.bottom
	
	def prep_aliens_shot(self):
		"""Turn the number of aliens_shot into a rendered image."""
		
		self.aliens_shot_description_image = (
			self.description_font.render('aliens shot:', True,
				self.ai_settings.aliens_shot_color)
			)
		self.aliens_shot_image = self.font.render(
			str(self.stats.aliens_shot), True,
			self.ai_settings.aliens_shot_color)
		
		#Position the description below the score.
		self.aliens_shot_description_rect = self.aliens_shot_description_image.get_rect()
		self.aliens_shot_description_rect.right = self.score_description_rect.right
		self.aliens_shot_description_rect.top = self.score_rect.bottom + self.space
		
		#Position the number of aliens shot below the description.
		self.aliens_shot_rect = self.aliens_shot_image.get_rect()
		self.aliens_shot_rect.right = self.score_rect.right
		self.aliens_shot_rect.top = self.aliens_shot_description_rect.bottom
	
	def prep_ships(self):
		"""Show how many ships are left."""
		self.ships = Group()
		for ship_number in range(self.stats.ships_left):
			ship = Ship(self.ai_settings, self.screen)
			ship.rect.x = self.space + ship_number * (ship.rect.width + 1)
			ship.rect.y = self.space
			self.ships.add(ship)
	
	def prep_number_bullets(self):
		"""Turn the number of aliens_shot into a rendered image."""
		self.number_bullets_description_image = self.description_font.render('bullets left:', True,
			self.ai_settings.bullets_color)
		
		self.number_bullets_image = self.font.render(
			str(self.stats.number_bullets), True,
			self.ai_settings.bullets_color)
		
		#Position the description below the ships.
		self.number_bullets_description_rect = self.number_bullets_description_image.get_rect()
		if len(self.ships.sprites()) > 0:
			left = self.ships.sprites()[0].rect.left
			top = self.ships.sprites()[0].rect.bottom + self.space
		else:
			left = self.space
			top = self.score_description_rect.top
		self.number_bullets_description_rect.left = left
		self.number_bullets_description_rect.top = top
		
		#Position the number of bullets below the score.
		self.number_bullets_rect = self.number_bullets_image.get_rect()
		self.number_bullets_rect.left = self.number_bullets_description_rect.left
		self.number_bullets_rect.top = self.number_bullets_description_rect.bottom
				
	def show_stats(self):
		"""Draw stats to the screen."""
		self.screen.blit(self.aliens_shot_description_image, self.aliens_shot_description_rect)
		self.screen.blit(self.aliens_shot_image, self.aliens_shot_rect)
		
		#Draw ships.
		self.ships.draw(self.screen)
		
		self.screen.blit(self.number_bullets_description_image, self.number_bullets_description_rect)
		self.screen.blit(self.number_bullets_image, self.number_bullets_rect)
	
	def show_score(self):
		"""Draw score to the screen."""
		self.screen.blit(self.score_description_image, self.score_description_rect)
		self.screen.blit(self.score_image, self.score_rect)
	
	def show_high_score(self):
		"""Draw high score to the screen."""
		self.screen.blit(self.high_score_description_image, self.high_score_description_rect)
		self.screen.blit(self.high_score_image, self.high_score_rect)
