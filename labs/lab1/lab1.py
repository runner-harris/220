"""
Name: Walker Harris
lab1.py
Problem: This function calculates the area of a rectangle.
Certification of Authenticity:
I hereby certify that the following assignment is entirely my own work.
"""

def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)

def calc_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    height = eval(input("Enter the height: "))
    volume = length * width * height
    print("Volume =", volume)

def shooting_percentage():
   shots = eval(input("Enter the amount of shots: "))
   made = eval(input("Enter the amount of shots made: "))
   percentage = made / shots * 100
   print("Shot percentage =", percentage)

def coffee():
    coffee = eval(input("Enter the number of pounds of coffee purchased: "))
    price = 10.5 * coffee + .86 * coffee + 1.5
    print("shipping cost =", price)

def kilometers_to_miles():
    kilometers = eval(input("Enter the number of kilometers traveled: "))
    miles = kilometers / 1.61
    print("miles =", miles)

calc_rec_area()
calc_volume()
shooting_percentage()
coffee()
kilometers_to_miles()
