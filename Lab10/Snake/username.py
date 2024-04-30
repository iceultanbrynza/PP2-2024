import pygame
from color_palette import *
pygame.font.init()
font = pygame.font.SysFont("Verdana", 24)
USERNAME = ''
input_window = pygame.Rect(500, 85, 140, 32)
def text_to_screen(screen, username_text, input_window):
    text_surface = font.render(username_text, True, colorBLACK)
    pygame.draw.rect(screen, colorWHITE, input_window)
    screen.blit(text_surface, (input_window.x, input_window.y ))