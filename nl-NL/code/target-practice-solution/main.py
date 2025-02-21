# Bibliotheekcode importeren!
from p5 import *
from random import randint


# De mouse_pressed functie komt hier
def mouse_pressed():
    # print('🎯')
    if raak_kleur == Color('blue').hex: # Net als bij functies worden 'if'-instructies ingesprongen
        print('Je hebt de buitenste cirkel geraakt, 50 punten!')
    elif raak_kleur == Color('red').hex:
        print('Je hebt de binnenste cirkel geraakt, 200 punten!')
    elif raak_kleur == Color('yellow').hex:
        print('In de roos, 500 punten!')
    else:
        print('Je hebt gemist! Geen punten!')


# De schiet_pijl functie komt hier
def schiet_pijl():
    global hit_colour
    pijl_x = randint(100, 300) # Bewaar een willekeurig getal tussen 100 en 300
    pijl_y = randint(100, 300) # Bewaar een willekeurig getal tussen 100 en 300
    raak_kleur = get(pijl_x, pijl_y).hex # Haal de geraakte kleur op
    # print(hit_colour)
    fill('sienna')
    circle(pijl_x, pijl_y, 15) # Teken een kleine cirkel op willekeurige coördinaten


def setup():
    # Stel je spel hier in
    size(400, 400) # breedte en hoogte
    no_stroke()


def draw():
    # Dingen om te doen in elk frame
    fill('cyan')
    rect(0, 0, 400, 250) # Lucht
    fill('lightgreen')
    rect(0, 250, 400, 150) # Gras
    fill('sienna') # Stel vulkeur van de pijl in op bruin
    triangle(150, 350, 200, 150, 250, 350) # Standaard
    fill('blue')
    circle(200, 200, 170) # Buitenste cirkel
    fill('red')
    circle(200, 200, 110) # Binnenste cirkel
    fill('yellow')
    circle(200, 200, 30) # Middelste cirkel
    schiet_pijl()


# Bewaar dit om je code uit te voeren
run(frame_rate=2)
