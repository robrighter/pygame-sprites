
import pygame
from pygame.locals import *

class RSprite(pygame.sprite.Sprite):
	def __init__(self):
		super(RSprite, self).__init__()
		self.surf = pygame.Surface((75, 25))
		self.surf.fill((255, 255, 255))
		self.rect = self.surf.get_rect()
		self.change_x = 0
		self.change_y = 0
	
	
	def go_left(self):
		self.change_x = -5
		
	def go_right(self):
		self.change_x = 5
	
	def jump(self):
		self.change_y = -200
	
	def run_stop(self):
		self.change_x = 0;
	
	def update(self):
		self.calculate_gravity()
		self.rect.x += self.change_x
		if self.rect.y < 500:
			self.rect.y += self.change_y
		else:
			self.rect.y = 500
			self.change_y = 0
		print self.rect.y
		
	def calculate_gravity(self):
		self.change_y += 1

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))
background = pygame.Surface(screen.get_size())
background.fill((0, 0, 0))
player = RSprite()

all_sprites = pygame.sprite.Group()
all_sprites.add(player)

running = True

while running:
	player_is_walking = False
	for event in pygame.event.get():
		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				running = False
			elif event.key == K_UP:
				player.jump()
			elif event.key == K_LEFT:
				player.go_left()
				player_is_walking = True
			elif event.key == K_RIGHT:
				player.go_right()
				player_is_walking = True
				
		elif event.type == QUIT:
			running = False
	if not player_is_walking:
		player.run_stop()
			
	screen.blit(background, (0, 0))
	player.update()
	for item in all_sprites:
		screen.blit(item.surf, item.rect)
	clock.tick(60)
	pygame.display.flip()
