from tkinter import *       # GUI tools
from tkinter import ttk     # GUI tools
from random import randrange  #


window = Tk()  # create the main window
window.title('Memory')  # set the window's title
mainframe = ttk.Frame(window, padding='5 5 10 10')  # create a frame inside the main window
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))  # make a grid inside the frame to position widgets
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

# StringVar() allows the variables to change globally
dstring = StringVar()  # the string that's displayed; is emptied when the player starts typing
string = str(randrange(0, 10))  # the string the player has to enter
answer = StringVar()  # the string the player has entered

dstring.set(string)


# displays the game's instructions and my signature
ttk.Label(mainframe, text='Memorize and enter the numbers.', anchor='nw', font='TkHeadingFont').grid(row=1, columnspan=2)
ttk.Label(mainframe, text='Leevi Aaltonen 2017', anchor='sw', font='TkSmallCaptionFont').grid(row=4)

# displays the string and score
display = ttk.Label(mainframe, textvariable=dstring, font='TkTextFont').grid(column=1, row=2)
# scoredisplay = ttk.Label(mainframe, textvariable=dscore, font='TkTextFont').grid(column=1, row=4)

# allows the player to enter the string
entry = ttk.Entry(mainframe, textvariable=answer, font='TkTextFont', exportselection=0).grid(column=1, row=3)
enter = ttk.Button(mainframe, text='Enter', command=).grid(column=2, row=3)

# adds space between all widgets
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

window.mainloop()  # starts the main event loop
