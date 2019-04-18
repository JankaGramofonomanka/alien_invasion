import pygame
import pygame.font
from pygame.sprite import Sprite

class PopUpMessage(Sprite):
	"""A class to manage pop up messages."""
	
	def __init__(self, ai_settings, screen, msg, color, x, y,
			coordinate_x = 'centerx', coordinate_y = 'centery'):
		super(Sprite, self).__init__()
		self.ai_settings = ai_settings
		self.msg = msg
		self.color = color
		self.time = ai_settings.pop_up_message_time
		
		self.screen = screen
		self.screen_rect = screen.get_rect()
		
		self.font = pygame.font.SysFont(None, 15)
		
		self.prep_message(x, y, coordinate_x, coordinate_y)
		
		
	def prep_message(self, x, y, coordinate_x, coordinate_y):
		"""Turn the message into a rendered image."""
		self.image = self.font.render(self.msg, True, self.color)
		self.rect = self.image.get_rect()
		self.prep_message_x(x, coordinate_x)
		self.prep_message_y(y, coordinate_y)
	
	def prep_message_x(self, x, coordinate_x):
		if coordinate_x == 'x' or coordinate_x == 'left':
			self.rect.x = x
		elif coordinate_x == 'centerx':
			self.rect.centerx = x
		elif coordinate_x == 'right':
			self.rect.right = x
	
	def prep_message_y(self, y, coordinate_y):
		if coordinate_y == 'y' or coordinate_y == 'top':
			self.rect.y = y
		elif coordinate_y == 'centery':
			self.rect.centery = y
		elif coordinate_y == 'bottom':
			self.rect.bottom = y
	
	def draw(self):
		self.screen.blit(self.image, self.rect)
	
	def update(self):
		self.time -= 1
