import tkinter as tk
from tkinter import ttk
from pprint import pprint

# DONE: Create the Ship and Make it Move
# TODO: Create Smooth Movement / Delta Time
# DONE: Shooting Mechanics
# DONE: RESIZE ASSETS TO FIT THE SCREEN
# DONE: Enemies and its AI
# TODO: Score / HighScore
# TODO: ENEMY SHOOTING
# TODO: SOUNDS
# TODO: GAME LOOP
# TODO: PLAYER LIFES
# TODO: RED ALIEN SPACESHIP
# TODO: BARRIERS

# RESEARCH: GARBAGE COLLECTION

root = tk.Tk()

player_img = tk.PhotoImage(file=r"C:\Users\Thej\Projects\Space-Invaders-Py\Assets\Player\Ship.png") # 16x16 (RESIZED: 6.0x (96x96))
bullet_img = tk.PhotoImage(file=r'C:\Users\Thej\Projects\Space-Invaders-Py\Assets\Player\Bullet.png')

# Enemies
crab_img = tk.PhotoImage(file=r"C:\Users\Thej\Projects\Space-Invaders-Py\Assets\Enemies\Crab-1.png") # 4.0x
squid_img = tk.PhotoImage(file=r"C:\Users\Thej\Projects\Space-Invaders-Py\Assets\Enemies\Squid-1.png")
octo_img = tk.PhotoImage(file=r"C:\Users\Thej\Projects\Space-Invaders-Py\Assets\Enemies\Octo-1.png")
ship_img = tk.PhotoImage(file=r"C:\Users\Thej\Projects\Space-Invaders-Py\Assets\Enemies\Alienship.png")

win_width, win_height = 1280, 720 # 960, 540
scr_width, scr_height = root.winfo_screenwidth(), root.winfo_screenheight()

player_speed = 15 
x = 0

bullets = []

debug_bg = ("Black", "Black", "Black")

squids, crabs, octos = {}, {}, {}
enemies_coords = {}

def config():
    root.title("Space-Invaders")

    x = (scr_width - win_width) // 2
    y = (scr_height - win_height) // 2

    root.geometry(f"{win_width}x{win_height}+{x}+{y}")
    root.resizable(False, False) # Width, Height

    frm = tk.Frame(root, bg=debug_bg[0]) # ROOT FRAME
    frm.pack(fill="both", expand=True)

    return frm

def main_area_draw(frm):
    main_area = tk.Canvas(frm, bg=debug_bg[1], highlightthickness=0)
    main_area.pack(side='bottom', fill=tk.BOTH, expand=True)

    return main_area

def player_draw(frm):
    player_cvw, player_cvh = win_width, 80 # (1280,80) Player Canvas Size
    # MidPoint of Canvas: 1280 // 2 x 80 // 2 = 640 x 40

    x0 = player_cvw // 2
    y0 = player_cvh // 2
    player_area = tk.Canvas(frm, bg=debug_bg[2], height=player_cvh, highlightthickness=0)
    player = player_area.create_image(x0,y0, image=player_img, tags="player")
    # player_area.move(player, 609.6, 0)
   
    player_area.pack(side="bottom", fill=tk.X)

    return player_area, player


def player_move(event, player_area, player, main_area, bullets):
    key_track = []

    player_size = player_area.bbox(player)
    player_coords = player_area.coords(player)
    window_height = root.winfo_width()

    key = event.keysym

    moving_right = False
    moving_left = False
    shooting = False
    
    if (key == "a" or key == "Left") and player_size[0] > 0: # 48 
        player_area.move(player, -player_speed, 0)
    elif (key == "d" or key == "Right") and player_size[2] < window_height:
        player_area.move(player, player_speed, 0)
    elif (key == 'space' or key == "up"):
        player_shoot(main_area, bullets, player_size)
        # winsound.PlaySound(fire_sound, winsound.SND_FILENAME | winsound.SND_ASYNC)
    else:
        player_area.move(player, 0, 0)



def player_shoot(main_area, bullets, player_size):
    bullet_size = 15
    half_size = bullet_size // 2

    x_midpoint = (player_size[0] + player_size[2]) // 2
    # x_midpoint , top_edge
    top_edge = player_size[1] 

    y1 = top_edge + 20 
    offset = 605

    # if len(bullets) < 1:
    bullet = main_area.create_image(x_midpoint, y1 + 590, image=bullet_img, tag="bullet")
    bullets.append(bullet)


def move_bullet(main_area, bullets):
    for bullet in bullets:
        main_area.move(bullet, 0, -15)
        b_coords = main_area.bbox(bullet) 

        if b_coords[3] < 0:
            main_area.delete(bullet)
            bullets.remove(bullet)

    root.after(17, lambda : move_bullet(main_area, bullets))


def find_mid_x(y, space_between, enemy_count, x0, x1):
    x_midpoint, y_midpoint = ((x0 + x1) / 2), ((y + y) / 2)

    distance = (((x_midpoint - x0) ** 2) + ((y_midpoint - y) ** 2)) ** 0.5
    x = (win_width // 2) - distance

    return x

def draw_rows(main_area, x, y, space_between, image_ref, enemy_count, enemy_type):
    for _ in range(enemy_count):
        enemy = main_area.create_image(x, y, image=image_ref, tag="enemy")
        coords = main_area.coords(enemy)

        enemies_coords[enemy] = coords

        x += space_between

    return

def enemies_draw(main_area):
    space_between = 65
    space_between_rows = 50

    enemy_count = 11

    x0 = win_width // 2
    x1 = x0 + (space_between * (enemy_count-1))
    y = 30

    # ROW 1
    y = y + space_between_rows
    x = find_mid_x(y, space_between, enemy_count, x0, x1)
    draw_rows(main_area, x, y, space_between, squid_img, enemy_count, 'squid')

    # ROW 2
    y = y + space_between_rows
    x = find_mid_x(y, space_between, enemy_count, x0, x1)
    draw_rows(main_area, x, y, space_between, crab_img, enemy_count, 'crab')

    # ROW 3
    y = y + space_between_rows
    x = find_mid_x(y, space_between, enemy_count, x0, x1)
    draw_rows(main_area, x, y, space_between, crab_img, enemy_count, 'crab')

    # ROW 4
    y = y + space_between_rows
    x = find_mid_x(y, space_between, enemy_count, x0, x1)
    draw_rows(main_area, x, y, space_between, octo_img, enemy_count, 'octo')

    # ROW 5
    y = y + space_between_rows
    x = find_mid_x(y, space_between, enemy_count, x0, x1)
    draw_rows(main_area, x, y, space_between, octo_img, enemy_count, 'octo')

    # main_area.delete(squid[6])

def move_enemies(main_area, direction, enemy_speed):
    shift = False
    hit_wall = False
    step = 40

    enemies_coords_values = list(enemies_coords.values())
    enemies_coords_values.sort()

    closest_to_right = enemies_coords_values[-1][0]
    closest_to_left = enemies_coords_values[0][0] 

    if direction == 1 and closest_to_right + step >= 1280:
        direction = -1
        shift = True

    elif direction == -1 and closest_to_left - step <= 0:
        direction = 1
        shift = True

    for enemy_id, enemy_coords in enemies_coords.items():
        if shift == True:
            main_area.move(enemy_id, 0, 50)
        else:
            main_area.move(enemy_id, step * direction, 0)


        enemies_coords[enemy_id] = main_area.coords(enemy_id)

    root.after(enemy_speed, lambda: move_enemies(main_area, direction, enemy_speed))

def bullet_overlapping(main_area):
    for enemy_id in list(enemies_coords.keys()):
        enemy_bbox = main_area.bbox(enemy_id)

        bullet_overlap = main_area.find_overlapping(*enemy_bbox)  # (51, 0)

        if len(bullet_overlap) > 1:
            print(bullet_overlap)
            enemies_coords.pop(bullet_overlap[0])
            main_area.delete(bullet_overlap[0])

            bullets.remove(bullet_overlap[1])
            main_area.delete(bullet_overlap[1])

    # print(overlap)
    root.after(17, lambda: bullet_overlapping(main_area))

def main():
    direction = 1
    enemy_speed = 800

    frm = config()
    player_area, player = player_draw(frm)
    main_area = main_area_draw(frm)

    enemies_draw(main_area)

    bullet_overlapping(main_area)
    move_enemies(main_area, direction, enemy_speed)
    move_bullet(main_area, bullets)

    root.bind('<KeyPress>', lambda event: player_move(event, player_area, player, main_area, bullets))


if __name__ == "__main__":
    main()
    root.mainloop()
