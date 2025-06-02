import pygame as pg
import Functions as F
from math import sqrt

map, biker_pos,bee_pos = F.load_map("map.txt")

stop, up, down, left, right = (0,0), (0,-1), (0,1), (-1, 0), (1,0)

pg.init()
pg.mixer.init()
scr = pg.display.set_mode((len(map[0])*30, len(map)*30))
wait_time = 10
running = True

pg.mixer.music.load("background.mp3")
pg.mixer.music.set_volume(0.4)
pg.mixer.music.play(-1)

while running:
    pg.event.pump()
    keys = pg.key.get_pressed()

    if keys[pg.K_ESCAPE]:
        running = False

    elif keys[pg.K_UP]:
        direction = up

    elif keys[pg.K_DOWN]:
        direction = down

    elif keys[pg.K_LEFT]:
        direction = left

    elif keys[pg.K_RIGHT]:
        direction = right

    else:
        direction = stop

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False


    scr.fill((60,95,45)) #clear the screen

    #GAME
    F.draw_map(scr,map)
    F.draw_bee(scr, bee_pos)
    F.draw_biker(scr, biker_pos)


    pg.display.flip() # show what was created in memory
    pg.time.wait(wait_time)

    for bik_row, bik_col in biker_pos:
        for bee_row, bee_col in bee_pos:
            distance = sqrt((bik_row - bee_row) ** 2 + (bik_col - bee_col) ** 2)
            if distance < 1:
                print("Game Over!")
                pg.mixer.music.stop()
                running = False

pg.quit()

