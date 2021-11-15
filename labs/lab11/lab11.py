"""
Name: Walker Harris
lab11.py
"""
import random


def words(ifn):
    infile = open(ifn, 'r')
    contents = infile.read()
    return contents.split('\n')


def random_word(lst):
    return lst[random.randint(0, len(lst) - 1)]


def fill(word, letters):
    secret = ['_'] * len(word)
    for letter in letters:
        for i in range(len(word)):
            if letter == word[i]:
                secret[i] = letter
    return ''.join(secret)


def won(word, letters):
    x = fill(word, letters)
    if x == word:
        return True


def play():
    w = words("wordlist.txt")
    secret = random_word(w)
    incorrect = 0
    current = "_" * len(secret)
    guesses = []
    while not(won(secret, current)) and incorrect != 7:
        display = fill(secret, guesses)
        print(display)
        for L in guesses:
            print(L, end='')
        letter = input("\nenter a letter: ")
        while letter in guesses:
            letter = input("enter a different letter: ")
        guesses.append(letter)
        display = fill(secret, guesses)
        if letter not in display:
            incorrect += 1
        else:
            current = display
    print("GAME OVER FOOL")


def main():
    # add other function calls here
    play()
    pass


main()
