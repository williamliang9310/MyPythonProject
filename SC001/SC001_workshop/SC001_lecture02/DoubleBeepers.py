"""
File: DoubleBeepers.py
Name:william
-------------------------------
TODO:
"""

from karel.stanfordkarel import *

def turn_back():
    for i in range(2):
        turn_left()
def double_beepers():

    while on_beeper():
        pick_beeper()
        move()
        for i in range(2):
            put_beeper()
        turn_back()
        move()
        turn_back()
        put_beeper()
        put_beeper()


def take_back_beepers():
    while on_beeper():
        pick_beeper()
        turn_back()
        move()
        put_beeper()
        turn_back()
        move()

def go_home():
    turn_back()
    while front_is_clear():
        move()
    turn_back()
def main():
    """
    Karel will double the beepers
    """
    move()
    double_beepers()
    move()
    take_back_beepers()
    go_home()
















#----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
