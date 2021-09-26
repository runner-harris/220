"""
Name: Walker Harris
traffic.py

Problem: Write a program that analyzes traffic patterns using nested loops.

Certification of Authenticity:
I hereby certify that all work on this assignment is entirely my own.

"""

def main():
    num = eval(input("How many roads were surveyed?: "))
    acc = 0
    acc2 = 0
    acc3 = 0
    for i in range(num):
        days = eval(input("How many days was road " + str(i + 1) + " surveyed? "))
        for _ in range(days):
            cars = eval(input("How many cars traveled on day " + str(_ + 1) + "? "))
            acc = acc + cars / days
            acc2 = acc2 + cars
            acc3 = acc2 / num
        print("Road " + str(i + 1) + " average vehicles per day: ", round(acc, 2))
        acc = 0
    print("Total number of vehicles traveled on all roads:", round(acc2, 2))
    print("Average number of vehicles per road:", round(acc3, 2))


if __name__ == "__main__":
    main()
