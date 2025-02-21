# importation des librairies de code !
from p5 import *
from random import randint


# La fonction mouse_pressed vient ici
def mouse_pressed():
    # print('🎯')
    if hit_colour == Color("blue").hex:
        print('Tu as touché le cercle extérieur, 50 points !')
    elif touche_couleur == Color('red').hex:
        print('Tu as touché le cercle intérieur, 200 points !')
    elif touche_couleur == Color('yellow').hex:
        print('Tu as touché le centre, 500 points !')
    else:
        print('Tu as loupé la cible ! Aucun point !')


# La fonction tire_fleche vient ici
def tire_fleche():
    global hit_colour
    arrow_x = randint(100, 300)
    arrow_y = randint(100, 300)
    hit_colour = get(arrow_x, arrow_y).hex
    # print(hit_colour)
    fill("brown")
    circle(arrow_x, arrow_y, 15)


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
    circle(200, 200, 110)  # Draw the inner circle
    fill("yellow")
    circle(200, 200, 30)  # Draw the middle circle
    tire_fleche()


# Garde ceci pour exécuter ton code
run(frame_rate=2)
