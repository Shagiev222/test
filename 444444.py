import pygame as pg

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Bone1:
    w = h = 150
    color = WHITE
    x = 100 
    y = 100
    border = 5 

class Bone2:
    w = h = 150 
    color = WHITE
    x = 100+100 
    y = 100
    border = 5
    
class Bone3:
    w = h = 150 
    color = WHITE 
    x = 100+200 
    y = 100
    border = 5
    
class Bone4:
    w = h = 150 
    color = WHITE 
    x = 100
    y = 100+100
    border = 5

class Bone5:
    w = h = 150 
    color = WHITE 
    x = 100+100
    y = 100+100
    border = 5
    
class Bone6:
    w = h = 150 
    color = WHITE 
    x = 100+200
    y = 100+100
    border = 5



pg.init() 
screen = pg.display.set_mode((1040, 680))
painter = pg.draw
running = True
while running:
    screen.fill(BLACK)
    
    list_events = pg.event.get()
    for event in list_events:
        print(event)
        if event.type == pg.QUIT:
            running = False
    
    pg.display.update() # Обновляем экран
    
pg.quit()