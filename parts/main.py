import sys, pygame,datetime
from player.player import Player
from objects.floor.floor import Floor
from misc.spritesheet import SpriteSheet

pygame.init()

size = width, height = 800, 800
speed = [5,5];
black = 0,0,0
screen = pygame.display.set_mode([500,500]);

floor_spritesheet = SpriteSheet("objects/floor/cave_tileset.png")
floor_big = floor_spritesheet.image_at((0,120,96,48))


floors = [
		Floor(screen,floor_big),
	] 
floors.append(Floor(screen,floor_big,floors[0].floor_rect))


player_spritesheet = SpriteSheet("player/images/player_spritesheet.png")
player_run = [
	player_spritesheet.image_at((65,44,25,31),scale2x=True),
	player_spritesheet.image_at((115,44,25,31),scale2x=True),
	player_spritesheet.image_at((165,44,25,31),scale2x=True),
	player_spritesheet.image_at((216,44,25,31),scale2x=True),
	player_spritesheet.image_at((264,44,25,31),scale2x=True),
	player_spritesheet.image_at((315,44,25,31),scale2x=True),
]

player_idle = [
	player_spritesheet.image_at((11,6,24,32),scale2x=True),
	player_spritesheet.image_at((62,6,24,32),scale2x=True),
	player_spritesheet.image_at((112,6,24,32),scale2x=True),
	player_spritesheet.image_at((162,6,24,32),scale2x=True),
]


player = Player(screen,100,1,idle_animation=player_idle,run_animation=player_run)
getTicksLastFrame = 0
while 1:
	t = pygame.time.get_ticks()
	deltaTime = (t - getTicksLastFrame) / 1000.0
	events = pygame.event.get()
	for event in events:
		if event.type == pygame.QUIT:
			sys.exit()
	screen.fill(black)
	player.on_floor = False
	for floor in floors:
		floor.blitme()
		collisionDetected = floor.floor_rect.colliderect(player.playerRect)
		if collisionDetected and not player.on_floor:
			player.on_floor = True

	player.dt = deltaTime
	player.handle_events(events)
	player.blitme()

	
	pygame.display.flip()
	getTicksLastFrame = t