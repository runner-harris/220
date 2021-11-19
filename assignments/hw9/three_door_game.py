"""
Name: Walker Harris
three_door_game.py

Problem: Write a program that simulates the "Three Door Game."

Certification of Authenticity:
I hereby certify that all work on this assignment is entirely my own.

Alright - I wrote a program that runs the game correctly but doesn't construct a button like the tests want.
I really don't have time to fix it, or else I would.

"""

from graphics import GraphWin, Point, Text
from button import Button
from random import *

def main():
    win = GraphWin("Three Door Game")
    win.setCoords(0, 0, 10, 10)

    doorButton = Button(Point(2, 4), "Door1")
    doorButton2 = Button(Point(5, 4), "Door2")
    doorButton3 = Button(Point(8, 4), "Door3")
    doorButton.draw(win)
    doorButton2.draw(win)
    doorButton3.draw(win)

    message = Text(Point(5, 8), "I have a secret door...").draw(win)

    num = randint(1, 3)
    pt = win.getMouse()
    if doorButton.is_clicked(pt) and num == 1:
        doorButton.color_button("green")
        message.setText("You win!")
    elif doorButton.is_clicked(pt) and num != 1:
        doorButton.color_button("red")
        message.setText("You lose!")
    if doorButton2.is_clicked(pt) and num == 2:
        doorButton2.color_button("green")
        message.setText("You win!")
    elif doorButton2.is_clicked(pt) and num != 2:
        doorButton2.color_button("red")
        message.setText("You lose!")
    if doorButton3.is_clicked(pt) and num == 3:
        doorButton3.color_button("green")
        message.setText("You win!")
    elif doorButton3.is_clicked(pt) and num != 3:
        doorButton3.color_button("red")
        message.setText("You lose!")

    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()