import pygame
import random

# initialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# background
background = pygame.image.load('assets/space-background.jpg')


#Title and Icon
pygame.display.set_caption("Space Invaders")

#todo: fix that, is not applying the icon
icon = pygame.image.load('assets/ufo-64px.png')
pygame.display.set_icon(icon)

#player ship
playerImg = pygame.image.load('assets/space-invaders-player-64px.png')
playerX = 400
playerY = 500
playerX_change = 0

#player enemy
enemyImg = pygame.image.load('assets/ufo-64px.png')
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyY_change = 5
enemyX_change = 1

#laser
laserImg = pygame.image.load('assets/laser.png')
laserX = 0
laserY = 480
laserX_change = 0
laserY_change = 10
laser_state = "ready"


def player(x,y):
	screen.blit(playerImg, (x,y))


def enemy(x,y):
	screen.blit(enemyImg, (x,y))

def fire_laser(x,y):
	global laser_state
	laser_state = "fire"
	screen.blit(laserImg, (x + 16,y + 10))

# game loop
running = True
while running:

	# RGB 
	screen.fill((0,0,0))
    #background image
	screen.blit(background, (0, 0))
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				playerX_change = -5	
			if event.key == pygame.K_RIGHT:
				playerX_change = 5		
			if event.key == pygame.K_SPACE:
				if laser_state is "ready":
					laserX = playerX
					fire_laser(laserX, laserY)	
					
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				playerX_change = 0		
	
	# checking for boundaries
	playerX += playerX_change

	if playerX <= 0:
	   playerX = 0
	elif playerX >= 736:
		playerX = 736  

	enemyX += enemyX_change

	if enemyX <= 0:
	   enemyX_change = 3
	   enemyY += enemyY_change
	elif enemyX >= 736:
	   enemyX_change = -3
	   enemyY += enemyY_change

	#laser movement
	if laserY <=0 :
		laserY = 480
		laser_state = "ready"
	if laser_state is "fire":
		fire_laser(laserX, laserY)
		laserY -= laserY_change
 	 

	player(playerX, playerY)
	enemy(enemyX, enemyY)
	pygame.display.update()

