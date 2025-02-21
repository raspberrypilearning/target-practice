## Dibuja tu blanco

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Tu juego necesita un blanco al que disparar flechas.
</div>
<div>

![El área de salida con el blanco y el soporte.](images/three-circles.png){:width="300px"}

</div>
</div>

### Dibuja un soporte triangular

--- task ---

Establece el color de relleno a `madera` (marrón).

Dibuja un triángulo usando las coordenadas x e y para cada una de las esquinas.

![Un triángulo marrón sobre hierba y contra un cielo con los puntos de coordenadas etiquetados en 150, 350 y 200, 150 y 250, 350). Las esquinas del lienzo también están etiquetadas como x=0, y=0 en la parte superior izquierda y x=400, y=400 en la parte inferior derecha.](images/stand_coords.png){:width="400px"}

--- code ---
---
language: python filename: main.py - draw() line_numbers: true line_number_start: 27
line_highlights: 29, 30
---

    fill(pasto)<br x-id="3" />
      rect(0, 250, 400, 150) 
      fill(madera) # Establece el color de relleno del soporte en madera<br x-id="5" />
      triangle(150, 350, 200, 150, 250, 350)

--- /code ---

--- /task ---

--- task ---

**Prueba:** Ejecuta tu código para ver el soporte de tu blanco:

![Un triángulo marrón sobre el césped y contra el cielo.](images/target-stand.png){:width="400px"}

--- /task ---

### Dibuja los círculos del blanco

--- task ---

La parte más grande del blanco es un **círculo** azul.

Establece el color de relleno en `externo` (azul).

Dibuja un círculo con coordenadas x e y para su centro y un ancho.

![Un triángulo marrón y un círculo azul sobre el césped y contra el cielo. El círculo está etiquetado con las coordenadas x=200, y=200 como el centro y el ancho del círculo de 170.](images/circle-coords.png){:width="400px"}

--- code ---
---
language: python filename: main.py - draw() line_numbers: true line_number_start: 17
line_highlights: 31, 32
---

    fill(madera)<br x-id="3" />
      triangle(150, 350, 200, 150, 250, 350)<br x-id="3" />
      fill(externo) # Establece el color de relleno del círculo en exterior<br x-id="4" />
      circle(200, 200, 170) # x, y, ancho del círculo

--- /code ---

--- /task ---

--- task ---

**Prueba:** Ejecuta tu código para ver el primer círculo grande azul.

El círculo azul se dibujó después del soporte, por lo que está al frente:

![Un triángulo marrón y un círculo azul sobre el césped y contra el cielo.](images/blue-circle.png){:width="400px"}

--- /task ---

El blanco está formado por círculos de diferentes tamaños con las mismas coordenadas centrales (200, 200); el centro de la pantalla.

--- task ---

**Agregue** círculos de colores para las partes interior y media del objetivo.

--- code ---
---
language: python filename: main.py - draw() line_numbers: true line_number_start: 29
line_highlights: 24, 25
---

    fill(madera)<br x-id="4" />
      triangle(150, 350, 200, 150, 250, 350)<br x-id="2" />
      fill(externo)<br x-id="3" />
      circle(200, 200, 170)
      fill(interno) # Establece el color de relleno del círculo en interior<br x-id="6" />
      circle(200, 200, 110) # Círculo interior - x, y, ancho del círculo<br x-id="2" />
      fill(medio) # Establece el color de relleno del círculo en medio<br x-id="6" />
      circle(200, 200, 30) # Círculo medio - x, y, ancho del círculo

--- /code ---

--- /task ---

--- task ---

**Prueba:** Vuelve a ejecutar tu proyecto para ver el blanco con tres círculos de colores.

![Un triángulo marrón con tres círculos de colores sobre el césped y contra el cielo.](images/three-circles.png){:width="400px"}

--- /task ---

--- save ---
