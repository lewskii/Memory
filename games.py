from tkinter import *       # GUI tools
from tkinter import ttk     # GUI tools
from random import randrange  #

mainwindow = Tk()  # create the main window
mainwindow.title('Games')  # set the window's title
mainframe = ttk.Frame(mainwindow, padding='5 5 10 5')  # create a frame inside the main window
mainframe.grid(row=0, sticky=(N, W, E, S))  # make a grid inside the frame to position widgets


def start():
    dstring.set('')  # sets the displayed string to nothing to hide it
    ansentry['state'] = 'enabled'  # enables the answer field (disabled at the beginning)
    ansentry.focus_set()  # sets focus to the answer field


def check(game, ans):
    if ans == string:
        exec(game + 'next()')
    else:
        end()


def memorynext():
    global string  # lets the outside variable be changed from inside the function
    global score
    string += str(randrange(0, 10))  # adds another random number to the string
    dstring.set(string)  # assigns the new string to the displayed string
    answer.set('')  # empties the answer field
    ansentry['state'] = 'disabled'  # disables the answer field
    score += 100  # adds 100 to the score
    scoreconv()  # sets the score display to display the new score


def end():
    toptext.set('Game over!')


def scoreconv():
    dscore.set('Score: ' + str(score))  # converts the score into a string with more clarity


def saveuser(name):
    try:
        scorefile = open(name + '.score', 'x', )  # creates a file for the player's scores
    except FileExistsError:
        scorefile = open(name + '.score', 'a')  # opens the given user's score file if it already exists


def spacing(frame):
    exec('for child in ' + frame + 'frame.winfo_children(): child.grid_configure(padx=5, pady=5)')
    # creates space between all widgets


user = StringVar()

# allows the user to enter a username
userlabel = ttk.Label(mainframe, text='Enter a username:').grid(row=1, sticky='e')  # labels the username entry field
userentry = ttk.Entry(mainframe, textvariable=user)  # creates the username entry field
userentry.focus_set()  # sets focus to the username entry field
userentry.grid(row=1, column=1, sticky='w')  # positions the username entry field

# calls the function to create a file for storing the player's scores
userentrybutton = ttk.Button(mainframe, text='Continue', command=lambda u: saveuser(user.get()))
userentrybutton.grid(row=1, column=2, sticky='w')

# my signature
signaturetext = 'Made by Leevi Aaltonen, 2017, released under MIT license.'  # the text is long so created a variable
signature = ttk.Label(mainframe, text=signaturetext, font='TkSmallCaptionFont')  # displays the signature
signature.grid(row=4, columnspan=3, sticky='sw')  # positions the signature

spacing('main')  # creates space between all widgets

userentry.bind('<Return>', lambda u: saveuser(user.get()))  # binds Enter to the score file creation function


def menu():



# memory game
def memory():
    global string
    global score
    global toptext
    global dstring
    global dscore
    global answer
    global ansentry
    memorywindow = Toplevel()  # creates the child window for the memory game
    memorywindow.title('Memory')  # sets the window's title
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

    # displays the game's instructions
    ttk.Label(memoryframe, textvariable=toptext, font='TkHeadingFont').grid(row=1, columnspan=3, sticky='w')

    # displays the string
    ttk.Label(memoryframe, textvariable=dstring, font='TkTextFont').grid(row=2, columnspan=2, sticky='w')
    # displays the score
    ttk.Label(memoryframe, textvariable=dscore, font='TkTextFont').grid(row=4, sticky='w')

    # hides the string and enables the answer field
    ttk.Button(memoryframe, text='Start', command=start).grid(column=2, row=2)

    # allows the player to enter the string
    ansentry = ttk.Entry(memoryframe, textvariable=answer, font='TkTextFont', exportselection=0, state='disabled')
    ansentry.grid(row=3, columnspan=2, sticky='w')  # positions the entry field

    # checks if the string is correct when pressed
    ansentrybutton = ttk.Button(memoryframe, text='Enter', command=lambda: check('memory', answer.get()))
    ansentrybutton.grid(column=2, row=3)

    # adds space between all widgets

    ansentry.bind('<Return>', lambda c: check('memory', answer.get()))  # calls the check function when Enter is pressed

    spacing('memory')  # creates space between all widgets

mainwindow.mainloop()  # starts the main event loop
