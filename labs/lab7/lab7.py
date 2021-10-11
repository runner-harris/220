"""
Name: Walker Harris
Partner: <your partner's name goes here – first and last>
lab7.py
"""


def cash_conversion():
    num = input("Enter your money: ")
    print('${}.{:0>2}'.format(num, 0))


def encode():
    x = input("Enter the message: ")
    k = eval(input("Enter the key: "))
    for c in x:
        i = ord(c) + k
        print(chr(i), end="")


def sphere_area(radius):
    area = 4 * 3.14 * (radius ** 2)
    return area


def surface_area():
    area = sphere_area(5)
    print(area)


def sphere_volume(radius):
    volume = (4 / 3) * 3.14 * (radius ** 3)
    return volume


def volume():
    vol = sphere_volume(5)
    print(vol)


def sum_n(n):
    acc = 0
    for i in range(n + 1):
        acc = acc + i
    return acc


def sum_n_cubes(n):
    acc = 0
    for i in range(n + 1):
        acc = acc + i ** 3
    return acc


def total():
    x = sum_n(3)
    print(x)
    y = sum_n_cubes(3)
    print(y)


def encode_better():
    x = input("Enter the message: ")
    k = input("Enter the key: ")
    acc = " "
    for i in range(len(x)):
        c = ord(x[i])
        key = ord(k[i])
        new = c + key - 97
        acc += chr(new)
    print(acc)


def main():
    # add function calls here
    # cash_conversion()
    # encode()
    # encode_better()
    # surface_area()
    # volume()
    # total()


    pass


main()
