import pygame
import math
import random
from pygame import mixer

# initialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# Sound
# mixer.music.load("assets/background.wav")
# mixer.music.play(-1)

# background
background = pygame.image.load('assets/space-background.jpg')

#Title and Icon
pygame.display.set_caption("Space Invaders")

#todo: fix that, is not applying the icon
icon = pygame.image.load('assets/ufo-64px.png')
pygame.display.set_icon(icon)

#player ship
playerImg = pygame.image.load('assets/space-invaders-player-64px.png')
playerX = 370
playerY = 480
playerX_change = 0

#player enemy
enemyImg = []
enemyX = []
enemyY = []
enemyY_change = []
enemyX_change = []
num_of_enemies = 4

for i in range(num_of_enemies):
	enemyImg.append(pygame.image.load('assets/ufo-64px.png'))
	enemyX.append(random.randint(0, 736))
	enemyY.append(random.randint(50, 150))
	enemyY_change.append(4)
	enemyX_change.append(40)

#laser
laserImg = pygame.image.load('assets/laser.png')
laserX = 0
laserY = 480
laserX_change = 0
laserY_change = 10
laser_state = "ready"

score_value = 0
font = pygame.font.Font('assets/FreeSansBold.ttf', 32)

textX = 10
testY = 10

#Game Over
over_font = pygame.font.Font('assets/FreeSansBold.ttf', 64)

def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

def player(x,y):
	screen.blit(playerImg, (x,y))

def enemy(x,y,i):
	screen.blit(enemyImg[i], (x, y))

def fire_laser(x,y):
	global laser_state
	laser_state = "fire"
	screen.blit(laserImg, (x + 16,y + 10))

def isCollision(enemyX, enemyY,laserX,laserY):
	distance = math.sqrt((math.pow(enemyX-laserX,2)) + (math.pow(enemyY-laserY,2)))
	if distance < 27:
		return True
	else:
		return False


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
					# bulletSound = mixer.Sound("assets/laser.wav")
					# bulletSound.play()
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

    # enemy movement
	for i in range(num_of_enemies):

		# Game Over
		if enemyY[i] > 440:
			for j in range(num_of_enemies):
				enemyY[j] = 2000
			game_over_text()
			break

		enemyX[i] += enemyX_change[i]
		if enemyX[i] <= 0:
			enemyX_change[i] = 3
			enemyY[i] += enemyY_change[i]
		elif enemyX[i] >= 736:
			enemyX_change[i] = -3
			enemyY[i] += enemyY_change[i]

		#collision
		collision = isCollision(enemyX[i], enemyY[i], laserX, laserY)
		if collision:
			# explosionSound = mixer.Sound("assets/explosion.wav")
			# explosionSound.play()
			laserY = 480
			laser_state = "ready"	
			score_value += 1
			enemyX[i] = random.randint(0, 736)
			enemyY[i] = random.randint(50, 150)

		enemy(enemyX[i], enemyY[i], i)
  
	#laser movement
	if laserY <=0 :
		laserY = 480
		laser_state = "ready"

	if laser_state is "fire":
		fire_laser(laserX, laserY)
		laserY -= laserY_change

	
	player(playerX, playerY)
	show_score(textX, testY)
	pygame.display.update()

