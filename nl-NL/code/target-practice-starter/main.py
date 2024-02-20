# Bibliotheekcode importeren
from p5 import *
from random import randint

# De mouse_pressed functie komt hier

# De schiet_pijl functie komt hier

def setup():
    # Stel je spel hier in
    size(400, 400) # breedte en hoogte

def draw():
    # Dingen om te doen in elk frame
    fill('cyan') # Stel de vulkleur voor de lucht in op cyaan
    rect(0, 0, 400, 250) # Teken een rechthoek voor de lucht met deze waarden voor x, y, breedte, hoogte

# Bewaar dit om je code uit te voeren
run(frame_rate=2)
