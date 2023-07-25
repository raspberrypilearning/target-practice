## Crie um plano de fundo

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Seu jogo precisa de um fundo colorido.
</div>
<div>

![A área de saída com um retângulo da cor do céu acima de um retângulo da cor da grama para criar o plano de fundo.](images/background.png){:width="300px"}

</div>
</div>

### Abra o projeto inicial

--- task ---

Open the [Target practice starter](https://editor.raspberrypi.org/en/projects/target-practice-starter){:target="_blank"} project. The code editor will open in another browser tab.

If you have a Raspberry Pi account, you can click on the **Save** button to save a copy to your **Projects**.

--- /task ---

### Editar o céu

--- task ---

O projeto inicial tem algum código já escrito para você.

Clique em **'Executar'** para ver um retângulo azul desenhado com x=`0`, y=`0` (topo da tela). Este retângulo com `400` x `250` píxels é o céu.

![Um retângulo azul com uma borda preta ao redor, acima de um retângulo cinza. O canto superior esquerdo da tela é marcado como x=0, y=0 esta é a origem do retângulo. A largura é destacada como 400 e a altura como 250. O código rect(0, 0, 400, 250) é mostrado.](images/sky_stroke.png){:width="400px"}

**Dica:** 💡 As coordenadas começam em (x=0, y=0) no canto superior esquerdo. Isso pode diferir de outros sistemas de coordenadas que você usou.

--- /task ---

--- task ---

O céu foi desenhado com uma borda preta (traço).

Para desativar o traçado para todas as formas, adicione `no_stroke()` à função `setup`:

--- code ---
---
language: python filename: main.py — setup() line_numbers: true line_number_start: 9
line_highlights: 12
---
def setup():
# Configure seu jogo aqui

    size(400, 400)  # Width and height of screen
    no_stroke()

--- /code ---

--- /task ---

--- task ---

**Run** your code again and notice 👀 that the border (stroke) has now disappeared.

**Tip:** 💡 You will need to press **Stop** to stop your program, this will make the **Run** button reappear.

--- /task ---

### Desenhe a grama

--- task ---

**Adicione** código para desenhar um retângulo verde na parte inferior da tela.

![A área de saída com um retângulo da cor do céu acima de um retângulo da cor da grama para criar o plano de fundo. O canto superior esquerdo do retângulo é marcado como x=0, y=250 esta é a origem do retângulo. A largura é destacada como 400 e a altura como 150. O código rect(0, 250, 400, 150) é mostrado.](images/green-grass.png){:width="400px"}

--- code ---
---
language: python filename: main.py — draw() line_numbers: true line_number_start: 14
line_highlights: 18-19
---
def draw():
# Coisas para fazer em cada imagem

    fill('cyan')  # Set the fill colour for the sky to cyan
    rect(0, 0, 400, 250)  # Draw a rectangle for the sky with these values for x, y, width, height
    fill('lightgreen')  # Set the fill colour for the grass to light green
    rect(0, 250, 400, 150)  # Draw a rectangle for the grass with these values for x, y, width, height

--- /code ---

**Tip:** 💡 We have added comments to our code, like `# Set the fill colour for the sky to cyan`, to tell you what it does. You don't need to add comments to your code, but they are helpful to remind you what lines of code do.

--- /task ---

--- task ---

**Test:** 🔄 Run your project again to view the finished background.

![The output area with a sky-coloured rectangle above a grass-coloured rectangle to create the background.](images/background.png){:width="400px"}

--- /task ---

--- save ---
