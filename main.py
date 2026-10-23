import tkinter as tk
from tkinter import ttk

# TODO: Create the Ship and Make it Move
# TODO: Create Smooth Movement / Delta Time
# TODO: Clean Up The Code / OOP
# TODO: Shooting Mechanics
# TODO: Enemies and its AI
# TODO: Score / HighScore
# TODO: Sounds

# RESEARCH: GARBAGE COLLECTION

def main(root):
    root.title("Space-Invaders")

    win_width, win_height = 1280, 720 # 960, 540
    scr_width, scr_height = root.winfo_screenwidth(), root.winfo_screenheight()

    x = (scr_width - win_width) // 2
    y = (scr_height - win_height) // 2
    
    root.geometry(f"{win_width}x{win_height}+{x}+{y}")
    root.resizable(False, False) # Width, Height
    # root.configure(bg="black")

    frm = tk.Frame(root, bg="Black") # ROOT FRAME
    frm.pack(fill="both", expand=True)

    # PLAYER
    player_cvw, player_cvh = win_width, 80 # (1280,80)
    player_x, player_y = 64, 64 # Size of Player
    player_speed = 10

    # Size of square: 60 x 60
    # MidPoint of Canvas: 1280 // 2 x 80 // 2 = 640 x 40

    X0 = (player_cvw // 2) - (player_x // 2)
    Y0 = (player_cvh // 2) - (player_y // 2)
    X1 = (player_cvw // 2) + (player_x // 2)
    Y1 = (player_cvh // 2) + (player_y // 2)
    # (610, 10, 670, 70)
   
    player_area = tk.Canvas(frm, bg="Black", height=player_cvh, highlightthickness=0) 

    player = player_area.create_image(640,40,image=player_img)
    # player = player_area.create_rectangle(X0, Y0, X1, Y1, fill='green' ,width=0)
   
    # player_area.move(player, 609.6, 0)
    
    # 609.6
    # Movement
    root.bind('<Right>', lambda event: player_area.move(player, 15, 0))
    root.bind('<d>', lambda event: player_area.move(player, 15, 0))
    root.bind('<Left>', lambda event: player_area.move(player, -15, 0))
    root.bind('<a>', lambda event: player_area.move(player, -15, 0))

    player_area.pack(side="bottom", fill=tk.X)

if __name__ == "__main__":
    root = tk.Tk() # Create the ROOT Window and the TK Instance
    # 16x16 (RESIZED: 6.0x (96x96))
    player_img = tk.PhotoImage(file=r"C:\Users\Thej\Projects\Space-Invaders-Py\Assets\Ship.png") 
    main(root)
    root.mainloop()
        
