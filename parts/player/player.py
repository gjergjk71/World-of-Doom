import pygame

class Player:
	def __init__(self,screen,run_animation,idle_animation,walking_speed=1,running_speed=100,walk_animation_speed=100,idle_animation_speed=5,run_animation_speed=10):
		self.screen = screen
		self.player_current_animation = idle_animation
		self.item = 0
		self.float_item = 0.0
		self.playerRect = idle_animation[0].get_rect()
		self.playerRect.x = 100
		self.playerRect.y = 100
		self.walking_speed = walking_speed
		self.running_speed = running_speed
		self.walk_animation_speed = walk_animation_speed
		self.run_animation_speed = run_animation_speed
		self.idle_animation_speed = idle_animation_speed
		self.motion = [0,0]
		self.float_x = self.playerRect.x
		self.float_y = self.playerRect.y
		self.gravity_float = 0
		self.gravity = 50
		self.on_floor = False
	def blitme(self):
		self.gravity_float += self.gravity * self.dt
		self.float_x += self.motion[0] * self.dt
		self.float_y += self.motion[1] * self.dt
		if int(self.gravity_float):
			if not self.on_floor:
				self.playerRect.y += int(self.gravity_float)
			self.gravity_float = 0
		if int(self.float_x):
			self.playerRect.x += int(self.float_x)
			self.float_x = 0
		if int(self.float_y):
			self.playerRect.y += int(self.float_y)
			self.float_y = 0

		if self.item >= len(self.player_current_animation):
			self.item = 0
			self.float_item = 0
		self.screen.blit(self.player_current_animation[self.item],self.playerRect)
		if self.player_current_animation == run_animation:
			self.float_item += self.dt * self.run_animation_speed
		elif self.player_current_animation == player_idle:
			self.float_item += self.dt * self.idle_animation_speed
		self.item = int(self.float_item)
	def handle_events(self,events):
		for event in events:
			if event.type == pygame.KEYDOWN:
				speed = self.running_speed
				if event.key in [pygame.K_LEFT,pygame.K_RIGHT]:
					self.player_current_animation = run_animation
				if event.key == pygame.K_LEFT: self.motion[0] = -speed;
				if event.key == pygame.K_RIGHT: self.motion[0] = speed
				if event.key == pygame.K_UP: self.motion[1] = -speed
				if event.key == pygame.K_DOWN: self.motion[1] = speed
			elif event.type == pygame.KEYUP:
				if event.key in [pygame.K_LEFT,pygame.K_RIGHT]:
					self.motion[0] = 0
				if event.key in [pygame.K_DOWN,pygame.K_UP]:
					self.motion[1] = 0
				if not self.motion[0] and not self.motion[1]:
					self.player_current_animation = player_idle
