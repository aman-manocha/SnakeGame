import pygame
import time
import random

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Aman first game')

block_size = 10
FPS = 30

clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 20)

def snake(lead_x,lead_y,block_size):
    pygame.draw.rect(gameDisplay, green, [lead_x,lead_y,block_size,block_size])

def message_to_screen(msg,color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [display_width/2, display_height/2])
    
def gameloop():
    gameExit = False
    gameOver = False

    lead_x = display_width/2
    lead_y = display_height/2
    
    lead_x_change = 0
    lead_y_change = 0

    randAppleX = round(random.randrange(0, display_width-block_size)/10.0)*10.0
    randAppleY = round(random.randrange(0, display_height-block_size)/10.0)*10.0

    while not gameExit:

        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game over!!!Press C to play again or Q to quit", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True 
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameloop()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0

        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            gameOver = True
        
        lead_x += lead_x_change
        lead_y += lead_y_change
        gameDisplay.fill(white)
        pygame.draw.rect(gameDisplay, red , [randAppleX, randAppleY, block_size, block_size])
        snake(lead_x,lead_y,block_size)
        pygame.display.update()

        if lead_x == randAppleX and lead_y == randAppleY:
            randAppleX = round(random.randrange(0, display_width-block_size)/10.0)*10.0
            randAppleY = round(random.randrange(0, display_height-block_size)/10.0)*10.0

        clock.tick(FPS)
        
    pygame.quit()
    quit()

gameloop()
