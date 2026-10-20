import tkinter as tk
from tkinter import ttk

def main(root):
    root.title("Space-Invaders")

    width, height = 800, 600
    scr_width, scr_height = root.winfo_screenwidth(), root.winfo_screenheight()

    x = (scr_width - width) // 2
    y = (scr_height - height) // 2
    
    root.geometry(f"{width}x{height}+{x}+{y}")




if __name__ == "__main__":
    root = tk.Tk() # Create the ROOT Window and the TK Instance
    main(root)
    root.mainloop()
        
