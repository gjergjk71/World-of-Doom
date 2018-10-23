import pygame
pygame.init()
pygame.display.set_mode()

class SpriteSheet:
	def __init__(self,filename):
		try:
			self.sheet = pygame.image.load(filename).convert()
		except pygame.error as message:
			print("Unable to load sprite sheet : {}".format(message))
			raise SystemExit
	def image_at(self,rectangle,colorkey=None,scale2x=False):
		rect = pygame.Rect(rectangle)
		image = pygame.Surface(rect.size).convert();
		image.blit(self.sheet, (0,0), rect)
		if colorkey is not None:
			if colorkey is -1:
				colorker = image.get_at((0,0))
			image.set_colorkey(colorkey,pygame.RLEACCEL)
		if scale2x:
			return pygame.transform.scale2x(image)
		else:
			return image