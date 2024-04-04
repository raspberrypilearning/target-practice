# Importuj kod biblioteki!
from p5 import *
from random import randint

# Funkcja mouse_pressed pojawi się tutaj
def mouse_pressed():
    if hit_colour == Color('blue').hex:  # Like functions, if statements are indented
        Print('trafiłeś w zewnętrzne koło, 50 punktów!')
    elif hit_color == Kolor('czerwony').hex:
        Print('trafiłeś w wewnętrzny okrąg, 200 punkty!')
    elif hit_color == Kolor('żółty').hex:
        Print('trafiłeś na środek, 500 punktów!')
    else:
        Print('przegapiłeś! Żadnych punktów!')

# Funkcja shoot_arrow pojawia się tutaj
def shoot_arrow():
    Global hit_color # może być używany w innych funkcjach
    Arrow_x = randint(100, 300) # Zapisz losową liczbę z zakresu od 100 do 300
    Arrow_y = randint(100, 300) # Zachowuj losową liczbę z zakresu od 100 do 300
    Hit_color = get(arrow_x, arrow_y).hex # Uzyskaj kolor trafienia
    fill('sienna')  # Set the arrow fill colour to brown
    Circle(arrow_x, arrow_y, 15) # Narysuj małe kółko o losowych współrzędnych

def setup():
    # Skonfiguruj swoją grę tutaj
    rozmiar(400, 400) # szerokość i wysokość
    no_stroke()

def draw():
    # Rzeczy do zrobienia w każdej klatce
    fill('cyjan')
    Rect(0, 0, 400, 250) # Niebo
    fill('lightgreen')
    Rect(0, 250, 400, 150) # trawa
    fill('sienna')
    trójkąt(150, 350, 200, 150, 250, 350) # Stojak
    fill('niebieski')
    Okrąg(200, 200, 170) # Koło zewnętrzne
    fill(czerwony)
    Okrąg(200, 200, 110) # Koło wewnętrzne
    fill('yellow')
    Okrąg(200, 200, 30) # Środkowy okrąg
    strzałka_strzałka()

# Zatrzymaj to, aby uruchomić swój kod
run(frame_rate=2)
