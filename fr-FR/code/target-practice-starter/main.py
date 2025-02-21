# importation des librairies de code
from p5 import *
from random import randint

# La fonction souris_pressee vient ici


# La fonction tire_fleche vient ici


def setup():
    # Configure ton jeu ici
    size(400, 400)
    no_stroke()


def draw():
    # Choses à faire dans chaque image
    fill("cyan")
    rect(0, 0, 400, 250)


# Garde ceci pour exécuter ton code
run(frame_rate=2)
