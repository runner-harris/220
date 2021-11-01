

def weighted_average(in_file_name, out_file_name):
    in_file = open(in_file_name, 'r')
    out_file = open(out_file_name, 'w')

    num_list = []
    for line in in_file:
        grades = line.split()
        for grade in grades:
            try:
                num_list.append(int(grade))
            except ValueError:
                pass
    print(num_list)




def main():
    weighted_average("grades.txt", "avg.txt")


main()