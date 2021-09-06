"""
Name: Walker Harris
lab2.py
Problem:
Certification of Authenticity:
I hereby certify that the following assignment is entirely my own work.
"""
import math
def sum_of_threes():
    upperbound = eval(input("enter an upper bound:"))
    acc = 0
    for x in range(0, upperbound + 1, 3):
      acc = acc + x
    print(acc)

def multiplication_table():
    for h in range(1, 11):
        for l in range(1, 11):
            print(h * l, end=" ")
        print()

def triangle_area():
    a = eval(input("enter the length of side one:"))
    b = eval(input("enter the length of side two:"))
    c = eval(input("enter the length of side three:"))
    s = (a + b + c)/2
    x = s*(s-a)*(s-b)*(s-c)
    area = math.sqrt(x)
    print(area)

def sumSquares():
    start = eval(input("enter the lower range:"))
    end = eval(input("enter the upper range:"))
    acc = 0
    for x in range(start, end + 1):
        acc = x ** 2 + acc
    print(acc)

def power():
    base = eval(input("enter the base:"))
    exp = eval(input("enter the exponent:"))
    acc = 1
    for x in range(exp):
        acc = acc * base
    print(acc)

power()
sumSquares()
triangle_area()
multiplication_table()
sum_of_threes()
