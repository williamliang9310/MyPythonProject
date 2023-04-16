"""
File: Steeplechase.py
Name: william
---------------------------------
TODO:
"""

from karel.stanfordkarel import *


def turn_right():
    for i in range(3):
        turn_left()




def up():
    while not front_is_clear():
        turn_left()
        move()
        turn_right()


def cross():
    move()
    turn_right()

def down():
    while front_is_clear():
        move()
    turn_left()


def jump():
    up()
    cross()
    down()

def main():
    """
    Karel will double the beepers
    """
    for i in range(11):
       if front_is_clear():
           move()
       else:
           jump()



# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
