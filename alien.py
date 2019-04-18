from random import randint

import pygame
from pygame.sprite import Sprite

from pop_up_message import PopUpMessage

class Alien(Sprite):
	"""A class to represent a single alien in the fleet."""
	
	def __init__(self, ai_settings, screen, image_name):
		"""Initialize the alien and set its starting position."""
		super(Alien, self).__init__()
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.ai_settings = ai_settings
		
		#Load the alien image and set its rect attrinute.
		self.image = pygame.image.load(image_name)
		self.rect = self.image.get_rect()
		
		#Start each new alien
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		
		#Store the alien's position.
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)
	
	def blitme(self):
		"""Draw the alien at its current location."""
		self.screen.blit(self.image, self.rect)
	
	def check_edges(self):
		"""Return True if alien is at edge of screen."""
		if self.rect.right <= self.screen_rect.right and self.rect.left >= 0:
			return True
		else:
			return False
	
	def pop_up(self, pop_ups, new_points, new_bullets):
		"""
		Show how many points and new bullets player got when alien is 
		shot.
		"""
		points_message = PopUpMessage(self.ai_settings,
			self.screen, str(new_points), self.ai_settings.score_color,
			self.rect.centerx, self.rect.centery,
			'centerx', 'bottom')
		pop_ups.append(points_message)
		
		bullets_message = PopUpMessage(self.ai_settings,
			self.screen, str(new_bullets), self.ai_settings.bullets_color,
			self.rect.centerx, self.rect.centery,
			'centerx', 'top')
		pop_ups.append(bullets_message)
	

class AlienGreen(Alien):
	"""A class to represent a single green alien."""
	
	def __init__(self, ai_settings, screen):
		"""Initialize the alien and set its starting position."""
		super(AlienGreen, self).__init__(ai_settings, screen,
			'images/spaceship_green_tr.bmp')
	
	def update(self):
		"""Move the alien right or left."""
		self.y += self.ai_settings.alien_speed_factor
		self.rect.y = self.y

class AlienMovingSideways(Alien):
	"""A mother class for AlienYellow and AlienRed."""
	
	def __init__(self, ai_settings, screen, image_name, x_range,
			x_speed_factor, y_speed_factor):
		super(AlienMovingSideways, self).__init__(ai_settings, screen,
			image_name)
		
		#fleet_direction of 1 represents right; -1 represents left.
		self.direction = -1 + (2 * randint(0, 1))
		
		self.x_range = x_range
		self.x_offset = float(randint(0, self.x_range))
		self.x_speed_factor = x_speed_factor
		self.y_speed_factor = y_speed_factor
		
	def check_x_range(self):
		if self.x_offset < self.x_range and self.check_edges():
			self.x_offset += (self.x_speed_factor * 
				self.ai_settings.alien_speed_factor)
		else:
			self.direction *= -1
			self.x_offset = 0
	
	def update(self):
		"""Move the alien down and right or left."""
		self.check_x_range()
		self.x += (self.x_speed_factor * self.direction *
			self.ai_settings.alien_speed_factor)
		self.y += (self.y_speed_factor * 
			self.ai_settings.alien_speed_factor)
		self.rect.x = self.x
		self.rect.y = self.y


class AlienYellow(AlienMovingSideways):
	"""A class to represent a single yellow alien."""
	
	def __init__(self, ai_settings, screen):
		"""Initialize the alien and set its starting position."""
		super(AlienYellow, self).__init__(ai_settings, screen,
			'images/spaceship_yellow_tr.bmp',
			ai_settings.yellow_alien_x_range, 1, 1)

class AlienRed(AlienMovingSideways):
	"""A class to represent a single red alien."""
	
	def __init__(self, ai_settings, screen):
		"""Initialize the alien and set its starting position."""
		super(AlienRed, self).__init__(ai_settings, screen,
			'images/spaceship_red_tr.bmp',
			ai_settings.red_alien_x_range,
			ai_settings.red_x_speed_factor,
			ai_settings.red_y_speed_factor)
		
