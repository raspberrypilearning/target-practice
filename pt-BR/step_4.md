## Atire a sua flecha

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Add an even smaller circle to represent an arrow.
</div>
<div>

![O alvo, com uma flecha circular marrom aparecendo em várias posições.](images/fire_arrow.gif){:width="300px"}

</div>
</div>

### Where will you shoot?

--- task ---

Adicione código para desenhar aleatoriamente um círculo marrom dentro de uma área de destino:

--- code ---
---
language: python filename: main.py — shoot_arrow() line_numbers: true line_number_start: 7
line_highlights: 8-12
---
# A função atirar_flecha vai aqui
def atirar_flecha():   
flecha_x = randint(100, 300) # Armazena um número aleatório entre 100 e 300    
flecha_y = randint(100, 300) # Armazena um número aleatório entre 100 e 300    
fill('sienna') # Define a cor de preenchimento da flecha como marrom   
circle(flecha_x, flecha_y, 15) # Desenha um pequeno círculo em coordenadas aleatórias

--- /code ---

--- /task ---

--- task ---

Vá para a função `draw` e invoque a sua nova função `atirar_flecha`.

--- code ---
---
language: python filename: main.py — draw() line_numbers: true line_number_start: 31
line_highlights: 33
---

    fill('yellow') # Define a cor de preenchimento do círculo para amarelo      
    circle(200, 200, 30) # Desenha o círculo do meio usando x, y, width
    atirar_flecha()

--- /code ---

--- /task ---

--- task ---

**Teste:** 🔄 Execute seu projeto. You should see the arrow in the centre.


**Test:** Click the **Run** button. You should see the arrow in the centre.

![a brown arrow circle in the centre of the target](images/arrow-centre.png)


--- /task ---

The arrow needs to move randomly.


--- task ---

Change the `arrow_x`{:.language-python} and `arrow_y`{:.language-python} variables to choose a random number between 100 and 300.

--- code ---
---
language: python filename: main.py - mouse_pressed() line_numbers: true line_number_start: 5
line_highlights: 9, 12
---
def atirar_flecha(): global cor_acerto # Pode ser usado em outras funções  
flecha_x = randint(100, 300) # Armazena um número aleatório entre 100 e 300    
flecha_y = randint(100, 300) # Armazena um número aleatório entre 100 e 300 cor_acerto = get(flecha_x, flecha_y).hex # Obtêm a cor do acerto     
fill('sienna') # Define a cor de preenchimento da flecha como marrom   
circle(flecha_x, flecha_y, 15) # Desenha um pequeno círculo em coordenadas aleatórias

--- /code ---

--- /task ---


--- task ---


**Teste:** 🔄 Execute seu projeto. You should see the arrow jump around the target.

![Uma animação do alvo com uma seta circular marrom aparecendo em diversas posições.](images/fire_arrow.gif)

--- /task ---

--- save ---
