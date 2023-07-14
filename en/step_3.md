## Draw your target

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Your game needs a target to shoot arrows at.
</div>
<div>

![The output area with the target and stand.](images/three-circles.png){:width="300px"}

</div>
</div>

### Draw a triangular stand

--- task ---

Set the fill colour to `sienna` (brown). 

Draw a triangle using the x and y coordinates for each of the corners.

![A brown triangle on grass and against a sky with the coordinate points labelled at 150, 350 and 200, 150 and 250, 350). The corners of the canvas are also labelled as x=0, y=0 in the top left and x=400, y=400 in the bottom right.](images/stand_coords.png){:width="400px"}

--- code ---
---
language: python
filename: main.py - draw()
line_numbers: true
line_number_start: 18
line_highlights: 20, 21
---
    fill('lightgreen')  # Set the fill colour for the grass to light green
    rect(0, 250, 400, 150)  # Draw a rectangle for the grass with these values for x, y, width, height
    fill('sienna')  # Brown colour
    triangle(150, 350, 200, 150, 250, 350)  # Draw a triangle for the target's stand

--- /code ---

--- /task ---

--- task ---

**Test:** 🔄 Run your code to see the stand for your target: 

![A brown triangle on grass and against a sky.](images/target-stand.png){:width="400px"}

--- /task ---

### Draw the target circles

--- task ---

The largest part of the target is a blue **circle**.

Set the fill colour to `blue`. 

Draw a circle with x and y coordinates for its centre and a width. 

![A brown triangle and blue circle on grass and against a sky. The circle is labelled with the coordinates x=200, y=200 as the centre and circle width of 170.](images/circle-coords.png){:width="400px"}

--- code ---
---
language: python
filename: main.py - draw()
line_numbers: true
line_number_start: 20
line_highlights: 22, 23
---

    fill('sienna')  # Brown colour
    triangle(150, 350, 200, 150, 250, 350)  # Draw a triangle for the target's stand 
    fill('blue')  # Set the circle fill colour to blue
    circle(200, 200, 170)  # Draw the outer circle
  
--- /code ---

--- /task ---

--- task ---

**Test:** Run your code to see the first large blue circle. 

The blue circle was drawn after the stand so it is in front.

![A brown triangle and blue circle on grass and against a sky.](images/blue-circle.png){:width="400px"}

--- /task ---

The target is made of different-sized circles with the same centre coordinates (200, 200). 

--- task ---

**Add** coloured circles for the inner and middle parts of the target. 

--- code ---
---
language: python
filename: main.py - draw()
line_numbers: true
line_number_start: 20
line_highlights: 24, 25
---

    fill('sienna')  # Brown colour
    triangle(150, 350, 200, 150, 250, 350)  # Draw a triangle for the target's stand 
    fill('blue')  # Set the circle fill colour to blue
    circle(200, 200, 170)  # Draw the outer circle
    fill('red')  # Set the colour for the circle fill to red
    circle(200, 200, 110)  # Draw the inner circle using x, y, width
    fill('yellow')  # Set the colour for the circle fill to yellow      
    circle(200, 200, 30)  # Draw the middle circle using x, y, width

--- /code ---

--- /task ---

--- task ---

**Test:** 🔄 Run your project to see the target with three coloured circles. 

![A brown triangle with three coloured circles on grass and against a sky.](images/three-circles.png){:width="400px"}

--- /task ---

--- task ---

**Choose:** 💭 Change any of the colours using a different colour name. You can find a list of all of the available colour names on [W3 Schools](https://www.w3schools.com/colors/colors_names.asp){:target="blank"}. 

![A brown triangle with three coloured circles on grass and against a sky. The colours have changed to pinks and purples.](images/alternative-colours.png){:width="400px"}

--- collapse ---
---
title: Example code using different colours
---

--- code ---
---
language: python
filename: main.py - draw()
line_numbers: false
line_number_start: 14
line_highlights: 
---
    
def draw():
# Things to do in every frame
    fill('BlueViolet')
    rect(0, 0, 400, 250)  # Sky
    fill('DeepSkyBlue')
    rect(0, 250, 400, 150)  # Ground
    fill('FireBrick')
    triangle(150, 350, 200, 150, 250, 350)  # Stand
    fill('LemonChiffon')
    circle(200, 200, 170)  # Outer circle
    fill('DeepPink')
    circle(200, 200, 110)  # Inner circle
    fill('BlueViolet')
    circle(200, 200, 30)  # Middle circle
  
--- /code ---

--- /collapse ---

--- /task ---

--- save ---