## Importa la biblioteca
from p5 import *
from random import randint

# The mouse_pressed function goes here


# The shoot_arrow function goes here


def setup():
    # Configura tu juego aquí
    size(400, 400)
    no_stroke()


def draw():
    # Things to do in every frame
    fill("cyan")
    rect(0, 0, 400, 250)


# Keep this to run your code
run(frame_rate=2)
