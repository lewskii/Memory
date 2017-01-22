from tkinter import *       # GUI tools
from tkinter import ttk     # GUI tools
from random import randrange  #


window = Tk()  # create the main window
window.title('Memory')  # set the window's title
mainframe = ttk.Frame(window, padding='5 5 10 10')  # create a frame inside the main window
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))  # make a grid inside the frame to position widgets


def scoreconv():
    dscore.set('Score: ' + str(score))


def check():
    global string
    global score
    if answer.get() == string:
        string += str(randrange(0, 10))  # adds another random number to the string
        dstring.set(string)  # assigns the new string to the displayed string
        answer.set('')  # empties the answer field
        entry['state'] = 'disabled'  # disables the answer field
        score += 100  # adds 100 to the score
        scoreconv()  # sets the score display to display the new score
    else:
        toptext.set('Game over!')


def start():
    dstring.set('')  # sets the displayed string to nothing to hide it
    entry['state'] = 'enabled'  # enables the answer field (disabled at the beginning)
    entry.focus_set()  # sets focus to the answer field


# StringVar() allows the variables to change globally
toptext = StringVar()  # the text displayed at the top of the page

dstring = StringVar()  # the displayed string; emptied when the player presses Start
string = str(randrange(0, 10))  # the string the player has to enter

answer = StringVar()  # the string the player has entered

score = 0  # the player's score, 0 at the beginning
dscore = StringVar()  # the displayed score


toptext.set('Memorize and enter the numbers.\nPress Start to begin each round.')
dstring.set(string)  # sets the displayed string
scoreconv()  # call the function to set the displayed score


# displays the game's instructions and my signature
instructions = ttk.Label(mainframe, textvariable=toptext, font='TkHeadingFont').grid(row=1, columnspan=3, sticky='w')
ttk.Label(mainframe, text='Leevi Aaltonen 2017', font='TkSmallCaptionFont').grid(row=4, sticky='sw')

# displays the string
display = ttk.Label(mainframe, textvariable=dstring, font='TkTextFont').grid(row=2, columnspan=2, sticky='w')
# displays the score
scoredisplay = ttk.Label(mainframe, textvariable=dscore, font='TkTextFont').grid(column=2, row=4, sticky='e')


# hides the string and enables the answer field
startbutton = ttk.Button(mainframe, text='Start', command=start).grid(column=2, row=2)


# allows the player to enter the string
entry = ttk.Entry(mainframe, textvariable=answer, font='TkTextFont', exportselection=0, state='disabled')
entry.grid(row=3, columnspan=2, sticky='w')  # positions the entry field (didn't fit on the same line as creating it)
# checks if the string is correct when pressed
enter = ttk.Button(mainframe, text='Enter', command=check).grid(column=2, row=3)


# adds space between all widgets
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

window.mainloop()  # starts the main event loop
