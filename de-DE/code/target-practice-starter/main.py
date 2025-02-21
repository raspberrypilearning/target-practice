# Bibliothekscode importieren
from p5 import *
from random import randint

# Die Funktion „mouse_pressed“ kommt hierher


# Die Funktion „schiess_pfeil“ kommt hierher


def setup():
    # Richte hier Dein Spiel ein
    size(400, 400) # Breite und Höhe
    no_stroke()


def draw():
    # Dinge die in jedem Frame passieren
    fill("cyan")
    rect(0, 0, 400, 250)


# Lass dies so stehen, um Deinen Code auszuführen
run(frame_rate=2)
