import pygame
import numpy as np
import math
import random


# 1. Initialize Pygame engine
pygame.init()

# 2. FULLSCREEN Configurations
# This automatically detects your exact monitor dimensions
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
WIDTH, HEIGHT = screen.get_size() # Gets your full width and height

pygame.display.set_caption("My Sandbox Engine")
clock = pygame.time.Clock()


#ID identifiers
EMPTY=0 
SAND=1
#color
SAND_COLOR=(225, 190, 110) 
#Dimensions
CELL_SIZE=8
#DIVIDING SCREEN INTO 8X8 GRIDS
GRID_W= WIDTH // CELL_SIZE
GRID_H=HEIGHT // CELL_SIZE
#creating matrix
grid=np.zeros((GRID_W,GRID_H),dtype=int)

def Physics():
    for y in range(GRID_H -2 ,-1,-1):
        for x in range (GRID_W):
            if grid[x,y] ==SAND:
                if grid[x,y+1] ==EMPTY:
                    #replaces old cell w new cell
                    grid[x,y] =EMPTY
                    grid[x,y+1]=SAND

# 3. Main Engine Loop
running = True
while running:
    # Set background color to dark slate gray
    screen.fill((30, 30, 40))

    # Check for engine quit events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # SAFEGUARD: Press the Escape key to exit fullscreen!
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    #mouse pressing code
    mouse_press=pygame.mouse.get_pressed()
    if mouse_press[0]:
        mx,my=pygame.mouse.get_pos()
        gx= mx // CELL_SIZE
        gy= my // CELL_SIZE

    #safety for not clicking outside of screen 
        if 0<gx<GRID_W and 0<gy<GRID_H:
            grid[gx,gy]=SAND
    Physics()
    for x in range(GRID_W):
        for y in range(GRID_H):
          if grid[x,y] ==SAND:
               rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
               pygame.draw.rect(screen, SAND_COLOR, rect)

    # Refresh screen visuals
    pygame.display.flip()
    
    # Cap framework velocity at 60 FPS
    clock.tick(0)
    

pygame.quit()
