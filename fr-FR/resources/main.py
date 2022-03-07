#!/bin/python3

# Importer le code de la bibliothèque
from p5 import *
from math import *
from random import randint

# La fonction souris_pressee vient ici
def souris_pressee():
  if couleur_touche == exterieur:  
    print('Tu as touché le cercle extérieur, 50 points !') #Comme les fonctions, les déclarations "if" sont indentés
  elif couleur_touche == interieur:    
    print('Tu as touché le cercle intérieur, 200 points !')   
  elif couleur_touche == centre:    
    print('Tu as touché le centre, 500 points !')   
  else:   
    print('Tu as loupé la cible ! Aucun point !')    
    
# La fonction tire_fleche vient ici
def tire_fleche():
  global couleur_touche 
  fleche_x = randint(100, 300)
  fleche_y = randint(100, 300)
  couleur_touche = get(fleche_x, fleche_y)
  ellipse(fleche_x, fleche_y, 15, 15)

def configuration():
# Configure ton jeu ici
  size(400, 400) # largeur et hauteur
  frame_rate(2)


def dessin():
# Choses à faire dans chaque image
  global exterieur, interieur, centre
  ciel = color(92, 204, 206) # Rouge = 92, Vert = 204, Bleu = 206
  herbe = color(149, 212, 122)
  bois = color(145, 96, 51)
  exterieur = color(0, 120, 180) 
  interieur = color(210, 60, 60)
  centre = color(220, 200, 0)

  no_stroke()
  fill(ciel)
  rect(0, 0, 400, 250)
  fill(herbe)
  rect(0, 250, 400, 150)
  
  fill(bois)
  triangle(150, 350, 200, 150, 250, 350)
  fill(exterieur)
  ellipse(200, 200, 170, 170)
  fill(interieur)   
  ellipse(200, 200, 110, 110) #Cercle intérieur   
  fill(centre)   
  ellipse(200, 200, 30, 30) #centre 
  
  fill(bois)
  tire_fleche() 
# Garde ceci pour exécuter ton code
run()
