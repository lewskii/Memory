from tkinter import *       # GUI tools
from tkinter import ttk     # GUI tools
from random import randrange  # returns a random integer in a given range
from os import makedirs, path  # for creating directories and displaying file paths
from datetime import datetime  # dates and times
from time import sleep  # stops the program for a specified time

print('Launched program')  # log message, printed in the console


# creates the login screen
def login():
    try:
        menuframe.destroy()
        print('Removed menu interface')  # log message, printed in the console
    except NameError:
        pass

    global loginframe  # global allows the variable to be used in all functions
    loginframe = ttk.Frame(mainwindow, padding='5 5 10 5')  # create a frame inside the main window
    loginframe.grid(row=0, sticky=(N, W, E, S))  # make the frame fill the window

    global user
    user = StringVar()  # the username, StringVar() allows the variable to change globally
    user.trace_variable('w', charlimit)

    # tells the user the characters that can't be used in the username
    badcharlabel = ttk.Label(loginframe, text='Username cannot contain characters / \\ : * ? " < > | +')
    badcharlabel.grid(row=0, columnspan=3, sticky='w')  # positions the label

    # allows the user to enter a username
    ttk.Label(loginframe, text='Enter a username:').grid(row=1, sticky='e')  # labels the username entry field
    userentry = ttk.Entry(loginframe, textvariable=user)  # creates the username entry field
    userentry.focus_set()  # sets focus to the username entry field
    userentry.grid(row=1, column=1, sticky='w')  # positions the username entry field

    # creates the main menu
    userentrybutton = ttk.Button(loginframe, text='Continue', command=lambda: checkname(user.get()))
    userentrybutton.grid(row=1, column=2, sticky='w')

    # my signature
    signaturetext = 'Made by Leevi Aaltonen, 2017, released under MIT license.'  # created variable because text is long
    signature = ttk.Label(loginframe, text=signaturetext, font='TkSmallCaptionFont')  # displays the signature
    signature.grid(row=2, columnspan=3, sticky='sw')  # positions the signature

    spacing('login')  # creates space between all widgets
    print('Created login interface')  # log message, printed in the console

    userentry.bind('<Return>', lambda cn: checkname(user.get()))  # binds Enter to the menu function


# limits the number of characters that can be entered into the username field
def charlimit(*args):
    s = user.get()
    if len(s) > 16:
        user.set(s[:16])
        print('Limited username length (16)')  # log message, printed in the console


# checks the username for forbidden characters
def checkname(name):
    badchars = ['/', '\\', '*', '?', ':', '"', '<', '>', '|', '+']  # these characters can't be used in the username
    if set(name).isdisjoint(badchars) and name.replace(' ', '') != '':
        print('Username is valid')  # log message, printed in the console
        menu()  # creates the menu if the username doesn't contain any bad characters
    else:
        print('Username is invalid')


# creates the main menu
def menu():
    loginframe.destroy()
    print('Removed login interface')  # log message, printed in the console

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
    print('Created menu interface')  # log message, printed in the console


# memory game
def memory():
    print('Launched memory game')
    global string  # lets the variable be used in all functions
    global dstring
    global score
    global dscore
    global toptext
    global answer
    global ansentry
    global memoryframe
    global memorywindow
    memorywindow = Toplevel()  # creates the child window for the memory game
    memorywindow.title('Memory')  # sets the window's title
    memorywindow.focus_set()  # sets focus to the window
    memorywindow.resizable(0, 0)  # disables resizing of the window
    memoryframe = ttk.Frame(memorywindow, padding='5 5 10 10')  # create a frame inside the main window
    memoryframe.grid(row=0, sticky=(N, W, E, S))  # make the frame fill the window

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

    # hides the string and enables the answer field and check button
    global startbutton
    startbutton = ttk.Button(memoryframe, text='Start', command=memorystart)
    startbutton.grid(column=2, row=1)  # positions the start button

    # allows the player to enter the string
    ansentry = ttk.Entry(memoryframe, textvariable=answer, font='TkTextFont', exportselection=0, state='disabled')
    ansentry.grid(row=2, columnspan=2, sticky='w')  # positions the entry field

    # checks if the string is correct when pressed (disabled in the beginning)
    global checkbutton
    checkbutton = ttk.Button(memoryframe, text='Enter', command=lambda: check('memory'), state='disabled')
    checkbutton.grid(column=2, row=2)

    memorywindow.bind('<space>', lambda s: memorystart())
    ansentry.unbind('<space>')
    ansentry.bind('<Return>', lambda c: check('memory'))  # calls the check function when Enter is pressed

    spacing('memory')  # creates space between all widgets
    print('Created memory game interface')  # log message, printed in the console


# creates space between all widgets in the frame with the given name
def spacing(frame):
    exec('for child in ' + frame + 'frame.winfo_children(): child.grid_configure(padx=5, pady=5)')


# starts a memory game round
def memorystart():
    if dstring.get() != '':
        print('Started memory game round', score + 1)  # log message, printed in the console
        dstring.set('')  # sets the displayed string to nothing to hide it
        ansentry['state'] = 'enabled'  # enables the answer field (disabled at the beginning)
        ansentry.focus_set()  # sets focus to the answer field
        startbutton['state'] = 'disabled'  # disables the start button
        checkbutton['state'] = 'enabled'  # enables the check button


# checks whether or not the player's answer is correct
def check(game):
    exec(game + 'window.focus_set()')  # sets focus to the game window
    checkbutton['state'] = 'disabled'  # disables the check button
    ansentry['state'] = 'disabled'  # disables the answer field
    if answer.get().replace(' ', '') == string:  # all spaces are removed from the answer before comparing
        print('Answer is correct')  # log message, printed in the console
        exec(game + 'next()')  # advances to the next level of the specified game if the answer is correct
    else:  # the game ends if the answer is incorrect
        print('Answer is incorrect')  # log message, printed in the console
        startbutton['state'] = 'disabled'  # disables the start button
        answer.set('')  # empties the answer field
        memorywindow.unbind('<space>')  # unbinds the spacebar from the start function
        # chooses the correct form of the word "level"
        if score == 1:
            levelstr = ' level.'
        else:
            levelstr = ' levels.'

        toptext.set('Game over! You passed ' + str(score) + levelstr)  # changes the text

        userfilename = user.get().replace(' ', '+')

        makedirs('scores/', exist_ok=True)  # creates the folder for the scores unless it exists
        try:
            open('scores/' + userfilename + '.score', 'x')  # creates the user's score file
        except FileExistsError:
            pass  # does nothing if the files exist
        try:
            open('scores/' + game + '.score', 'x')  # creates the game's highscore file
        except FileExistsError:
            pass  # does nothing if the files exist

        # writes the user's score to their file
        with open('scores/' + userfilename + '.score', 'a') as scorefile:
            scoreline = datetime.now().ctime().replace(' ', '+') + ' ' + game.title() + ' ' + str(score) + '\n'
            scorefile.write(scoreline)
        print('Saved the score to', path.dirname(path.realpath(__file__)) +
              '\\scores\\' + userfilename + '.score')  # log message, printed in the console

        # saving highscores into a file
        highscores = {}  # creates a dictionary for the highscores
        with open('scores/' + game + '.score') as highscorefile:  # opens the file to be used for the indented code
            for line in highscorefile:  # does the indented code to every line in the file
                split = line.split()  # splits the current line into a list, items separated by spaces
                highscores[split[0]] = split[1]  # adds the first two list items into the highscore dictionary
        try:
            if int(highscores[userfilename]) < score:
                highscores[userfilename] = score  # replaces the player's old highscore if the player passes it
                print('New highscore in', game, 'for', user.get() + ':', score)
        except KeyError:
            highscores[userfilename] = score  # sets the player's highscore if it doesn't exist
        with open('scores/' + game + '.score', 'w') as highscorefile:
            for i in highscores:
                highscorefile.write(i + ' ' + str(highscores[i]) + '\n')  # writes the updated highscores to the file

        exec(game + 'window.after(3500, lambda: ' + game + 'window.destroy())')  # closes the specified window
        print('Closing', game, 'window')  # log message, printed in the console


# readies the next round in the memory game
def memorynext():
    global string  # lets the outside variable be changed from inside the function
    global score
    string += str(randrange(0, 10))  # adds another random number to the string
    dstring.set(string)  # assigns the new string to the displayed string
    answer.set('')  # empties the answer field
    score += 1  # adds 1 to the score
    dscore.set('Levels passed: ' + str(score))  # converts the score into a string with more clarity
    startbutton['state'] = 'enabled'  # enables the start button


mainwindow = Tk()  # create the main window
mainwindow.title('Memory')  # set the window's title
mainwindow.resizable(0, 0)  # disables resizing of the window
login()  # calls the function to create the login screen

mainwindow.mainloop()  # starts the main event loop
print('Program closing')