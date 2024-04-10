import pygame
import time, random
from color_palette import *

pygame.init()

WIDTH = 600
HEIGHT = 600
SCORE = 0
CELL = 30
FPS = 6
addition = 1
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
def draw_grid():
    for i in range(HEIGHT // 2):
        for j in range(WIDTH // 2):
            pygame.draw.rect(screen, colorGRAY, (i * CELL, j * CELL, CELL, CELL), 1)

def draw_grid_chess():
    colors = [colorWHITE, colorGRAY]

    for i in range(HEIGHT // 2):
        for j in range(WIDTH // 2):
            pygame.draw.rect(screen, colors[(i + j) % 2], (i * CELL, j * CELL, CELL, CELL))

screen = pygame.display.set_mode((HEIGHT, WIDTH))

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x}, {self.y}"

class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx = 1
        self.dy = 0
    def move(self):
    
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y
        self.body[0].x += self.dx
        self.body[0].y += self.dy

    def draw(self):
        head = self.body[0]
        pygame.draw.rect(screen, colorRED, (head.x * CELL, head.y * CELL, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def check_collision(self, food):
        global FPS, SCORE, addition
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:
            #for various snake's poses
            if head.y == self.body[-1].y and self.body[-1].x>head.x:
                self.body.append(Point(self.body[-1].x+1, head.y))
            elif head.y == self.body[-1].y and self.body[-1].x<head.x:
                self.body.append(Point(self.body[-1].x-1, head.y))
            elif head.x == self.body[-1].x and self.body[-1].y>head.y:
                self.body.append(Point(self.body[-1].x, self.body[-1].y+1))
            elif head.x == self.body[-1].x and self.body[-1].y<head.y:
                self.body.append(Point(self.body[-1].x, self.body[-1].y-1))
            elif head.x == self.body[1].x:
                if head.y<self.body[-1].y:
                    self.body.append(Point(self.body[-1].x+1, self.body[-1].y))
                else:
                    self.body.append(Point(self.body[-1].x-1, self.body[-1].y))
            elif head.y == self.body[1].y:
                if head.x<self.body[-1].x:
                    self.body.append(Point(self.body[-1].x, self.body[-1].y-1))
                else:
                    self.body.append(Point(self.body[-1].x, self.body[-1].y+1))
            # self.body.append(Point(head.x, head.y))
            FPS+=1
            SCORE+=addition
            #after every five eaten food the level is changed
            if FPS%5==0:
                addition+=1
            food.update(self)
    def check_wall(self):
        head = self.body[0]
        if head.x == 21 or head.y == 21 or head.x == -1 or head.y == -1:
            return True
    def check_self(self):
        head = self.body[0]
        for i in range(1,len(self.body)):
            if head.x == self.body[i].x and head.y == self.body[i].y:
                return True

class Food:
    def __init__(self):
        self.pos = Point(9, 9)
    def draw(self):
        pygame.draw.rect(screen, colorGREEN, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))
    def update(self, snake):
        self.pos = Point(random.randint(0, 20), random.randint(0, 20))
        for i in snake.body:
            if self.pos.x == i.x and self.pos.y == i.y: #check if snake's coordinates coincide with food's coordinates
                self.update(snake)
        self.draw()


clock = pygame.time.Clock()
food = Food()
snake = Snake()

done = False
while not done:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake.dx = 1
                snake.dy = 0
            elif event.key == pygame.K_LEFT:
                snake.dx = -1
                snake.dy = 0
            elif event.key == pygame.K_DOWN:
                snake.dx = 0
                snake.dy = 1
            elif event.key == pygame.K_UP:
                snake.dx = 0
                snake.dy = -1
    result = font.render(f"Your score: {SCORE}", True, colorYELLOW)
    level_result = font.render(f"Your level: {FPS//5}", True, colorYELLOW)
    level = font_small.render(f"{FPS//5}", True, colorBLUE)
    if snake.check_wall():
        screen.fill(colorRED)
        screen.blit(result, (85, 250))
        screen.blit(level_result, (85, 180))
        pygame.display.flip()
        time.sleep(2)
        done = True
    elif snake.check_self():
        screen.fill(colorRED)
        pygame.display.flip()
        
        done = True
    else:
        draw_grid_chess()
        screen.blit(level, (10, 10))
        food.draw()
        snake.move()
        snake.check_collision(food)
        
        snake.draw()
    
    pygame.display.flip()
    clock.tick(FPS)