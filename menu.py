from button import Button

class Menu():
	"""A class to represent a menu."""
	
	def __init__(self, screen, space=10):
		"""Initialize a list of buttons."""
		self.buttons = []
		self.space = space
		self.height = 0
		self.screen = screen
		self.screen_rect = screen.get_rect()
		#Number of selected button.
		self.selected = -1
	
	def add(self, button, n = 'default'):
		"""Add a button to menu."""
		if n == 'default':
			n = len(self.buttons)
		if self.buttons:
			if self.selected >= n:
				self.selected += 1
		else:
			self.selected = 0
		self.buttons.insert(n, button)
		self.height = self.get_height()
	
	def remove(self, n):
		"""Remove a button from the menu."""
		self.buttons[self.selected].selected = False
		del self.buttons[n]
		self.height = self.get_height()
		self.selected = self.selected % len(self.buttons)
		self.select(self.selected)
	
	def select(self, n=0):
		"""Select a button."""
		if self.buttons:
			self.buttons[self.selected].selected = False
			self.selected = n
			self.buttons[n].selected = True
		else:
			self.selected = -1
	
	def get_height(self):
		"""Return height of all buttons."""
		height = 0
		if self.buttons:
			for button in self.buttons:
				height += button.height + self.space
			height -= self.space
		return height
	
	def get_top(self):
		"""Return top of first button ."""
		return self.screen_rect.centery - (self.height / 2)
	
	def prep_buttons(self):
		"""Place buttons in a right position."""
		prev_button_bot = self.get_top() - self.space
		for button in self.buttons:
			button.rect.y = prev_button_bot + self.space
			button.prep_msg()
			prev_button_bot = button.rect.bottom
	
	def draw_buttons(self):
		"""Draw all buttons from 'self.buttons'."""
		self.prep_buttons()
		for button in self.buttons:
			button.draw_button()
	

	
		
