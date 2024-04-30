import pygame
from color_palette import *
import random
SCORE = 0
addition = 1
start_time = 0
def draw_grid(screen, width, height, cell):
    for i in range(height // 2):
        for j in range(width // 2):
            pygame.draw.rect(screen, colorGRAY, (i * cell, j * cell, cell, cell), 1)

def draw_grid_chess(screen, width, height, cell, color1, color2):
    colors = [color1, color2]

    for i in range(height // 2):
        for j in range(width // 2):
            pygame.draw.rect(screen, colors[(i + j) % 2], (i * cell, j * cell, cell, cell))

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x}, {self.y}"

class Snake:
    def __init__(self, body):
        self.body = body
        if self.body[0].y == self.body[1].y and self.body[0].x > self.body[-1].x:
            self.dx = 1
            self.dy = 0
        if self.body[0].y == self.body[1].y and self.body[0].x < self.body[-1].x:
            self.dx = -1
            self.dy = 0
        if self.body[0].x == self.body[1].x and self.body[0].y < self.body[-1].y:
            self.dx = 0
            self.dy = -1
        if self.body[0].x == self.body[1].x and self.body[0].y > self.body[-1].y:
            self.dx = 0
            self.dy = 1
    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y

        self.body[0].x += self.dx
        self.body[0].y += self.dy

    def draw(self, screen, cell):
        head = self.body[0]
        pygame.draw.rect(screen, colorRED, (head.x * cell, head.y * cell, cell, cell))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorYELLOW, (segment.x * cell, segment.y * cell, cell, cell))

    def check_collision(self, food):
        global FPS, SCORE, addition
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:
            if self.body[-2].y == self.body[-1].y and self.body[-1].x>self.body[-2].x:
                self.body.append(Point(self.body[-1].x+1, self.body[-1].y))
            elif self.body[-2].y == self.body[-1].y and self.body[-1].x<self.body[-2].x:
                self.body.append(Point(self.body[-1].x-1, self.body[-1].y))
            elif self.body[-2].x == self.body[-1].x and self.body[-1].y>self.body[-2].y:
                self.body.append(Point(self.body[-1].x, self.body[-1].y+1))
            elif self.body[-2].x == self.body[-1].x and self.body[-1].y<self.body[-2].y:
                self.body.append(Point(self.body[-1].x, self.body[-1].y-1))
            return True
    def check_wall(self):
        head = self.body[0]
        if head.x == 27 or head.y == 21 or head.x == -1 or head.y == -1:
            return True
    def check_self(self):
        head = self.body[0]
        for i in range(1,len(self.body)):
            if head.x == self.body[i].x and head.y == self.body[i].y:
                return True
    def check_obstacles(self, wall):
        head = self.body[0]
        for i in range(len(wall.body)):
            if head.x == wall.body[i].x and head.y == wall.body[i].y:
                return True
class Food:
    def __init__(self):
        self.pos = Point(9, 9)
    def draw(self, screen, cell):
        pygame.draw.rect(screen, colorGREEN, (self.pos.x * cell, self.pos.y * cell, cell, cell))
    def disappearing(self,snake, walls, screen, cell):
        import time
        global start_time
        end_time = time.time()
        if end_time - start_time >= 3:
            self.update(snake, walls, screen, cell)
    def update(self, snake, walls, screen, cell):
        import time
        global start_time
        self.pos = Point(random.randint(0, 26), random.randint(0, 20))
        for i in snake.body:
            if self.pos.x == i.x and self.pos.y == i.y: #check if snake's coordinates coincide with food's coordinates
                self.update(snake, walls, screen, cell)
        for wall in walls.body:
            if self.pos.x == wall.x and self.pos.y == wall.y:
                self.update(snake, walls, screen, cell)
        self.draw(screen, cell)
        start_time = time.time()
        
class Wall:
    def __init__(self):
        self.rect = [Point(5,4), Point(6,4), Point(7,4), Point(5,5), Point(6,5), Point(7,5), Point(20,11), Point(21,11), Point(20, 12), Point(21,12), Point(20,13), Point(21,13)]
        self.gap = [Point(3, 13), Point(3, 14), Point(3, 15), Point(3, 16), Point(4, 16),Point(5, 16),Point(6, 16), Point(5, 13), Point(6, 14), Point(5, 14)]
        self.body = self.rect + self.gap
    def draw(self, screen, cell):
        for i in range(len(self.body)):
            pygame.draw.rect(screen, colorYELLOW, (self.body[i].x * cell, self.body[i].y * cell, cell, cell))
