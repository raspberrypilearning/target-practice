## Desenhe a grama

--- task ---

Abra o projeto [Tiro ao alvo inicial](https://editor.raspberrypi.org/en/projects/target-practice-starter){:target="_blank"}.

--- /task ---


--- task ---

**Adicione** código para desenhar um retângulo verde na parte inferior da tela.

![A área de saída com um retângulo da cor do céu acima de um retângulo da cor da grama para criar o plano de fundo. O canto superior esquerdo do retângulo é marcado como x=0, y=250 esta é a origem do retângulo. A largura é destacada como 400 e a altura como 150. O código rect(0, 250, 400, 150) é mostrado.](images/green-grass.png){:width="400px"}

--- code ---
---
language: python filename: main.py — draw() line_numbers: true line_number_start: 14
line_highlights: 12
---
def draw(): # Things to do in every frame fill('cyan')  
rect(0, 0, 400, 250)  
fill('lightgreen')  
rect(0, 250, 400, 150) --- /code ---

--- /task ---

--- task ---

**Teste:** 🔄 Execute seu projeto novamente para visualizar o plano de fundo finalizado.

![A área de saída com um retângulo da cor do céu acima de um retângulo da cor da grama para criar o plano de fundo.](images/background.png){:width="400px"}

--- /task ---

--- save ---
