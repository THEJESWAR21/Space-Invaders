import tkinter as tk
from tkinter import ttk

# TODO: Create the Ship and Make it Move
# TODO: OOP
# TODO: Shooting Mechanics
# TODO: Enemies and its AI
# TODO: Score / HighScore
# TODO: Sounds
# RESEARCH: FRAME, GRID AND PACK

def main(root):
    root.title("Space-Invaders")

    win_width, win_height = 1280, 720 # 960, 540
    scr_width, scr_height = root.winfo_screenwidth(), root.winfo_screenheight()

    x = (scr_width - win_width) // 2
    y = (scr_height - win_height) // 2
    
    root.geometry(f"{win_width}x{win_height}+{x}+{y}")
    # root.resizable(False, False) # Width, Height
    # root.configure(bg="black")

    frm = tk.Frame(root, bg="Black") # ROOT FRAME
    frm.pack(fill="both", expand=True)

    player_cvw, player_cvh = win_width, 80
    player_x, player_y = 60, 60
    player_area = tk.Canvas(frm, bg="Red", height=player_cvh, highlightthickness=0) 

    # Size of square: 60 x 60
    # Size of Canvas: 1280 x 80
    # MidPoint of Canvas: 1280 // 2 x 80 // 2 = 640 x 40
    # X0: 640 - 30 = 610 (player_cvw // 2) - (player_x // 2)
    # y0: 40 - 30 = 10 (player_cvh // 2) - (player_y // 2)
    # x1: 640 + 30 = 670 (player_cvw // 2) + (player_x // 2)
    # y1: 40 + 30 = 70 (player_cvh // 2) + (player_y // 2)

    X0 = (player_cvw // 2) - (player_x // 2)
    Y0 = (player_cvh // 2) - (player_y // 2)
    X1 = (player_cvw // 2) + (player_x // 2)
    Y1 = (player_cvh // 2) + (player_y // 2)
    
    # (610, 10, 670, 70)

    
    player = player_area.create_rectangle(X0, Y0, X1, Y1, fill='green' ,width=0)
    player_area.pack(side="bottom", fill=tk.X)

    root.update_idletasks()


if __name__ == "__main__":
    root = tk.Tk() # Create the ROOT Window and the TK Instance
    main(root)
    root.mainloop()
        
