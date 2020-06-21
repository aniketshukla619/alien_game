class Settings():
	
	def __init__(self):
		
		self.screen_width = 1200
		self.screen_height = 650
		self.bg_color = (230,230,230)
		self.ship_speed_factor = 1
		self.ship_limit = 3
		

		#bullet
		self.bullet_speed = 1
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 60,60,60
		self.bullet_allowed = 3

		#alien setting
		self.alien_speed = 1
		self.fleet_drop_speed = 10
		self.fleet_direction = 1
