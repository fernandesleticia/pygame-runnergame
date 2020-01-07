import pygame

# initialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

#Title and Icon
pygame.display.set_caption("Space Invaders")

#todo: fix that, is not applying the icon
icon = pygame.image.load('assets/ufo.png')
pygame.display.set_icon(icon)

#player ship
playerImg = pygame.image.load('assets/space-invaders-player-64px.png')
playerX = 400
playerY = 500

def player():
	screen.blit(playerImg, (playerX,playerY))

# game loop
running = True
while running:

	# RGB 
	screen.fill((0,0,0))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	
	player()
	pygame.display.update()

