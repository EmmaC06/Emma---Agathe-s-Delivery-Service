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

startscreen = pg.image.load("scrstart.png")
startscreenrect = startscreen.get_rect()


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

# 4 - Making Biker and the Bees move

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


def check_tree (pos, direction, maze):
    tree = []
    for row_idx, row in enumerate(maze):
        for col_idx, char in enumerate(row):
            if char == "#":
                tree.append((row_idx, col_idx))

    for (row_idx, col_idx) in pos:
        check_row = round (row_idx + direction[1]*0.5)
        check_col = round (col_idx + direction[0]*0.5)
        if (check_row, check_col) in tree:
            return True
    return False

def check_behive (pos, direction, maze):
    hive = []
    for row_idx, row in enumerate(maze):
        for col_idx, char in enumerate(row):
            if char == "W":
                hive.append((row_idx, col_idx))

    for (row_idx, col_idx) in pos:
        check_row = round (row_idx + direction[1]*0.5)
        check_col = round (col_idx + direction[0]*0.5)
        if (check_row, check_col) in hive:
            return True
    return False

def bee_move(pos, direction, maze):
    directions = [UP, DOWN, LEFT, RIGHT]
    possible_direction = {UP : DOWN, DOWN : UP, LEFT : RIGHT, RIGHT : LEFT}

    possible = []

    for direction in directions:
        if direction == possible_direction.get(direction):
            continue #allows the bees to not go back directly

        #Next cells
        next_row = round(pos[0] + direction[1]*0.5)
        next_col = round(pos[1] + direction[0] * 0.5)

        if 0 <= next_row < len(maze) and 0 <= next_col < len(maze[0]):
            if maze[next_row][next_col] != "#" :
                possible.append(direction)

    return possible

# start screen: draw screen and press 'b'
def start_screen(scr, map):
    # Draw the start screen image
    scr.blit(startscreen, (0, 0))
    
    # Set up fonts
    title_font = pg.font.Font(None, 48)
    story_font = pg.font.Font(None, 28)
    small_font = pg.font.Font(None, 22)

    black = (0, 0, 0)

    # title
    title = "Thank you for choosing EA Delivery Service"
    titlesurface = title_font.render(title, True, black)
    title_rect = titlesurface.get_rect(center=(660, 80))
    scr.blit(titlesurface, title_rect)

    # story
    story1 = "Agathe and Emma found bee hives. Help them"
    story2 = "collect all flowers and deliver it to the"
    story3 = "house, avoiding the b(ee)'s! Don't get stung"
    story4 = "and don't be late, it'll cost you loads!"

    storysurface1 = story_font.render(story1, True, black)
    story_rect1 = storysurface1.get_rect(center=(660, 120))
    scr.blit(storysurface1, story_rect1)

    storysurface2 = story_font.render(story2, True, black)
    story_rect2 = storysurface2.get_rect(center=(660, 150))
    scr.blit(storysurface2, story_rect2)

    storysurface3 = story_font.render(story3, True, black)
    story_rect3 = storysurface3.get_rect(center=(660, 180))
    scr.blit(storysurface3, story_rect3)

    storysurface4 = story_font.render(story4, True, black)
    story_rect4 = storysurface4.get_rect(center=(660, 210))
    scr.blit(storysurface4, story_rect4)


    # True story
    truestory_surface = small_font.render("[Based on a true story]", True, black)
    truestory_rect = truestory_surface.get_rect(center=(660, 250))
    scr.blit(truestory_surface, truestory_rect)

    # Press B to start
    pressb_surface = small_font.render("Press 'B' to start", True, black)
    pressb_rect = pressb_surface.get_rect(center=(660, 300))
    scr.blit(pressb_surface, pressb_rect)

    pg.display.flip()
    
    startwait = True
    while startwait:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_b:
                    startwait = False
        pg.time.wait(100)

    # shows message after pressing on a b(ee)
    scr.fill((60, 95, 45))  
    background = draw_map(scr, map)
    scr.blit(background, (0, 0))
    font = pg.font.Font(None, 40)
    text = font.render("oh no! you pressed on a bee, all the b(ee)'s are looking for you now. Run!", True, (255, 255, 0))
    text_rect = text.get_rect(center=(scr.get_width() // 2, scr.get_height() // 2))
    scr.blit(text, text_rect)
    pg.display.flip()

    # press key again
    wait = True
    while wait:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.KEYDOWN:
                wait = False
        pg.time.wait(300)

# drawing final screen
def final_screen(scr, map):
    scr.fill((60, 95, 45))  
    background = draw_map(scr, map)
    scr.blit(background, (0, 0))
    
    font = pg.font.Font(None, 40)
    text = font.render("thankyou for the flowers! it took you a while though", True, (255, 255, 0))
    text_rect = text.get_rect(center=(scr.get_width() // 2, scr.get_height() // 2))
    scr.blit(text, text_rect)
    
    pg.display.flip()

    pg.time.wait(3000)

