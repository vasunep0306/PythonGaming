import pygame, sys
from pygame.locals import *

#set up pygame
pygame.init()

#Set up the window
windowSurface = pygame.display.set_mode((500,400), 0, 32)
pygame.display.set_caption('Hello World')

#Set up the colors
colors = dict()
colors["BLACK"] = (0,0,0)
colors["WHITE"] = (255,255,255)
colors["RED"] = (255,0,0)
colors["GREEN"] = (0,255,0)
colors["BLUE"] = (0,0,255)
colors["GRAY"] = (128,128,128)

# Set up the fonts
basicFont = pygame.font.SysFont(None, 48)

