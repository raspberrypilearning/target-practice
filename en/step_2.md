## Set up your screen

- Acknowldge global variables, mention coordinates, colour theory

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
In this step you will create the background for your game.
</div>
<div>
Image, gif or video showing what they will achieve by the end of the step. ![](images/image.png){:width="300px"}
</div>
</div>

<mark>define SKY_BLUE constant, Draw sky and run(), color theory (collapse), coordinates (collapse) for rect</mark>

--- task ---

Open the [Python archery starter](https://trinket.io/python/bbcc44911d) project. Remix it.

[[[working-offline]]]

--- save ---

--- /task ---

The first step in making your game is to draw the sky and grass backdrop. The starter already contains some colours you can use to do this.

--- task ---

Inside your `draw` function, set the colour you want to fill the sky with to `SKY_BLUE` by using the `fill` function:

--- code ---
---
language: python
filename: main.py — draw
line_numbers: true
line_number_start: 14 
line_highlights: 25-26
---
def draw():
  # Things to do in every frame
  
  global BLACK, GRASS_GREEN, GREY, SKY_BLUE, WHITE, WOOD_BROWN
  
  BLACK = color(0, 0, 0)
  GRASS_GREEN = color(149, 212, 122)
  GREY = color(236, 236, 236)
  SKY_BLUE = color(92, 204, 206)
  WHITE = color(255, 255, 255)
  WOOD_BROWN = color(145, 96, 51)

  fill(SKY_BLUE)


--- /code ---

**Tip:** Shapes will always be drawn with the fill colour set the last time `fill` was called, even if that was in another function. This can sometimes be the cause of bugs!

--- /task ---

--- task ---

Now, draw a sky blue rectangle by calling the `rect` function after your fill

[[[processing-python-rect]]]

--- code ---
---
language: python
filename: main.py — draw
line_numbers: true
line_number_start: 14 
line_highlights: 27
---
def draw():
  # Things to do in every frame
  
  global BLACK, GRASS_GREEN, GREY, SKY_BLUE, WHITE, WOOD_BROWN
  
  BLACK = color(0, 0, 0)
  GRASS_GREEN = color(149, 212, 122)
  GREY = color(236, 236, 236)
  SKY_BLUE = color(92, 204, 206)
  WHITE = color(255, 255, 255)
  WOOD_BROWN = color(145, 96, 51)

  fill(SKY_BLUE)
  rect(0, 0, 400, 250)


--- /code ---

--- save ---

**Test:** Run your code to see the sky you've drawn.

--- /task ---

That's a bit strange, there's a black line around your sky! This is because, when the program starts, it automatically sets a black border — called a **stroke** — around everything it draws.

--- task ---

Turn off the stroke by adding `no_stroke()` before you start drawing the sky. This function will turn off any stroke that may be active.

--- code ---
---
language: python
filename: main.py — draw
line_numbers: true
line_number_start: 14 
line_highlights: 25-26
---
def draw():
  # Things to do in every frame
  
  global BLACK, GRASS_GREEN, GREY, SKY_BLUE, WHITE, WOOD_BROWN
  
  BLACK = color(0, 0, 0)
  GRASS_GREEN = color(149, 212, 122)
  GREY = color(236, 236, 236)
  SKY_BLUE = color(92, 204, 206)
  WHITE = color(255, 255, 255)
  WOOD_BROWN = color(145, 96, 51)

  no_stroke()
  fill(SKY_BLUE)
  rect(0, 0, 400, 250)


--- /code ---

--- save ---

**Test:** Check that the stroke is now gone.

--- /task ---

--- task ---

Now add a `rect` in `GRASS_GREEN` below the sky, to be the grass.

--- code ---
---
language: python
filename: main.py — draw
line_numbers: true
line_number_start: 14 
line_highlights: 29-30
---
def draw():
  # Things to do in every frame
  
  global BLACK, GRASS_GREEN, GREY, SKY_BLUE, WHITE, WOOD_BROWN
  
  BLACK = color(0, 0, 0)
  GRASS_GREEN = color(149, 212, 122)
  GREY = color(236, 236, 236)
  SKY_BLUE = color(92, 204, 206)
  WHITE = color(255, 255, 255)
  WOOD_BROWN = color(145, 96, 51)

  no_stroke()
  fill(SKY_BLUE)
  rect(0, 0, 400, 250)
  fill(GRASS_GREEN)
  rect(0, 250, 400, 400)


--- /code ---

--- save ---

**Test:** View your finished background

--- /task ---