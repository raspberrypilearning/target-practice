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

Abra o projeto [Tiro ao alvo inicial](https://editor.raspberrypi.org/pt-BR/projects/target-practice-starter){:target="_blank"}. O editor de código será aberto em outra guia do navegador.

Se você possui uma conta Raspberry Pi, você pode clicar no botão **Salvar** para salvar uma cópia do seu projeto em seus **Projetos**.

--- /task ---

### Edite o céu

--- task ---

O projeto inicial já possui algum código escrito para você.

Clique em **'Executar'** para ver um retângulo azul desenhado com x=`0`, y=`0` (topo da tela). Este retângulo com `400` x `250` píxeis é o céu.

![Um retângulo azul com uma borda preta ao redor, acima de um retângulo cinza. O canto superior esquerdo da tela é marcado como x=0, y=0 esta é a origem do retângulo. A largura é destacada como 400 e a altura como 250. O código rect(0, 0, 400, 250) é mostrado.](images/sky_stroke.png){:width="400px"}

**Dica:** 💡 As coordenadas começam em (x=0, y=0) no canto superior esquerdo. Isso pode diferir de outros sistemas de coordenadas que você usou.

--- /task ---

--- task ---

O céu foi desenhado com uma borda preta (traço).

Para desativar o traçado para todas as formas, adicione `no_stroke()` à função `setup`:

--- code ---
---
language: python
filename: main.py — setup()
line_numbers: true
line_number_start: 9
line_highlights: 12
---
def setup():
# Configure seu jogo aqui
    size(400, 400)  # Largura e altura da tela
    no_stroke()

--- /code ---

--- /task ---

--- task ---

**Execute** seu código novamente e observe 👀 que a borda (traço) agora desapareceu.

**Dica:** 💡 Você precisará pressionar **Stop** para parar seu programa, isso fará com que o botão **Run** reapareça.

--- /task ---

### Desenhe a grama

--- task ---

**Adicione** código para desenhar um retângulo verde na parte inferior da tela.

![A área de saída com um retângulo da cor do céu acima de um retângulo da cor da grama para criar o plano de fundo. O canto superior esquerdo do retângulo é marcado como x=0, y=250 esta é a origem do retângulo. A largura é destacada como 400 e a altura como 150. O código rect(0, 250, 400, 150) é mostrado.](images/green-grass.png){:width="400px"}

--- code ---
---
language: python
filename: main.py — draw()
line_numbers: true
line_number_start: 14
line_highlights: 18-19
---
def draw():
# Coisas para fazer em cada quadro
    fill('cyan') # Define a cor de preenchimento do céu para ciano
    rect(0, 0, 400, 250) # Desenha um retângulo para o céu com estes valores para x, y, largura, altura
    fill('lightgreen ') # Define a cor de preenchimento da grama para verde claro
    rect(0, 250, 400, 150) # Desenha um retângulo para a grama com esses valores para x, y, largura, altura

--- /code ---

**Dica:** 💡 Adicionamos comentários ao nosso código, como `# Define a cor de preenchimento do céu para ciano`, para informar o que ele faz. Você não precisa adicionar esses comentários ao seu código, mas eles podem ser úteis para lembrá-lo do que as linhas de código fazem.

--- /task ---

--- task ---

**Teste:** 🔄 Execute seu projeto novamente para visualizar o plano de fundo finalizado.

![A área de saída com um retângulo da cor do céu acima de um retângulo da cor da grama para criar o plano de fundo.](images/background.png){:width="400px"}

--- /task ---

--- save ---
