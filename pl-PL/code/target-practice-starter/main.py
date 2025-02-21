## Import library code
from p5 import *
from random import randint

# Funkcja mouse_pressed pojawi się tutaj


# Funkcja shoot_arrow pojawia się tutaj


def setup():
    # Set up your game here
    size(400, 400)
    no_stroke()


def draw():
    # Rzeczy do zrobienia w każdej klatce
    fill("cyan")
    rect(0, 0, 400, 250)


# Zatrzymaj to, aby uruchomić swój kod
run(frame_rate=2)
