import pygame

pygame.init()
pygame.font.init()

size = 700, 560
screen = pygame.display.set_mode(size)

WHITE = (229, 229, 229)
GREEN = (74, 200, 74)
RED = (200, 0, 0)
YELLOW = (200, 200, 0)
BLUE = (0, 145, 200)
WHITE_FONT = (255, 255, 255)
BLACK = (0, 0, 0)
BUTTON_COLOR = (177, 156, 217)

font = pygame.font.SysFont('EB Garamond', 15)
title_font = pygame.font.SysFont('Times New Roman', 45)
question_font = pygame.font.SysFont('Times New Roman', 25)

table = pygame.image.load("ELEMENTS.png").convert_alpha()
X_buton = pygame.image.load("X_Button.png").convert_alpha()
fire = pygame.image.load("fire.png").convert_alpha()

table_of_elements = pygame.transform.scale(table, (600, 400))
X_Button = pygame.transform.scale(X_buton, (25, 25))
flame = pygame.transform.scale(fire, (25, 25))