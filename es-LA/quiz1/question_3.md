
--- question ---
---
legend: Pregunta 3 de 3
---

A circle is drawn using the following code:

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

Which of the images below show the correct position of this circle in the output area?

--- choices ---

- ( ) ![Un círculo verde centrado en la esquina inferior derecha del área de salida.](images/bottom-right.png)

  --- feedback ---

  No del todo, para centrar el círculo en la esquina inferior derecha, las coordenadas deberían ser las mismas que el tamaño de la pantalla. In this example, the ellipse would be `circle(400, 400, 300)`.

  --- /feedback ---

- ( ) ![Un círculo verde centrado en el medio del área de salida.](images/centre.png)

  --- feedback ---

  No del todo, para centrar el círculo en el medio, las coordenadas tendrían que ser la mitad del tamaño de la pantalla. In this example, `circle(200, 200, 300)`.

  --- /feedback ---

- (x) ![Un círculo verde centrado en la esquina superior izquierda del área de salida.](images/top-left.png)

  --- feedback ---

  ¡Correcto! Este círculo está centrado en las coordenadas (0,0), la esquina superior izquierda de la pantalla.

  --- /feedback ---

- ( ) ![Un círculo verde centrado hacia el lado superior derecho del área de salida.](images/random-side.png)

  --- feedback ---

  No, this circle would have code of `circle(350, 150, 300)` to centre it towards the top-right of the screen. La coordenada `x` es qué tan lejos está la elipse a través de la pantalla, y la coordenada `y` es qué tan lejos está hacia abajo de la pantalla.

  --- /feedback ---

--- /choices ---

--- /question ---
