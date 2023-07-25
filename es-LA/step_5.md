## Gana puntos

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Tu juego agregará puntajes según el lugar donde golpea la flecha.
</div>
<div>

![El blanco, con la flecha apareciendo en una variedad de posiciones y las puntuaciones apareciendo como texto debajo del juego.](images/points-scored.gif){:width="300px"}

</div>
</div>

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
We use <span style="color: #0faeb0; font-weight: bold;"> conditions</span> all the time to make decisions. We could say 'if the pencil is blunt, then sharpen it'. Similarly, `if` conditions let us write code that do something different depending on whether a condition is true or false.
</p>

### Mostrar el puntaje

--- task ---

Delete ❌ the `print('🎯')` line of code.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 8
line_highlights: 28
---
# La función mouse_pressed va aquí
def mouse_pressed():


--- /code ---

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Usamos <span style="color: #0faeb0; font-weight: bold;">condiciones</span> todo el tiempo para tomar decisiones. Podríamos decir 'si el lápiz está desafilado, entonces afilalo'. De manera similar, las condiciones `if` nos permiten escribir código que hace algo diferente dependiendo de si una condición es verdadera o falsa.
</p>

--- task ---

`print` a message `if` the `color_de_impacto` is equal to `externo` 🎯.

Nota 👀 que el código usa dos signos de igual `==` para significar **igual a**.

--- code ---
---
language: python filename: main.py - mouse_pressed() line_numbers: true line_number_start: 8
line_highlights: 9
---

# La función mouse_presionado va aquí
def mouse_pressed():     
if color_de_impacto == externo:      
print('Le diste al círculo externo, ¡50 puntos!') # Al igual que las funciones, las declaraciones 'if' están indentandas

--- /code ---

Ve a la función `draw()` y agrega `, externo, interno, medio` a la lista de variables globales.

--- /task ---

--- task ---

**Prueba:** Ejecuta tu proyecto. Intenta detener la flecha en el círculo exterior azul para ver su mensaje.

**Consejo:** 💡 `frame_rate()`, en `setup`, controla qué tan rápido se dibuja tu juego. Si va demasiado rápido, configúralo en un número más bajo.

![El área de salida con la flecha tocando el círculo exterior. La declaración de impresión de puntos aparece en el área de salida.](images/blue-points.png)

global madera, externo, interno, medio    
cielo = color(92, 204, 206) # Rojo = 92, Verde = 204, Azul = 206    
pasto = color(149, 212, 122)    
madera = color(145, 96, 51)    
externo = color(0, 120, 180)    
interno = color(210, 60, 60)   
medio = color(220, 200, 0)

**Depurar:** Asegúrate de que tu código coincida exactamente y de que hayas indentado el código dentro de tu declaración `if`.

def mouse_pressed():    
if color_de_impacto == externo:   
print('Le diste al círculo externo, ¡50 puntos!')   
elif color_de_impacto == interno:   
print('Le diste al círculo interno, ¡200 puntos!')   
elif color_de_impacto == medio:    
print('¡Le diste al centro, 500 puntos!')   
else:   
print('¡Fallaste! ¡Sin puntos!')

--- /task ---

`elif` (else - if) se puede usar para agregar más condiciones a tu declaración `if`. Estos se leerán de arriba a abajo. Tan pronto como se encuentre una condición **Verdadera**, se actuará. Las condiciones restantes serán ignoradas.

--- task ---

Gana puntos si la flecha cae en los círculos `interior` o `medio` 🎯:

--- code ---
---
language: python filename: main.py - mouse_pressed() line_numbers: true line_number_start: 7
line_highlights: 9, 10
---

def mouse_pressed(): if hit_colour == Color('blue').hex:   
print('You hit the outer circle, 50 points!') elif hit_colour == Color('red').hex: print('You hit the inner circle, 200 points!') elif hit_colour == Color('yellow').hex: print('You hit the middle, 500 points!')

--- /code ---

--- /task ---

--- task ---

**Prueba:** Ejecuta tu proyecto. Intenta detener la flecha en los círculos interior y medio para ver sus mensajes.

![El área de salida con la flecha tocando el círculo interior. La declaración de impresión de puntos aparece en el área de salida.](images/yellow-points.png)

**Depuración:** 🐞 Comprueba que tu sangría coincida con el ejemplo.

**Depuración:** 🐞 Si ve un mensaje sobre `interno` o `medio` que están 'not defined', vuelve a `draw()` y verifica que estén en la línea que declara variables globales.

def mouse_pressed():    
if color_de_impacto == externo:    
print('Le diste al círculo externo, ¡50 puntos!')    
elif color_de_impacto == interno:    
print('Le diste al círculo interno, ¡200 puntos!')   
elif color_de_impacto == medio:    
print('¡Le diste al centro, 500 puntos!')

Borra❌ la línea de código `print( red(color_de_impacto), green(color_de_impacto), blue(color_de_impacto) )`.

--- /task ---

### Fallar el blanco

Hay una decisión más que debes tomar: ¿qué sucede si la flecha no aterriza en ninguno de los círculos del blanco? ❌ ❌

Para hacer esta última verificación, usa `else`.

--- task ---

Agrega código a `print` para mostrar un mensaje `else` ya que ninguna de las condiciones `if` y `elif` se han cumplido.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 26
line_highlights: 11, 12, 13, 14
---

def mouse_pressed(): if hit_colour == Color('blue').hex:   
print('You hit the outer circle, 50 points!') elif hit_colour == Color('red').hex: print('You hit the inner circle, 200 points!') elif hit_colour == Color('yellow').hex: print('You hit the middle, 500 points!') else:   
print('You missed! No points!')

--- /code ---

--- /task ---

--- task ---

**Prueba:** 🔄 Ejecuta tu proyecto. Intenta detener la flecha en el pasto o el cielo para ver el mensaje de error.

**Elije:** 💭 Cambia la cantidad de puntos que ganas para los diferentes colores si así lo deseas.

--- /task ---

--- save ---
