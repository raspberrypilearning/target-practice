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
language: python filename: main.py — disparar_flecha() line_numbers: true line_number_start: 9
line_highlights: 10, 11, 12, 13, 14
---
# La función disparar_flecha va aquí
def disparar_flecha():   
flecha_x = randint(100, 300) # Almacena un número aleatorio entre 100 y 300    
flecha_y = randint(100, 300) # Almacena un número aleatorio entre 100 y 300    
fill(wood) # Establece el color de relleno de la flecha en madera   
circle(flecha_x, flecha_y, 15) # Dibuja un pequeño círculo en coordenadas aleatorias

--- /code ---

--- /task ---

--- task ---

Ve a la función `draw` y llama a tu nueva función `shoot_arrow`.

--- code ---
---
language: python filename: main.py — draw() line_numbers: true line_number_start: 42
line_highlights: 44
---

    fill(medio)<br x-id="4" />
      circle(200, 200, 30)<br x-id="4" />
      disparar_flecha()

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

Convierte `color_de_impacto` en un **variable global** para que pueda usarse en todo tu código:

Agrega código a `get` el color del píxel en el centro de la flecha y guárdalo en la variable `color_de_impacto`. In order to compare the colours, we need to use the hexadecimal code this can be done with the `.hex` string.

--- code ---
---
language: python filename: main.py — disparar_flecha() line_numbers: true line_number_start: 9
line_highlights: 13
---
# La función shoot_arrow va aquí
def disparar_flecha():    
flecha_x = randint(100, 300)    
flecha_y = randint(100, 300)    
color_de_impacto = get(flecha_x, flecha_y) # Consigue el color en que cayó la flecha fill(madera)  
circle(flecha_x, flecha_y, 15)

--- /code ---

**Consejo:** 💡 El código para `obtener` el color debe estar**antes** del código para dibujar el `círculo` lo contrario, ¡siempre guardará el color de madera de la flecha!

--- /task ---

### Imprime el color cuando se presiona el mouse

La biblioteca `p5` "escucha" por ciertos eventos, uno de ellos es presionar el botón del mouse. Cuando detecta que el botón ha sido presionado, ejecutará el código que se le haya dado en la función `mouse_pressed`.

--- task ---

Define tu función `mouse_pressed()` debajo del comentario **# La función mouse_pressed va aquí**.

Add code to print the target emoji 🎯 when the mouse is clicked.

--- code ---
---
language: python filename: main.py - mouse_pressed() line_numbers: true line_number_start: 7
line_highlights: 8, 9
---

# La función mouse_pressed va aquí
def mouse_pressed():    
print( red(color_de_impacto), green(color_de_impacto), blue(color_de_impacto) )

--- /code ---

--- /task ---

--- task ---

**Test:** Ejecuta tu proyecto.

El proyecto imprime el `color_de_impacto` cada vez que se vuelve a dibujar la flecha.

![El blanco, con una flecha circular marrón apareciendo en una variedad de posiciones.](images/fire_arrow.gif)

**Depuración:** 🐞 Si ves un mensaje sobre `color_de_impacto` 'not defined', vuelve a `disparar_flecha()` y comprueba que tienes la línea `global color_de_impacto`.

**Depurar:** Verifica la línea `print` con mucho cuidado en busca de comas y paréntesis.

--- /task ---

--- save ---
