## Import kódu knihovny
from p5 import *
from random import randint

# Zde je funkce mouse_pressed


# Zde je funkce shoot_arrow


def setup():
    # Zde si nastav svou hru
    size(400, 400)
    no_stroke()


def draw():
    # Co dělat v každém snímku
    fill("cyan")
    rect(0, 0, 400, 250)


# Toto si ponech pro spuštění kódu
run(frame_rate=2)
