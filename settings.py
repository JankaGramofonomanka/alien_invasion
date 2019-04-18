class Settings():
	"""A class to store all settings for Alien Invasion."""
	
	def __init__(self):
		"""Initialize the game's static settings."""
		#Screen settings
		self.screen_width = 800
		self.screen_height = 600
		self.bg_color = (30, 30, 30)
		
		#Ship settings.
		self.ship_limit = 3
		self.ship_slow_speed_factor = 1 / 7
		
		#Bullet settings.
		self.bullet_width = 1
		self.bullet_height = 30
		self.bullet_color = 255, 255, 0
		
		#How quickly the game speeds up
		self.speedup_scale = 1.01
		#How quickly the alien point values increase
		self.score_scale = 1.5
		
		#How often different alien types spawn.
		self.yellow_prob = 20.0
		self.red_prob = self.yellow_prob * 0.22
		
		#When different alien types start to spawn.
		self.yellow_start = 10
		self.red_start = 30
		
		#How far aliens move sideways.
		self.yellow_alien_x_range = 100
		self.red_alien_x_range = 100
		
		#How fast red aliens move in relation to other aliens.
		self.red_x_speed_factor = 1.5
		self.red_y_speed_factor = 1.1
		
		#How fast pop ups vanish.
		self.pop_up_message_time = 750
		
		#Message and stats colors.
		self.score_color = (255, 255, 255)
		self.high_score_color = (200, 200, 200)
		self.aliens_shot_color = (0, 200, 0)
		self.bullets_color = (200, 200, 0)
		
		self.high_score_filename = "scores/high_score.txt"
		
		#Space between stats informations.
		self.sb_space = 10
		
		self.initialize_dynamic_settings()
	
	def initialize_dynamic_settings(self):
		"""Initialize settings that change throughout the game."""
		self.ship_speed_factor = 0.125
		self.bullet_speed_factor = 3
		self.alien_speed_factor = 0.05
		
		#number of bullets in ships magazine at each ship respawn.
		self.first_number_bullets = 10.0
		
		#slow ship movement.
		self.slow_mo = False
		
		#Scoring
		self.green_points = 50
		self.yellow_points = 100
		self.red_points = 175
		
		#Getting bullets.
		self.green_bullets = 2.0
		self.yellow_bullets = 4.0
		self.red_bullets = 7.0
		
		#Alien generation interval
		self.interval = 5000.0
		self.timer = 300
	
	def increase_speed(self, k = 1):
		"""Increase speed settings and alien point values."""
		self.ship_speed_factor *= (self.speedup_scale ** k)
		self.bullet_speed_factor *= (self.speedup_scale ** k)
		self.alien_speed_factor *= (self.speedup_scale ** k)
		
		self.interval *= (1 / (self.speedup_scale ** k))
		
		#Increase number of points per alien.
		self.green_points *= (self.speedup_scale ** k)
		self.yellow_points *= (self.speedup_scale ** k)
		self.red_points *= (self.speedup_scale ** k)
		
		#Increase number of bullets per alien.
		self.green_bullets *= (self.speedup_scale ** k)
		self.yellow_bullets *= (self.speedup_scale ** k)
		self.red_bullets *= (self.speedup_scale ** k)
		
		#Increase number of bullets per player respawn.
		self.first_number_bullets *= (self.speedup_scale ** k)

