import math
import random
import pygame

#constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT= 500
PLAYER_START_Y=200
PLAYER_START_X=250
ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150
ENEMY_SPEED_X=4
ENEMY_SPEED_Y = 10
BULLET_SPEED_Y=10
COLLISION_DISTANCE = 27

#initialize pygame
pygame.init()

#create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

#Background
background = pygame.image.load('background.png')

#Caption and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.loaf("ufo.png")
pygame.display.set_icon(icon)

#Player
playerImg = pygame.image.load("player.png")
playerX=PLAYER_START_X
playerY=PLAYER_START_Y 
playerX_change = 0

#Enemy
enemyImg = []
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]
num_of_enemies=10

for _i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0,SCREEN_WIDTH-64)) #64 is the size of the enemy
    enemyY.append(random.randint(ENEMY_START_Y_MIN,ENEMY_START_Y_MAX))
    enemyX_change.append(ENEMY_SPEED_X)
    enemyY_change.append(ENEMY_SPEED_Y)

#BulletImg
bulletImg = pygame.image.load("bullet.png")
bulletX=0
bulletY=PLAYER_START_Y
bulletX_change = 0
bulletY_change=BULLET_SPEED_Y
bullet_state = "ready"

#score
score_value=0
font = pygame.font.Font('freesansbold.ttf',64)
def show_score(x,y):
    #Display the current score on the screen
    score = font.render("Score : "+str(score_value,True ,(255,255,255)))
    screen.blit(over_text,(200,250))

def game_over_text():
    #display the game is over text
    over_text=over_font.render("GAME OVER",True,(254,254,254))
    screen.blit(over_text,(200,250))

def player(x,y):
    #draw the player on the screen
    screen.blit(playerImg,(x,y))

def enemy(x,y,i):
    #Draw an enemy on the screen
    screen.blit(enemyImg[i],(x,y))

def fire_bullet(x,y):
    #Fire a bullet from the player's position
    global bullet_state
    bullet_state = "fire"
    screen_blit(bulletImg, (x+16,y+10))

def iscollision(enemyX,enemyY,bulletX,bulletY):
    #check if there is a collision between the enemy and a bullet
    distance = math.sqrt((enemyX-bulletX)**2 + (enemyY - bulletY)**2)
    return distance < COLLISION_DISTANCE