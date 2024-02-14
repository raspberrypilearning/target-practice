# importation des librairies de code
from p5 import *
from random import randint

# La fonction souris_pressee vient ici

# La fonction tire_fleche vient ici

def setup():
    # Configure ton jeu ici
    size(400, 400) # largeur et hauteur de l'écran

def draw():
    # Choses à faire dans chaque image
    fill('cyan') # Définit la couleur de remplissage du ciel sur cyan
    rect(0, 0, 400, 250) # Dessine un rectangle pour le ciel avec ces valeurs pour x, y, largeur, hauteur

# Garde ceci pour exécuter ton code
run(frame_rate=2)
