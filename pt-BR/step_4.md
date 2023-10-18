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
language: python filename: main.py — atirar_flecha() line_numbers: true line_number_start: 7
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

**Teste:** 🔄 Execute seu código e veja a flecha aparecer em uma posição aleatória a cada quadro.

![Uma animação do alvo com uma seta circular marrom aparecendo em diversas posições.](images/fire_arrow.gif)

O plano de fundo e o alvo serão desenhados sobre a flecha antiga. Isso significa que você só vê uma flecha de cada vez.

--- /task ---

### Obtenha a cor atingida pela flecha

A função `get()` retorna a cor de um píxel.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Um <span style="color: #0faeb0; font-weight: bold;">píxel</span>, abreviação de elemento de imagem, é um único ponto colorido dentro de uma imagem. As imagens são compostas de muitos píxels coloridos.
</p>

--- task ---

Adicione uma **variável global** chamada `cor_acerto` que pode ser usada em todo o seu código.

Adicione o código para obter `get` a cor do píxel no centro da flecha e armazene-o na variável `cor_acerto`. Para comparar as cores, precisamos usar o código hexadecimal. Isso pode ser feito com a string `.hex`.

--- code ---
---
language: python filename: main.py — atirar_flecha() line_numbers: true line_number_start: 7
line_highlights: 9, 12
---
# A função atirar_flecha vai aqui
def atirar_flecha(): global cor_acerto # Pode ser usado em outras funções  
flecha_x = randint(100, 300) # Armazena um número aleatório entre 100 e 300    
flecha_y = randint(100, 300) # Armazena um número aleatório entre 100 e 300 cor_acerto = get(flecha_x, flecha_y).hex # Obtêm a cor do acerto     
fill('sienna') # Define a cor de preenchimento da flecha como marrom   
circle(flecha_x, flecha_y, 15) # Desenha um pequeno círculo em coordenadas aleatórias

--- /code ---

**Dica:** 💡 O código para obter `get` a cor precisa ser **antes** do código para desenhar o `círculo`. Caso contrário, você sempre salvará a cor da madeira da flecha!

--- /task ---

### Imprima a cor quando o mouse é pressionado

A biblioteca `p5` 'escuta' certos eventos, um deles é o pressionamento do botão do mouse. Quando detecta que o botão foi pressionado, ela executará qualquer código que tenha sido fornecido na função `mouse_pressed`.

--- task ---

Defina a sua função `mouse_pressed()` sob o comentário **# A função mouse_pressed vai aqui**.

Adicione o código para imprimir o emoji alvo 🎯 quando o mouse for clicado.

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

**Teste:** 🔄 Execute seu projeto.

O projeto imprime 🎯 cada vez que a seta é redesenhada.

![Uma animação do alvo com uma seta circular marrom aparecendo em diversas posições.](images/fire_arrow.gif)

**Depurar:** 🐞 Se você estiver vendo uma mensagem sobre `cor_acerto` como 'não definido', volte para `atirar_flecha()` e verifique se você incluiu a linha `global cor_acerto`.

**Depurar:** 🐞 Verifique a linha `print` com muito cuidado para ver se há vírgulas e colchetes.

--- /task ---

--- save ---
