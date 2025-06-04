import pygame as pg
import Functions as F
from math import sqrt
import random

# screen : 1320 x 630

map, biker_pos,bee_pos = F.load_map("map.txt")

STOP, UP, DOWN, LEFT, RIGHT = (0, 0), (0, -1), (0, 1), (-1, 0), (1, 0)
direction = STOP or UP or DOWN or LEFT or RIGHT

biker_speed = 0.1
bee_speed = 0.05

pg.init()
pg.mixer.init()
scr = pg.display.set_mode((len(map[0])*30, len(map)*30))
wait_time = 10
running = True

pg.mixer.music.load("background.mp3")
pg.mixer.music.set_volume(0.4)
pg.mixer.music.play(-1)
print("I am going to win the competition!!!!")

F.start_screen(scr, map)

bees = []
for pos in bee_pos:
    start_direction = random.choice([UP, DOWN, LEFT, RIGHT])
    bees.append ({"pos":list(pos), "direction" :start_direction})

while running:
    pg.event.pump()
    keys = pg.key.get_pressed()

    if keys[pg.K_ESCAPE]:
        running = False

    elif keys[pg.K_UP]:
        direction = UP

    elif keys[pg.K_DOWN]:
        direction = DOWN

    elif keys[pg.K_LEFT]:
        direction = LEFT

    elif keys[pg.K_RIGHT]:
        direction = RIGHT

    else:
        direction = STOP

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False


    scr.fill((60,95,45)) #clear the screen

    #GAME
    F.draw_map(scr,map)
    F.draw_bee(scr, [bee["pos"] for bee in bees])
    F.draw_biker(scr, biker_pos)

    # Move Biker
    if not F.check_tree(biker_pos, direction, map):
        biker_pos = F.move(biker_pos, direction, biker_speed)

        for (row_idx, col_idx) in biker_pos:
            if map[round(row_idx)][round(col_idx)] == "F":
                map[round(row_idx)][round(col_idx)] = " "

    # Move Bees Randomly

    for bee in bees:
        if F.check_tree([bee["pos"]], bee["direction"], map):
            option = F.bee_move(bee["pos"], bee["direction"], map)
            if option:
                bee["direction"] = random.choice(option)
            else:
                bee["direction"] = STOP

        elif F.check_behive([bee["pos"]], bee["direction"], map):
            option = F.bee_move(bee["pos"], bee["direction"], map)
            if option:
                bee["direction"] = random.choice(option)
            else:
                bee["direction"] = STOP

        new_pos = F.move([bee["pos"]], bee["direction"], bee_speed)
        bee["pos"] = new_pos[0]


    pg.display.flip() # show what was created in memory
    pg.time.wait(wait_time)

    # Win
    flower = sum(row.count("F") for row in map)
    if flower == 0:
        print("You win!")
        running = False

    # Lose

    for bik_row, bik_col in biker_pos:
        for bee in bees:
            bee_row, bee_col = bee["pos"]
            distance = sqrt((bik_row - bee_row) ** 2 + (bik_col - bee_col) ** 2)
            if distance < 1:
                print("Game Over!")
                running = False


pg.quit()




