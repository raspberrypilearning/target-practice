# Importa la libreria di codice!
from p5 import *
from random import randint

# La funzione mouse_pressed va qui
def mouse_pressed():
    if hit_colour == Color('blue').hex:  # Like functions, if statements are indented
        print('Hai colpito il cerchio esterno, 50 punti!')
    elif hit_colour == Color('red').hex:
        print('Hai colpito il cerchio esterno, 200 punti!')
    elif hit_colour == Color('yellow').hex:
        print('Hai colpito il cerchio intermedio, 500 punti!')
    else:
        print('L'hai mancato! Zero punti!')

# La funzione shoot_arrow va qui
def shoot_arrow():
    global hit_color # Può essere utilizzato in altre funzioni
    arrow_x = randint(100, 300)  # Memorizza un numero casuale compreso tra 100 e 300
    arrow_y = randint(100, 300)  # Memorizza un numero casuale compreso tra 100 e 300
    hit_color = get(arrow_x, arrow_y).hex # Ottieni il colore del risultato
    fill('sienna')  # Set the arrow fill colour to brown
    circle(arrow_x, arrow_y, 15)  # Disegna un piccolo cerchio a coordinate casuali

def setup():
    # Imposta il tuo gioco qui
    size(400, 400)  # larghezza e altezza
    no_stroke()

def draw():
    # Cose da fare in ogni fotogramma
    fill('cyan')
    rect(0, 0, 400, 250)  # Cielo
    fill('lightgreen')
    rect(0, 250, 400, 150)  # Erba
    fill('sienna')
    triangle(150, 350, 200, 150, 250, 350)  # Piedistallo
    fill('blue')
    circle(200, 200, 170)  # Cerchio esterno
    fill('red')
    circle(200, 200, 110)  # Cerchio interno
    fill('yellow')
    circle(200, 200, 30)  # Cerchio intermedio
    shoot_arrow()

# Conserva questa parte per eseguire il codice
run(frame_rate=2)
