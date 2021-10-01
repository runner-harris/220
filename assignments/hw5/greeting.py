"""
Name: Walker Harris
greeting.py

Problem: Write a program that creates a valentines day card.

Certification of Authenticity:
I hereby certify that all work on this assignment is entirely my own.

"""
import time
import graphics

def main():
    win = graphics.GraphWin("Greeting Card", 400, 400)

    pointa = graphics.Point(170, 150)
    circa = graphics.Circle(pointa, 40)
    circb = circa.clone()
    circb.move(60, 0)
    circa.setOutline("pink")
    circb.setOutline("pink")
    circa.setFill("pink")
    circb.setFill("pink")
    circa.draw(win)
    circb.draw(win)

    triangle = graphics.Polygon(graphics.Point(130, 155),
                                graphics.Point(270, 155), graphics.Point(200, 290))
    triangle.setOutline("pink")
    triangle.setFill("pink")
    triangle.draw(win)

    arrow = graphics.Line(graphics.Point(0, 400), graphics.Point(50, 350))
    arrow.setOutline("black")
    arrow.draw(win)

    feather1 = graphics.Line(graphics.Point(0, 390), graphics.Point(10, 390))
    feather2 = graphics.Line(graphics.Point(10, 390), graphics.Point(10, 400))
    feather3 = graphics.Line(graphics.Point(-10, 400), graphics.Point(0, 400))
    feather4 = graphics.Line(graphics.Point(0, 400), graphics.Point(0, 410))
    tip1 = graphics.Line(graphics.Point(40, 350), graphics.Point(50, 350))
    tip2 = graphics.Line(graphics.Point(50, 350), graphics.Point(50, 360))
    tip1.draw(win)
    tip2.draw(win)
    feather1.draw(win)
    feather2.draw(win)
    feather3.draw(win)
    feather4.draw(win)

    greeting = graphics.Text(graphics.Point(200, 100), "Happy Valentines Day!")
    greeting.draw(win)

    for _ in range(15):
        arrow.move(10, -10)
        feather1.move(10, -10)
        feather2.move(10, -10)
        feather3.move(10, -10)
        feather4.move(10, -10)
        tip1.move(10, -10)
        tip2.move(10, -10)
        time.sleep(0.1)

    instruction = graphics.Text(graphics.Point(200, 300), "Click anywhere to close")
    instruction.draw(win)
    win.getMouse()
    win.close()


if __name__ == "__main__":
    main()
