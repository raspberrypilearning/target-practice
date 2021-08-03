#!/bin/python3

from p5 import *
from math import *
from random import randint

arrow_x = 400
arrow_y = 400


def setup():
  frame_rate(5)
  size(400, 400)


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
    
    
def shoot_arrow():
  global arrow_x, arrow_y
  global pixel_colour
  arrow_x = randint(100, 300)
  arrow_y = randint(100, 300)
  pixel_colour = color(get(arrow_x, arrow_y))
    
  point(arrow_x, arrow_y)
  
  
def draw():
  
  global YELLOW, RED, BLUE, BLACK, GREY, WHITE, SKY_BLUE, GRASS_GREEN, WOOD_BROWN
  
  BLACK = color(0, 0, 0)
  BLUE = color(0, 110, 191)
  GRASS_GREEN = color(149, 212, 122)
  GREY = color(236, 236, 236)
  RED = color(255, 0, 0)
  SKY_BLUE = color(92, 204, 206)
  WHITE = color(255, 255, 255)
  WOOD_BROWN = color(145, 96, 51)
  YELLOW = color(252, 249, 0)
  
  
  # Backdrop
  no_stroke()
  fill(SKY_BLUE)
  rect(0, 0, 400, 250)
  fill(GRASS_GREEN)
  rect(0, 250, 400, 400)
  
  # Draw a target
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
  
  shoot_arrow()
  
run()