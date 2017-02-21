
import pygame
from pygame.locals import *

class RSprite(pygame.sprite.Sprite):
	def __init__(self):
		super(RSprite, self).__init__()
		self.surf = pygame.Surface((75, 25))
		self.surf.fill((255, 255, 255))
		self.rect = self.surf.get_rect()

pygame.init()
screen = pygame.display.set_mode((800, 600))
player = RSprite()

running = True

while running:
	for event in pygame.event.get():
		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				running = False
		elif event.type == QUIT:
			running = False
	screen.blit(player.surf, (400, 300))
	pygame.display.flip()
