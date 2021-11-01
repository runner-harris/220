"""
Name: <Walker Harris>
lab9.py
"""
from graphics import *
import math


def addTen(nums):
    for i in range(len(nums)):
        nums[i] += 10


def squareEach(nums):
    for i in range(len(nums)):
        nums[i] **= 2

def sumList(nums):
    acc = 0
    for i in range(len(nums)):
        acc += nums[i]
    return acc


def toNumbers(strList):
    for i in range(len(strList)):
        strList[i] = float(strList[i])


def writeSumOfSquares():
    infile = input("enter file name: ")
    outfile = input("enter outfile name: ")
    readfile = open(infile, 'r')
    writefile = open(outfile, 'w')
    for line in readfile:
        nums = line.split()
        toNumbers(nums)
        squareEach(nums)
        summation = sumList(nums)
        writefile.write("Sum of squares = " + str(summation) + "\n")


def starter():
    weight = float(input("enter the players weight: "))
    numWins = int(input('enter the players wins: '))
    if 150 <= weight < 160 and numWins >=5:
        print('is a starter')
    elif weight > 199 or numWins > 20:
        print('is a starter')
    else:
        print('not a starter')


def leapYear():
    year = eval(input("Enter a year: "))
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True


def circleOverlap():
    win = GraphWin("circle", 400, 400)
    p1 = win.getMouse()
    p2 = win.getMouse()
    r = math.sqrt((p1.getX() - p2.getX()) ** 2 + (p1.getY() - p2.getY()) ** 2)
    c1 = Circle(p1, r)
    c1.draw(win)
    p3 = win.getMouse()
    r2 = math.sqrt((p3.getX() - p2.getX()) ** 2 + (p3.getY() - p2.getY()) ** 2)
    c2 = Circle(p3, r2)
    c2.draw(win)
    p4 = math.sqrt((p1.getX() - p3.getX()) ** 2 + (p1.getY() - p3.getY()) ** 2)

    if p4 <= (r2 + r2):
        Text(Point(200, 300), "The circles overlap.").draw(win)
    else:
        Text(Point(200, 300), "The circles do not overlap.").draw(win)
    win.getMouse()
    win.close()


def main():
    # add other function calls here
    addTen([5, 7, 2])
    squareEach([3, 5.7, 2])
    sumList([1, 2, 3])
    toNumbers([3, 5.7, 2])
    writeSumOfSquares()
    starter()
    leapYear()
    circleOverlap()
    pass


main()
