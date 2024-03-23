import pygame
from math import cos, sin, pi
import datetime

_image_library = {}
def get_image(path):
        global _image_library
        image = _image_library.get(path)
        if image == None:
                image = pygame.image.load(path)
                _image_library[path] = image
        return image
        
pygame.init()

screen = pygame.display.set_mode((850, 850))
center = screen.get_rect().center

done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    current_time = datetime.datetime.now()
    sec = current_time.second
    minute = current_time.minute
    screen.fill((255,255,255))
    screen.blit(get_image('clock.jpeg'), (0,0))
    
    rotated_min = pygame.transform.rotate(pygame.transform.rotate(get_image('min.png'), 85), -minute*6)
    screen.blit(rotated_min, rotated_min.get_rect(center = screen.get_rect().center))
    
    rotated = pygame.transform.rotate(pygame.transform.rotate(get_image('sec.png'), 90), -sec*6)
    screen.blit(rotated, rotated.get_rect(center = screen.get_rect().center))
    
    pygame.display.flip()
    clock.tick(60)
    