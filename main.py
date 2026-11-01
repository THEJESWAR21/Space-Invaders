import tkinter as tk
from tkinter import ttk
from pprint import pprint
import random

# DONE: Create the Ship and Make it Move
# DONE: Create Smooth Movement / Delta Time
# DONE: Shooting Mechanics
# DONE: RESIZE ASSETS TO FIT THE SCREEN
# DONE: Enemies and its AI
# DONE: ENEMY SHOOTING
# DONE: PLAYER LIFES
# DONE: Score

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

debug_bg = ("Black", "Black", "Black")
enemies_coords = {}

pressed_keys = set()

score = 0
player_lifes = 3
enemy_speed = 800

direction = 1
bullets = []
def config():
    root.title("Space-Invaders")

    x = (scr_width - win_width) // 2
    y = (scr_height - win_height) // 2

    root.geometry(f"{win_width}x{win_height}+{x}+{y}")
    root.resizable(False, False) # Width, Height
    root.configure(bg="black")

    frm = tk.Frame(root, bg=debug_bg[0]) # ROOT FRAME
    frm.pack(fill="both", expand=True)

    return frm

def main_area_draw(frm):
    main_area = tk.Canvas(frm, bg=debug_bg[1], highlightthickness=0)
    main_area.pack(side='bottom', fill=tk.BOTH, expand=True)

    return main_area

def player_draw(main_area):
    player_cvw, player_cvh = win_width, 80 # (1280,80) Player Canvas Size
    # MidPoint of Canvas: 1280 // 2 x 80 // 2 = 640 x 40

    x0 = player_cvw // 2
    y0 = win_height - 50
    # main_area = tk.Canvas(frm, bg=debug_bg[2], height=player_cvh, highlightthickness=0)
    player = main_area.create_image(x0,y0, image=player_img, tags="player")
    # main_area.move(player, 609.6, 0)
   
    # main_area.pack(side="bottom", fill=tk.X)

    return player


def on_key_press(event):
    pressed_keys.add(event.keysym)

def on_key_release(event):
    pressed_keys.discard(event.keysym)

def player_move(player, main_area, bullets):
    dx, dy = 0 , 0
    player_speed = 15 

    player_size = main_area.bbox(player)
    player_coords = main_area.coords(player)
    window_height = root.winfo_width()

    if ('a' in pressed_keys) and (player_size[0] > 0):
        dx = -player_speed
    elif ('d' in pressed_keys) and (player_size[2] < window_height):
        dx = player_speed

    if dx != 0 or dy != 0:
        main_area.move(player, dx, dy)

    root.after(30, lambda: player_move(player, main_area, bullets))

def player_shoot(event, bullets, player, main_area):
    player_size = main_area.bbox(player)

    bullet_size = 15
    half_size = bullet_size // 2

    x_midpoint = (player_size[0] + player_size[2]) // 2
    # x_midpoint , top_edge
    top_edge = player_size[1] 

    y1 = top_edge
    offset = 20

    # if len(bullets) < 3:
    bullet = main_area.create_image(x_midpoint, y1 - offset, image=bullet_img, tag="bullet")
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

def bullet_overlapping(main_area, bullets, score_ui, score):
    for bullet in bullets:
        bullet_bbox = main_area.bbox(bullet)
        bullet_overlap = main_area.find_overlapping(*bullet_bbox)
      
        if len(bullet_overlap) > 1:
            for overlap_id in bullet_overlap:
                enemy_tag = main_area.gettags(overlap_id)
                try:
                    if enemy_tag[0] == "enemy":
                        enemies_coords.pop(overlap_id)
                        main_area.delete(overlap_id)

                        bullets.remove(bullet_overlap[-1])
                        main_area.delete(bullet_overlap[-1])
                        score += 50
                        main_area.itemconfig(score_ui, text=f"SCORE: {score}")
                        print('Enemy', overlap_id, 'DIED')
                        break
                except IndexError:
                    break


    root.after(17, lambda: bullet_overlapping(main_area, bullets, score_ui, score))


enemy_bullets = []
def enemy_bullet_draw(main_area):
    random_enemy = random.choice(list(enemies_coords.values()))

    enemy_bullet = main_area.create_image(random_enemy[0], random_enemy[1] + 30, image=bullet_img, tag="enemy_bullet")
    enemy_bullets.append(enemy_bullet)

    root.after(500, lambda: enemy_bullet_draw(main_area))


def enemy_bullet_move(main_area):
    for bullet in enemy_bullets:
        main_area.move(bullet, 0, 15)
        eb_coords = main_area.bbox(bullet)

        if eb_coords[3] > 1280:
            main_area.delete(bullet)
            enemy_bullets.remove(bullet)

    root.after(30, lambda: enemy_bullet_move(main_area))

def player_death(main_area, player, player_lifes, bullets, lifes_ui, score):
    player_coords = main_area.bbox(player)
    player_overlap = main_area.find_overlapping(*player_coords)

    if len(player_overlap) > 1:
        for item in player_overlap:
            item_tag = main_area.gettags(item)

            if item_tag[0] == 'enemy_bullet':
                print("Player Life -1")
                player_lifes -= 1
                main_area.itemconfig(lifes_ui, text=f"LIFES: 0{player_lifes}")
                enemy_bullets.remove(item)
                main_area.delete(item)

            elif item_tag[0] == "enemy":
                show_end_screen()

    if player_lifes == 0:
        show_end_screen()

    root.after(100, lambda: player_death(main_area, player, player_lifes, bullets, lifes_ui, score))

def ui_elements(main_area, player_lifes, score):
    lifes_ui = main_area.create_text(1200, 30, text=f"LIFES: 0{player_lifes}", fill="white", font=("Arial", 15, "bold"))
    score_ui = main_area.create_text(80, 30, text=f"SCORE: {score}", fill="white", font=("Arial", 15, "bold"))

    return lifes_ui, score_ui

def show_end_screen():
    Score_var = tk.IntVar(value=score)

    for widget in root.winfo_children():
        try:
            widget.pack_forget()
        except tk.TclError:
            pass

    end_label = tk.Label(root, text="Game Over / The End", font={"Arial", 50}, bg="black", fg="White")
    end_label.pack(pady=50)

    score_label_1 = tk.Label(root, text="FINAL SCORE:", font={"Arial", 20}, bg="Black", fg="White")
    score_label_1.pack(pady=70)

    restart_btn = tk.Button(root, text='QUIT', command=root.destroy, bg="Black", fg="White")
    restart_btn.pack(pady=10)


def main():
    frm = config()
    main_area = main_area_draw(frm)
    lifes_ui, score_ui = ui_elements(main_area, player_lifes, score)
    player = player_draw(main_area)

    enemies_draw(main_area)
    player_move(player, main_area, bullets)

    bullet_overlapping(main_area, bullets, score_ui, score)
    move_enemies(main_area, direction, enemy_speed)
    move_bullet(main_area, bullets)

    enemy_bullet_draw(main_area)
    enemy_bullet_move(main_area)

    player_death(main_area, player, player_lifes, bullets, lifes_ui, score)

    # root.bind('<KeyPress>', lambda event: player_move(event, main_area, player, main_area, bullets))
    root.bind('<KeyPress>', lambda event: on_key_press(event))
    root.bind('<KeyRelease>', lambda event: on_key_release(event))
    root.bind('<space>', lambda event: player_shoot(event, bullets, player, main_area))

    check_next_level(main_area)

def check_next_level(main_area):
    if len(enemies_coords) <= 0:
        player_lifes = 3
        enemy_speed += 200

        for widget in root.winfo_children():
            widget.pack_forget()

        main()

    else:
        root.after(100, lambda: check_next_level(main_area))




if __name__ == "__main__":
    main()
    root.mainloop()
