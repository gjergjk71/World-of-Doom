import pygame

class Inventory:
	def __init__(self,screen,inventory_opened,inventory_closed,closeInventory_rect,slots,items,state="Closed"):
		self.screen = screen
		self.inventory_opened = inventory_opened
		self.inventoryOpened_rect = inventory_opened.get_rect()
		self.inventory_closed = inventory_closed
		self.inventoryClosed_rect = inventory_closed.get_rect()
		self.closeInventory_rect = closeInventory_rect
		self.slots = slots
		self.items = items
		self.state = state
	def blitme(self):
		if self.state == "Open":
			self.screen.blit(self.inventory_opened,self.inventoryOpened_rect)
		elif self.state == "Closed":
			self.screen.blit(self.inventory_closed,self.inventoryClosed_rect)
	def handle_events(self,events):
		for event in events:
			if event.type == pygame.MOUSEBUTTONUP:
				pos = pygame.mouse.get_pos()
				if self.inventoryClosed_rect.collidepoint(pos):
					self.state = "Open"
				elif self.closeInventory_rect.collidepoint(pos):
					self.state = "Closed"
