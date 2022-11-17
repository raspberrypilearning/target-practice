## Dispara tu flecha

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Al hacer clic o tocar, se disparará una flecha en la posición de un blanco en movimiento. 
</div>
<div>

![El blanco, con una flecha circular marrón que aparece en una variedad de posiciones.](images/fire_arrow.gif){:width="300px"}

</div>
</div>

### Dibuja un blanco en cada cuadro

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;"> Las computadoras crean el efecto de movimiento al mostrar muchas imágenes una tras otra. Cada imagen se llama un <span style="color: #0faeb0; font-weight: bold;"> fotograma </span>.   
</p>

--- task ---

Define tu función `shoot_arrow()` debajo del comentario **# La función shoot_arrow va aquí**.

Agrega código para dibujar aleatoriamente un círculo marrón dentro de un área objetivo:

![Un rectángulo que muestra las coordenadas del área objetivo en un rectángulo semitransparente. El área objetivo está entre x=100 e y=100 a x=300 e y=300, por lo que cubre todo el blanco y más.](images/target_area.png)

--- code ---
---
language: python filename: main.py — shoot_arrow() line_numbers: true line_number_start: 9
line_highlights: 10, 11, 12, 13, 14
---
# La función disparar_flecha va aquí
def shoot_arrow():   
arrow_x = randint(100, 300) # Store a random number between 100 and 300    
arrow_y = randint(100, 300) # Store a random number between 100 and 300    
fill(wood) # Set the arrow to fill colour to wood   
circle(arrow_x, arrow_y, 15) # Draw a small circle at random coordinates

--- /code ---

--- /task ---

--- task ---

Ve a la función `draw` y llama a tu nueva función `shoot_arrow`.

--- code ---
---
language: python filename: main.py — draw() line_numbers: true line_number_start: 42
line_highlights: 44
---
  fill(middle)    
circle(200, 200, 30)    
shoot_arrow()

--- /code ---

--- /task ---

--- task ---

**Prueba:** 🔄 Ejecuta tu código y observa que la flecha aparece en una posición aleatoria en cada cuadro.

![El blanco, con una flecha circular marrón apareciendo en una variedad de posiciones.](images/fire_arrow.gif)

El fondo y el objetivo se dibujarán sobre la flecha anterior. Esto significa que solo verás una flecha a la vez.

--- /task ---

### Obtener el color donde se clavó la flecha

La función `get()` devuelve el color de un píxel.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Un <span style="color: #0faeb0; font-weight: bold;">píxel</span>, abreviatura de elemento de imagen (picture element), es un punto de un solo color dentro de una imagen. Las imágenes están formadas por muchos píxeles de colores.
</p>

--- task ---

Agrega código a `get` el color del píxel en el centro de la flecha y guárdalo en la variable `hit_color`.

--- code ---
---
language: python filename: main.py — shoot_arrow() line_numbers: true line_number_start: 9
line_highlights: 13
---
# La función shoot_arrow va aquí
def shoot_arrow():    
arrow_x = randint(100, 300)    
arrow_y = randint(100, 300)    
hit_color = get(arrow_x, arrow_y) # Get the hit colour fill(wood)  
circle(arrow_x, arrow_y, 15)

--- /code ---

**Consejo:** 💡 El código para `obtener` el color debe estar**antes** del código para dibujar el `círculo` lo contrario, ¡siempre guardará el color de madera de la flecha!

--- /task ---

### Imprime el color cuando se presiona el mouse

La biblioteca `p5` "escucha" por ciertos eventos, uno de ellos es presionar el botón del mouse. Cuando detecta que el botón ha sido presionado, ejecutará el código que se le haya dado en la función `mouse_pressed`.

--- task ---

Define tu función `mouse_pressed()` debajo del comentario **# La función mouse_pressed va aquí**.

Agrega código para imprimir las cantidades de rojo, verde y azul en el píxel en el que aterriza la flecha.

--- code ---
---
language: python filename: main.py - mouse_pressed() line_numbers: true line_number_start: 7
line_highlights: 8, 9
---

# La función mouse_pressed va aquí
def mouse_pressed():    
print( red(hit_color), green(hit_color), blue(hit_color) )

--- /code ---

--- /task ---

--- task ---

Convierte `hit_color` en un **variable global** para que pueda usarse en todo tu código:

--- code ---
---
language: python filename: main.py - shoot_arrow() line_numbers: true line_number_start: 11
line_highlights: 13
---
# La función disparar_flecha va aquí
def shoot_arrow():    
global hit_color # Can be used in other functions     
arrow_x = randint(100, 300)     
arrow_y = randint(100, 300)     
hit_color = get(arrow_x, arrow_y) # Save the colour before drawing the arrow fill(wood)     
circle(arrow_x, arrow_y, 15)

--- /code ---

--- /task ---

--- task ---

**Test:** Ejecuta tu proyecto.

El proyecto imprime el `hit_color` cada vez que se vuelve a dibujar la flecha.

![El blanco, con una flecha circular marrón apareciendo en una variedad de posiciones.](images/fire_arrow.gif)

**Depuración:** 🐞 Si ves un mensaje sobre `hit_color` 'not defined', vuelve a `shoot_arrow()` y comprueba que tienes la línea `global hit_color`.

**Depurar:** Verifica la línea `print` con mucho cuidado en busca de comas y paréntesis.

--- /task ---


