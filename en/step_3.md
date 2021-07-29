## Draw your target

 - Reduce the target to three rings (yellow, blue, white)
 - 
 - Elipse positoning (use ingredient?)
 - Triangle positioning (if different?)
 - Stroke needs explaining

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
In this step you will create a target stand and the coloured circles. 
</div>
<div>
![The output area with the target and stand.](images/initial_target.png){:width="300px"}
</div>
</div>

<mark>Draw the rest of the scene - define new colours explain coordinate system for different shapes</mark>

--- task ---

The wooden stand will sit behind the target circles so needs to be drawn first. The order in which you draw things can be very important for complex images.

Draw a **triangle** using the function `triangle(x1, y1, x2, y2, x3, y3)`. Triangles have three sets of coordinates each representing the position of one of the triangle's corners. The stand will have corners at (150, 350), (200, 150), and (250, 350).

--- code ---
---
language: python
filename: main.py - draw
line_numbers: true
line_number_start: 27 
line_highlights: 30-32
---
  fill(GRASS)
  rect(0, 250, 400, 150) # x, y, width, height
  
  # Draw a target
  fill(WOOD) # Set the fill colour to wood
  triangle(150, 350, 200, 150, 250, 350)


--- /code ---

--- /task ---

--- task ---

**Test:** Run your code to see the stand for your target. 

--- /task ---

--- task ---

The largest part of the target will be a `GREY` **circle** using `ellipse(x, y, width, height)`. The **x** and **y** coordinates are the centre position of the circle. To make a perfect circle the **width** and **height** must be the same. 

--- code ---
---
language: python
filename: main.py - draw
line_numbers: true
line_number_start: 30
line_highlights: 33-34
---

# Draw a target
  fill(WOOD)
  triangle(150, 350, 200, 150, 250, 350)
  fill(GREY)
  ellipse(200, 200, 170, 170) # 200, 200 is the middle of the screen. 
  
--- /code ---

--- /task ---

--- task ---

**Test:** Run your code to see the first large grey circle.

**Debug:** You might have used a different spelling of 'grey' — this is one of those words that has a different spelling in different parts of the English-speaking world.

--- /task ---

--- task ---

The starter project had colours `SKY`, `GRASS`, `WOOD` and `GREY` defined as global variables. When you make a variable `global` it can be read from anywhere in the project. You will need to create some more global variables to store colours needed for the rest of the target. 

Create two new colours and add them to the line that makes the variables global (don't forget the commas!)

<mark>!!! WE ARE HERE !!!</mark>

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 
line_highlights: 
---

def draw():
  
  global SKY, GRASS, WOOD, GREY,
 
  GRASS = color(149, 212, 122)
  SKY = color(92, 204, 206)
  WOOD = color(145, 96, 51)
  GREY = color(236, 236, 236)
  BLUE = color(0, 110, 191)
  YELLOW = color(252, 249, 0)
  RED = color(255, 0, 0)
  BLACK = color(0, 0, 0)

--- /code ---
[[[generic-theory-simple-colours]]]

--- /task ---

--- task ---

The target will be made of up a number of circles with different sizes but the same centre coordinates. 

Add two more circles to represent an inner circle and the bullseye.

--- code ---
---
language: python
filename: main.py - draw
line_numbers: true
line_number_start: 
line_highlights: 
---

# Draw a target
  fill(WOOD)
  triangle(150, 350, 200, 150, 250, 350) # Stand
  fill(GREY)
  ellipse(200, 200, 170, 170) # Outter circle
  fill(BLUE)
  ellipse(200, 200, 110, 110) # Inner circle
  fill(YELLOW)
  ellipse(200, 200, 30, 30) # Bullseye
  
--- /code ---

--- /task ---

--- task ---

So far the shapes have been

--- code ---
---
language: python
filename: main.py - draw
line_numbers: true
line_number_start: 
line_highlights: 
---

 # Draw a target
  fill(WOOD_BROWN)
  triangle(150, 350, 200, 150, 250, 350)
  strokeWeight(1)
  stroke(WHITE)
  fill(GREY)
  ellipse(200, 200, 170, 170)
  fill(BLACK)
  ellipse(200, 200, 140, 140)
  fill(BLUE)
  ellipse(200, 200, 110, 110)
  fill(RED)
  ellipse(200, 200, 70, 70)
  fill(YELLOW)
  ellipse(200, 200, 30, 30)

--- /code ---

--- /task ---

--- save ---



