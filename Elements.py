import pygame
from Settings import *

X_button = pygame.Rect(15, 10, 30, 28)

def draw():
    screen.blit(table_of_elements, (60, 50))
    pygame.draw.rect(screen, WHITE, X_button)
    screen.blit(X_Button, (20, 20))