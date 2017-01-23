from tkinter import *       # GUI tools
from tkinter import ttk     # GUI tools
from random import randrange  #

mainwindow = Tk()  # create the main window
mainwindow.title('Memory')  # set the window's title
mainframe = ttk.Frame(mainwindow, padding='5 5 10 5')  # create a frame inside the main window
mainframe.grid(row=0, sticky=(N, W, E, S))  # make a grid inside the frame to position widgets


def start():
    dstring.set('')  # sets the displayed string to nothing to hide it
    ansentry['state'] = 'enabled'  # enables the answer field (disabled at the beginning)
    ansentry.focus_set()  # sets focus to the answer field


def check(ans):
    global string
    global score
    if ans == string:
        string += str(randrange(0, 10))  # adds another random number to the string
        dstring.set(string)  # assigns the new string to the displayed string
        answer.set('')  # empties the answer field
        ansentry['state'] = 'disabled'  # disables the answer field
        score += 100  # adds 100 to the score
        scoreconv()  # sets the score display to display the new score
    else:
        end()


def end():
    toptext.set('Game over!')


def scoreconv():
    dscore.set('Score: ' + str(score))  # converts the score into a string with more clarity


def saveuser(name):
    try:
        scorefile = open(name + '.score', 'x', )  # creates a file for the player's scores
    except FileExistsError:
        scorefile = open(name + '.score', 'r+a')  # opens the given user's score file if it already exists


user = StringVar()

ttk.Label(mainframe, text='Enter a username:').grid(row=1, sticky='e')  # label the entry box
userentry = ttk.Entry(mainframe, textvariable=user).grid(row=1, column=1, sticky='w')  # create the entry box

# adds space between all widgets
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

# userentry.bind('<Return>', lambda c: saveuser(user.get()))


memorywindow = Toplevel()  # create the main window
memorywindow.title('Memory')  # set the window's title
memoryframe = ttk.Frame(memorywindow, padding='5 5 10 10')  # create a frame inside the main window
memoryframe.grid(row=0, sticky=(N, W, E, S))  # make a grid inside the frame to position widgets


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
instructions = ttk.Label(memoryframe, textvariable=toptext, font='TkHeadingFont').grid(row=1, columnspan=3, sticky='w')
ttk.Label(memoryframe, text='Leevi Aaltonen 2017', font='TkSmallCaptionFont').grid(row=4, sticky='sw')

# displays the string
display = ttk.Label(memoryframe, textvariable=dstring, font='TkTextFont').grid(row=2, columnspan=2, sticky='w')
# displays the score
scoredisplay = ttk.Label(memoryframe, textvariable=dscore, font='TkTextFont').grid(column=2, row=4, sticky='e')


# hides the string and enables the answer field
startbutton = ttk.Button(memoryframe, text='Start', command=start).grid(column=2, row=2)


# allows the player to enter the string
ansentry = ttk.Entry(memoryframe, textvariable=answer, font='TkTextFont', exportselection=0, state='disabled')
ansentry.grid(row=3, columnspan=2, sticky='w')  # positions the entry field (didn't fit on the same line as creating it)
# checks if the string is correct when pressed
ansentrybutton = ttk.Button(memoryframe, text='Enter', command=lambda: check(answer.get())).grid(column=2, row=3)


# adds space between all widgets
for child in memoryframe.winfo_children():
    child.grid_configure(padx=5, pady=5)


ansentry.bind('<Return>', lambda c: check(answer.get()))  # calls the check function when the Enter key is pressed

mainwindow.mainloop()  # starts the main event loop
