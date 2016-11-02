import sys
# https://docs.python.org/2/library/turtle.html
import turtle
import random
import string

# IMPORT CUSTOM FILES

import site
def get_main_path():
    app_path = sys.path[0] # sys.path[0] is current path in subdirectory
    split_on_char = "/"
    return split_on_char.join(app_path.split(split_on_char)[:-1])
main_path = get_main_path()
print ("Importing subfolder: %s") % (main_path+'/helpers')
site.addsitedir(main_path+'/helpers')
from helpers import reusable # __init__.py required in the helpers subdirectory

# Settings
REPLAY_QTY = 100
SHAPE = reusable.shape["rectangle"]

def draw_boundary(boundary_drawer, distance_x, distance_y):
    distance = distance_x
    for i in range(0, SHAPE["sides"]):
        boundary_drawer.forward(distance)
        boundary_drawer.right(SHAPE["angle"])
        if (SHAPE == reusable.shape["rectangle"] and distance == distance_x):
            distance = distance_y
        else:
            distance = distance_x

def draw_square(some_player, distance):
    for i in range(1, 5):
        some_player.forward(distance)
        some_player.right(90)

def calculate_start_position_for_canvas(bounds_w, bounds_h):
    start_position_x = random.randint(0, bounds_w)/2
    start_position_y = random.randint(0, bounds_h)/2
    return start_position_x, start_position_y

def calculate_max_move_distance_for_position(bounds_w, bounds_h, start_position_x, start_position_y):
    return min(bounds_w - start_position_x, bounds_h - start_position_y)

def move_dist_random(bounds_w, bounds_h, start_position_x, start_position_y):
    return random.randint(0, calculate_max_move_distance_for_position(bounds_w, bounds_h, start_position_x, start_position_y)) # inclusive

def rand_dims():
    return random.randint(20, 400)

def generate_rand_boundary(current_bgcolor):
    bounds_w, bounds_h = rand_dims(), rand_dims()
    boundary = turtle.Turtle()
    boundary.color(current_bgcolor)
    boundary.goto(-bounds_w/2, bounds_h/2)
    boundary.shape("arrow")
    boundary.color("white")
    boundary.speed("0")
    draw_boundary(boundary, bounds_w, bounds_h)
    boundary.color(current_bgcolor)
    boundary.home()
    return bounds_w, bounds_h

# randomly generate an integer cast as string, or a letter in order to compose the hexadecimal colour
# TODO - Refactor into one line http://stackoverflow.com/questions/18414907/constraining-random-hex-colour-generator-to-a-certain-range-of-colours
def generate_rand_char_for_hex():
    rand_option = random.randint(0,1)
    if rand_option == 0:
        return str(random.randint(0,9))
    else:
        return random.choice(string.ascii_lowercase[0:6])

def generate_rand_color():
    hex_array = range(6) # initialize array with 6 elements
    for i in hex_array:
        hex_array[i] = generate_rand_char_for_hex()
    return str("#" + "".join(hex_array))

def draw_art():
    canvas = turtle.Screen() # TurtleScreen object

    for i in range(REPLAY_QTY):
        current_bgcolor = generate_rand_color()
        canvas.bgcolor(current_bgcolor)
        bounds_w, bounds_h = generate_rand_boundary(current_bgcolor)
        start_position_x, start_position_y = calculate_start_position_for_canvas(bounds_w, bounds_h)
        player1 = turtle.Turtle()
        player1.shape("turtle")
        player1.color(generate_rand_color())
        player1.speed("0") # very fast
        player1.setposition(start_position_x, start_position_y)
        for i in range (0, 36):
            move_dist = move_dist_random(bounds_w, bounds_h, start_position_x, start_position_y)
            draw_square(player1, move_dist)
            player1.right(10)

    canvas.exitonclick()

draw_art()