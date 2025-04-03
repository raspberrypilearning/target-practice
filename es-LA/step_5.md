## ¿Que color te salió?

A continuación, agregarás código para obtener el color en la ubicación de la flecha.

### Obtener el color donde se clavó la flecha

--- task ---

**Depuración:** 🐞 Si ve un mensaje sobre `interno` o `medio` que están 'not defined', vuelve a `draw()` y verifica que estén en la línea que declara variables globales.

Agregue código para `obtener (get)` el color en el centro de la flecha y almacenarlo en la variable `hit_colour` .


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

**Prueba:** Ejecuta tu proyecto. Deberías ver los colores impresos en la **salida de texto**, en formato hexadecimal.

--- /task ---

### Imprime el color cuando se presiona el mouse

--- task ---

Comment out the line that prints the colour. Esto significa que no funcionará.

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

--- task ---

**Prueba:** Ejecuta tu proyecto. Intenta detener la flecha en los círculos interior y medio para ver sus mensajes.

![emoji de objetivo impreso al hacer clic con el mouse](images/target_printed.gif)

--- /task ---

--- save ---