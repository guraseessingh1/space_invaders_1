import pygame

pygame.font.init()
pygame.mixer.init()

WIDTH = 900
HEIGHT = 900

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("space invaders")
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
border = pygame.Rect(WIDTH//2-5,0,10,HEIGHT)

HEALTH_FONT =  pygame.font.SysFont("ariel",45)
WINNER_FONT =  pygame.font.SysFont("comicsans",100)

FPS = 60
VELOCITY = 5
B_VELOCITY = 7
MAX_BULLET = 3
SHIP_WIDTH = 55
SHIP_HEIGHT = 40

y_ship_image = pygame.image.load("assets/spaceship_yellow.png")
y_ship_image = pygame.transform.scale(y_ship_image,(SHIP_WIDTH,SHIP_HEIGHT))
yellow_ship = pygame.transform.rotate(y_ship_image,90)