import tkinter as tk
from tkinter import ttk, PhotoImage

# TODO: Create the Ship and Make it Move
# TODO: OOP
# TODO: Shooting Mechanics
# TODO: Enemies and its AI
# TODO: Score / HighScore
# TODO: Sounds
# RESEARCH: FRAME, GRID AND PACK

def main(root):
    root.title("Space-Invaders")

    width, height = 960, 540
    scr_width, scr_height = root.winfo_screenwidth(), root.winfo_screenheight()

    x = (scr_width - width) // 2
    y = (scr_height - height) // 2
    
    root.geometry(f"{width}x{height}+{x}+{y}")
    root.resizable(False, False) # Width, Height
    root.configure(bg="black")


if __name__ == "__main__":
    root = tk.Tk() # Create the ROOT Window and the TK Instance
    main(root)
    root.mainloop()
        
