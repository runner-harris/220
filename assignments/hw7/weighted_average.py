"""
Name: Walker Harris
weighted_average.py

Problem: Write a program that interprets data from a file and writes it to a new file.

Certification of Authenticity:
I hereby certify that all work on this assignment is entirely my own.

"""


def weighted_average(in_file_name, out_file_name):
    in_file = open(in_file_name, 'r')
    out_file = open(out_file_name, 'w')
    students = 0
    class_grades = 0
    for line in in_file:
        parts = line.split(": ")
        nums = parts[1].split()
        grades = 0
        total_weight = 0
        for i in range(0, len(nums) - 1, 2):
            weight = float(nums[i])
            grade = float(nums[i + 1])
            total_weight += float(weight)
            grades += grade * weight

        if total_weight == 100:
            avg = grades / 100
            class_grades += avg
            students += 1
            out_file.write(parts[0] + "'s " + "average: " + str(round(avg, 1)) + "\n")
        elif total_weight > 100:
            out_file.write(parts[0] + "'s " + "average: Error: The weights are more than 100." + "\n")
        else:
            out_file.write(parts[0] + "'s " + "average: Error: The weights are less than 100." + "\n")
    class_avg = round(class_grades / students, 1)
    out_file.write("Class average: " + str(class_avg))


def main():
    weighted_average("grades.txt", "avg.txt")


main()




