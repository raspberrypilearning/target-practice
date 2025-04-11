## Import kódu knihovny

from p5 import *
from random import randint


# Zde je funkce mouse_pressed
def mouse_pressed():
    # print('🎯')
    if hit_colour == Color("modrá").hex:
        print("Trefil jsi vnější kruh, 50 bodů!")
    elif hit_colour == Color("červená").hex:
        print("Trefil jsi vnitřní kruh, 200 bodů!")
    elif hit_colour == Color("žlutá").hex:
        print("Trefil jsi střed, 500 bodů!")
    else:
        print("Vedle! Žádné body!")


# Zde je funkce shoot_arrow
def shoot_arrow():
    global hit_colour
    arrow_x = randint(100, 300)
    arrow_y = randint(100, 300)
    hit_colour = get(arrow_x, arrow_y).hex
    # print(hit_colour)
    fill("brown")
    circle(arrow_x, arrow_y, 15)


def setup():
    # Zde si nastav svou hru
    size(400, 400)
    no_stroke()


def draw():
    # Co dělat v každém snímku
    fill("cyan")
    rect(0, 0, 400, 250)
    fill("lightgreen")
    rect(0, 250, 400, 150)
    fill("brown")
    triangle(150, 350, 200, 150, 250, 350)
    fill("blue")
    circle(200, 200, 170)
    fill("red")
    circle(200, 200, 110)  # Nakresli vnitřní kruh
    fill("yellow")
    circle(200, 200, 30)  # Nakresli prostřední kruh
    shoot_arrow()


# Toto si ponech pro spuštění kódu
run(frame_rate=2)
