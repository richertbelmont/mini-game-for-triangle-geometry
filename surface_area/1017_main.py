import pygame
from pygame.locals import *
import button

# Initialize Pygame
pygame.init()

#create display window
SCREEN_HEIGHT = 500
SCREEN_WIDTH = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Draw Rectangle with Mouse')
FONT = pygame.font.Font(None, 36)

#load button images
start_img = pygame.image.load('start_btn.png').convert_alpha()
exit_img = pygame.image.load('exit_btn.png').convert_alpha()

#create button instances
start_button = button.Button(100, 200, start_img, 0.8, SCREEN_HEIGHT, SCREEN_WIDTH)
exit_button = button.Button(450, 200, exit_img, 0.8, SCREEN_HEIGHT, SCREEN_WIDTH)

# Initialize coordinates
x=0
y=0
w=0
h=0
drawmode=True

#game loop
run = True
while run:

	screen.fill((202, 228, 241))

	#event handler
	for event in pygame.event.get():
		#quit game
		if event.type == pygame.QUIT:
			run = False
		if event.type == MOUSEBUTTONDOWN:
			x,y = pygame.mouse.get_pos()
			drawmode = True
		if event.type == MOUSEBUTTONUP:
			x1,y1 = pygame.mouse.get_pos()
			w=abs(x1-x)
			h=abs(y1-y)
			drawmode= False

	rect = pygame.Rect(x,y,w,h)
	if drawmode == False:
		pygame.draw.rect(screen, (255,0,0), rect)
		fw = round(w/100)
		fh = round(h/100)
		if fw == 0 or fh == 0:
			fw += 1
			fh +=1
		text = FONT.render(
                f"Width: {fw}, Height: {fh}", True, (0, 0, 0)
            )
		if start_button.draw(screen):
			print('START')
		screen.blit(text, (20, 20))
	pygame.display.update()
	#pygame.display.flip()
pygame.quit()