
class Inventory:
	def __init__(self,screen,inventory_image,x,y,w,h,slots,items):
		self.screen = screen
		self.inventory_image = inventory_image
		self.inventory_rect = inventory_image.get_rect()
		self.inventory_rect.x = x
		self.inventory_rect.y = y
		self.inventory_rect.w = w
		self.inventory_rect.h = h
		self.slots = slots
		self.items = items
	def blitme(self):
		self.screen.blit(self.inventory_image,self.inventory_rect)
