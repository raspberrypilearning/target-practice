## Desenhe o seu alvo

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Seu jogo precisa de um alvo para atirarmos as flechas.
</div>
<div>

![A área de saída com o alvo e suporte.](images/three-circles.png){:width="300px"}

</div>
</div>

### Desenhe um suporte triangular

--- task ---

Defina a cor de preenchimento como `sienna` (marrom).

Desenhe um triângulo usando as coordenadas x e y para cada um dos cantos.

![Um triângulo marrom na grama e um céu com os pontos de coordenadas rotulados em 150, 350 e 200, 150 e 250, 350). Os cantos da tela também são rotulados como x=0, y=0 no canto superior esquerdo e x=400, y=400 no canto inferior direito.](images/stand_coords.png){:width="400px"}

--- code ---
---
language: python filename: main.py - draw() line_numbers: true line_number_start: 18
line_highlights: 20, 21
---

    fill('lightgreen') # Define a cor de preenchimento da grama para verde claro
    rect(0, 250, 400, 150) # Desenha um retângulo para a grama com estes valores para x, y, largura, altura
    fill(' sienna') # Cor marrom
    triangle(150, 350, 200, 150, 250, 350) # Desenha um triângulo para o suporte do alvo

--- /code ---

--- /task ---

--- task ---

**Teste:** 🔄 Execute seu código para ver o suporte para o seu alvo:

![Um triângulo marrom na grama e um céu de fundo.](images/target-stand.png){:width="400px"}

--- /task ---

### Desenhe os círculos do alvo

--- task ---

A maior parte do alvo é um **círculo** azul.

Defina a cor de preenchimento como `azul`.

Desenhe um círculo com coordenadas x e y para seu centro e largura.

![Um triângulo marrom e um círculo azul na grama e um céu de fundo. O círculo é rotulado com as coordenadas x=200, y=200 como centro e a largura do círculo de 170.](images/circle-coords.png){:width="400px"}

--- code ---
---
language: python filename: main.py - draw() line_numbers: true line_number_start: 20
line_highlights: 22, 23
---

    fill('sienna') # Cor marrom
    triangle(150, 350, 200, 150, 250, 350) # Desenha um triângulo para o suporte do alvo 
    fill('blue') # Define a cor de preenchimento do círculo para azul
    circle(200, 200, 170) # Desenha o círculo externo

--- /code ---

--- /task ---

--- task ---

**Teste:** Execute seu código para ver o primeiro grande círculo azul.

O círculo azul foi desenhado depois do suporte, então fica na frente.

![Um triângulo marrom e um círculo azul na grama e um céu de fundo.](images/blue-circle.png){:width="400px"}

--- /task ---

O alvo é feito de círculos de tamanhos diferentes com as mesmas coordenadas centrais (200, 200).

--- task ---

**Adicione** círculos coloridos para as partes interna e medianas do alvo.

--- code ---
---
language: python filename: main.py - draw() line_numbers: true line_number_start: 20
line_highlights: 24, 25, 26, 27
---

    fill('sienna') # Cor marrom
    triangle(150, 350, 200, 150, 250, 350) # Desenha um triângulo para o suporte do alvo 
    fill('blue') # Define a cor de preenchimento do círculo para azul
    circle(200, 200, 170) # Desenha o círculo externo
    fill('red') # Define a cor do preenchimento do círculo para vermelho
    circle(200, 200, 110) # Desenha o círculo interno usando x, y, width
    fill('yellow') # Define a cor de preenchimento do círculo para amarelo      
    circle(200, 200, 30) # Desenha o círculo do meio usando x, y, largura

--- /code ---

--- /task ---

--- task ---

**Teste:** 🔄 Execute seu projeto para ver o alvo com três círculos coloridos.

![Um triângulo marrom com três círculos coloridos na grama e um céu de fundo.](images/three-circles.png){:width="400px"}

--- /task ---

--- save ---
