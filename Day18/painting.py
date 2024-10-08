import random
from turtle import Turtle, Screen
from colors import color_rgbs


# Initialize the turtle
timmy_the_turtle = Turtle()
timmy_the_turtle.speed("fastest")
timmy_the_turtle.penup()
timmy_the_turtle.hideturtle()

# Set up the screen
screen = Screen()
screen.colormode(255)

# Function to draw dots with extracted colors
def draw_dots(turtle, colors, dot_size, spacing, rows, cols):
    for row in range(rows):
        for col in range(cols):
            turtle.dot(dot_size, random.choice(colors))
            turtle.forward(spacing)
        turtle.backward(spacing * cols)
        turtle.right(90)
        turtle.forward(spacing)
        turtle.left(90)

# Position the turtle to start drawing
timmy_the_turtle.setpos(-200, -200 + 50 * 10)

# Draw the dots
draw_dots(timmy_the_turtle, color_rgbs, 20, 50, 10, 10)

# Keep the window open
screen.exitonclick()