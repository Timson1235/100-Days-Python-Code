import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.title("Turtle Race")
screen.setup(width=800, height=600)

# Ask the user to predict the winner
colors = ["red", "blue", "green", "yellow", "orange", "purple"]
user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color: red, blue, green, yellow, orange, purple")

# Create the finish line
finish_line = 350

# Function to create a turtle
def create_turtle(color, y_position):
    new_turtle = turtle.Turtle()
    new_turtle.shape("turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(-350, y_position)
    return new_turtle

# Create turtles
y_positions = [-100, -60, -20, 20, 60, 100]
turtles = []

for i in range(len(colors)):
    turtles.append(create_turtle(colors[i], y_positions[i]))

# Function to start the race
def start_race():
    winner = None
    while not winner:
        for racer in turtles:
            racer.forward(random.randint(1, 10))
            if racer.xcor() >= finish_line:
                winner = racer
                break
    return winner

# Draw the finish line
finish_line_turtle = turtle.Turtle()
finish_line_turtle.penup()
finish_line_turtle.goto(finish_line, -150)
finish_line_turtle.pendown()
finish_line_turtle.left(90)
finish_line_turtle.forward(300)
finish_line_turtle.hideturtle()

# Start the race
winner = start_race()

# Announce the winner
winner_color = winner.pencolor()
winner.goto(0, 0)
winner.color("gold")
winner.write("Winner!", align="center", font=("Arial", 24, "bold"))

# Print if the user's prediction was correct
if user_bet.lower() == winner_color:
    print(f"Congratulations! Your bet was correct! The {winner_color} turtle won!")
else:
    print(f"Sorry, your bet was incorrect. The {winner_color} turtle won.")

# Keep the window open
screen.mainloop()
