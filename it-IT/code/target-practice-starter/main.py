# Importa la libreria di codice
from p5 import *
from random import randint

# La funzione mouse_pressed va qui


# La funzione shoot_arrow va qui


def setup():
    # Imposta il tuo gioco qui
    size(400, 400)  # larghezza e altezza dello schermo
    no_stroke()


def draw():
    # Cose da fare in ogni fotogramma
    fill("cyan")
    rect(0, 0, 400, 250)


# Conserva questa parte per eseguire il codice
run(frame_rate=2)
