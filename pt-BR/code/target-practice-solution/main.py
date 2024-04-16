# Importa código da biblioteca!
from p5 import *
from random import randint

# A função mouse_pressed vai aqui
def mouse_pressed():
    if cor_acerto == Color('blue').hex:  # Como as funções, as instruções 'if' são indentadas
        print('Você acertou o círculo externo, 50 pontos!')
    elif cor_acerto == Color('red').hex:
        print('Você acertou o círculo interno, 200 pontos!')
    elif cor_acerto == Color('yellow').hex:
        print('Você acertou o meio, 500 pontos!')
    else:
        print('Você errou! Sem pontos!')

# A função atirar_flecha vai aqui
def atirar_flecha():
    global cor_acerto  # Pode ser usado em outras funções
    flecha_x = randint(100, 300)  # Armazena um número aleatório entre 100 e 300
    flecha_y = randint(100, 300)  # Armazena um número aleatório entre 100 e 300
    cor_acerto = get(flecha_x, flecha_y).hex  # Obtém a cor acertada
    fill('sienna')  # Defina a cor de preenchimento da flecha como marrom
    circle(flecha_x, flecha_y, 15)  # Desenha um pequeno círculo em coordenadas aleatórias

def setup():
    # Configure seu jogo aqui
    size(400, 400) # largura e altura
    no_stroke()

def draw():
    # Coisas para fazer em cada quadro
    fill('cyan')
    rect(0, 0, 400, 250) # Céu
    fill('lightgreen')
    rect(0, 250, 400, 150) # Grama
    fill('sienna')
    triangle(150, 350, 200, 150, 250, 350) # Suporte
    fill('blue')
    círculo(200, 200, 170) # Círculo externo
    fill('red')
    círculo(200, 200, 110) # Círculo interno
    fill('yellow')
    círculo(200, 200, 30) # Círculo do meio
    atirar_flecha()

# Mantenha isto para executar seu código
run(frame_rate=2)
