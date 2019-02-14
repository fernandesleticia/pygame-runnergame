import pygame

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255, 0, 0)

char_width = 73

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Char Run')
clock = pygame.time.Clock()

crashed = False
charImg = pygame.image.load('assets/char.png')

def char(x,y):
	gameDisplay.blit(charImg, (x,y))

def text_objects(text, font):
	textSurface = font.render(text, True, black)
	return textSurface, textSurface.get_rect()

def message_display(text):
	largeText = pygame.font.Font('assets/Candle Mustard.ttf', 90)
	TextSurf, TextRect = text_objects(text, largeText)
	TextRect.center = ((display_width/2),(display_height/2))
	gameDisplay.blit(TextSurf, TextRect)

	pygame.display.update()

	time.sleep(2)

	game_loop()

def crash():
	message_display('End')
    

def game_loop():
	x =  (display_width * 0.45)
	y = (display_height * 0.7)
	x_change = 0
    #char_speed = 0
	gameExit = False

	while not gameExit :
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				#gameExit  = True
				#print(event)
				pygame.quit()
				quit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					x_change = -5
				elif event.key == pygame.K_RIGHT:
					x_change = 5
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					x_change = 0

		x += x_change

		gameDisplay.fill(white)
		char(x,y)

		if x> display_width - char_width or x<0:
			#gameExit = True
			crash()
		pygame.display.update()
		clock.tick(60)

game_loop()
pygame.quit()
quit()