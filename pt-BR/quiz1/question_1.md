## Teste rápido

Responda às três perguntas. Há dicas para guiá-lo para a resposta correta.

Após responder cada pergunta, clique em **Ver minha resposta**.

Divirta-se!

--- question ---
---
legend: Pergunta 1 de 3
---
In your project you added `randint(100, 300)` to your `shoot_arrow()` function. What does `randint(100, 300)` do?

--- code ---
---
language: python
---

def shoot_arrow(): global hit_colour arrow_x = randint(100, 300) arrow_y = randint(100, 300)

--- /code ---

--- choices ---

- (x) It chooses a random whole number between 100 and 300.

  --- feedback ---

Está correto. Uma borda preta será desenhada ao redor de suas formas se você não usar esta função.

  --- /feedback ---

- ( ) It makes the arrow move randomly around the screen.

  --- feedback ---

Não exatamente. This code part of how the arrow moves randomly but you need other code too to achieve that goal.

  --- /feedback ---

- ( ) Preenche a forma com uma determinada cor.

  --- feedback ---

  Não exatamente. A função fill() faz isso e geralmente inclui uma cor fornecida.

  --- /feedback ---

- ( ) It draws a circle of a random size.

  --- feedback ---

  Não exatamente. A função Circle() seria usada para desenhar um círculo.

  --- /feedback ---

--- /choices ---

--- /question ---
