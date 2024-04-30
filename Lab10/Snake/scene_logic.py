import pygame
import time
from color_palette import *
from snake import Point, Snake, Food, Wall, draw_grid_chess
#from db import *
from username import *

import psycopg2
LEVEL = 1
body_pause = [Point(10, 11), Point(10, 12), Point(10, 13)] 
conn = psycopg2.connect(
    host='localhost', 
    dbname='snake_data', 
    user='postgres', 
    password='Фныщ2005'
    )
cur = conn.cursor()
cur.execute("""DROP TABLE snake;""")
conn.commit()

cur.execute("""CREATE TABLE snake (
            ID SERIAL PRIMARY KEY,
            Username VARCHAR(255),
            Score INTEGER,
            Level INTEGER
);
""")
conn.commit()

def insert_data(username, score, cur):
    cur.execute(f"""INSERT INTO snake (Username, Score, Level) VALUES
                ('{username}', {score}, {LEVEL});""")
    conn.commit()
def selecting_data(username):
    cur.execute(f"""SELECT Score FROM snake
                WHERE Username = '{username}';""")
    row = cur.fetchone()
    if row:
        return row[0]
    else:
        return ''
    conn.commit()
def check_username(username):
    cur.execute(f"""SELECT '{username}' FROM snake;""")
    row = cur.fetchone()
    if row:
        return True
    else:
        return False
def update_data(username, score):
    cur.execute(f"""UPDATE snake
                SET Score = {score}
                WHERE Username = '{username}';""")
    conn.commit()
FPS = 10
SCORE = 0
cnt = 0
class SceneBase:
    def __init__(self):
        self.next = self
    
    def ProcessInput(self, events, pressed_keys):
        print("uh-oh, you didn't override this in the child class")

    def Update(self):
        print("uh-oh, you didn't override this in the child class")

    def Render(self, screen):
        print("uh-oh, you didn't override this in the child class")

    def SwitchToScene(self, next_scene):
        self.next = next_scene
    
    def Terminate(self):
        self.SwitchToScene(None)

def run_game(width, height, starting_scene):
    pygame.init()
    global FPS
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()

    active_scene = starting_scene

    while active_scene != None:
        pressed_keys = pygame.key.get_pressed()
        
        # Event filtering
        filtered_events = []
        for event in pygame.event.get():
            quit_attempt = False
            if event.type == pygame.QUIT:
                quit_attempt = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit_attempt = True
            if quit_attempt:
                active_scene.Terminate()
            else:
                filtered_events.append(event)
        active_scene.ProcessInput(filtered_events, pressed_keys)
        active_scene.Update(screen)
        active_scene.Render(screen)
        
        active_scene = active_scene.next
        
        pygame.display.flip()
        clock.tick(FPS)

# The rest is code where you implement your game using the Scenes model

class MenuScene(SceneBase):
    def __init__(self):
        super().__init__()
        self.menu_items = ["Play", "Continue", "Options", "Quit"]
        self.active_index = 0
        pygame.font.init()
        self.font = pygame.font.SysFont("sfpro", 60)
    
    def ProcessInput(self, events, pressed_keys):
        global USERNAME
        global cnt, body_pause
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and self.active_index == 0:
                    # Move to the next scene when the user pressed Enter
                    body_pause = [Point(10, 11), Point(10, 12), Point(10, 13)] 
                    self.SwitchToScene(FirstLevel())
                elif event.key == pygame.K_RETURN and self.active_index == 1:
                    self.SwitchToScene(FirstLevel())
                elif event.key == pygame.K_RETURN and self.active_index == 3:
                    self.Terminate()
                elif event.key == pygame.K_DOWN:
                    self.active_index += 1
                    if self.active_index >= len(self.menu_items):
                        self.active_index = 0
                elif event.key == pygame.K_UP:
                    self.active_index -= 1
                    if self.active_index < 0:
                        self.active_index = len(self.menu_items) - 1
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        USERNAME = USERNAME[:-1]
                    elif event.key == pygame.K_SPACE:
                        cnt+=1
                        if cnt%2 != 0:
                            insert_data(USERNAME, SCORE, cur)
                    elif cnt%2 == 0:
                        USERNAME += event.unicode

    def Update(self, screen):
        pass
    
    def Render(self, screen):
        global USERNAME, SCORE, input_window, cur, scores
        # For the sake of brevity, the title scene is a blank red screen
        screen.fill((255, 0, 0))
        for i, item in enumerate(self.menu_items):
            text = item
            if i == self.active_index:
                text = '+' + text

            rendered_text = self.font.render(text, True, colorBLACK)
            screen.blit(rendered_text, (60, i * 60 + 60))
        text_to_screen(screen, USERNAME, input_window)
        text1 = font.render('Create profile', True, colorYELLOW)
        screen.blit(text1, (490, 55))
        if check_username(USERNAME):
            record1 = font.render(f'Your record: {selecting_data(USERNAME)}', True, colorYELLOW)
            record2 = font.render(f'Your level: {LEVEL}', True, colorYELLOW)
            screen.blit(record1, (480, 120))
            screen.blit(record2, (490, 150))

#LOGIC FOR LEVELS
class GameScene(SceneBase):
    def __init__(self):
        super().__init__()
        self.cell = 30
        self.snake = Snake(body_pause)
        self.food = Food()
        self.wall = Wall()
    def ProcessInput(self, events, pressed_keys):
        global body_pause
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.snake.dx = 1
                    self.snake.dy = 0
                elif event.key == pygame.K_LEFT:
                    self.snake.dx = -1
                    self.snake.dy = 0
                elif event.key == pygame.K_DOWN:
                    self.snake.dx = 0
                    self.snake.dy = 1
                elif event.key == pygame.K_UP:
                    self.snake.dx = 0
                    self.snake.dy = -1 
                elif event.key == pygame.K_SPACE:
                    body_pause = self.snake.body
    def Update(self, screen):
        global SCORE, USERNAME
        self.snake.move()
    def Render(self, screen):
        self.food.disappearing(self.snake, self.wall, screen, self.cell)

#NEW LEVELS
class FirstLevel(GameScene):
    def __init__(self):
        super().__init__()
    def ProcessInput(self, events, pressed_keys):
        super().ProcessInput(events, pressed_keys)
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.SwitchToScene(MenuScene())
                #if event.key == pygame.K_1:
                    #time.sleep(100)
    def Update(self, screen):
        global FPS, SCORE, body_pause
        super().Update(screen)
        FPS = 10
        if self.snake.check_wall():
            body_pause = [Point(10, 11), Point(10, 12), Point(10, 13)] 
            self.SwitchToScene(MenuScene())
            SCORE = 0
        if self.snake.check_self():
            body_pause = [Point(10, 11), Point(10, 12), Point(10, 13)] 
            self.SwitchToScene(MenuScene())
            SCORE = 0
        if self.snake.check_collision(self.food) and SCORE ==10:
            SCORE +=1
            self.SwitchToScene(NewLevelMenu())
        elif self.snake.check_collision(self.food):
            SCORE+=1
            update_data(USERNAME, SCORE)
            self.food.update(self.snake, self.wall, screen, self.cell)
    def Render(self, screen):
        super().Render(screen)
        width = screen.get_width()
        height = screen.get_height()
        draw_grid_chess(screen, width, height, self.cell, colorWHITE, colorGRAY)
        self.snake.draw(screen, self.cell)
        self.food.draw(screen, self.cell)
class SecondLevel(GameScene):
    def __init__(self):
        super().__init__()
    def ProcessInput(self, events, pressed_keys):
        super().ProcessInput(events, pressed_keys)
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.SwitchToScene(NewLevelMenu())
    def Update(self, screen):
        super().Update(screen)
        global FPS, SCORE, body_pause
        FPS = 15
        if self.snake.check_wall():
            self.SwitchToScene(NewLevelMenu())
            body_pause = [Point(10, 11), Point(10, 12), Point(10, 13)]
            SCORE = 10
        if self.snake.check_self():
            body_pause = [Point(10, 11), Point(10, 12), Point(10, 13)]
            self.SwitchToScene(NewLevelMenu())
        if self.snake.check_obstacles(self.wall):
            self.SwitchToScene(NewLevelMenu())
            SCORE = 10
        if self.snake.check_collision(self.food) and SCORE ==19:
            SCORE +=1
            self.SwitchToScene(FinalLevelMenu())
        elif self.snake.check_collision(self.food):
            SCORE+=1
            update_data(USERNAME, SCORE)
            self.food.update(self.snake, self.wall, screen, self.cell)
    def Render(self, screen):
        super().Render(screen)
        width = screen.get_width()
        height = screen.get_height()
        draw_grid_chess(screen, width, height, self.cell, colorBLACK, colorBLACK)
        self.snake.draw(screen, self.cell)
        self.food.draw(screen, self.cell)
        self.wall.draw(screen, self.cell)
class NewLevelMenu(SceneBase):
    def __init__(self):
        super().__init__()
        global LEVEL
        self.menu_items = ["Play", "Continue", "Quit"]
        self.active_index = 0
        pygame.font.init()
        self.font = pygame.font.SysFont("sfpro", 60)
        LEVEL = 2
    def ProcessInput(self, events, pressed_keys):
        global body_pause
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and self.active_index == 0: 
                    # Move to the next scene when the user pressed Enter
                    body_pause = [Point(10, 11), Point(10, 12), Point(10, 13)] 
                    self.SwitchToScene(SecondLevel())
                elif event.key == pygame.K_RETURN and self.active_index == 1:
                    self.SwitchToScene(SecondLevel())
                elif event.key == pygame.K_DOWN:
                    self.active_index += 1
                    if self.active_index >= len(self.menu_items):
                        self.active_index = 0
                elif event.key == pygame.K_UP:
                    self.active_index -= 1
                    if self.active_index < 0:
                        self.active_index = len(self.menu_items) - 1
    def Update(self, screen):
        pass
    def Render(self, screen):
        screen.fill((255, 0, 0))
        for i, item in enumerate(self.menu_items):
            text = item
            if i == self.active_index:
                text = '+'+text
            rendered_text = self.font.render(text, True, colorBLACK)
            screen.blit(rendered_text, (325, i * 60 + 225))
        if check_username(USERNAME):
            record1 = font.render(f'Your record: {selecting_data(USERNAME)}', True, colorYELLOW)
            record2 = font.render(f'Your level: {LEVEL}', True, colorYELLOW)
            screen.blit(record1, (315, 120))
            screen.blit(record2, (320, 150))
class FinalLevelMenu(NewLevelMenu):
    def __init__(self):
        super().__init__()
        LEVEL = 3
    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and self.active_index == 0:
                    # Move to the next scene when the user pressed Enter
                    self.SwitchToScene(FirstLevel())
                elif event.key == pygame.K_DOWN:
                    self.active_index += 1
                    if self.active_index >= len(self.menu_items):
                        self.active_index = 0
                elif event.key == pygame.K_UP:
                    self.active_index -= 1
                    if self.active_index < 0:
                        self.active_index = len(self.menu_items) - 1
    def Update(self, screen):
        pass
    def Render(self, screen):
        super().Render(screen)
        final_text = "FINAL"
        final_render = self.font.render(final_text, True, colorYELLOW)
        screen.blit(final_render, (325, 400))
run_game(800, 600, MenuScene())