import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("white")
    brad.speed(5)

    brad.forward(100)
    brad.left(90)
    brad.forward(100)
    brad.left(90)
    brad.forward(100)
    brad.left(90)
    brad.forward(100)
    brad.left(90)

    window.exitonclick()

draw_square()
