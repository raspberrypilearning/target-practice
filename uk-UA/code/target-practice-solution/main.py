## Імпортуй код бібліотеки

from p5 import *
from random import randint


# Тут буде функція mouse_pressed
def mouse_pressed():
    # print('🎯')
    if hit_colour == Color("blue").hex:
        print("Стріла в зовнішньому колі — 50 балів!")
    elif hit_colour == Color("red").hex:
        print("Стріла у внутрішньому колі — 200 балів!")
    elif hit_colour == Color("yellow").hex:
        print("Стріла у центрі — 500 балів!")
    else:
        print("Стріла не влучила! Нуль балів!")


# Тут буде функція shoot_arrow
def shoot_arrow():
    global hit_colour
    arrow_x = randint(100, 300)
    arrow_y = randint(100, 300)
    hit_colour = get(arrow_x, arrow_y).hex
    # print(hit_colour)
    fill("brown")
    circle(arrow_x, arrow_y, 15)


def setup():
    # Налаштуй свою гру тут
    size(400, 400)
    no_stroke()


def draw():
    # Що відбувається на кожному кадрі
    fill("cyan")
    rect(0, 0, 400, 250)
    fill("lightgreen")
    rect(0, 250, 400, 150)
    fill("brown")
    triangle(150, 350, 200, 150, 250, 350)
    fill("blue")
    circle(200, 200, 170)
    fill("red")
    circle(200, 200, 110)  # Намалюй внутрішнє коло
    fill("yellow")
    circle(200, 200, 30)  # Намалюй середнє коло
    shoot_arrow()


# Цей рядок запускає код
run(frame_rate=2)
