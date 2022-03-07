#!/bin/python3

# Bibliotheekcode importeren
from p5 import *
from math import *
from random import randint

# De muis_ingedrukt functie komt hier
def muis_ingedrukt():
  if raak_kleur == buitenste:  
    print('Je raakt de buitenste cirkel, 50 punten!') #Net als functies, zijn 'if'-instructies ingesprongen
  elif raak_kleur == binnenste:    
    print('Je hebt de binnenste cirkel geraakt, 200 punten!')   
  elif raak_kleur == roos:    
    print('In de roos, 500 punten!')   
  else:   
    print('Je hebt gemist! Geen punten!')    
    
# De schiet_pijl functie komt hier
def schiet_pijl():
  global raak_kleur 
  pijl_x = randint(100, 300)
  pijl_y = randint(100, 300)
  raak_kleur = get(pijl_x, pijl_y)
  ellipse(pijl_x, pijl_y, 15, 15)

def setup():
# Stel je spel hier in
  size(400, 400) # breedte en hoogte
  frame_rate(2)


def draw():
# Te regelen in ieder frame
  global buitenste, binnenste, roos
  lucht = color(92, 204, 206) # Rood = 92, Groen = 204, Blauw = 206
  gras = color(149, 212, 122)
  hout = color(145, 96, 51)
  buitenste = color(0, 120, 180) 
  binnenste = color(210, 60, 60)
  roos = color(220, 200, 0)

  no_stroke()
  fill(lucht)
  rect(0, 0, 400, 250)
  fill(gras)
  rect(0, 250, 400, 250)
  
  fill(hout)
  triangle(150, 350, 200, 150, 250, 350)
  fill(buitenste)
  ellipse(200, 200, 170, 170)
  fill(binnenste)   
  ellipse(200, 200, 110, 110) #Binnenste cirkel   
  fill(roos)   
  ellipse(200, 200, 30, 30) #Roos 
  
  fill(hout)
  schiet_pijl()
# Bewaar dit om je code uit te voeren
run()
