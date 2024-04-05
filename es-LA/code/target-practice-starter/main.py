# Import library code
from p5 import *
from random import randint

# The mouse_pressed function goes here

# The shoot_arrow function goes here

def setup():
    # Configura tu juego aquí
    size(400, 400)  # width and height of screen

def draw():
    # Things to do in every frame
    fill('cyan') # Establece el color de relleno del cielo en cian
    rect(0, 0, 400, 250)  # Draw a rectangle for the sky with these values for x, y, width, height

# Keep this to run your code
run(frame_rate=2)
