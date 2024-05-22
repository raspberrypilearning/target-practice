# Bibliothekscode importieren!
from p5 import *
from random import randint

# Die Funktion „mouse_pressed“ kommt hierher
def mouse_pressed():
    if getroffene_farbe == Color('blue').hex: # Wie bei Funktionen sind auch 'if'-Anweisungen eingerückt
        print('Du hast den äußeren Kreis getroffen, 50 Punkte!')
    elif getroffene_farbe == Color('red').hex:
        print('Du hast den inneren Kreis erreicht, 200 Punkte!')
    elif getroffene_farbe == Color('yellow').hex:
        print('Du hast die Mitte getroffen, 500 Punkte!')
    else:
        print('Daneben! Keine Punkte!')

# Die Funktion „schiess_pfeil“ kommt hierher
def schiess_pfeil():
    global getroffene_farbe # Kann in anderen Funktionen verwendet werden
    pfeil_x = randint(100, 300) # Speichere eine Zufallszahl zwischen 100 und 300
    pfeil_y = randint(100, 300) # Speichere eine Zufallszahl zwischen 100 und 300
    getroffene_farbe = get(pfeil_x, pfeil_y).hex # Hole die Trefferfarbe
    fill('sienna') # Stelle die Füllfarbe des Pfeils auf Braun ein
    circle(pfeil_x, pfeil_y, 15) # Zeichne einen kleinen Kreis an zufälligen Koordinaten

def setup():
    # Richte hier Dein Spiel ein
    size(400, 400) # Breite und Höhe
    no_stroke()

def draw():
    # Dinge die in jedem Frame passieren
    fill('cyan')
    rect(0, 0, 400, 250) # Himmel
    fill('lightgreen')
    rect(0, 250, 400, 150) # Gras
    fill('sienna')
    triangle(150, 350, 200, 150, 250, 350) # Stand
    fill('blue')
    circle(200, 200, 170) # Äußerer Kreis
    fill('red')
    circle(200, 200, 110) # Innerer Kreis
    fill('yellow')
    circle(200, 200, 30) # Mitte
    schiess_pfeil()

# Lass dies so stehen, um Deinen Code auszuführen
run(frame_rate=2)
