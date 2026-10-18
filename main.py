from tkinter import Tk, ttk

def main():
    root = Tk() # Create the ROOT Window and the TK Instance
    frm = ttk.Frame(root, padding=10) # FRAME Widget
    frm.grid()
    ttk.Label(frm, text="Hello, World!").grid(column=0, row=0) # Grid is used to position the Label
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
    print(frm.grid_size())
    root.mainloop()


if __name__ == "__main__":
    main()
        
