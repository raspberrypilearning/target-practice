## Fire your arrow

This covering over earlier drawings is how the background is cleared between frames of your animation. In the first animation below the background is not being redrawn, and all of the versions of the circle remain visible. The second animation makes it look like a single, moving, circle by redrawing the background in every frame.

![An animation with a green circle that changes its x-coordinate each time the frame is redrawn. The background is not redrawn so the previous versions of the circle remain on the screen, overlapping each other.](images/animation_no_bg_erase.gif)

![An animation with a green circle that changes its x-coordinate each time the frame is redrawn. The background is redrawn so the previous versions of the circle are erased leaving only the latest version of the circle.](images/animation_bg_erase.gif)

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
In this step you will create an arrow that moves randomly across the target area.
</div>
<div>
![The target, with a brown circle arrow appearing in a variety of positions.](images/fire_arrow.gif){:width="300px"}
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
line_number_start: 9
line_highlights: 10-15
---
# The shoot_arrow function goes here
def shoot_arrow():
  arrow_x = 200
  arrow_y = 200
  ellipse(arrow_x, arrow_y, 15, 15)

--- /code ---

--- /task ---

--- task ---

Go to the `draw()` code that creates the target and add code at the end to set the `fill()` to `BROWN`, turn off the `WHITE` stroke you have set, and then call your new `shoot_arrow()` function. 

--- code ---
---
language: python
filename: main.py — draw()
line_numbers: true
line_number_start: 51
line_highlights: 54-57
---
  fill(YELLOW)
  ellipse(200, 200, 30, 30)
  
  # Arrow
  fill(BROWN)
  no_stroke()
  shoot_arrow()

--- /code ---

--- /task ---

--- task ---

**Test:** Run you code and see the arrow appear in the bullseye.

![The target on the background with a brown circle arrow](images/arrow-middle.png)

--- /task ---

--- task ---

To make the arrow move randomly you can use some code from a library. 

Find the `import` statements, at the top of your code, and from the `random` library import `randint`. 

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 3
line_highlights: 6
---
# Import library code
from p5 import *
from math import *
from random import randint
--- /code ---

--- /task ---

--- task ---

Go to your `shoot_arrow()` function and change the `arrow_x` and `arrow_y` values to choose random numbers between `100` and `300`. 

This will let some shots miss the target, without them going all the way to the edges of your game.

![A rectangle showing the target area coordinattes in a semi transparent rectangle](images/target_area.png)

--- code ---
---
language: python
filename: main.py — shoot_arrow()
line_numbers: true
line_number_start: 10
line_highlights: 12-13
---
# The shoot_arrow function goes here
def shoot_arrow():
  arrow_x = randint(100, 300)
  arrow_y = randint(100, 300)
  ellipse(arrow_x, arrow_y, 15, 15)


--- /code ---

--- /task ---

--- task ---

Finally, create a global variable called `hit_color` to use to check what colour the arrow has hit. 

Add a `get()` function, inside a `color()` function, which gets the colour at the `arrow_x` and `arrow_y` coordinates. 

--- code ---
---
language: python
filename: main.py — shoot_arrow() 
line_numbers: true
line_number_start: 10
line_highlights: 12, 15
---
# The shoot_arrow function goes here
def shoot_arrow():
  global hit_color
  arrow_x = randint(100, 300)
  arrow_y = randint(100, 300)
  hit_color = color(get(arrow_x, arrow_y))
  ellipse(arrow_x, arrow_y, 15, 15)

--- /code ---

**Tip:** The code to get the colour and save it needs to be before the code to draw the ellipse otherwise you will always save the BROWN colour of the arrow! 

--- /task ---

--- task ---

**Test:** Run your project, the arrow is redrawn at random coordinates. 

The project gets the `hit_color` each time the arrow is redrawn — you'll use that value in the next step.

![The target, with a brown circle arrow appearing in a variety of positions.](images/fire_arrow.gif)

--- /task ---

--- save ---

