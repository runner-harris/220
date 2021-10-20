"""
Name: Walker Harris
vigenere.py

Problem: Write a program that implements a vigenere cipher.

Certification of Authenticity:
I hereby certify that all work on this assignment is entirely my own.

"""
from graphics import *


def code(message, keyword):
    message = message.replace(" ", "")
    message = message.upper()

    keyword = keyword.upper()
    new_code = ' '
    start = ord('A')
    for i in range(len(message)):
        b = i % len(keyword)
        c = ord(message[i]) - start
        k = start + (ord(keyword[b]) - start + c) % 26
        new_code += chr(k)
    return new_code.strip()


def main():
    win = GraphWin("Vigenere", 400, 300)
    Text(Point(60, 50), "Message to code").draw(win)
    Text(Point(70, 100), "Enter keyword").draw(win)

    message = Entry(Point(200, 50), 20).draw(win)
    keyword = Entry(Point(200, 100), 15).draw(win)

    button = Rectangle(Point(170, 150), Point(230, 200)).draw(win)
    button_label = Text(Point(200, 175), "Encode").draw(win)

    win.getMouse()

    message = message.getText()
    keyword = keyword.getText()
    new_code = code(message, keyword)
    code(message, keyword)
    Text(Point(200, 175), new_code).draw(win)

    button.undraw()
    button_label.undraw()

    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()
