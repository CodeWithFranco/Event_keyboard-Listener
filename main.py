import turtle

screen = turtle.Screen()
player = turtle.Turtle()

player.shape('turtle')
player.color('turquoise')
player.penup()


def turn_left():
    player.left(10)

def turn_right():
    player.right(10)


def move_forward():
    player.pendown()
    player.forward(20)


def move_backward():
    player.pendown()
    player.back(20)


screen.onkeypress(turn_left, "a")
screen.onkeypress(turn_right, "d")
screen.onkeypress(move_forward, "w")
screen.onkeypress(move_backward, "s")
screen.listen()

turtle.done()
