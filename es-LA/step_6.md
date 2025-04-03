## Gana puntos

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Añade una puntuación basada en dónde impacta la flecha.
</div>
<div>

![Una animación del blanco, con la flecha apareciendo en una variedad de posiciones y puntajes que aparecen como texto debajo del juego.](images/points-scored.gif){:width="300px"}

</div>
</div>

--- task ---

Comenta la línea para imprimir el carácter 🎯 para que ya no se ejecute.

--- code ---
---
language: python line_numbers: true line_number_start: 6
line_highlights: 7
---
def mouse_pressed(): # print('🎯')

--- /code ---

--- /task ---

--- task ---

Muestra un mensaje **si (if)** el `hit_colour`{:.language-python} es igual al `color del círculo exterior` (azul).

--- code ---
---
language: python line_numbers: true line_number_start: 6
line_highlights: 8-9
---
def mouse_pressed():    
# print('🎯') if hit_colour == Color('blue').hex: print(''Le diste al círculo externo, ¡50 puntos!')

--- /code ---

**Consejo:** Si cambiaste el color de tu círculo exterior, deberás reemplazar `blue (azul)` con el nombre del color que hayas elegido.

--- /task ---

--- task ---

**Prueba:** Haz clic en el botón **Ejecutar (Run)**. Espera a que la flecha aterrice en el círculo azul y luego haz clic con el botón izquierdo del mouse. ![puntos obtenidos al hacer clic en el círculo azul](images/blue_circle_points.gif)

--- /task ---

`elif`{:.language-python} se puede usar para agregar más condiciones a tu declaración `if`{:.language-python}.

--- task ---

Agrega más código para sumar puntos si la flecha cae en los círculos **internos ** o en los círculos **centrales **.

--- code ---
---
language: python line_numbers: true line_number_start: 6
line_highlights: 10-14
---

def mouse_pressed(): # print('🎯') if hit_colour == Color('blue').hex: print(''Le diste al círculo externo, ¡50 puntos!') elif hit_colour == Color('red').hex: print('You hit the inner circle, 200 points!') elif hit_colour == Color('yellow').hex: print('¡Le diste al centro, 500 puntos!')

--- /code ---

--- /task ---

--- task ---

**Test:** Click the **Run** button.You should score points whenever you hit the target.

![points being scored on any area of target](images/yellow-points.png)

--- /task ---

### Fallar el blanco

There is one more decision you need to make: what happens if the arrow does not land on any of the target circles?

To do this last check, you use `else`{:.language-python}.

--- task ---

Add code to `print` a message when none of the `if` and `elif` statements are true.

--- code ---
---
language: python line_numbers: true line_number_start: 12
line_highlights: 14-15
---

    elif hit_colour == Color('yellow').hex:
            print('¡Le diste al centro, 500 puntos!')
    else:   
        print('¡Fallaste! ¡Sin puntos!')

--- /code ---

--- /task ---

--- task ---

**Test:** Click the **Run** button. Fire the arrow in the grass or sky to see the miss message.

![no points printed when outside target](images/missed_no_points.gif)

--- /task ---

--- save ---
