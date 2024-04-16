
--- question ---
---
legend: Pergunta 3 de 3
---

Um círculo é desenhado usando o seguinte código:

--- code ---
---
language: python
---

def setup():   
  size(400, 400)   
  fill(0, 255, 0)   
  no_stroke()

def draw():   
  circle(0, 0, 300)

run()

--- /code ---

Qual das imagens abaixo mostra a posição correta deste círculo na área de saída?

--- choices ---

- ( ) ![Um círculo verde centralizado no canto inferior direito da área de saída.](images/bottom-right.png)

  --- feedback ---

  Não necessariamente. Para centralizar o círculo no canto inferior direito, as coordenadas precisariam ser iguais ao tamanho da tela. Neste exemplo, a elipse seria `circle(400, 400, 300)`.

  --- /feedback ---

- ( ) ![Um círculo verde centralizado no meio da área de saída.](images/centre.png)

  --- feedback ---

  Não necessariamente. Para centralizar o círculo no meio, as coordenadas precisariam ser metade do tamanho da tela. Neste exemplo, `circle(200, 200, 300)`.

  --- /feedback ---

- (x) ![Um círculo verde centralizado no canto superior esquerdo da área de saída.](images/top-left.png)

  --- feedback ---

  Está correto! Este círculo está centralizado nas coordenadas (0,0), no canto superior esquerdo da tela.

  --- /feedback ---

- ( ) ![Um círculo verde centralizado no canto superior direito da área de saída.](images/random-side.png)

  --- feedback ---

  Não, este círculo teria o código `circle(350, 150, 300)` para centralizá-lo no canto superior direito da tela. A coordenada `x` é a posição horizontal da elipse na tela, e a coordenada `y` é posição vertical da elipse na tela.

  --- /feedback ---

--- /choices ---

--- /question ---
