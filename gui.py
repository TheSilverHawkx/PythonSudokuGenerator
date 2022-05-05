from doctest import master
from logging import root
from tkinter import *
from tkinter import ttk


class GameWindow():

    def __init__(self):
        self.root = Tk()
        # self.ttk = ttk.
        self.root.frame()
        # Handle default window size
        # root.minsize(400,400)
        # root.maxsize(500,500)
        root.geometry("400x400")


# def click():
#     new_lbl = tk.Label(root, text="LETS GOOOOOOO")
#     new_lbl.grid(row=2,column=4)
#     root.children["restart_btn"].set


# label = tk.Label(root,text="My Suduko")
# start_button = tk.Button(root,text="Start game",command=click, fg="blue")
# restart_button = tk.Button(root,text="Restart game", state=tk.DISABLED,name=restart_btn)

# label.grid(row=0,columnspan=master)
# start_button.grid(row=1,column=0)
# restart_button.grid(row=1,column=1)

# root.mainloop()