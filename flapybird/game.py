import pygame, sys
from pygame.locals import *

WINDOWWIDTH = 400 # Chiều dài cửa sổ
WINDOWHEIGHT = 300 # Chiều cao cửa sổ

WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)

pygame.init()

### Xác định FPS ###
FPS = 60
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Event')

class Car():
    def __init__(self):
        self.x = 100 # Vị trí của xe
    
    ## Tạo surface và vẽ hình chiếc xe lên đó ##
        self.surface = pygame.Surface((100, 50), SRCALPHA)
        pygame.draw.polygon(self.surface, RED, ((15, 0), (65, 0), (85, 15), (100, 15), (100, 40), (0, 40), (0, 15)))
        pygame.draw.circle(self.surface, GREEN, (15, 40), 10)
        pygame.draw.circle(self.surface, GREEN, (85, 40), 10)
    def draw(self): # Hàm dùng để vẽ xe
        DISPLAYSURF.blit(self.surface, (self.x, 100))

    def update(self, moveLeft, moveRight): # Hàm dùng để thay đổi vị trí xe
        if moveLeft == True:
            self.x -= 2
        if moveRight == True:
            self.x += 2

        if self.x + 100 > WINDOWWIDTH:
            self.x = WINDOWWIDTH - 100
        if self.x < 0:
            self.x = 0

car = Car()
moveLeft = False
moveRight = False
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                moveLeft = True
            if event.key == K_RIGHT:
                moveRight = True
        
        if event.type == KEYUP:
            if event.key == K_LEFT:
                moveLeft = False
            if event.key == K_RIGHT:
                moveRight = False

    DISPLAYSURF.fill(WHITE)
    
    car.draw()
    car.update(moveLeft, moveRight)

    pygame.display.update()
    fpsClock.tick(FPS)