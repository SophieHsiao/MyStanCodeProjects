"""
File: Steeplechase.py
Name: TODO:
---------------------------------
TODO:
"""

from karel.stanfordkarel import *


def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    for i in range(11):

        if front_is_clear():
            #facing east
            move()
        else:
            jump()
            turn_left() #Karel needs to face east after jumping down


def jump():
    """
    pre-condition:Karel is on the left side of the wall, facing East
    post-condition: Karel is on the right of the wall
    """
    up()
    cross()
    down()


def up():
    """
    pre-condition:Karel is on the right of the wall, facing east
    post-condition:Karel is facing north
    """
    turn_left()
    #facing north
    while not right_is_clear():
        move()

    """
    while not front_is_clear():
        turn_left()
        move()
        turn_right()
    """


def turn_right():
    for i in range(3):
        turn_left()


def cross():
    """
    pre-condition:Karel is facing north
    post-condition:Karel is on the upper right,facing south
    """
    turn_right()
    move()
    turn_right()


def down():
    """
    pre-condition:Karel is on the upper right,facing south
    post-condition:Karel is at the left side of the wall,facing south
    """
    while front_is_clear():
        move()

# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
