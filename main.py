import colorgram
import turtle
import random


def set_initial_position(screen_height, screen_width, num_spots_x, num_spots_y):
    turtle.screensize(screen_height, screen_width)
    turtle.setworldcoordinates(0, 0, screen_width, screen_height)

    x_0 = - screen_width / num_spots_x / 2
    y_0 = - screen_height / num_spots_y / 2

    return [x_0, y_0]


def next_row(x_0, delta_y):
    y = tim.ycor()
    tim.sety(y + delta_y)
    tim.setx(x_0)


def paint(screen_height, screen_width, num_spots_x, num_spots_y):
    initial_position = set_initial_position(screen_height, screen_width, num_spots_x, num_spots_y)
    x_0 = initial_position[0]
    y_0 = initial_position[1]
    delta_x = -2 * x_0
    delta_y = -2 * y_0

    tim.penup()
    tim.goto(x_0, y_0)
    dot_size = - (x_0 + y_0)

    for _ in range(num_spots_y):
        next_row(x_0, delta_y)
        for _ in range(num_spots_x):
            tim.forward(delta_x)
            tim.dot(dot_size, random.choice(color_list))


turtle.colormode(255)
colors = colorgram.extract("image.jpg", 35)
color_list = []
for color in colors:
    color_list.append(color.rgb)

tim = turtle.Turtle()
tim.speed(0)
tim.shape("turtle")

paint(209, 241, 13, 11)

screen = turtle.Screen()
screen.exitonclick()
