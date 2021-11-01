"""
Name: Walker Harris
interest.py

Problem: Write a program that computes the monthly interest charge on a credit card account.

Certification of Authenticity:
I hereby certify that all work on this assignment is entirely my own.

"""


def main():
    apr = eval(input("enter the annual interest rate: "))
    days = eval(input("enter the number of days in the billing cycle: "))
    prev_balance = eval(input("enter the previous net balance: "))
    payment = eval(input("enter the payment amount: "))
    day_paid = eval(input("enter the day of the billing cycle in which you paid:"))
    avg_daily_balance = ((prev_balance * days)-(payment * (days - day_paid))) / (days)
    mpr = (apr / 12) / 100
    acc = 0
    for acc in range(days):
        acc = avg_daily_balance * mpr
    print(round(acc, 2))


if __name__ == '__main__':
    main()
