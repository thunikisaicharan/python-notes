import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Pink Heart")
screen.bgcolor("white")

# Create a turtle
pen = turtle.Turtle()
pen.fillcolor("pink")
pen.pensize(3)
pen.speed(3)

# Draw a heart shape
pen.begin_fill()
pen.left(140)
pen.forward(180)
pen.circle(-90, 200)
pen.left(120)
pen.circle(-90, 200)
pen.forward(180)
pen.end_fill()

# Hide the turtle and display the window
pen.hideturtle()
turtle.done()
