import turtle

#  screen set up
screen = turtle.Screen()
screen.title("Key Bindings")

# Creating a turtle named key
key = turtle.Turtle()
key.shape("turtle")
key.color("black")
key.pensize(1)

# Function to change key's color
def change_color(color):
    key.color(color)

# Function to increase pen width
def increase_pen_width():
    width = key.pensize()
    if width < 20:
        key.pensize(width + 1)

# Function to decrease pen width
def decrease_pen_width():
    width = key.pensize()
    if width > 1:
        key.pensize(width - 1)

# Function to move key forward
def move_forward():
    key.forward(10)

# Function to move key backward
def move_backward():
    key.backward(10)

# Function to turn key left
def turn_left():
    key.left(45)

# Function to turn key right
def turn_right():
    key.right(45)

# key bindings
screen.onkey(lambda: change_color("red"), "r")
screen.onkey(lambda: change_color("green"), "g")
screen.onkey(lambda: change_color("blue"), "b")
screen.onkey(increase_pen_width, "+")
screen.onkey(decrease_pen_width, "-")
screen.onkey(move_forward, "Up")
screen.onkey(move_backward, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")

screen.listen()

turtle.done()