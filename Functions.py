import pygame as pg

# Loading the images

bee = pg.image.load("bee.PNG")
beerect = bee.get_rect()

flower = pg.image.load("flower.png")
flowerrect = flower.get_rect()

beehive = pg.image.load("beehive.png")
beehiverect = beehive.get_rect()

biker = pg.image.load("persons .PNG")
bikerrect = biker.get_rect()

tree = pg.image.load("tree.png")
treerect = tree.get_rect()

delivery = pg.image.load("delivery.png")
deliveryrect = delivery.get_rect()


# wrongmap.txt

def load_map (mapfile):
    map = []
    biker_pos = []
    bee_pos = []
    with open(mapfile,"r") as f:
        lines = f.readlines()
        line_coord = 0
        for line in lines:
            char_coord = 0
            map.append(list(line.strip()))
            for char in line:
                if char == "P":
                    biker_pos.append((line_coord,char_coord))
                if char == "B":
                    bee_pos.append((line_coord,char_coord))
                char_coord += 1
            line_coord += 1
        mapfile = f.read()
    return map,biker_pos,bee_pos

# 2 - Initializing the screen

def init_screen(nrows, ncols):
    scr = pg.display.set_mode((nrows*30,ncols*30))
    return scr

# 3 - Drawing Functions ( Filling the Screen )

def draw_map (scr,map):
    for row_idx, row in enumerate(map):
        for col_idx, char in enumerate(row):
            if char == "#":
                treerect.center = (col_idx*30+15, row_idx*30+15)
                scr.blit(tree,treerect)
            elif char == "W":
               beehiverect.center = (col_idx * 30 + 15, row_idx * 30 + 15)
               scr.blit(beehive, beehiverect)
            elif char == "F":
                flowerrect.center = (col_idx * 30 + 15, row_idx * 30 + 15)
                scr.blit(flower,flowerrect)
            elif char == "D":
                deliveryrect.center = (col_idx * 30 + 15, row_idx * 30 + 15)
                scr.blit(delivery,deliveryrect)
    return scr


def draw_bee (scr,pos):
    for (row, col) in pos:
       beerect.center = (col*30+15,row*30+15)
       scr.blit(bee,beerect)
    return scr

def draw_biker (scr,pos):
    for (row,col) in pos:
        bikerrect.center = (col*30+15, row*30+15)
        scr.blit(biker, bikerrect)
    return scr

# 4 - Making Pacman and the Ghosts move

STOP, UP, DOWN, LEFT, RIGHT = (0, 0), (0, -1), (0, 1), (-1, 0), (1, 0)
direction = STOP or UP or DOWN or LEFT or RIGHT

def move (pos, direction, speed):
    newpos = []
    for coord in pos:
        y = coord[0]
        x = coord[1]

        # moving with rounding position
        if direction == STOP:
            newpos.append((y,x))
        elif direction == UP:
            x = round(x)
            y = y + direction[1]*speed
            newpos.append((y,x))
        elif direction == DOWN:
            x = round(x)
            y = y + direction[1]*speed
            newpos.append((y,x))
        elif direction == LEFT:
            y = round(y)
            x = x + direction[0]*speed
            newpos.append((y,x))
        elif direction == RIGHT:
            y = round(y)
            x = x + direction[0]*speed
            newpos.append((y,x))
    return newpos


