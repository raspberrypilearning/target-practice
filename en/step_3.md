## Draw your target
<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
In this step you will create a target stand and a target with coloured circles — smaller circles are worth more points than larger ones. 
</div>
<div>
![The output area with the target and stand.](images/outline-circles.png){:width="300px"}
</div>
</div>

The wooden stand will sit behind the target circles so needs to be drawn first. The order in which you draw things can be very important for complex images.

Computer graphics are made of **layers**. In your game, each shape is a layer. Objects on higher layers sit in front of objects on lower layers. Imagine cutting all the shapes out of paper. Depending on how you arrange and overlap that paper, the final result could look very different.

--- task ---

Draw a **triangle** using the function `triangle(x1, y1, x2, y2, x3, y3)`. Triangles have three sets of coordinates each representing the position of one of the triangle's corners. 

--- collapse ---
---
title: Triangle coordinates
---

  Here are three example triangles each with different sets of coordinates. Look at the grid position of each to see how the x and y coordinates position the corners of the triangles:
  + Green triangle: triangle(50, 50, 150, 50, 180, 100)
  + Blue triangle: triangle(210, 280, 300, 350, 380, 100)
  + Brown triangle: triangle(50, 150, 200, 250, 180, 350)
  
  ![The output area with three triangles.](images/triangles-coords.png)

--- /collapse ---

The stand will have corners at (150, 350), (200, 150), and (250, 350).

--- code ---
---
language: python
filename: main.py - draw()
line_numbers: true
line_number_start: 31
line_highlights: 34-36
---
  fill(GREEN)
  rect(0, 250, 400, 150) # x, y, width, height
  
  # Draw a target
  fill(BROWN) # Set the fill colour to brown
  triangle(150, 350, 200, 150, 250, 350)


--- /code ---

**Tip:** We have added comments to our code like `# Set the fill colour to brown` to tell you what it does. You don't need to add these comments to your code but you can do to help you remember why it's there.

--- save ---

--- /task ---

--- task ---

**Test:** Run your code to see the stand for your target. 

![A brown triangle against a blue sky on green grass.](images/target-stand.png)

--- /task ---

--- task ---

The largest part of the target will be a `GREY` **circle** using `ellipse(x, y, width, height)`.  An ellipse is a shape with a single side and no corners. It can be squashed, like an oval, or perfecly round, like a circle. The **x** and **y** coordinates are the centre position of the circle. 

**Tip:** To make a perfect circle the **width** and **height** must be the same. 

--- code ---
---
language: python
filename: main.py - draw()
line_numbers: true
line_number_start: 34
line_highlights: 37-39
---
# Draw a target
  fill(BROWN)
  triangle(150, 350, 200, 150, 250, 350)
  fill(GREY)
  # 200, 200 is the middle of the screen.
  ellipse(200, 200, 170, 170) # Outter circle
  
--- /code ---

--- save ---

--- /task ---

--- task ---

**Test:** Run your code to see the first large grey circle.

![A brown triangle and grey circle against a blue sky on green grass.](images/grey-circle.png)

**Debug:** You might have used a different spelling of 'grey' — this is one of those words that has a different spelling in different parts of the English-speaking world.

--- /task ---

The starter project had colours `GREEN`, `GREY`, `BLUE`, `BROWN`, and `WHITE` defined as global variables. When you make a variable `global` it can be read from anywhere in the project. 

--- task ---

Create two new global variables to store colours `RED` and `YELLOW` for the remaining circles:

 + Add the `RED` and `YELLOW` variables to the line that makes the variables global (don't forget the commas!)
 + Assign colours to the `RED` and `YELLOW` variables using `color()`

The `color()` function expects three numbers: one each for red, green, and blue.

[[[generic-theory-simple-colours]]]

--- code ---
---
language: python
filename: main.py - draw()
line_numbers: true
line_number_start: 17
line_highlights: 20, 27-28
---
def draw():
  # Things to do in every frame
  
  global GREEN, GREY, BLUE, BROWN, WHITE, RED, YELLOW
  
  GREEN = color(149, 212, 122)
  GREY = color(236, 236, 236) # The outter circle
  BLUE = color(92, 204, 206)
  BROWN = color(145, 96, 51)
  WHITE = color(255,255,255)
  RED = color(255, 0, 0) # The inner circle
  YELLOW = color(252, 249, 0) # The bullseye

--- /code ---

--- /task ---

--- task ---

The target will be made of up a number of circles with different sizes but the same centre coordinates. 

Add two more circles to represent an inner circle and the bullseye. Change the `fill()` before drawing each circle. 

--- code ---
---
language: python
filename: main.py - draw()
line_numbers: true
line_number_start: 36
line_highlights: 42-45
---
  # Draw a target
  fill(BROWN) # Set the fill colour to brown
  triangle(150, 350, 200, 150, 250, 350)
  fill(GREY)
  # 200, 200 is the middle of the screen.
  ellipse(200, 200, 170, 170) # Outter circle
  fill(RED)
  ellipse(200, 200, 110, 110) # Inner circle
  fill(YELLOW)
  ellipse(200, 200, 30, 30) # Bullseye
--- /code ---

--- save ---

--- /task ---

--- task ---

**Test:** Run your project again to see the target with three colour circles.

![A brown triangle with three coloured circles against a blue sky on green grass.](images/three-circles.png)

**Debug:** You might have used 'colo**u**r' instead of 'color'. Just like with 'gr**e**y' and 'gr**a**y', these words have diffrent spellings in different places. The makers of Python use the 'color' spelling, so you have to use it too!

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
In Japan, the Samurai introduced a requirement for learning archery. The Japanese martial art of archery is known as <span style="color: #0faeb0; font-weight: bold;">Kyūdō</span> and the bullseye is called <span style="color: #0faeb0; font-weight: bold;">zuboshi</span>. The term zuboshi is also used in English; to show that someone has done or said something that is "exactly right."
</p>

--- task ---

You set `no_stroke()` when drawing your background, so all of the shapes after that have been drawn without a **stroke** outline too.

A `WHITE` variable has been created for you. The RGB colour values for white are (255, 255, 255) this is the maximum amount of each colour. What do you think the values for black are?

Set the colour of the `stroke()` to `WHITE` for the circles. To control the thinkness of the outline, add `stroke_weight()` and set this to `3`. 

--- code ---
---
language: python
filename: main.py - draw()
line_numbers: true
line_number_start: 36
line_highlights: 39–40
---
  # Draw a target
  fill(BROWN) # Set the fill colour to wood
  triangle(150, 350, 200, 150, 250, 350)
  stroke(WHITE) # A white outline
  stroke_weight(3) # A thick outline
  fill(GREY)
--- /code ---

--- save ---

--- /task ---

--- task ---

**Test:** Run your project to see the outline around the circles in your target. 

![A brown triangle with three coloured circles, each ringed in white, against a blue sky on green grass.](images/outline-circles.png)

--- /task ---
