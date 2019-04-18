class GameStats():
	"""Track statistics for Alien Invasion."""
	
	def __init__(self, ai_settings):
		"""Initialize statistics."""
		self.ai_settings = ai_settings
		self.high_score_filename = ai_settings.high_score_filename
		self.reset_stats()
		
		#Start game in an inactive state.
		self.game_active = False
		
		#
		self.first_game = True
		
		#High score should never be reset.
		try:
			with open(self.high_score_filename) as high_score_file:
				high_score =  int(high_score_file.read())
		except FileNotFoundError:
			high_score = 0
		
		self.high_score = high_score
	
	def reset_stats(self):
		"""Initialize statistics that can change during the game."""
		self.ships_left = self.ai_settings.ship_limit
		self.score = 0
		self.aliens_shot = 0
		self.number_bullets = int(self.ai_settings.first_number_bullets)
		self.game_paused = False
	
	def check_high_score(self, sb, n=0):
		"""Check to see if there's a new high score."""
		if n == 0:
			if self.score > self.high_score:
				self.high_score = self.score
				sb.prep_high_score()
		else:
			try:
				with open(self.high_score_filename) as high_score_file:
					high_score = int(high_score_file.read())
			except FileNotFoundError:
				high_score  = 0
			if high_score < self.high_score:
				with open(self.high_score_filename, 'w') as high_score_file:
					high_score_file.write(str(self.high_score))
