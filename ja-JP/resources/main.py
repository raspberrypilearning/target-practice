#!/bin/python3

# ライブラリコードをインポートする
from p5 import *
from math import *
from random import randint

#  mouse_pressed関数はここにあります
def mouse_pressed():
  if hit_color == outer:  
    print('外側の円に当たった、50点！') #関数と同様に'if'文はインデントが必要です
  elif hit_color == inner:    
    print('内側の円に当たった、 200点！')   
  elif hit_color == bullseye:    
    print( 'ブルズアイに当たった、500ポイント！')   
  else:   
    print('外した！ ポイントなし！')    
    
# shoot_arrow関数はここにあります
def shoot_arrow():
  global hit_color 
  arrow_x = randint(100, 300)
  arrow_y = randint(100, 300)
  hit_color = get(arrow_x, arrow_y)
  ellipse(arrow_x, arrow_y, 15, 15)

def setup():
# ここでゲームをセットアップします
  size(400, 400) # 幅と高さ
  frame_rate(2)


def draw():
# すべてのフレームで行うこと
  global outer, inner, bullseye
  sky = color(92, 204, 206) # 赤 = 92, 緑 = 204, 青 = 206
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
  ellipse(200, 200, 110, 110) #内側の円   
  fill(bullseye)   
  ellipse(200, 200, 30, 30) #ブルズアイ 
  
  fill(wood)
  shoot_arrow()
# コードを実行するためにこれを保持します
run()
