## Importer le code de la bibliothèque
from p5 import *
from random import randint


# La fonction souris_pressee vient ici
def mouse_pressed():
    # print('🎯')
    if couleur_touchee == Color("blue").hex:
        print('Tu as touché le cercle extérieur, 50 points !')
    elif couleur_touchee == Color('red').hex:
        print('Tu as touché le cercle intérieur, 200 points !')
    elif couleur_touchee == Color('yellow').hex:
        print('Tu as touché le centre, 500 points !')
    else:
        print('Tu as loupé la cible ! Aucun point !')


# La fonction tire_fleche vient ici
def tire_fleche():
    global couleur_touchee
    fleche_x = randint(100, 300)
    fleche_y = randint(100, 300)
    couleur_touchee = get(fleche_x, fleche_y).hex
    # print(couleur_touchee)
    fill("brown")
    circle(fleche_x, fleche_y, 15)


def setup():
    # Configure ton jeu ici
    size(400, 400)
    no_stroke()


def draw():
    # Choses à faire dans chaque image
    fill("cyan")
    rect(0, 0, 400, 250)
    fill("lightgreen")
    rect(0, 250, 400, 150)
    fill("brown")
    triangle(150, 350, 200, 150, 250, 350)
    fill("blue")
    circle(200, 200, 170)
    fill("red")
    circle(200, 200, 110)  # Dessiner le cercle intérieur
    fill("yellow")
    circle(200, 200, 30)  # Dessiner le cercle du milieu
    tire_fleche()


# Garde ceci pour exécuter ton code
run(frame_rate=2)
