"""
Name: Walker Harris
lab4.py
"""

from graphics import *
from math import *

def squares():
    """  <---  You can use tripled quotes to write a multi-line comment....

    Modify the following function to:

    Draw squares (20 X 20) instead of circles. Make sure that the center of the square
    is at the point where the user clicks. Make the window 400 by 400.

    Have each successive click draw an additional square on the screen (rather
    than just moving the existing one).

    Display a message on the window "Click again to quit" after the loop, and
    wait for a final click before closing the window.
    """
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Lab 4", width, height)

    # number of times user can move circle
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to move square")
    instructions.draw(win)

    # builds a square
    shape = Rectangle(Point(50, 50), Point(70, 70))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)



    # allows the user to click multiple times to move the circle
    for i in range(num_clicks):


        user_click = win.getMouse()
        shape = Rectangle(Point(user_click.x - 10, user_click.y - 10), Point(user_click.x + 10, user_click.y + 10))
        shape.setOutline("red")
        shape.setFill("red")
        shape.draw(win)

    instructions.setText("Click again to quit.")

    win.getMouse()
    win.close()



def rectangle():
    """
    This program displays information about a rectangle drawn by the user.
    Input: Two mouse clicks for the opposite corners of a rectangle.
    Output: Draw the rectangle.
         Print the perimeter and area of the rectangle.
    Formulas: area = (length)(width)   and    perimeter = 2(length+width)
    """
    width = 400
    height = 400
    win = GraphWin("Lab4 Rectangle", width, height)

    p1 = win.getMouse()
    p2 = win.getMouse()

    rectangle = Rectangle(p1, p2)
    rectangle.draw(win)

    x1 = p1.getX()
    x2 = p2.getX()
    y1 = p1.getY()
    y2 = p2.getY()

    length = abs(x2 - x1)
    width = abs(y2 - y1)
    area = length * width
    perimeter = 2 * (length + width)

    txt = Text(Point(50,50), "The area is: " + str(area))
    txt2 = Text(Point(80, 80), "The perimeter is: " + str(perimeter))
    txt.draw(win)
    txt2.draw(win)

    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click again to close")
    instructions.draw(win)

    win.getMouse()
    win.close()

    pass

def circle():
    width = 400
    height = 400
    win = GraphWin("Lab4 Cricle", width, height)

    p1 = win.getMouse()
    p2 = win.getMouse()
    x1 = p1.getX()
    x2 = p2.getX()
    y1 = p1.getY()
    y2 = p2.getY()
    r = sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))

    circle = Circle(p1, r)
    circle.draw(win)
    txt = Text(Point(100, 50), "The radius is: " + str(r))
    txt.draw(win)



    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click again to close")
    instructions.draw(win)
    win.getMouse()
    win.close()


def pi2():

    n = eval(input("Enter the number of terms to sum: "))
    acc = 0
    for i in range(n):
        num = 4
        denom = 1 + 2 * i     #i = loop variable
        frac = (num / denom) * ((-1) ** i)
        acc = acc + frac

    print(acc)
    print(pi - acc)

def main():
    squares()
    rectangle()
    circle()
    pi2()


main()
