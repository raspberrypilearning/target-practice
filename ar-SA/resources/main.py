#!/bin/python3

# استيراد مكتبة التعليمات البرمجية
from p5 import *
from math import *
from random import randint

# نضع دالة mouse_pressed هنا
def mouse_pressed():
  if hit_color == outer:  
    print('You hit the outer circle, 50 points!') #Like دالة ، يتم وضع مسافة بادئة لعبارات 'if'
  elif hit_color == inner:    
    print('You hit the inner circle, 200 points!')   
  elif hit_color == bullseye:    
    print('You hit the bullseye, 500 points!')   
  else:   
    print('You missed! No points!')    
    
# نضع دالة shoot_arrow هنا
def shoot_arrow():
  global hit_color 
  arrow_x = randint(100, 300)
  arrow_y = randint(100, 300)
  hit_color = get(arrow_x, arrow_y)
  ellipse(arrow_x, arrow_y, 15, 15)

def setup():
# قم بإعداد لعبتك هنا
  size(400, 400) # العرض والارتفاع
  frame_rate(2)


def draw():
# أشياء للقيام بها في كل إطار
  global outer, inner, bullseye
  sky = color(92, 204, 206) # احمر = 92, اخضر = 204, ازرق = 206
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
  ellipse(200, 200, 110, 110) #الدائرة الداخلية   
  fill(bullseye)   
  ellipse(200, 200, 30, 30) #مركز الهدف 
  
  fill(wood)
  shoot_arrow()
# احتفظ بهذا لتشغيل التعليمات البرمجية الخاصة بك
run()
