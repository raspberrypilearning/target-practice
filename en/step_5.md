## What colour did you hit?

Next, you will add some code to get the colour at the location of the arrow.

### Get the colour hit by the arrow 

--- task ---

Add a new **global variable** called `hit_colour`. 

Add code to `get` the colour at the centre of the arrow ,and store it in the `hit_colour` variable. 


--- code ---
---
language: python
line_numbers: true
line_number_start: 9
line_highlights: 10, 13, 14
---
def shoot_arrow():
    global hit_colour  
    arrow_x = randint(100, 300)  
    arrow_y = randint(100, 300) 
    hit_colour = get(arrow_x, arrow_y).hex
    print(hit_colour)
    fill('brown')
    circle(arrow_x, arrow_y, 15)

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
language: python
line_numbers: true
line_number_start: 13
line_highlights: 14
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
language: python
line_numbers: true
line_number_start: 5
line_highlights: 6-7
---
# The mouse_pressed function goes here    
def mouse_pressed():    
    print('🎯')
--- /code ---

--- /task ---

--- task --- 
**Test:** Click the **Run** button. You should see the 🎯 character printed when you click the mouse on the target.

![target emoji printed when mouse clicked](images/target_printed.gif)
--- /task ---


--- save ---