# import all the necessary modules
from random import randrange  # built-in module
from time import sleep  # built-in module
from misctools import *

# start sequence
"""
sign('2017')  # prints a signature with the given time (technically anything goes but it won't look as intended)
sleep(4)
clear()  # clears the console
print('\n\n\n      Memory')
sleep(4)
clear()
"""

name = input('\n\n\n      Enter a username: ')  # prompts the player to choose a username
clear()

try:
    scorefile = open(name + '.score', 'x', )  # creates a file for the player's scores
except FileExistsError:
    scorefile = open(name + '.score', 'r')  # if a file for the chosen username exists, opens the existing file instead

print('\n\n\n      Memorize and enter the string of numbers.')
sleep(4)
clear()

string = ''     #
score = 0       # assign default values to variables
wait = 2        #

while True:
    string += str(randrange(0, 10))  # adds a random number to the string
    print('\n\n\n     ', string)  # prints the string
    sleep(wait)  # waits for a set time, 2 seconds at the beginning
    clear()
    ans = input('\n\n\n      Enter the string: ')  # prompts the player to enter the string from their memory
    clear()
    if ans == string:  # checks if the answer is correct
        score += 100  # adds 100 to the player's score (larger numbers for more oomph)
        wait += 0.2  # adds 0.2 seconds to the wait between printing the string and clearing the console
    else:  # if the answer isn't correct:
        clear()
        print('Score:', score)  # prints the player's score
        input()  # waits for the player to press Enter before ending the loop
        break  # ends the loop

input()
