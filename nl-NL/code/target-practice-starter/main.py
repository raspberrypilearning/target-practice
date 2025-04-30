# Bibliotheekcode importeren
from p5 import *
from random import randint

# De mouse_pressed functie komt hier


# De schiet_pijl functie komt hier


def setup():
    # Stel je spel hier in
    size(400, 400)
    no_stroke()


def draw():
    # Dingen om te doen in elk frame
    fill("cyan")
    rect(0, 0, 400, 250)


# Bewaar dit om je code uit te voeren
run(frame_rate=2)
