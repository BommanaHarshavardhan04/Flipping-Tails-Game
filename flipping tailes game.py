import random
import turtle

screen = turtle.Screen()
screen.bgcolor("yellow")

def Square(x, y):
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.color('white', 'green')
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(50)
        turtle.left(90)
    turtle.end_fill()


def Numbering(x, y):
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def Coordinates(count):
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def click(x, y):
    spot = Numbering(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

def draw():
    turtle.clear()
    turtle.goto(0, 0)
    turtle.stamp()

    for count in range(64):
        if hide[count]:
            x, y = Coordinates(count)
            Square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = Coordinates(mark)
        turtle.up()
        turtle.goto(x + 2, y)
        turtle.color('black')
        turtle.write(tiles[mark], font=('Arial', 30, 'normal'))

    turtle.update()
    turtle.ontimer(draw, 10)

tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64


random.shuffle(tiles)
turtle.tracer(False)
turtle.onscreenclick(click)
draw()
turtle.done()
