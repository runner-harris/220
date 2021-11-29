"""
Name: Walker Harris
lab13.py
"""


def binary(value, nums):
    left = 0
    right = len(nums) - 1
    while left <= right:
        middle = (left + right) //2
        middle_value = nums[middle]
        if value == middle_value:
            return middle
        if value < middle_value:
            right = middle - 1
        if value > middle_value:
            left = middle + 1
    return -1


def selection_sort(values):
    for i in range(len(values)):
        lowest = values[i]
        pos = i
        for j in range(i + 1, len(values)):
            if i < j:
                lowest = values[j]
                pos = j
        values[i], values[pos] = values[pos], values[i]
        return lowest

def calc_area(rectangle):
    p1 = rectangle.getP1()
    p2 = rectangle.getP2()
    dx = abs(p1.getX() - p2.getx())
    dy = abs(p1.gety() - p2.getY())
    return dx * dy


def rect_sort(rectangles):
    dict = {}
    areas = []
    for rect in rectangles:
        dict[calc_area(rect)] = rect
        areas.append(calc_area(rect))
    selection_sort(areas)
    for i in range(len(areas)):
        rectangles[i] = dict[areas[i]]


def star_find(filename):
    in_file = open(filename, 'r')
    signals = in_file.read().split()
    found = []
    for i in range(len(signals)):
        current = int(signals[i])
        if current >= 4000 and current <= 5000:
            found.append(current)
        if len(found) == 5:
            break
    print(len(found))
    print(found)
    if len(found) != 5:
        print("we didnt find 5")
        print("we found: ", len(found))



def main():
    # add other function calls here
    star_find("signals.txt")
    pass


main()
