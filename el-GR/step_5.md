## Κέρδισε πόντους

Next, you will add some code to get the colour at the location of the arrow.

### Get the colour hit by the arrow

--- task ---

Add a new **global variable** called `hit_colour`.

language: python filename: main.py line_numbers: true line_number_start: 26


--- code ---
---
global outer, inner, bullseye    
sky = color(92, 204, 206) #Κόκκινο = 92, Πράσινο = 204, Μπλε = 206    
grass = color(149, 212, 122)    
wood = color(145, 96, 51)    
outer = color(0, 120, 180)    
inner = color(210, 60, 60)   
bullseye = color(220, 200, 0)
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

### Run code when the mouse is pressed

--- task ---

Comment out the line that prints the colour. This means it will not run.

--- code ---
---
language: python line_numbers: true line_number_start: 13
line_highlights: 10-11
---

    global outer, inner, bullseye

--- /code ---

--- /task ---

--- task ---

Add code to print the target emoji 🎯 **when the mouse is clicked**.

--- code ---
---
language: python line_numbers: true line_number_start: 5
line_highlights: 12-15
---
# Ενέργειες που πρέπει να γίνονται σε κάθε καρέ
def mouse_pressed():    
print('🎯')

--- /code ---

--- /task ---

--- task ---

**Test:** Click the **Run** button. You should see the 🎯 character printed when you click the mouse on the target.

![target emoji printed when mouse clicked](images/target_printed.gif)

--- /task ---

--- save ---