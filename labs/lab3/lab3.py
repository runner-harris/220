"""
Name: Walker Harris
lab3.py
"""

def average():
    tests = eval(input("enter the amount of tests: "))
    acc = 0
    for i in range(tests):
        hw = eval(input("Enter the hw grade: "))
        acc = acc + hw / tests
    print("This is the average", acc)

def tip_jar():
    totaltips = 0
    for i in range(5):
        tip = eval(input("enter the amount of your tip:"))
        totaltips = totaltips + tip
    print(totaltips)

def newton():
    x = eval(input("enter the value: "))
    refine = eval(input("enter the amount you want to improve the function: "))
    approx = x / 2
    for i in range(refine):
        approx = (approx + (x / approx)) / 2
    print(approx)

def sequence():
    num = eval(input("enter the number of items: "))
    for i in range(1, num):
         print(1 + (i // 2) * 2)


def pi():
    n = eval(input("enter number of terms: "))
    acc = 1
    for i in range(n + 1):
        numerator = 2 + ((i // 2) * 2)
        denomenator = 1 + (((i + 1) // 2) * 2)
        fract = numerator / denomenator
        acc = fract * acc
    print(acc)


sequence()
average()
tip_jar()
newton()
pi()