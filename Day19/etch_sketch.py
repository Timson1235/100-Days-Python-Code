import turtle as t

# Initialize the screen
screen = t.Screen()
screen.title("Etch A Sketch")
screen.setup(width=800, height=600)

# Initialize the turtle
etch_turtle = t.Turtle()
etch_turtle.shape("turtle")
etch_turtle.speed("fastest")

# Functions to control the turtle
def move_forward():
    etch_turtle.forward(20)

def move_backward():
    etch_turtle.backward(20)

def turn_left():
    new_heading = etch_turtle.heading() + 10
    etch_turtle.setheading(new_heading)

def turn_right():
    new_heading = etch_turtle.heading() - 10
    etch_turtle.setheading(new_heading)

def clear_screen():
    etch_turtle.clear()
    etch_turtle.penup()
    etch_turtle.home()
    etch_turtle.pendown()

# Key bindings
screen.listen()
screen.onkey(move_forward, "Up")
screen.onkey(move_backward, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(clear_screen, "c")

# Keep the window open
screen.mainloop()
