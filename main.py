import tkinter as tk
from tkinter import ttk

# DONE: Create the Ship and Make it Move
# TODO: Create Smooth Movement / Delta Time
# TODO: Shooting Mechanics
# TODO: Enemies and its AI
# TODO: Score / HighScore
# TODO: Sounds
# RESEARCH: GARBAGE COLLECTION

root = tk.Tk()
player_img = tk.PhotoImage(file=r"C:\Users\Thej\Projects\Space-Invaders-Py\Assets\Player\Ship.png") # 16x16 (RESIZED: 6.0x (96x96))
bullet_img = tk.PhotoImage(file=r'C:\Users\Thej\Projects\Space-Invaders-Py\Assets\Player\Bullet.png')

win_width, win_height = 1280, 720 # 960, 540
scr_width, scr_height = root.winfo_screenwidth(), root.winfo_screenheight()

player_speed = 15 

bullets = []

def config():
    root.title("Space-Invaders")

    x = (scr_width - win_width) // 2
    y = (scr_height - win_height) // 2

    root.geometry(f"{win_width}x{win_height}+{x}+{y}")
    root.resizable(False, False) # Width, Height
    # root.configure(bg="black")

    frm = tk.Frame(root, bg="Black") # ROOT FRAME
    frm.pack(fill="both", expand=True)

    return frm

def main_area_draw(frm):
    main_area = tk.Canvas(frm, bg="red", highlightthickness=0)
    main_area.pack(side='bottom', fill=tk.BOTH, expand=True)

    return main_area


def player_draw(frm):
    player_cvw, player_cvh = win_width, 80 # (1280,80) Player Canvas Size
    # player_x, player_y = 60, 0 # Size of Player Sprite

    # Size of square: 60 x 60
    # MidPoint of Canvas: 1280 // 2 x 80 // 2 = 640 x 40

    x0 = player_cvw // 2
    y0 = player_cvh // 2
   
    player_area = tk.Canvas(frm, bg="lightgreen", height=player_cvh, highlightthickness=0)
    player = player_area.create_image(x0,y0, image=player_img)
    # player_area.move(player, 609.6, 0)
   
    player_area.pack(side="bottom", fill=tk.X)

    return player_area, player

def player_move(event, player_area, player, main_area, bullets):
    player_size = player_area.bbox(player)
    player_coords = player_area.coords(player)
    window_height = root.winfo_width()

    key = event.keysym
    # x_pos, y_pos = player_area.coords(player)
    
    if (key == "a" or key == "Left") and player_size[0] > 0: # 48 
        player_area.move(player, -player_speed, 0)
    elif (key == "d" or key == "Right") and player_size[2] < window_height:
        player_area.move(player, player_speed, 0)
    elif (key == 'space' or key == "up"):
        # player_shoot(main_area)
        player_shoot(main_area, bullets, player_size)
    else:
        player_area.move(player, 0, 0)

    return


def player_shoot(main_area, bullets, player_size):
    # x0, y0, x1, y1 = player_size
    bullet_size = 15
    half_size = bullet_size // 2

    x_midpoint = (player_size[0] + player_size[2]) // 2
    # x_midpoint , top_edge
    top_edge = player_size[1] 

    # x0 = x_midpoint - half_size
    # y0 = top_edge - bullet_size
    # x1 = x_midpoint + half_size
    y1 = top_edge + 20 
    offset = 605

    # bullet = main_area.create_rectangle(x0 ,y0 + offset,x1,y1 + offset, fill='white', outline='white')
    bullet = main_area.create_image(x_midpoint, y1 + 590, image=bullet_img)
    bullets.append(bullet)

    # root.update_idletasks()

def move_bullet(main_area, bullets):
    for bullet in bullets:
        main_area.move(bullet, 0, -10)
        b_coords = main_area.bbox(bullet) 

        if b_coords[3]  < 0:
            main_area.delete(bullet)
            bullets.remove(bullet)


    print(bullets)

    root.after(20, lambda : move_bullet(main_area, bullets))



# def every_frame():
#     print("Hello")
#     root.after(5000, every_frame)

def main():
    frm = config()
    player_area, player = player_draw(frm)
    main_area = main_area_draw(frm)
    move_bullet(main_area, bullets)

    root.bind('<KeyPress>', lambda event: player_move(event, player_area, player, main_area, bullets))

    # every_frame()

if __name__ == "__main__":
    main()
    root.mainloop()
        
