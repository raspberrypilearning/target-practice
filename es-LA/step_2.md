## Crea un fondo

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Tu juego necesita un fondo colorido.
</div>
<div>

![El área de resultados con un rectángulo de color cielo sobre otro rectángulo de color césped para crear un fondo.](imagenes/fondo.png){ancho="300px"}

</div>
</div>

### Abre el proyecto inicial

--- task ---

Abre el [proyecto inicial de Tiro al blanco](https://trinket.io/python/9973649e5c){:target="_blank"}.

Si tienes una cuenta en Trinket, puedes hacer clic en el botón **Remix** para guardar una copia en tu biblioteca **My Trinkets**.

--- /task ---

### Edita el cielo

--- task ---

El proyecto de inicio ya tiene código pre escrito para ti.

Haz clic en **'Run'** para ver un rectángulo relleno de azul dibujado de x=`0`, y=`0` (la parte superior de la pantalla). Este rectángulo de `400` x `250` píxeles es el cielo.

![Un rectángulo azul con un borde negro alrededor, encima de un rectángulo gris. La esquina superior izquierda del lienzo está marcada como x=0, y=0, este es el origen del rectángulo. El ancho se resalta como 400 y la altura como 250. Se muestra el código rect(0, 0, 400, 250).](images/sky_stroke.png){:width="400px"}

**Consejo:** 💡 Las coordenadas comienzan desde (x=0, y=0) en la esquina superior izquierda. Esto puede ser diferente a otros sistemas de coordenadas que hayas utilizado.

--- /task ---

--- task ---

El cielo se ha dibujado con un borde negro (stroke).

Para desactivar el trazo para todas las formas, agrega `no_stroke()` a la función `setup`:

--- code ---
---
language: python filename: main.py — setup() line_numbers: true line_number_start: 11
line_highlights: 15
---
def setup():
# Configura aquí tu juego

    size(400, 400) # ancho y alto de la pantalla
      frame_rate(2)
      no_stroke()

--- /code ---

--- /task ---

--- task ---

global madera cielo = color(92, 204, 206) # Rojo = 92, Verde = 204, Azul = 206 pasto = color(149, 212, 122) madera = color(145, 96, 51) externo = color(0, 120, 180)

**Ejecute** (run) tu código nuevamente y observa 👀 que el borde (stroke) ha desaparecido.

--- /task ---

### Dibuja el césped

--- task ---

**Agregue** código para dibujar un rectángulo verde en la parte inferior de la pantalla.

![El área de salida con un rectángulo color cielo sobre un rectángulo color hierba para crear el fondo. La esquina superior izquierda del rectángulo está marcada como x=0, y=250, este es el origen del rectángulo. El ancho de 400 y la altura de 150 están resaltados. Se muestra el código rect(0, 250, 400, 150).](images/green-grass.png){:width="400px"}

--- code ---
---
language: python filename: main.py — draw() line_numbers: true line_number_start: 17
line_highlights: 27, 28
---
def draw():
# Cosas que hacer en cada cuadro

    fill(cielo)<br x-id="5" />
      rect(0, 0, 400, 250)<br x-id="5" />
      fill(pasto) # Establece el color de relleno en césped
      rect(0, 250, 400, 150) # x, y, ancho, alto

--- /code ---

**Consejo:** 💡 Hemos agregado comentarios a nuestro código, como `# Establece el color de relleno en césped`, para decir lo que hace. No necesits agregar estos comentarios a tu código, pero pueden ser útiles para recordarte qué hacen.

--- /task ---

--- task ---

**Prueba:** Ejecuta tu proyecto de nuevo para ver el fondo terminado.

![El área de salida con un rectángulo color cielo sobre un rectángulo color césped para crear el fondo.](images/background.png){:width="400px"}

--- /task ---

--- save ---