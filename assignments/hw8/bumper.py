"""
Name: Walker Harris
bumper.py

Problem: Write a program that simulates two bumper cars.

Certification of Authenticity:
I hereby certify that all work on this assignment is entirely my own.

"""
from random import randint
import math
import graphics


def get_random(move_amount):
    rand_num = randint(-move_amount, move_amount)
    return rand_num


def get_random_color():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    return graphics.color_rgb(red, green, blue)


def did_collide(ball, ball2):
    dist = math.sqrt((ball.getCenter().getX() - ball2.getCenter().getX())
                     ** 2 + (ball.getCenter().getY() - ball2.getCenter().getY()) ** 2)
    ball_dist = abs(ball.getRadius() + ball2.getRadius())
    if dist <= ball_dist:
        return True
    return False


def hit_horizontal(ball, win):
    bottom = win.height - ball.getRadius()
    top = ball.getRadius()
    center = ball.getCenter().getY()
    if center <= top or center >= bottom:
        return True
    return False


def hit_vertical(ball, win):
    right = win.width - ball.getRadius()
    left = ball.getRadius()
    center = ball.getCenter().getX()
    if center <= left or center >= right:
        return True
    return False


def main():
    win = graphics.GraphWin("Bumper", 600, 400)
    radius = get_random(15)
    ball_a = graphics.Circle(graphics.Point(150, 100), radius).draw(win)
    ball_b = graphics.Circle(graphics.Point(150, 150), radius).draw(win)
    ball_a.setFill(get_random_color())
    ball_b.setFill(get_random_color())
    dx_1 = get_random(3)
    dy_1 = get_random(3)
    dx_2 = get_random(3)
    dy_2 = get_random(3)

    for _ in range(500):
        graphics.time.sleep(0.01)
        ball_a.move(dx_1, dy_1)
        ball_b.move(dx_2, dy_2)
        if did_collide(ball_a, ball_b):
            dy_1 *= -1
            dy_2 *= -1
            dx_1 *= -1
            dx_2 *= -1
        elif hit_vertical(ball_a, win):
            dx_1 *= -1
        elif hit_vertical(ball_b, win):
            dx_2 *= -1
        elif hit_horizontal(ball_a, win):
            dy_1 *= -1
        elif hit_horizontal(ball_b, win):
            dy_2 *= -1


main()
