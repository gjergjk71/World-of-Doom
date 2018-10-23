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