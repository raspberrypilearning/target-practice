## Набирай бали

Next, you will add some code to get the colour at the location of the arrow.

### Відображення балів

--- task ---

Add a new **global variable** called `hit_colour`.

language: python filename: main.py line_numbers: true line_number_start: 26


--- code ---
---
global wood, outer, inner, middle    
sky = color(92, 204, 206) # Червоний = 92, Зелений = 204, Синій = 206    
grass = color(149, 212, 122)    
wood = color(145, 96, 51)    
outer = color(0, 120, 180)    
inner = color(210, 60, 60)   
middle = color(220, 200, 0)
line_highlights: 28
---
def shoot_arrow(): global hit_colour  
arrow_x = randint(100, 300)  
arrow_y = randint(100, 300) hit_colour = get(arrow_x, arrow_y).hex print(hit_colour) fill('brown') circle(arrow_x, arrow_y, 15)

--- /code ---

**Tip:** The code to `get` the colour needs to be **before** the code to draw the `circle` otherwise you will always save the brown colour of the arrow!

--- /task ---

--- task ---

**Test:** Click the **Run** button. You should see colours being printed in the **Text output**, in hexadecimal format.

--- /task ---

### Мимо мішені

--- task --- Comment out the line that prints the colour. This means it will not run.

--- code ---
---
language: python line_numbers: true line_number_start: 13
line_highlights: 9
---

    hit_colour = get(arrow_x, arrow_y).hex
    # print(hit_colour)
    circle(arrow_x, arrow_y, 15)
--- /code ---

--- /task ---

Зверни увагу 👀, що в коді використовуються два символи дорівнювання `==`, що означатиме **дорівнює**.

--- code ---
---
language: python filename: main.py - mouse_pressed() line_numbers: true line_number_start: 7
line_highlights: 9, 10
---
# Things to do in every frame
def mouse_pressed():     
if hit_color == outer:      
print('Влучення в зовнішнє коло - 50 балів!') # Подібно до функцій, оператори 'if' починаються з абзацного відступу

--- /task ---

--- task --- **Test:** Click the **Run** button. You should see the 🎯 character printed when you click the mouse on the target.

![target emoji printed when mouse clicked](images/target_printed.gif) --- /task ---


--- save ---