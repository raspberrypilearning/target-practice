# Importuj kod biblioteki
from p5 import *
from random import randint

# Funkcja mouse_pressed pojawi się tutaj

# Funkcja shoot_arrow pojawia się tutaj

def setup():
    # Set up your game here
    rozmiar(400, 400) # szerokość i wysokość ekranu

def draw():
    # Rzeczy do zrobienia w każdej klatce
    fill('cyan')  # Set the fill colour for the sky to cyan
    Rect(0, 0, 400, 250) # Narysuj prostokąt nieba za pomocą tych wartości dla x, y, width, height

# Zatrzymaj to, aby uruchomić swój kod
run(frame_rate=2)
