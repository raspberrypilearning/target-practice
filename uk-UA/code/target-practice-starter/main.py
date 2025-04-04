## Імпортуй код бібліотеки
from p5 import *
from random import randint

# Тут буде функція mouse_pressed


# Тут буде функція shoot_arrow


def setup():
    # Налаштуй свою гру тут
    size(400, 400)
    no_stroke()


def draw():
    # Що відбувається на кожному кадрі
    fill("cyan")
    rect(0, 0, 400, 250)


# Цей рядок запускає код
run(frame_rate=2)
