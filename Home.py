import pygame
from Settings import *

text_font = pygame.font.SysFont('EB Garamond', 25)
log = pygame.image.load("logo.png")
logo = pygame.transform.scale(log, (130,130))

Elements_button = pygame.Rect(100, 150, 200, 100)
Quizzes_button = pygame.Rect(400, 150, 200, 100)
Articles_button = pygame.Rect(100, 300, 200, 100)
Shop_button = pygame.Rect(400, 300, 200, 100)

text_surface = text_font.render('Table Of Elements', True, BLACK)
quiz_surface = text_font.render('Quiz', True, BLACK)
article_surface = text_font.render('Articles', True, BLACK)
shop_surface = text_font.render('Hoop Stars', True, BLACK)
title_surface1 = title_font.render('Chemistry Cards', True, BLACK)

def draw():
    screen.blit(logo, (10,10))

    pygame.draw.rect(screen, BUTTON_COLOR, Elements_button)
    screen.blit(text_surface, (120, 200))

    pygame.draw.rect(screen, (BUTTON_COLOR), Quizzes_button)
    screen.blit(quiz_surface, (475, 200))

    pygame.draw.rect(screen, BUTTON_COLOR, Articles_button)
    screen.blit(article_surface, (170, 350))

    pygame.draw.rect(screen, (BUTTON_COLOR), Shop_button)
    screen.blit(shop_surface, (450, 350))

    screen.blit(title_surface1, (195, 50))