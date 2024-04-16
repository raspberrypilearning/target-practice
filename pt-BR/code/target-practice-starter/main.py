# Importar código da biblioteca
from p5 import *
from random import randint

# A função mouse_pressed vai aqui

# A função atirar_flecha vai aqui

def setup():
    # Configure seu jogo aqui
    size(400, 400)  # largura e altura da tela

def draw():
    # Coisas para fazer em cada quadro
    fill('cyan') # Defina a cor de preenchimento do céu como ciano
    rect(0, 0, 400, 250) # Desenhe um retângulo para o céu com estes valores para x, y, largura, altura

# Mantenha isto para executar seu código
run(frame_rate=2)
