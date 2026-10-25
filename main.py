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
player_img = tk.PhotoImage(file=r"C:\Users\Thej\Projects\Space-Invaders-Py\Assets\Ship2.png") # 16x16 (RESIZED: 6.0x (96x96))
squid_img = tk.PhotoImage(file=r"C:\Users\Thej\Projects\Space-Invaders-Py\Assets\Ship2.png") # 16x16 (RESIZED: 6.0x (96x96))

win_width, win_height = 1280, 720 # 960, 540
scr_width, scr_height = root.winfo_screenwidth(), root.winfo_screenheight()

player_speed = 15 

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

def player_draw(frm):
    player_cvw, player_cvh = win_width, 80 # (1280,80) Player Canvas Size
    # player_x, player_y = 60, 0 # Size of Player Sprite

    # Size of square: 60 x 60
    # MidPoint of Canvas: 1280 // 2 x 80 // 2 = 640 x 40

    x0 = player_cvw // 2
    y0 = player_cvh // 2
    # X0 = (player_cvw // 2) - (player_x // 2)
    # Y0 = (player_cvh // 2) - (player_y // 2)
    # X1 = (player_cvw // 2) + (player_x // 2)
    # Y1 = (player_cvh // 2) + (player_y // 2)
    # (610, 10, 670, 70)
   
    player_area = tk.Canvas(frm, bg="Black", height=player_cvh, highlightthickness=0) 
    player = player_area.create_image(x0,y0, image=player_img)
    player = player_area.create_image(x0,y0, image=player_img)
    # player_area.move(player, 609.6, 0)
   
    player_area.pack(side="bottom", fill=tk.X)

    return player_area, player

def player_move(event, player_area, player):
    player_size = player_area.bbox(player)
    window_height = root.winfo_width()

    key = event.keysym
    # x_pos, y_pos = player_area.coords(player)
    
    if (key == "a" or key == "Left") and player_size[0] > 0: # 48 
        player_area.move(player, -player_speed, 0)
    elif (key == "d" or key == "Right") and player_size[2] < window_height:
        player_area.move(player, player_speed, 0)
    else:
        player_area.move(player, 0, 0)

    return


def every_frame():
    print("Hello")
    root.after(5000, every_frame)

def main():
    frm = config()
    player_area, player = player_draw(frm)

    root.bind('<KeyPress>', lambda event: player_move(event, player_area, player))

    # every_frame()

if __name__ == "__main__":
    main()
    root.mainloop()
        
