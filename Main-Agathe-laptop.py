import pygame as pg
import Functions as F

map, biker_pos,bee_pos = F.load_map("map.txt")

pg.init()
screen = pg.display.set_mode((len(map[0])*30, len(map)*30))
wait_time = 10
running = True

while running:
    pg.event.pump()
    escape = pg.K_ESCAPE.get_pressed()

    if escape[pg.K_ESCAPE]:
        running = False

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False



    screen.fill((0,0,0)) #clear the screen

    #GAME


    pg.display.flip() # show what was created in memory
    pg.time.wait(wait_time)

pg.quit()
