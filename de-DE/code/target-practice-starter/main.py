# Bibliothekscode importieren
from p5 import *
from random import randint

# Die Funktion „mouse_pressed“ kommt hierher

# Die Funktion „schiess_pfeil“ kommt hierher

def setup():
    # Richte hier Dein Spiel ein
    size(400, 400) # Breite und Höhe

def draw():
    # Dinge die in jedem Frame passieren
    fill('cyan') # Setzt die Füllfarbe für den Himmel auf Cyan
    rect(0, 0, 400, 250) # Zeichnet ein Rechteck für den Himmel mit diesen Werten für x, y, Breite, Höhe

# Lass dies so stehen, um Deinen Code auszuführen
run(frame_rate=2)
