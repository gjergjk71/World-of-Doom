import pygame

class Item:
	def __init__(self,screen,inventory,x,y,w,h,item_image=None):
		self.inventory = inventory
		self.screen = screen
		self.item_image = item_image
		self.item_rect = pygame.Rect((x,y,w,h))
		self.dragging = False
	def blitme(self):
		if self.item_image:
			self.screen.blit(self.item_image,self.item_rect)
	def handle_events(self,events):
		for event in events:
			pos = pygame.mouse.get_pos()
			if self.inventory.state == "Open":
				if event.type == pygame.MOUSEBUTTONDOWN:
					if event.button == 1 and self.item_rect.collidepoint(pos):
						self.dragging = True
						print(self.dragging)
				elif event.type == pygame.MOUSEBUTTONUP:
					if event.button == 1:
						self.dragging = False
				if self.dragging:
					self.item_rect.x = pos[0]
					self.item_rect.y = pos[1]

class Inventory:
	def __init__(self,screen,inventory_opened,inventory_closed,closeInventory_rect,items,slots,state="Closed"):
		self.screen = screen
		self.inventory_opened = inventory_opened
		self.inventoryOpened_rect = inventory_opened.get_rect()
		self.inventory_closed = inventory_closed
		self.inventoryClosed_rect = inventory_closed.get_rect()
		self.closeInventory_rect = closeInventory_rect
		self.slots = slots
		self.items = items
		self.state = state
		self.slot_width =  11
		self.slot_height =  12
		self.slot_difference = 3
		self.starting_x = 13
		self.starting_y = 45
		for i in range(self.slots[0]):
			item_x = self.starting_x
			item_y = self.starting_y
			for s in range(i):
				item_y += self.slot_height + self.slot_difference
			for x in range(self.slots[1]):
				for l in range(x):
					item_x += self.slot_width + self.slot_difference
				item = Item(self.screen,self,item_x,item_y,self.slot_width,self.slot_height)
				self.items.append(item)
	def blitme(self):	
		if self.state == "Open":
			self.screen.blit(self.inventory_opened,self.inventoryOpened_rect)
		elif self.state == "Closed":
			self.screen.blit(self.inventory_closed,self.inventoryClosed_rect)
		for item in self.items:
			item.blitme()
	def handle_events(self,events):
		for event in events:
			self.open_close_inventory(event)
	def handle_item_events(self,events):
		for item in self.items:
			item.handle_events(events)
	def open_close_inventory(self,event):
		if event.type == pygame.MOUSEBUTTONUP:
			pos = pygame.mouse.get_pos()
			if self.inventoryClosed_rect.collidepoint(pos):
				self.state = "Open"
			elif self.closeInventory_rect.collidepoint(pos):
				self.state = "Closed"