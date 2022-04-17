import sys, pygame
from item import *
pygame.init()

# size represents the size
size = width, height = 640, 480
# backgroundColor represents the background color
backgroundColor = (100, 100, 100)
# the speed of the first ball
ballSpeed1 = [2,4]
# the speed of the seoncd ball1
ballSpeed2 = [1,3]


black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 120)

screen = pygame.display.set_mode(size)

# define two balls
ball = Item(size, ballSpeed1)
ball2 = Item(size, ballSpeed2, blue)

testSurface = pygame.Surface((50,50))

FPS = 20
delta = 1/20
clock = pygame.time.Clock()
isRunning = True
while isRunning:
  for event in pygame.event.get():
    if event.type == pygame.QUIT: sys.exit()
    
  ball.randomBounceOnCollide(ball2.rect)
  ball2.randomBounceOnCollide(ball.rect)  
    
  ball.move(delta)
  ball2.move(delta)
  
  screen.fill(backgroundColor)
  ball.blit(screen)
  ball2.blit(screen)
  pygame.display.flip()
  clock.tick(FPS)
