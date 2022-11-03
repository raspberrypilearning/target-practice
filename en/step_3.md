## Draw your target

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Your game needs a target to shoot arrows at.
</div>
<div>

![The output area with the target and stand.](images/three-circles.png){:width="300px"}

</div>
</div>

### Draw the stand

The triangular wooden stand is partly behind the target circles so it must be drawn first. 

--- task ---

Draw a brown `triangle()` with corners at coordinates (150, 350), (200, 150), and (250, 350).

![A brown triangle on grass and against a sky with the coordinate points labelled.](images/stand_coords.png)

--- code ---
---
language: python
filename: main.py - draw()
line_numbers: true
line_number_start: 26
line_highlights: 28-29
---
  fill(grass)   
  rect(0, 250, 400, 150) # x, y, width, height
  fill(wood) # Set the stand fill colour to brown     
  triangle(150, 350, 200, 150, 250, 350)

--- /code ---

--- /task ---

--- task ---

**Test:** Run your code to see the stand for your target. 

![A brown triangle on grass and against a sky.](images/target-stand.png)

--- /task ---

### Draw the target circles

The target circles will cover the brown triangle where they overlap, because they are drawn later. 

--- task ---

The largest part of the target will be a blue **circle** made by using the `ellipse()` function.

An ellipse is a shape with a single side and no corners. It can be squashed, like an oval, or perfecly round, like a circle. 

An ellipse needs `x` and `y` coordinates, width, and height. The `x` and `y` coordinates of an ellipse are the centre position. 

**Tip:** To make a circle, the **width** and **height** must be the same. 

--- code ---
---
language: python
filename: main.py - draw()
line_numbers: true
line_number_start: 28
line_highlights: 30-31
---

  fill(wood)   
  triangle(150, 350, 200, 150, 250, 350)   
  fill(outer)    
  ellipse(200, 200, 170, 170) # Outer circle. 200, 200 is the middle of the screen
  
--- /code ---

--- /task ---

--- task ---

**Test:** Run your code to see the first large blue circle.

![A brown triangle and blue circle on grass and against a sky.](images/blue-circle.png)

--- /task ---

--- task ---

Create two new variables called `inner` and `bullseye` to store colours for the remaining circles. 

The `color()` function expects three numbers: one each for red, green, and blue.

We used numbers that give traditional archery target colours, but you can use whatever colours you like as long as they are different from each other.

[[[generic-theory-simple-colours]]]

--- code ---
---
language: python
filename: main.py - draw()
line_numbers: true
line_number_start: 17
line_highlights: 23-24
---
def draw():   
  # Things to do in every frame
  sky = color(92, 204, 206)   
  grass = color(149, 212, 122)   
  wood = color(145, 96, 51)   
  outer = color(0, 120, 180) # Blue    
  inner = color(210, 60, 60) # Red    
  bullseye = color(220, 200, 0) # Yellow    

--- /code ---

--- /task ---

--- task ---

The target is made of different-sized circles with the same centre coordinates (200, 200) — the middle of the screen. 

Add two more circles to represent an inner circle and the bullseye. Change the `fill()` before drawing each circle. 

--- code ---
---
language: python
filename: main.py - draw()
line_numbers: true
line_number_start: 30
line_highlights: 34-37
---
  fill(wood)    
  triangle(150, 350, 200, 150, 250, 350) # Stand    
  fill(outer)   
  ellipse(200, 200, 170, 170) # Outer circle   
  fill(inner)   
  ellipse(200, 200, 110, 110) # Inner circle   
  fill(bullseye)   
  ellipse(200, 200, 30, 30) # Bullseye   
  
--- /code ---

--- /task ---

--- task ---

**Test:** Run your project again to see the target with three coloured circles. Change the colours until you are happy with them.

![A brown triangle with three coloured circles on grass and against a sky.](images/three-circles.png)

**Debug:** Python uses the American spelling of 'color' (without a 'u') so make sure you do the same.

--- /task ---

--- save ---

