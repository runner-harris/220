"""
Name: Walker Harris
Lab6.py
"""


def name_reverse():
    """
    Read a name in first-last order and display it in last-comma-first order.
    """
    name = input("Enter your first and last name: ")
    x = name.split(' ')
    print(x[1] + ", " + x[0])


def company_name():
    domain = str(input("Enter a website name: "))
    x = domain.split('.')
    print(str(x[1]))


def initials():
    names = eval(input("how many names are there? "))
    for i in range(names):
        first = input("Enter the first name of student " + str(i + 1) + ": ")
        last = input("Enter " + first + "'s last name: ")
        initial = first[0] + last[0]
        print(first +"'s initials are " + initial.upper())



def names():
    names = input("Enter a list of names, first and last only, separated by commas: ")
    name_list = names.split(', ')
    for name in name_list:
        name = name.split(' ')
        first = name[0][0].upper()
        last = name[1][0].upper()
        print(first + last, end=" ")


def thirds():
    num = eval(input("how many sentences will be input/ "))
    for i in range(num):
        sentence = input("\n enter a sentence: ")
        for ch in range(2, len(sentence), 3):
            print(sentence[ch], end=" ")


def word_average():
    acc = 0
    sentence = input("enter a sentence: ")
    word = sentence.split()
    for i in word:
        acc = acc + len(word)
    acc = acc / len(word)
    print(acc)


def pig_latin():
    sentence = input("enter a sentence ")
    sentence = sentence.lower()
    sen = sentence.split(" ")
    for word in sen:
        x = word[1:]
        x = x + word[0] + "ay"
        print(x, end=" ")


def main():
    # name_reverse()
    # company_name()
    # initials()
    # names()
    # thirds()
    # word_average()
    #pig_latin()
    # add other function calls here

main()
