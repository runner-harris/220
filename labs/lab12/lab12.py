"""
Name: Walker Harris
lab12.py
"""

from random import randint


def find_and_remove_first(list, value):
    try:
        i = list.index(value)
        list[i] = "Walker"
    except:
        pass
    print(list)


def read_data(int):
    f = open(int, 'r')
    data = f.read()
    data = data.split()
    print(data)
    return data


def is_in_linear(search_val, values):
    i = 0
    while i < len(values):
        if search_val in values:
            print("true")
            return True
        i += 1
    return False


def good_input():
    num = eval(input("enter a number between 1 and 10: "))
    while num >= 1 and num <= 10:
        print(num)
        return num
    if not (num >= 1 and num <= 10):
        print(num, " is not in range")


def num_digits():
    num = eval(input("enter a number: "))
    while num >= 1:
        digits = 0
        while num != 0:
            num = num // 10
            digits += 1
        print("digits are: ", digits)
        num = eval(input("enter a new number, '0' to quit: "))


def hi_lo_game():
    secret = randint(1, 100)
    guess = 1
    num = eval(input("guess a number between 1 and 100: "))
    while num != secret and guess <= 7:
        guess += 1
        if num < secret:
            print("too low!")
        else:
            print("too high!")
        num = eval(input("guess again: "))
    if secret == num:
        print("you won in ", guess, " guesses")
    else:
        print("you lost")


def main():
    # add other function calls here
    # find_and_remove_first(["walker", "john", "bill"], 1)
    # read_data("text.txt")
    # is_in_linear(4, [2, 4, 5])
    # good_input()
    # num_digits()
    # hi_lo_game()
    pass


main()
