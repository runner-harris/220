"""
Name: Walker Harris
lab5.py
"""

from graphics import *
from math import *


def target():
    w = 500
    h = 500
    win = GraphWin("Archery Target", w, h)

    # Add code here to get the dimensions and draw the target
    r = (w / 5) / 2
    circ1 = Circle(Point(w/2, h/2), r * 5)
    circ1.setFill("white")
    circ1.draw(win)
    circ2 = Circle(Point(250, 250), r * 4)
    circ2.setFill("black")
    circ2.draw(win)
    circ3 = Circle(Point(250, 250), r * 3)
    circ3.setFill("blue")
    circ3.draw(win)
    circ4 = Circle(Point(250, 250), r * 2)
    circ4.setFill("red")
    circ4.draw(win)
    circ5 = Circle(Point(250, 250), r)
    circ5.setFill("yellow")
    circ5.draw(win)

    # Wait for another click to exit
    win.getMouse()
    win.close()


def triangle():
    win_width = 500
    win_height = 500
    win = GraphWin("Draw a Triangle", win_width, win_height)

    # Add code here to accept the mouse clicks, draw the triangle.
    p1 = win.getMouse()
    p2 = win.getMouse()
    p3 = win.getMouse()

    dxside1 = p1.getX() - p2.getX()
    dyside1 = p1.getY() - p2.getY()
    dxside2 = p2.getX() - p3.getX()
    dyside2 = p2.getY() - p3.getY()
    dxside3 = p3.getX() - p1.getX()
    dyside3 = p3.getY() - p1.getY()

    s1 = sqrt(dxside1 ** 2 + dyside1 ** 2)
    s2 = sqrt(dxside2 ** 2 + dyside2 ** 2)
    s3 = sqrt(dxside3 ** 2 + dyside3 ** 2)

    length = s1 + s2 + s3
    s = (s1 + s2 + s3) / 2
    area = sqrt(s *(s - s1) * (s - s2) * (s - s3))

    tex = Text(Point(200, 200), "length: " + str(length))
    tex2 = Text(Point(200, 300), "area: " + str(area))
    tex.draw(win)
    tex2.draw(win)

    triangle_1 = Polygon(p1, p2, p3)
    triangle_1.draw(win)

    # Wait for another click to exit
    win.getMouse()
    win.close()


def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")
    red_entry = Entry(Point(200, 220), 10)
    red_entry.draw(win)

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")
    green_entry = Entry(Point(200, 250,), 10)
    green_entry.draw(win)

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")
    blue_entry = Entry(Point(200, 280), 10)
    blue_entry.draw(win)

    # display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)

    win.getMouse()
    for i in range(5):
        red = int(red_entry.getText())
        blue = int(blue_entry.getText())
        green = int(green_entry.getText())
        color = color_rgb(red, green, blue)
        shape.setFill(color)
        win.getMouse()

    win.getMouse()
    win.close()


def process_string():
    s1 = "Hello World"
    print(s1[0])
    print(s1[-1])
    print(s1[2:6])
    print(s1[0] + s1[-1])
    print(s1[0:3] * 10)
    for i in s1:
        print(i)
    print(len(s1))


def process_list():
    pt = Point(5, 10)
    values = [5, 'hi', 2.5, 'there', pt, '7.2']
    x = values[1] + values[3]
    print(x)
    x = float(values[0]) + float(values[2])
    print(x)
    x = values[1] * 5
    print(x)
    x = [values[2], values[3], values[4]]
    print(x)
    x = [values[2], values[3], values[0]]
    print(x)
    x = [values[2], values[0], float(values[5])]
    print(x)
    x = float(values[0]) + float(values[2]) + float(values[5])
    print(x)
    x = len(values)
    print(x)


def another_series():
    num = eval(input("Enter the number of terms: "))
    s = 0
    for i in range(num):
        y = 2 + (2 * (i % 3))
        s = s + y
        print(y, end=" ")
    print("sum = ", s)


def main():
    target()
    triangle()
    color_shape()
    process_string()
    process_list()
    another_series()
    pass


main()
