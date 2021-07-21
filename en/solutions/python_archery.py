#!/bin/python3

from p5 import *
from math import *
from random import randint

def setup():
  frame_rate(5)
  size(400, 400)
  global shoot
  shoot = False

def mouse_pressed():
  if pixel_colour == YELLOW:
    print('You hit yellow, 500 points!')
  elif pixel_colour == RED:
    print('You hit red, 300 points!')
  elif pixel_colour == BLUE:
    print('You hit blue, 200 points!')
  elif pixel_colour == BLACK:
    print('You hit black, 100 points!')
  elif pixel_colour == GREY:
    print('You hit white, 50 points!')
  else:    
    print('You missed, No points !')
    
    
def target():
  global pixel_colour
  if frame_count%40 == 0:
    target_x = randint(100, 300)
    target_y = randint(100, 300)
    pixel_colour = color(get(target_x, target_y))
    
  point(target_x, target_y)
  
def draw():
  
  global YELLOW, RED, BLUE, BLACK, GREY, WHITE, SKY_BLUE, GRASS_GREE, WOOD_BROWN
  
  YELLOW = color (252, 249, 0)
  RED = color(255, 0, 0)
  BLUE = color(0, 110, 191)
  BLACK = color(0, 0, 0)
  GREY = color(236, 236, 236)
  WHITE = color(255, 255, 255)
  SKY_BLUE = color(92, 204, 206)
  GRASS_GREEN = color(149, 212, 122)
  WOOD_BROWN = color(145, 96, 51)
  
  # Backdrop
  noStroke()
  fill(SKY_BLUE)
  rect(0, 0, 400, 250)
  fill(GRASS_GREEN)
  rect(0, 250, 400, 400)
  
  # Target
  fill(WOOD_BROWN)
  triangle(150, 350, 200, 150, 250, 350)
  strokeWeight(1)
  stroke(WHITE)
  fill(GREY)
  ellipse(200, 200, 170, 170)
  fill(BLACK)
  ellipse(200, 200, 140, 140)
  fill(BLUE)
  ellipse(200, 200, 110, 110)
  fill(RED)
  ellipse(200, 200, 70, 70)
  fill(YELLOW)
  ellipse(200, 200, 30, 30)
  
  # Arrow
  stroke(WOOD_BROWN)
  strokeWeight(10)
  
  target()
  
run()
