"""
File: BeeperRowAdv.py
Name:
------------------------------
This program makes Karel fill up
Street 1 with some beepers already
existed
(This should be world insensitive)
"""

from karel.stanfordkarel import *


def main():
    """
    Karel will fill the first Street in any world
    """
    while front_is_clear():
        if on_beeper():
            move()
        else:
            put_beeper()
            move()
    if not on_beeper(): #不能只加一句put_beeper 否則若遇到最後有球則無法應用（OBOB)
        put_beeper()
    else:#若else後不須執行則可直接省略
        pass












####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)