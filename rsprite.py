
import pygame
from pygame.locals import *

class RSprite(pygame.sprite.Sprite):
	def __init__(self):
		super(RSprite, self).__init__()
		self.surf = pygame.Surface((75, 25))
		self.surf.fill((255, 255, 255))
		self.rect = self.surf.get_rect()
	
	def update(self, pressed_keys):
		if pressed_keys[K_UP]:
			self.rect.move_ip(0, -5)
		if pressed_keys[K_DOWN]:
			self.rect.move_ip(0, 5)
		if pressed_keys[K_LEFT]:
			self.rect.move_ip(-5, 0)
		if pressed_keys[K_RIGHT]:
			self.rect.move_ip(5, 0)

pygame.init()
screen = pygame.display.set_mode((800, 600))
background = pygame.Surface(screen.get_size())
background.fill((0, 0, 0))
player = RSprite()

all_sprites = pygame.sprite.Group()
all_sprites.add(player)

running = True

while running:
	for event in pygame.event.get():
		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				running = False
		elif event.type == QUIT:
			running = False
	screen.blit(background, (0, 0))
	pressed_keys = pygame.key.get_pressed()
	player.update(pressed_keys)
	for item in all_sprites:
		screen.blit(item.surf, item.rect)
	pygame.display.flip()
