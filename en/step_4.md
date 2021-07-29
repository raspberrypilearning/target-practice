## Aim your bow

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
In this step you will create an arrow that moves randomly across the target area.
</div>
<div>
![The target on the background with a brown circle arrow](images/arrow-target.png){:width="300px"}
</div>
</div>

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Archery as a  <span style="color: #0faeb0; font-weight: bold;"> competitive sport </span> dates back to medieval England. Nowadays team and individual Archery events are held at they Olympic Games and Paralympic Games with targets that are 122cm in diameter. The bullseye measures 12.2cm in diameter (about the size of an apple). Archers shoot at the target from a distance of 70m (around 230ft)! </p>

--- task ---

Find the comment **# The shoot_arrow function goes here** and below it add code to define your `shoot_arrow()` function. 

Create two new variables **arrow_x** and **arrow_y** and set them both to `200` (the centre of the screen). Add a small `ellipse()` to represent the arrow.

--- code ---
---
language: python
filename: main.py — shoot_arrow()
line_numbers: true
line_number_start:  
line_highlights: 10-12
---
# The shoot_arrow function goes here
def shoot_arrow():
  arrow_x = 200
  arrow_y = 200
  ellipse(arrow_x, arrow_y, 10, 10)


--- /code ---

--- /task ---

--- task ---

Below the code in `draw()` that creates the target, add code to set the `fill()` to `WOOD` then 

--- code ---
---
language: python
filename: main.py — draw()
line_numbers: true
line_number_start:  
line_highlights: 10-12
---
  fill(YELLOW)
  ellipse(200, 200, 30, 30)
  
  # Arrow
  fill(WOOD)
  shoot_arrow()

--- /code ---

--- save ---

--- /task ---

--- task ---

**Test:** 

--- /task ---

--- task ---

To create random movements for the arrow you can use some code that has already been written and stored in a library. At the top of your code, find the `import` statements and add code to import `randint` from the `random` library. 

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1 
line_highlights: 4
---
# Import library code
from p5 import *
from math import *
from random import randint
--- /code ---

--- /task ---

--- task ---

Go to your `shoot_arrow()` function and amend the `arrow_x` and `arrow_y` values to choose random numbers between `100` and `300`. This will let some shots miss the target, without them going all the way to the edges of your game.

--- code ---
---
language: python
filename: main.py — shoot_arrow()
line_numbers: true
line_number_start:  
line_highlights: 10-12
---
# The shoot_arrow function goes here
def shoot_arrow():
  arrow_x = randint(100, 300)
  arrow_y = randint(100, 300)
  ellipse(arrow_x, arrow_y, 10, 10)

--- /code ---

--- /task ---

--- task ---

Finally, you need to check what colour the arrow has hit. You can do this with the `get()` function, which gets the colour at the x and y coordinates you provide. Store it in a variable called `pixel_colour`.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: main.py — shoot_arrow() 
line_highlights: 10-12
---
# The shoot_arrow function goes here
def shoot_arrow():
  arrow_x = randint(100, 300)
  arrow_y = randint(100, 300)
  ellipse(arrow_x, arrow_y, 10, 10)
  pixel_colour = get(arrow_x, arrow_y)


--- /code ---

--- /task ---

