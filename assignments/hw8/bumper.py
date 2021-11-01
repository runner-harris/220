from graphics import *
from random import randint


def get_random(move_amount):
    rand_num = randint(-move_amount, move_amount)
    return rand_num


def main():
    win = GraphWin("Bumper", 400, 400)

    radius = 10
    ball_a = Circle(Point(100, 200), radius).draw(win)
    ball_b = Circle(Point(100, 250), radius).draw(win)
    ball_a.setFill('red')
    ball_b.setFill('yellow')
    dx = get_random(10)
    dy = get_random(10)
    dx_2 = get_random(10)
    dy_2 = get_random(10)
    left_side = radius
    right_side = win.getWidth() - radius
    bottom = win.getHeight() - radius
    top = radius

    while True:
        time.sleep(0.01)
        ball_a.move(dx, dy)
        ball_b.move(dx_2, dy_2)
        if ball_a.getCenter().getY() <= top or ball_a.getCenter().getY() >= bottom:
            dy = -dy
        elif ball_a.getCenter().getX() <= left_side or ball_a.getCenter().getX() >= right_side:
            dx = -dx
        if ball_b.getCenter().getY() <= top or ball_b.getCenter().getY() >= bottom:
            dy_2 = -dy_2
        elif ball_b.getCenter().getX() <= left_side or ball_b.getCenter().getX() >= right_side:
            dx_2 = -dx_2




    win.getMouse()
    win.close()


main()