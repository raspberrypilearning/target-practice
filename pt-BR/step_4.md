## Atire a sua flecha

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Quando você clicar ou tocar, uma flecha será disparada na posição de um círculo alvo em movimento. 
</div>
<div>

![O alvo, com uma flecha circular marrom aparecendo em várias posições.](images/fire_arrow.gif){:width="300px"}

</div>
</div>

### Desenhe um círculo alvo a cada quadro

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;"> Os computadores criam o efeito de movimento mostrando muitas imagens uma após a outra. Cada imagem é chamada de <span style="color: #0faeb0; font-weight: bold;">quadro</span>.   
</p>

--- task ---

Defina a sua função `atirar_flecha()` sob o comentário **# A função atirar_flecha vai aqui**.

Adicione código para desenhar aleatoriamente um círculo marrom dentro de uma área de destino:

![Um retângulo mostrando as coordenadas da área do alvo em um retângulo semitransparente. A área alvo está entre x=100 e y=100 e x=300 e y=300, então cobre todo o alvo e é mais ampla.](images/target_area.png)

--- code ---
---
language: python filename: main.py — shoot_arrow() line_numbers: true line_number_start: 7
line_highlights: 8-12
---
# A função atirar_flecha vai aqui
def shoot_arrow():   
arrow_x = randint(100, 300)  # Store a random number between 100 and 300    
arrow_y = randint(100, 300)  # Store a random number between 100 and 300    
fill('sienna')  # Set the arrow to fill colour to brown   
circle(arrow_x, arrow_y, 15)  # Draw a small circle at random coordinates

--- /code ---

--- /task ---

--- task ---

Vá para a função `draw` e invoque a sua nova função `atirar_flecha`.

--- code ---
---
language: python filename: main.py — draw() line_numbers: true line_number_start: 31
line_highlights: 33
---

    fill('yellow')  # Set the colour for the circle fill to yellow      
    circle(200, 200, 30)  # Draw the middle circle using x, y, width
    shoot_arrow()

--- /code ---

--- /task ---

--- task ---

**Test:** 🔄 Run your code and see the arrow appear in a random position each frame.

![An animation of target with a brown circle arrow appearing in a variety of positions.](images/fire_arrow.gif)

The background and target will be drawn over the old arrow. This means you only see one arrow at a time.

--- /task ---

### Obtenha a cor atingida pela flecha

The `get()` function returns the colour of a pixel.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
A <span style="color: #0faeb0; font-weight: bold;">pixel</span>, short for picture element, is a single coloured dot within an image. Images are made up of lots of coloured pixels.
</p>

--- task ---

Add a **global variable** called `hit_colour` that can be used throughout your code.

Add code to `get` the colour of the pixel at the centre of the arrow and store it in the `hit_colour` variable. In order to compare the colours, we need to use the hexadecimal code this can be done with the `.hex` string.

--- code ---
---
language: python filename: main.py — shoot_arrow() line_numbers: true line_number_start: 7
line_highlights: 8, 11
---
# A função atirar_flecha vai aqui
def shoot_arrow(): global hit_colour  # Can be used in other functions  
arrow_x = randint(100, 300)  # Store a random number between 100 and 300    
arrow_y = randint(100, 300)  # Store a random number between 100 and 300 hit_colour = get(arrow_x, arrow_y).hex  # Get the hit colour     
fill('sienna')  # Set the arrow to fill colour to brown   
circle(arrow_x, arrow_y, 15)  # Draw a small circle at random coordinates

--- /code ---

**Dica:** 💡 O código para obter `get` a cor precisa ser **antes** do código para desenhar o `círculo`. Caso contrário, você sempre salvará a cor da madeira da flecha!

--- /task ---

### Imprima a cor quando o mouse é pressionado

A biblioteca `p5` 'escuta' certos eventos, um deles é o pressionamento do botão do mouse. Quando detecta que o botão foi pressionado, ela executará qualquer código que tenha sido fornecido na função `mouse_pressed`.

--- task ---

Defina a sua função `mouse_pressed()` sob o comentário **# A função mouse_pressed vai aqui**.

Add code to print the target emoji 🎯 when the mouse is clicked.

--- code ---
---
language: python filename: main.py - mouse_pressed() line_numbers: true line_number_start: 5
line_highlights: 6
---

# A função mouse_pressed vai aqui
def mouse_pressed():    
print('🎯')

--- /code ---

--- /task ---

--- task ---

**Test:** 🔄 Run your project.

The project prints 🎯 each time the arrow is redrawn.

![An animation of target with a brown circle arrow appearing in a variety of positions.](images/fire_arrow.gif)

**Debug:** 🐞 If you are seeing a message about `hit_colour` being 'not defined', then go back to `shoot_arrow()` and check that you have included the `global hit_colour` line.

**Debug:** 🐞 Check the `print` line really carefully for commas and brackets.

--- /task ---

--- save ---
