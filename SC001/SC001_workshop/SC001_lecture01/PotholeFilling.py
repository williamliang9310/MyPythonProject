"""
File: PotholeFilling.py
Name: william:
--------------------------
This program shows karel filling 3
potholes. Students learn the concept of
decomposition through the process.
"""

from karel.stanfordkarel import *

def turn_right():
    for i in range(3):
        turn_left()

def put_99_brrpers():
    for i in range(99):
        put_beeper()

def go_right():
    turn_right()
    move()

def go_in():
    turn_right()
    move()

def turn_back():
    for i in range(2):
        turn_left()

def go_out():
    turn_back()
    move()

def go_next():
    go_out()
    go_right()
    move()
    go_in()
    put_99_brrpers()


def main():
    """
    TODO:
    """
    move()
    turn_right()
    move()
    put_99_brrpers()
    for i in range(2):
        go_next()
    go_out()
    go_right()


# ----- DO NOT EDIT CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
