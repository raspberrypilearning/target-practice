## Dispara tu flecha

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Add an even smaller circle to represent an arrow.
</div>
<div>

![El blanco, con una flecha circular marrón que aparece en una variedad de posiciones.](images/fire_arrow.gif){:width="300px"}

</div>
</div>

### Where will you shoot?

--- task ---

Add a function to draw a brown circle at coordinates `200`, `200`.

--- code ---
---
language: python filename: main.py - mouse_pressed() line_numbers: true line_number_start: 7
line_highlights: 10, 11, 12, 13, 14
---
# La función disparar_flecha va aquí
def disparar_flecha():    
global color_de_impacto # Se puede utilizar en otras funciones     
flecha_x = randint(100, 300)     
flecha_y = randint(100, 300)     
color_de_impacto = get(flecha_x, flecha_y) # Guardar el color antes de dibujar la flecha fill(madera)     
circle(flecha_x, flecha_y, 15)

--- /code ---

--- /task ---

--- task ---

Ve a la función `draw` y llama a tu nueva función `disparar_flecha`.

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

--- task --- **Test:** Click the **Run** button. You should see the arrow in the centre.


**Test:** Ejecuta tu proyecto. You should see the arrow in the centre.

![a brown arrow circle in the centre of the target](images/arrow-centre.png)


--- /task ---

The arrow needs to move randomly.


--- task ---

Change the `arrow_x`{:.language-python} and `arrow_y`{:.language-python} variables to choose a random number between 100 and 300.

--- code ---
---
language: python filename: main.py — disparar_flecha() line_numbers: true line_number_start: 9
line_highlights: 13
---
def disparar_flecha():    
flecha_x = randint(100, 300)    
flecha_y = randint(100, 300)    
color_de_impacto = get(flecha_x, flecha_y) # Consigue el color en que cayó la flecha fill(madera)  
circle(flecha_x, flecha_y, 15)

--- /code ---

--- /task ---


--- task ---


**Test:** Click the **Run** button. You should see the arrow jump around the target.

![El blanco, con una flecha circular marrón apareciendo en una variedad de posiciones.](images/fire_arrow.gif)

--- /task ---

--- save ---
