from tkinter import *       # GUI tools
from random import *


def start(dstringvar, entryfield):
    dstringvar.set('')  # sets the displayed string to nothing to hide it
    entryfield['state'] = 'enabled'  # enables the answer field (disabled at the beginning)
    entryfield.focus_set()  # sets focus to the answer field


def check(stringvar, dstringvar, entryfield, scorevar, dscorevar, textvar, name, ans):
    global string
    global score
    if ans == string:
        stringvar += str(randrange(0, 10))  # adds another random number to the string
        dstringvar.set(string)  # assigns the new string to the displayed string
        ans.set('')  # empties the answer field
        entryfield['state'] = 'disabled'  # disables the answer field
        scorevar += 100  # adds 100 to the score
        scoreconv(score)  # sets the score display to display the new score
    else:
        textvar.set('Game over!')


def scoreconv(scorevar, dscorevar):
    dscorevar = StringVar()
    dscorevar.set('Score: ' + str(scorevar))
