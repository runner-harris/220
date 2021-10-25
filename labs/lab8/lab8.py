"""
Name: Walker Harris
Lab8.py
"""
from encryption import encode, encode_better


def number_words(in_file_name, out_file_name):
    in_file = open(in_file_name, 'r')
    out_file = open(out_file_name, 'w+')
    i = 1
    for line in in_file:
        words = line.split()
        for word in words:
            out_file.write(str(i) + " " + word + '\n')
            i += 1
    in_file.close()
    out_file.close()


def hourly_wages(in_file_name, out_file_name):
    in_file = open(in_file_name, 'r')
    out_file = open(out_file_name, 'w')
    for line in in_file:
        parts = line.split()
        wage = float(parts[2])
        wage += 1.65
        wage = str(wage * int(parts[3]))
        out_file.write(str(parts[0] + " " + parts[1] + " " + wage + "\n"))
    in_file.close()
    out_file.close()


def calc_check_sum(isbn):
    acc = 0
    for i in range(10):
        pos = 10 - i
        acc += int(isbn[i]) * pos
    return acc


def send_message(file, friend):
    in_file = open(file, 'r')
    out_file = open(friend + '.txt', 'w')
    for line in in_file:
        out_file.write(line)


def send_safe_message(file, friend, key):
    in_file = open(file, 'r')
    out_file = open(friend + '.txt', 'w')
    for line in in_file:
        out_file.write(encode(line, key))


def send_uncrackable_message(file, friend, pad):
    padfile = open(pad, 'r')
    key = padfile.read()
    in_file = open(file, 'r')
    out_file = open(friend + '.txt', 'w')
    for line in in_file:
        out_file.write(encode_better(line, key))


def main():
    # add other function calls here
    number_words("Walrus.txt", "Wout.txt")
    hourly_wages("hourly_wages.txt", "new.txt")
    calc_check_sum('0072946520')
    send_message("message.txt", "Bob")
    send_safe_message("secret_message.txt", "Bill", 3)
    send_uncrackable_message("safest_message.txt", "Walker", "pad.txt")
    pass


main()
