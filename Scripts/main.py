import pygame
from sys import exit
import tkinter

#The Info Window
infoScreen = tkinter.Tk()
infoScreen.title("PyRunner")
infoScreen.geometry("500x100")

label1 = tkinter.Label(infoScreen, text="Game created by supperfangamm3").pack()
label2 = tkinter.Label(infoScreen, text="This game is still in developement so there might be bugs!").pack()
label3 = tkinter.Label(infoScreen, text="Press the button to start the game (This window will reappear upon bootup)").pack()
but = tkinter.Button(infoScreen, text="I understand", command=infoScreen.destroy).pack()

infoScreen.mainloop()

#The game itself
pygame.init()

#Make the screen
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("PyRunner")

#Make a font
font = pygame.font.Font(None, 50)

#Get the assets
SKY = pygame.image.load("GameAssets/Sky.png").convert()
GROUND = pygame.image.load("GameAssets/Ground.png").convert()
SCORE = font.render("Score", True, "Black")
SCORE_RECT = SCORE.get_rect(topleft = (0, 0))

ENEMY1 = pygame.image.load("GameAssets/Enemy.png").convert_alpha()

ENEMY_RECT = ENEMY1.get_rect(bottomright = (600, 300))


#Get the player (Placeholder)

PLAYER = pygame.image.load("GameAssets/Player2.png").convert_alpha()
PLAYER_RECT = PLAYER.get_rect(midbottom = (80, 300))
PLAYER_GRAV = 0

clock = pygame.time.Clock()

#GAME CONFIGURATION
while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        exit()
      
      #Make the player jump 
      if event.type  == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
          PLAYER_GRAV = -20

    #Load the assets
    screen.blit(SKY, (0,0))
    screen.blit(GROUND, (0,300))


    pygame.draw.rect(screen, "Red", SCORE_RECT, 2)

    screen.blit(SCORE, SCORE_RECT)
    
    ENEMY_RECT.x += -3
    if ENEMY_RECT.right <= 0:
      ENEMY_RECT.left = 800
   
    screen.blit(ENEMY1, ENEMY_RECT)

    PLAYER_GRAV += 1
    PLAYER_RECT.y += PLAYER_GRAV
    if PLAYER_RECT.bottom >= 300:
      PLAYER_RECT.bottom = 300
    screen.blit(PLAYER, PLAYER_RECT)

    pygame.display.update()
    clock.tick(60)
