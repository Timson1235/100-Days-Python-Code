from turtle import Turtle, Screen
import turtle as t
import heroes
import random
t.colormode(255)

tim = Turtle()
tim.color("SkyBlue")
tim.penup()


#Draw a circle
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

#dashed Line
def dashed_line():
    for _ in range(15):
        tim.forward(10)
        tim.penup()
        tim.forward(10)
        tim.pendown()

#Turtle shapes
# times = 3
# for _ in range(8):
#     for _ in range(times):
#         tim.forward(100)
#         tim.right(360/times)
#     times += 1

#random color
# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     random_color = (r,g,b)
#     return random_color


# #random walk
# # List of angles
# angles = [45, 90, 135, 180, 225, 270,315, 360]
# colors = ["sky blue", "lawn green", "magenta", "moccasin", "firebrick", "sienna", "powder blue", "medium orchid"]
# tim.speed(10)
# tim.pensize(8)

# for _ in range(200):
#     random_angle = random.choice(angles)
#     tim.setheading(random_angle)
#     tim.forward(30)
#     tim.color(random_color())





screen = Screen()
screen.exitonclick()
