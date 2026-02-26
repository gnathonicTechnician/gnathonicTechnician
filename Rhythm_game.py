'''
RHYTHM GAME 
by Madison Sagun and Jayla Harris
TBD
'''
import pygame
import math
import os
import sys
os.environ['SDL_AUDIODRIVER'] = 'dsp'

# initializing display
pygame.init()
screen_length = 600
size = screen_length, screen_length
screen = pygame.display.set_mode(size)
running = True
alive = True

# rhythm timing or something
bpm = 140
bps = bpm/60

# icon variables
icon_size = screen_length/6
icon_x = (screen_length/2) - (icon_size/2)
icon_y = (screen_length/2) - (icon_size/2)
img_icon = pygame.image.load("lancer.jpg")
img_icon = pygame.transform.scale(img_icon, (icon_size, icon_size))

def draw_rect(color, x, y, width, height):
    rect = pygame.draw.rect(screen, color, [x, y, width, height], 0, 0)

    return rect

while running:
    screen.fill("#FFFFFF")
    screen.blit(img_icon, (icon_x, icon_y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    pygame.display.update()

pygame.quit()
sys.exit()