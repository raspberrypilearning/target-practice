## What colour did you hit?

Next, you will add some code to get the colour at the location of the arrow.

### Get the colour hit by the arrow

--- task ---

**Depuración:** 🐞 Si ve un mensaje sobre `interno` o `medio` que están 'not defined', vuelve a `draw()` y verifica que estén en la línea que declara variables globales.

Add code to `get` the colour at the centre of the arrow ,and store it in the `hit_colour` variable.


--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 8
line_highlights: 28
---
def mouse_pressed():    
if color_de_impacto == externo:   
print('Le diste al círculo externo, ¡50 puntos!')   
elif color_de_impacto == interno:   
print('Le diste al círculo interno, ¡200 puntos!')   
elif color_de_impacto == medio:    
print('¡Le diste al centro, 500 puntos!')   
else:   
print('¡Fallaste! ¡Sin puntos!')

--- /code ---

**Elije:** 💭 Cambia la cantidad de puntos que ganas para los diferentes colores si así lo deseas.

--- /task ---

--- task ---

**Prueba:** Ejecuta tu proyecto. You should see colours being printed in the **Text output**, in hexadecimal format.

--- /task ---

### Run code when the mouse is pressed

--- task ---

Comment out the line that prints the colour. This means it will not run.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 26
line_highlights: 9
---

    hit_colour = get(arrow_x, arrow_y).hex
    # print(hit_colour)
    circle(arrow_x, arrow_y, 15)

--- /code ---

--- /task ---

--- task ---

Add code to print the target emoji 🎯 **when the mouse is clicked**.

--- code ---
---
language: python filename: main.py - mouse_pressed() line_numbers: true line_number_start: 7
line_highlights: 9, 10
---
# La función mouse_pressed va aquí
def mouse_pressed():    
print('🎯')

--- /code ---

--- /task ---

**Prueba:** Ejecuta tu proyecto. Intenta detener la flecha en los círculos interior y medio para ver sus mensajes.

![target emoji printed when mouse clicked](images/target_printed.gif) --- /task ---

--- save ---