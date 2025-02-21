# importation des librairies de code !
from p5 import *
from random import randint


# La fonction souris_pressee vient ici
def souris_pressee():
    # print('🎯')
    if touche_couleur == Color('blue').hex: # Comme les fonctions, les instructions 'if' sont indentées
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
    fleche_x = randint(100, 300) # Stocke un nombre aléatoire entre 100 et 300
    fleche_y = randint(100, 300) # Stocke un nombre aléatoire entre 100 et 300
    touche_couleur = get(fleche_x, fleche_y).hex # Récupère la couleur de l'endroit touché
    # print(hit_colour)
    fill('sienna')
    circle(fleche_x, fleche_y, 15) # Dessine un petit cercle à des coordonnées aléatoires


def setup():
    # Configure ton jeu ici
    size(400, 400) # largeur et hauteur
    no_stroke()


def draw():
    # Choses à faire dans chaque image
    fill('cyan')
    rect(0, 0, 400, 250) # Ciel
    fill('lightgreen')
    rect(0, 250, 400, 150) # Herbe
    fill('sienna') # Définit la flèche pour remplir la couleur sur marron
    triangle(150, 350, 200, 150, 250, 350) # Support
    fill('blue')
    circle(200, 200, 170)  # Cercle extérieur
    fill('red')
    circle(200, 200, 110)  # Cercle intérieur
    fill('yellow')
    circle(200, 200, 30)  # Cercle du milieu
    tire_fleche()


# Garde ceci pour exécuter ton code
run(frame_rate=2)
