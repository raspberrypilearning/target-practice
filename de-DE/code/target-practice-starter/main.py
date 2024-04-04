# Bibliothekscode importieren
from p5 import *
from random import randint

# Die Funktion „mouse_pressed“ kommt hierher

# Die Funktion „schiess_pfeil“ kommt hierher

def setup():
    # Set up your game here
    size(400, 400) # Breite und Höhe

def draw():
    # Dinge die in jedem Frame passieren
    fill('cyan')  # Set the fill colour for the sky to cyan
    rect(0, 0, 400, 250) # Zeichnet ein Rechteck für den Himmel mit diesen Werten für x, y, Breite, Höhe

# Lass dies so stehen, um Deinen Code auszuführen
run(frame_rate=2)
