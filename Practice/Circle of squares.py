import turtle

my_turtle = turtle.Turtle()

my_turtle.color("Blue")

def square(length):
    for i in range(4):
        my_turtle.forward(length)
        my_turtle.right(90)

for i in range(100):
    square(75)
    my_turtle.right(10)