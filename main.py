from tkinter import *       # GUI tools
from tkinter import ttk     # GUI tools

mainwindow = Tk()  # create the main window
mainwindow.title('Memory')  # set the window's title
mainframe = ttk.Frame(mainwindow, padding='5 5 10 5')  # create a frame inside the main window
mainframe.grid(row=0, sticky=(N, W, E, S))  # make a grid inside the frame to position widgets


def saveuser(name):
    try:
        scorefile = open(name + '.score', 'x', )  # creates a file for the player's scores
    except FileExistsError:
        scorefile = open(name + '.score', 'r+a')  # opens the given user's score file if it already exists


user = StringVar()

ttk.Label(mainframe, text='Enter a username:').grid(row=1, sticky='e')  # label the entry box
entry = ttk.Entry(mainframe, textvariable=user).grid(row=1, column=1, sticky='w')  # create the entry box

# adds space between all widgets
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

# entry.bind('<Return>', lambda c: saveuser(user.get()))

mainwindow.mainloop()
