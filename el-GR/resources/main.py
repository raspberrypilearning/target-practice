#!/bin/python3

# Εισαγωγή του κώδικα της βιβλιοθήκης
from p5 import *
from math import *
from random import randint

# Η συνάρτηση mouse_pressed πηγαίνει εδώ
def mouse_pressed():
  if hit_color == outer:  
    print('Έχεις πετύχει τον εξωτερικό κύκλο, 50 πόντοι!') #Όπως οι συναρτήσεις, οι δηλώσεις 'if' έχουν εσοχή
  elif hit_color == inner:    
    print ('Έχεις πετύχει τον εσωτερικό κύκλο, 200 βαθμοί!')   
  elif hit_color == bullseye:    
    print ('Έχεις πετύχει το κέντρο του στόχου, 500 πόντοι!')   
  else:   
    print('Έχασες! Δεν παίρνεις πόντους!')    
    
# Η συνάρτηση shoot_arrow πηγαίνει εδώ
def shoot_arrow():
  global hit_color 
  arrow_x = randint(100, 300)
  arrow_y = randint(100, 300)
  hit_color = get(arrow_x, arrow_y)
  ellipse(arrow_x, arrow_y, 15, 15)

def setup():
# Όρισε τις παραμέτρους του παιχνιδιού σου εδώ
  size(400, 400) # πλάτος και ύψος
  frame_rate(2)


def draw():
# Ενέργειες που πρέπει να γίνονται σε κάθε καρέ
  global outer, inner, bullseye
  sky = color(92, 204, 206) # Κόκκινο = 92, Πράσινο = 204, Μπλε = 206
  grass = color(149, 212, 122)
  wood = color(145, 96, 51)
  outer = color(0, 120, 180) 
  inner = color(210, 60, 60)
  bullseye = color(220, 200, 0)

  no_stroke()
  fill(sky)
  rect(0, 0, 400, 250)
  fill(grass)
  rect(0, 250, 400, 150)
  
  fill(wood)
  triangle(150, 350, 200, 150, 250, 350)
  fill(outer)
  ellipse(200, 200, 170, 170)
  fill(inner)   
  ellipse(200, 200, 110, 110) #Εσωτερικός κύκλος   
  fill(bullseye)   
  ellipse(200, 200, 30, 30) #Κέντρο στόχου 
  
  fill(wood)
  shoot_arrow()
# Από εδώ εκτελείς τον κώδικά σου
run()
