## Importar código de biblioteca

from p5 import *
from random import randint


# The mouse_pressed function goes here
def mouse_pressed():
    # imprimir('🎯')
    if hit_colour == Color("blue").hex:
        print("Le diste al círculo externo, ¡50 puntos!")
    elif hit_colour == Color("red").hex:
        print("Le diste al círculo interno, ¡200 puntos!")
    elif hit_colour == Color("yellow").hex:
        print("¡Le diste al centro, 500 puntos!")
    else:
        print("¡Fallaste! ¡Sin puntos!')


# The shoot_arrow function goes here
def shoot_arrow():
    global hit_colour
    arrow_x = randint(100, 300)
    arrow_y = randint(100, 300)
    hit_colour = get(arrow_x, arrow_y).hex
    # print(hit_colour)
    fill("brown")
    circle(arrow_x, arrow_y, 15)


def setup():
    # Configura tu juego aquí
    size(400, 400)
    no_stroke()


def draw():
    # Things to do in every frame
    fill("cyan")
    rect(0, 0, 400, 250)
    fill("lightgreen")
    rect(0, 250, 400, 150)
    fill("brown")
    triangle(150, 350, 200, 150, 250, 350)
    fill("blue")
    circle(200, 200, 170)
    fill("red")
    circle(200, 200, 110) # Dibuja el círculo interior
    fill("yellow")
    circle(200, 200, 30) # Dibuja el círculo del medio
    shoot_arrow()


# Keep this to run your code
run(frame_rate=2)
