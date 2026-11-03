import tkinter as tk
from tkinter import ttk
from pprint import pprint
import random

# DONE: Create the Ship and Make it Move
# DONE: Create Smooth Movement
# DONE: Shooting Mechanics
# DONE: RESIZE ASSETS TO FIT THE SCREEN
# DONE: Enemies and its AI
# DONE: ENEMY SHOOTING
# DONE: PLAYER LIFES
# DONE: Score
# DONE: GAME LOOP
# DONE: END GAME SCREEN

root = tk.Tk()

# SPRITES
player_img = tk.PhotoImage(file=r"C:\Users\Thej\Projects\Space-Invaders-Py\Assets\Player\Ship.png") # 16x16 (RESIZED: 6.0x (96x96))
bullet_img = tk.PhotoImage(file=r'C:\Users\Thej\Projects\Space-Invaders-Py\Assets\Player\Bullet.png')
crab_img = tk.PhotoImage(file=r"C:\Users\Thej\Projects\Space-Invaders-Py\Assets\Enemies\Crab-1.png") # 4.0x
squid_img = tk.PhotoImage(file=r"C:\Users\Thej\Projects\Space-Invaders-Py\Assets\Enemies\Squid-1.png")
octo_img = tk.PhotoImage(file=r"C:\Users\Thej\Projects\Space-Invaders-Py\Assets\Enemies\Octo-1.png")
# ship_img = tk.PhotoImage(file=r"C:\Users\Thej\Projects\Space-Invaders-Py\Assets\Enemies\Alienship.png")

win_width, win_height = 1280, 720 # 960, 540
debug_bg = ("Black", "Black", "Black")
enemies_coords = {}
pressed_keys = set()
bullets = []
enemy_bullets = []

# STATE VARIABLES
score = tk.IntVar(value=0)
player_lifes = tk.IntVar(value=3)
enemy_speed = tk.IntVar(value=800)
level = 0

direction = 1

def config():
    """ SETUP THE WINDOW """

    scr_width, scr_height = root.winfo_screenwidth(), root.winfo_screenheight()
    root.title("Space-Invaders")

    # Position Of window on screen
    x = (scr_width - win_width) // 2
    y = (scr_height - win_height) // 2

    root.geometry(f"{win_width}x{win_height}+{x}+{y}")
    root.resizable(False, False) # Width, Height
    root.configure(bg="black")

    frm = tk.Frame(root, bg=debug_bg[0]) # ROOT FRAME
    frm.pack(fill="both", expand=True)

    return frm

def main_area_draw(frm):
    """ DRAW MAIN CANVAS """ 
    main_area = tk.Canvas(frm, bg=debug_bg[1], highlightthickness=0)
    main_area.pack(side='bottom', fill=tk.BOTH, expand=True)

    return main_area

def player_draw(main_area):
    """ DRAW PLAYER AT THE CENTER"""
    # player_cvw, player_cvh = win_width, 80 # (1280,80) Player Canvas Size
    # MidPoint of Canvas: 1280 // 2 x 80 // 2 = 640 x 40

    x0 = win_width // 2 # Center on X Axis
    y0 = win_height - 50 # Position From Bottom And Lift Up

    # main_area = tk.Canvas(frm, bg=debug_bg[2], height=player_cvh, highlightthickness=0)
    player = main_area.create_image(x0,y0, image=player_img, tags="player")

    return player

def on_key_press(event):
    pressed_keys.add(event.keysym)

def on_key_release(event):
    pressed_keys.discard(event.keysym)

def player_move(player, main_area):
    """ PLAYER MOVEMENT SETUP """
    dx, dy = 0 , 0
    player_speed = 15 

    try:
        player_size = main_area.bbox(player)
        player_coords = main_area.coords(player) # (x,y)
        window_height = root.winfo_width()
    except:
        return

    # Check for player position and key
    if ('a' in pressed_keys) and (player_size[0] > 0):
        dx = -player_speed
    elif ('d' in pressed_keys) and (player_size[2] < window_height):
        dx = player_speed

    if dx != 0 or dy != 0:
        main_area.move(player, dx, dy)

    root.after(30, lambda: player_move(player, main_area))

def player_shoot(event, bullets, player, main_area):
    """ CREATE THE BULLET ABOVE PLAYER """
    player_size = main_area.bbox(player) # (x0,y0,y0,y1)

    bullet_size = 15
    half_size = bullet_size // 2

    x_midpoint = (player_size[0] + player_size[2]) // 2 # Midpoint of player
    top_edge = player_size[1] # Y Axis Position

    y1 = top_edge
    offset = 20 # Offset from midpoint of player

    if len(bullets) < 1:
        bullet = main_area.create_image(x_midpoint, y1 - offset, image=bullet_img, tag="bullet")
        bullets.append(bullet)

def move_bullet(main_area, bullets):
    """ MOVE CREATED BULLETS UP """
    for bullet in bullets:
        try:
            main_area.move(bullet, 0, -15)
            b_coords = main_area.bbox(bullet) 

            if b_coords[3] < 0:
                main_area.delete(bullet)
                bullets.remove(bullet)
        except TypeError:
            break
        except ValueError:
            break
        except tk.TclError:
            break

    root.after(17, lambda : move_bullet(main_area, bullets))


def find_mid_x(y, space_between, enemy_count, x0, x1):
    """ CENTER THE ENEMIES ON SCREEN """
    x_midpoint, y_midpoint = ((x0 + x1) / 2), ((y + y) / 2) # Find Midpoint of a Line
    distance = (((x_midpoint - x0) ** 2) + ((y_midpoint - y) ** 2)) ** 0.5 # Find Distance of a line
    x = (win_width // 2) - distance

    return x

def draw_rows(main_area, x, y, space_between, image_ref, enemy_count, enemy_type):
    """ BLUEPRINT FOR CREATING ROW OF ENEMIES """
    for _ in range(enemy_count):
        enemy = main_area.create_image(x, y, image=image_ref, tag="enemy")
        coords = main_area.coords(enemy)

        enemies_coords[enemy] = coords

        x += space_between

    return

def enemies_draw(main_area):
    """ DRAW ENEMIES FROM THE BLUEPRINT """
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
    #
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

def move_enemies(main_area, direction, enemy_speed):
    """ MOVE DRAWN ENEMIES """
    shift = False
    hit_wall = False
    step = 40

    enemies_coords_values = list(enemies_coords.values())
    enemies_coords_values.sort()

    try:
        # FIND THE CLOSEST ENEMY TO THE EDGE
        closest_to_right = enemies_coords_values[-1][0]
        closest_to_left = enemies_coords_values[0][0] 
    except IndexError:
        closest_to_right = 0
        closest_to_left = 0

    # SHIFTING DIRECTION STATE OF ENEMIES
    if direction == 1 and closest_to_right + step >= 1280:
        direction = -1
        shift = True

    elif direction == -1 and closest_to_left - step <= 0:
        direction = 1
        shift = True

    # SHITING DIRECTION ON SCREEN USING SHIFT STATE
    for enemy_id, enemy_coords in enemies_coords.items():
        try:
            if shift == True:
                main_area.move(enemy_id, 0, 50)
            else:
                main_area.move(enemy_id, step * direction, 0)

            enemies_coords[enemy_id] = main_area.coords(enemy_id)
        except tk.TclError:
            break

    root.after(enemy_speed.get(), lambda: move_enemies(main_area, direction, enemy_speed))

def bullet_overlapping(main_area, bullets, score_ui, score):
    """ DELETE ENEMY IF A BULLET COLLIDES"""
    for bullet in bullets:
        try:
            bullet_bbox = main_area.bbox(bullet)
            bullet_overlap = main_area.find_overlapping(*bullet_bbox)
        except TypeError:
            break
        except tk.TclError:
            break
          
        if len(bullet_overlap) > 1:
            for overlap_id in bullet_overlap:
                enemy_tag = main_area.gettags(overlap_id)
                try:
                    if enemy_tag[0] == "enemy":
                        enemies_coords.pop(overlap_id)
                        main_area.delete(overlap_id)

                        bullets.remove(bullet_overlap[-1])
                        main_area.delete(bullet_overlap[-1])
                        score.set(score.get() + 50)
                        main_area.itemconfig(score_ui, text=f"SCORE: {score.get()}")
                        print('Enemy', overlap_id, 'DIED')
                        break
                except IndexError:
                    break
                except tk.TclError:
                    break

    root.after(17, lambda: bullet_overlapping(main_area, bullets, score_ui, score))


def enemy_bullet_draw(main_area):
    """ CREATE ENEMY BULLET SPRITES USING ENEMY POSITION """
    try:
        random_enemy = random.choice(list(enemies_coords.values()))

        enemy_bullet = main_area.create_image(random_enemy[0], random_enemy[1] + 30, image=bullet_img, tag="enemy_bullet")
        enemy_bullets.append(enemy_bullet)

        root.after(1000, lambda: enemy_bullet_draw(main_area))
    except IndexError:
        return
    except tk.TclError:
        return
        

def enemy_bullet_move(main_area):
    """ MOVE CREATED ENEMY BULLETS DOWN """
    for bullet in enemy_bullets:
        try:
            main_area.move(bullet, 0, 15)
            eb_coords = main_area.bbox(bullet)

            if eb_coords[3] > 1280:
                main_area.delete(bullet)
                enemy_bullets.remove(bullet)
        except TypeError:
            break
        except tk.TclError:
            break

    root.after(30, lambda: enemy_bullet_move(main_area))

def player_death(main_area, player, player_lifes, bullets, lifes_ui):
    """ PLAYER DIES AFTER 3 HITS"""
    try:
        player_coords = main_area.bbox(player)
        player_overlap = main_area.find_overlapping(*player_coords)
    except tk.TclError:
        return

    if len(player_overlap) > 1:
        for item in player_overlap:
            # CHECK TAGS OF OVERLAPPING ITEMS
            item_tag = main_area.gettags(item)

            try:
                if item_tag[0] == 'enemy_bullet':
                    print("Player Life -1")
                    player_lifes.set(player_lifes.get() - 1)
                    main_area.itemconfig(lifes_ui, text=f"LIFES: 0{player_lifes.get()}")
                    enemy_bullets.remove(item)
                    main_area.delete(item)

                elif item_tag[0] == "enemy":
                    # GAME OVER
                    show_end_screen()
            except ValueError:
                break

    if player_lifes.get() == 0:
        # GAME OVER
        show_end_screen()

    root.after(100, lambda: player_death(main_area, player, player_lifes, bullets, lifes_ui))

def ui_elements(main_area, player_lifes, score):
    """ CREATE UI ELEMENT ON SCREEN"""
    lifes_ui = main_area.create_text(1200, 30, text=f"LIFES: 0{player_lifes.get()}", fill="white", font=("Arial", 15, "bold"))
    score_ui = main_area.create_text(80, 30, text=f"SCORE: {score.get()}", fill="white", font=("Arial", 15, "bold"))

    return lifes_ui, score_ui

def show_end_screen():
    """ END SCREEN DESIGN """
    for widget in root.winfo_children():
        try:
            widget.pack_forget()
        except tk.TclError:
            pass

    end_label = tk.Label(root, text="Game Over", font=("Arial", 50, "bold"), bg="black", fg="White").pack(pady=30)

    score_label_1 = tk.Label(root, text=f"FINAL SCORE:", font=("Arial", 20, "bold"), bg="Black", fg="White").pack(pady=40)
    score_label_2 = tk.Label(root, text=f"{score.get()}", font=("Arial", 100, "bold"), bg="Black", fg="White").pack(pady=50)

    restart_btn = tk.Button(root, text='QUIT', command=root.destroy,font=('Arial', 20, "bold") , bg="Black", fg="White", width=50, height=50).pack(pady=70)

def level_layout():
    """ LEVEL LAYOUT EVERY ROUND """
    # MAIN
    frm = config()
    main_area = main_area_draw(frm)
    lifes_ui, score_ui = ui_elements(main_area, player_lifes, score)
    
    # PLAYER
    player = player_draw(main_area)
    player_move(player, main_area)
    player_death(main_area, player, player_lifes, bullets, lifes_ui)

    # ENEMIES
    enemies_draw(main_area)
    bullet_overlapping(main_area, bullets, score_ui, score)
    move_enemies(main_area, direction, enemy_speed)
    enemy_bullet_draw(main_area)
    enemy_bullet_move(main_area)

    # KEY BINDING
    root.bind('<KeyPress>', lambda event: on_key_press(event))
    root.bind('<KeyRelease>', lambda event: on_key_release(event))
    root.bind('<space>', lambda event: player_shoot(event, bullets, player, main_area))

def main(level, player_lifes, enemy_speed, score):
    """ INCREATE DIFFICULTY AS LEVEL INCREASES """

    if level == 0 and len(enemies_coords) == 0:
        level_layout()
        level += 1
    elif level > 0 and len(enemies_coords) == 0:
        player_lifes.set(3)
        enemy_speed.set(enemy_speed.get() - 300)

        bullets.clear()
        enemy_bullets.clear()
        pressed_keys.clear()

        # DESTORY ALL ELEMENT ON SCREEN
        for widget in root.winfo_children():
            widget.destroy()

        level += 1
        level_layout()

    root.after(17, lambda: main(level, player_lifes, enemy_speed, score))

if __name__ == "__main__":
    main(level, player_lifes, enemy_speed, score)
    root.mainloop()
