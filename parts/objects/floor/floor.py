
class Floor:
	def __init__(self,screen,last_floor_rect=None):
		self.screen = screen
		self.floor_image = floor_big
		self.floor_rect = self.floor_image.get_rect()
		if last_floor_rect is None:
			self.floor_rect.x = 200
			self.floor_rect.y = self.screen.get_height() - (self.floor_rect.w / 2)
		else:
			self.floor_rect.x += last_floor_rect.w + 10
			self.floor_rect.y = last_floor_rect.y
	def blitme(self):
		self.screen.blit(self.floor_image,self.floor_rect)