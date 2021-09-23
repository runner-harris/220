"""
Name: Walker Harris
mean.py

Problem: Write a program that calculates mean.

Certification of Authenticity:
I hereby certify that all work on this assignment is entirely my own.

"""
import math


def main():
    # what will the program do?
    # -->output the root-mean-square(RMS) average, the harmonic mean, and the geometric mean.
    # what will be the inputs and outputs?
    # -->inputs will be number of values of to entered, and their respective values.
    # -->outputs will be the rms, the harmonic, and the geometric means.
    # what is a step-by-step list of what the program must do, aka an algorithm?
    # -->ask user for inputs
    # -->use those inputs to calculate rms, harmonic, and geometric averages
    # -->print those averages to the screen
    # implement your code:

    num = eval(input("enter the values to be entered: "))
    acc = 0
    acc2 = 0
    acc3 = 1
    for i in range(num):
        values = eval(input("enter value " + str(i + 1) + ": "))
        acc = (acc + values ** 2)
        rms = math.sqrt(acc / num)

        acc2 = acc2 + (1 / values)
        harmonic_mean = num / acc2

        acc3 = (acc3 * values)
        geometric_mean = acc3 ** (1 / num)

    print(round(rms, 3))
    print(round(harmonic_mean, 3))
    print(round(geometric_mean, 3))


if __name__ == '__main__':
    main()
