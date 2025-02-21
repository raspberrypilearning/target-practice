## Dibuja el césped

--- task ---

Abre el [proyecto inicial de Tiro al blanco](https://trinket.io/python/88502d5879){:target="_blank"}.

--- /task ---


--- task ---

**Agregue** código para dibujar un rectángulo verde en la parte inferior de la pantalla.

![El área de salida con un rectángulo color cielo sobre un rectángulo color hierba para crear el fondo. La esquina superior izquierda del rectángulo está marcada como x=0, y=250, este es el origen del rectángulo. El ancho de 400 y la altura de 150 están resaltados. Se muestra el código rect(0, 250, 400, 150).](images/green-grass.png){:width="400px"}

--- code ---
---
language: python filename: main.py — draw() line_numbers: true line_number_start: 17
line_highlights: 15
---
def draw(): # Things to do in every frame fill('cyan')  
rect(0, 0, 400, 250)  
fill('lightgreen')  
rect(0, 250, 400, 150) --- /code ---

--- /task ---

--- task ---

**Prueba:** Ejecuta tu proyecto de nuevo para ver el fondo terminado.

![El área de salida con un rectángulo color cielo sobre un rectángulo color césped para crear el fondo.](images/background.png){:width="400px"}

--- /task ---

--- save ---
