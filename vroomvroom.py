import pygame
if False:
    import pygame._view
import time
import random
import sys

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (100,0,0)
green = (0,100,0)
bright_red = (255, 0 ,0)
bright_green = (0, 255, 0)
blue = (0,0,255)
block_colour = (53, 115, 255)

smallText = pygame.font.SysFont("comicsansms", 10)
mediumText = pygame.font.SysFont("comicsansms", 20)
ehText = pygame.font.SysFont("comicsansms", 50)
largeText = pygame.font.SysFont("comicsansms", 80)
exLargeText = pygame.font.SysFont("comicsansms", 105)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("vroom vroom")
clock = pygame.time.Clock()

carImg = pygame.image.load("resources/img/motorcycle.png")
icon = pygame.image.load("resources/img/icon.png")
rockImg = pygame.image.load("resources/img/rock.png")
rock2Img = pygame.image.load("resources/img/rock2.png")
wallpaper = pygame.image.load("resources/img/wallpaper.png")
button = pygame.image.load("resources/img/button.png")
button_pressed = pygame.image.load("resources/img/button_pressed.png")

pygame.display.set_icon(icon)


randomSong = random.randint(1,3)
if randomSong == 1:
	randomSong = "resources/snd/leftrightexcluded.wav"
if randomSong == 2:
	randomSong = "resources/snd/Soliloquy.wav"
if randomSong == 3:
	randomSong = "resources/snd/ZombiesAreComing.wav"
crash_sound = pygame.mixer.Sound("resources/snd/crash.wav")
pygame.mixer.music.load(randomSong)



car_width = 44

def things_dodged(count):
	font = pygame.font.SysFont("comicsansms", 25)
	text = font.render("Dodged: " + str(count), True, black)
	gameDisplay.blit(text, (0,0))
	
def things(thingx, thingy, thingw, thingh, color):
	pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def car(x,y):
	gameDisplay.blit(carImg, (x,y))

def rock(x,y):
	gameDisplay.blit(rockImg, (x,y))
	
def rock2(x,y):
	gameDisplay.blit(rock2Img, (x,y))
	
def text_objects(text, font):
	textSurface = font.render(text, True, black)
	return textSurface, textSurface.get_rect()

def message_display(text):
	TextSurf, TextRect = text_objects(text, exLargeText)
	TextRect.center = ((display_width / 2, display_height / 2))
	gameDisplay.blit(TextSurf, TextRect)
	pygame.display.update()

def quitGame():
	pygame.quit()
	sys.exit()

def buttonImg(msg,x,y,w,h,inb4,aftr,action):
	"""turns long code into function"""
	#if 150 + 189 > mouse[0] > 150 and 250 + 49 > mouse[1] > 250:
	#	gameDisplay.blit(button_pressed, (150, 250))
	#else:
	#	gameDisplay.blit(button, (150, 250))
	
	#textSurf, textRect = text_objects("GO!", mediumText)
	#textRect.center = ((150 +(189/2)), (250+(49/2)))
	#gameDisplay.blit(textSurf, textRect)
	
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()

	if x+w > mouse[0] > x and y+h > mouse[1] > y:
		gameDisplay.blit(aftr, (x, y))
		if click[0] == 1:
			action()
	else:
		gameDisplay.blit(inb4, (x, y))

	textSurf, textRect = text_objects(msg, mediumText)
	textRect.center = ( (x+(w/2)), (y+(h/2)) )
	gameDisplay.blit(textSurf, textRect)

	
	
	
	
def crash():

	pygame.mixer.music.stop()
	pygame.mixer.Sound.play(crash_sound)
	
	TextSurf, TextRect = text_objects("Game Over", largeText)
	TextRect.center = ((display_width/2),(100))
	gameDisplay.blit(TextSurf, TextRect)
	TextSurf, TextRect = text_objects("You Crashed", largeText)
	TextRect.center = ((display_width/2),(200))
	gameDisplay.blit(TextSurf, TextRect)    

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					game_loop()
				if event.key == pygame.K_RETURN:
					game_loop()			
                
        #gameDisplay.fill(white)
        

		buttonImg("Play Again",150,300,189,49,button,button_pressed,game_loop)
		buttonImg("Quit",450,300,189,49,button,button_pressed,quitGame)

		pygame.display.update()
		clock.tick(15) 
def unpause():
	global pause
	pygame.mixer.music.unpause()
	pause = False
	
def paused():

	pygame.mixer.music.pause()

	while pause:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					unpause()
				if event.key == pygame.K_RETURN:
					unpause()
				if event.key == pygame.K_ESCAPE:
					unpause()

					
		#gameDisplay.blit(wallpaper, (0,0))
		
		TextSurf, TextRect = text_objects("Paused", largeText)
		TextRect.center = ((display_width / 2, 100))
		gameDisplay.blit(TextSurf, TextRect)
		
		mouse = pygame.mouse.get_pos()
		#buttonRect("Return!",150,450,100,50,green,bright_green)
		#buttonRect("Quit", 550,450,100,50,red,bright_red)	
		buttonImg("Return!",150,250,189,49,button,button_pressed,unpause)
		buttonImg("Exit",450,250,189,49,button,button_pressed,quitGame)
		
		
		pygame.display.update()
		clock.tick(15)
	
def game_intro():
	intro = True
	while intro:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					game_loop()
				if event.key == pygame.K_RETURN:
					game_loop()
	
		gameDisplay.blit(wallpaper, (0,0))
		
		TextSurf, TextRect = text_objects("vroom vroom", largeText)
		TextRect.center = ((display_width / 2, 100))
		gameDisplay.blit(TextSurf, TextRect)
		TextSurf, TextRect = text_objects("by sean", ehText)
		TextRect.center = ((display_width / 2, 150))
		gameDisplay.blit(TextSurf, TextRect)
		
		
		mouse = pygame.mouse.get_pos()
		#buttonRect("GO!",150,450,100,50,green,bright_green)
		#buttonRect("Quit", 550,450,100,50,red,bright_red)	
		buttonImg("GO!",150,250,189,49,button,button_pressed,game_loop)
		buttonImg("Exit",450,250,189,49,button,button_pressed,quitGame)
		
		
		pygame.display.update()
		clock.tick(15)
	

def game_loop():
	global pause
	
	pygame.mixer.music.play(-1)
	
	x = (display_width * 0.45)
	y = (display_height * 0.8)

	x_change = 0
	
	thing_startx = random.randrange(0, display_width)
	thing_starty = -600
	thing_secondary = -200
	thing_speed = 7
	thing_secondary_speed = 0
	thing_width = 75
	thing_height = 45
	
	dodged = 0
	rock2_active = False
	
	gameExit = False
	while not gameExit:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:#the x button
				pygame.quit()
				sys.exit()
				
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					pause = True
					paused()
				if event.key == pygame.K_LEFT or event.key == pygame.K_a:
					x_change = -5
				elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
					x_change = 5
					
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_a or event.key == pygame.K_RIGHT or event.key == pygame.K_d:
					x_change = 0
			
		x += x_change
		
		gameDisplay.fill(white)
		
		car(x,y)
		rock(thing_startx, thing_starty)
		#things(thing_startx, thing_starty, thing_width, thing_height, block_colour)
		thing_starty += thing_speed
		thing_secondary += thing_secondary_speed
		
		if rock2_active == True:
			rock2(thing_secondarx, thing_secondary)
			
		things_dodged(dodged)
		
		
		if thing_starty > display_height:
			thing_starty = 0 - thing_height
			thing_startx = random.randrange(0, display_width)
			dodged += 1
			thing_speed += 0.2
			#thing_width += (dodged * 1.03)
			
		if thing_secondary > display_height and rock2_active == True:
			thing_secondary = 0 - thing_height
			thing_secondarx = random.randrange(0, display_width)
			dodged += 1
			thing_secondary_speed += 0.2
			#thing_width += (dodged * 1.03)
			
		if dodged == 10 and rock2_active == False:
			thing_secondarx = random.randrange(0, display_width)
			rock2(thing_secondarx, thing_secondary)
			
			thing_secondary_speed += 7
			rock2_active = True
		
		if dodged >= 20:
			thing_speed += 0.3
			thing_secondary_speed += 0.3
			
			
		if x < -car_width + (car_width/2):
			crash()
		if x > display_width or x+(car_width/2) > display_width:
			crash()
		
		if y < thing_starty + thing_height:
			#print("y crossing")
			
			if x > thing_startx and x < thing_startx + thing_width or  x + car_width > thing_startx and x + car_width < thing_startx + thing_width:
				#print("x crossing")
				crash()
		if y < thing_secondary + thing_height:
			#print("y crossing")
			
			if x > thing_secondarx and x < thing_secondarx + thing_width or x + car_width > thing_secondarx and x + car_width < thing_secondarx + thing_width:
				#print("x crossing")
				crash()
		pygame.display.update()
		clock.tick(60)

game_intro()
game_loop()
pygame.quit()
sys.exit()