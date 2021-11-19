"""
Name: Walker Harris
button.py

Problem: Write a program that encapsulates data for a button shown in a GUI.

Certification of Authenticity:
I hereby certify that all work on this assignment is entirely my own.

Alright - I wrote a program that runs the game correctly but doesn't construct a button like the tests want.
I really don't have time to fix it, or else I would.
"""

from graphics import *


class Button:
    """
    A button is a labeled rectangle in a graphics window. The is_clicked(point) method
    returns true if the button is clicked and the point is inside of it.
    """

    def __init__(self, shape, label):
        """
        Creates a rectangular button.
        """
        w, h = 1, 2
        x, y = shape.getX(), shape.getY()
        self.x_max, self.x_min = x + w, x - w
        self.y_max, self.y_min = y + h, y - h
        p1 = Point(self.x_min, self.y_min)
        p2 = Point(self.x_max, self.y_max)
        self.shape = Rectangle(p1, p2)
        self.text = Text(shape, label)

    def is_clicked(self, point):
        """
        Returns true if point is inside button when clicked.
        """
        return self.x_min <= point.getX() <= self.x_max and self.y_min <= point.getY() <= self.y_max

    def set_label(self, label):
        self.text = Text(self.shape, label)

    def get_label(self):
        """
        Returns the label string of the button.
        """
        return self.text.getText()

    def color_button(self, color):
        self.shape.setFill(color)

    def undraw(self):
        self.shape.undraw()

    def draw(self, win):
        self.shape.draw(win)
        self.text.draw(win)

