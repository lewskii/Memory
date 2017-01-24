from tkinter import *       # GUI tools
from tkinter import ttk     # GUI tools
from random import randrange  #


# creates the login screen
def login():
    try:
        menuframe.destroy()
    except NameError:
        pass

    global mainframe
    mainframe = ttk.Frame(mainwindow, padding='5 5 10 5')  # create a frame inside the main window
    mainframe.grid(row=0, sticky=(N, W, E, S))  # make the frame fill the window

    global user
    user = StringVar()

    # allows the user to enter a username
    ttk.Label(mainframe, text='Enter a username:').grid(row=0, sticky='e')  # labels the username entry field
    userentry = ttk.Entry(mainframe, textvariable=user)  # creates the username entry field
    userentry.focus_set()  # sets focus to the username entry field
    userentry.grid(row=0, column=1, sticky='w')  # positions the username entry field

    # calls the function to create a file for storing the player's scores
    userentrybutton = ttk.Button(mainframe, text='Continue', command=menu)
    userentrybutton.grid(row=0, column=2, sticky='w')

    # my signature
    signaturetext = 'Made by Leevi Aaltonen, 2017, released under MIT license.'  # created variable because text is long
    signature = ttk.Label(mainframe, text=signaturetext, font='TkSmallCaptionFont')  # displays the signature
    signature.grid(row=3, columnspan=3, sticky='sw')  # positions the signature

    spacing('main')  # creates space between all widgets

    userentry.bind('<Return>', menu)  # binds Enter to the menu function


# creates the main menu
def menu(self):
    """
    try:
        open('scores/' + user.get() + '.score', 'x', )  # creates a file for the player's scores
    except FileExistsError:
        pass  # does nothing if the file exists
    """
    global mainframe

    mainframe.destroy()

    global menuframe  # lets the variable be used in all functions
    menuframe = ttk.Frame(mainwindow, padding='5 5 10 10')  # creates a new frame inside the main window
    menuframe.grid(row=0, sticky=(N, W, E, S))  # make the frame fill the window
    ttk.Label(menuframe, text='User').grid(row=0)  # labels the user options
    ttk.Label(menuframe, textvariable=user).grid(row=1)  # displays the current username
    ttk.Label(menuframe, text='Games').grid(row=0, column=1, columnspan=2)  # labels the game options

    # not yet functional
    scorebutton = ttk.Button(menuframe, text='Scores', state='disabled')  # displays scores
    scorebutton.grid(row=2)  # positions the button
    logoutbutton = ttk.Button(menuframe, text='Log out', command=login)  # allows changing username
    logoutbutton.grid(row=3)  # positions the button

    ttk.Label(menuframe, text='Memory').grid(row=1, column=1)  # label the memory options
    ttk.Button(menuframe, text='Play', command=memory).grid(row=2, column=1)  # launches the memory game
    # not yet functional
    ttk.Button(menuframe, text='Highscores', state='disabled').grid(row=3, column=1)  # shows the game's highscores

    spacing('menu')  # creates space between all widgets


# memory game
def memory():
    global string  # lets the variable be used in all functions
    global dstring
    global score
    global dscore
    global toptext
    global answer
    global ansentry
    global memoryframe
    memorywindow = Toplevel()  # creates the child window for the memory game
    memorywindow.title('Memory')  # sets the window's title
    memorywindow.focus_set()
    memoryframe = ttk.Frame(memorywindow, padding='5 5 10 10')  # create a frame inside the main window
    memoryframe.grid(row=0, sticky=(N, W, E, S))  # make the frame fill the window

    # StringVar() allows the variables to change globally
    toptext = StringVar()  # the text displayed at the top of the page

    dstring = StringVar()  # the displayed string; emptied when the player presses Start
    string = str(randrange(0, 10))  # the string the player has to enter

    answer = StringVar()  # the string the player has entered

    score = 0  # the player's score, 0 at the beginning
    dscore = StringVar()  # the displayed score

    toptext.set('Memorize and enter the numbers.\nPress the spacebar to begin each round.')
    dstring.set(string)  # sets the displayed string
    dscore.set('Levels passed: ' + str(score))  # converts the score into a string with more clarity

    # displays the game's instructions
    ttk.Label(memoryframe, textvariable=toptext, font='TkHeadingFont').grid(row=0, columnspan=3, sticky='w')

    # displays the string
    ttk.Label(memoryframe, textvariable=dstring, font='TkTextFont').grid(row=1, columnspan=2, sticky='w')
    # displays the score
    ttk.Label(memoryframe, textvariable=dscore, font='TkTextFont').grid(row=3, sticky='w')

    # hides the string and enables the answer field
    ttk.Button(memoryframe, text='Start', command=memorystart).grid(column=2, row=1)

    # allows the player to enter the string
    ansentry = ttk.Entry(memoryframe, textvariable=answer, font='TkTextFont', exportselection=0, state='disabled')
    ansentry.grid(row=2, columnspan=2, sticky='w')  # positions the entry field

    # checks if the string is correct when pressed
    ansentrybutton = ttk.Button(memoryframe, text='Enter', command=lambda: check('memory', answer.get()))
    ansentrybutton.grid(column=2, row=2)

    memorywindow.bind('<space>', memorystart)
    ansentry.bind('<Return>', lambda c: check('memory', answer.get()))  # calls the check function when Enter is pressed

    spacing('memory')  # creates space between all widgets


# creates space between all widgets in the frame with the given name (must follow naming convention)
def spacing(frame):
    exec('for child in ' + frame + 'frame.winfo_children(): child.grid_configure(padx=5, pady=5)')


# starts a memory game round
def memorystart(self):
    dstring.set('')  # sets the displayed string to nothing to hide it
    ansentry['state'] = 'enabled'  # enables the answer field (disabled at the beginning)
    ansentry.focus_set()  # sets focus to the answer field


# checks whether or not the player's answer is correct
def check(game, ans):
    if ans.replace(' ', '') == string:  # all spaces are removed from the answer before comparing
        exec(game + 'next()')  # advances to the next level of the specified game if the answer is correct
    else:
        end()  # calls the end function if the answer is incorrect


# readies the next round in the memory game
def memorynext():
    global string  # lets the outside variable be changed from inside the function
    global score
    string += str(randrange(0, 10))  # adds another random number to the string
    dstring.set(string)  # assigns the new string to the displayed string
    answer.set('')  # empties the answer field
    ansentry['state'] = 'disabled'  # disables the answer field
    score += 1  # adds 1 to the score
    dscore.set('Levels passed: ' + str(score))  # converts the score into a string with more clarity


# ends the current game
def end():
    # chooses the correct form of the word "level"
    if score == 1:
        levelstr = ' level.'
    else:
        levelstr = ' levels.'

    endtext = 'Game over! You passed ' + str(score) + levelstr  # sets the text to change to
    toptext.set(endtext)  # changes the text

    # with open(name + '.score', 'x', )

mainwindow = Tk()  # create the main window
mainwindow.title('Games')  # set the window's title
login()

mainwindow.mainloop()  # starts the main event loop
