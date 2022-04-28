import pygame, random
pygame.init()

window = pygame.display.set_mode((600,400))
pygame.display.set_caption("cube game")

white = (255,255,255)
yellow = (255,255,0)
magenta = (255, 0, 255)
green = (0, 255, 0)
bg_color = white

speed = 5 
cubeX = 250 
cubeY = 250 
cubeSize = 20 
run = True

cubeSize = 20
food = [random.randrange(1,500),random.randrange(1,500), 10, 10]
Bfood = [random.randrange(1,500),random.randrange(1,500), 10, 10]

while run:
  window.fill(bg_color)
  

  keys = pygame.key.get_pressed()
  if keys[pygame.K_UP]:
    print("up")
  if keys[pygame.K_DOWN]:
    print("down")
  if keys[pygame.K_LEFT]:
    print("left")
  if keys[pygame.K_RIGHT]:
    print("right")
    
  pygame.display.update()
  pygame.event.pump()