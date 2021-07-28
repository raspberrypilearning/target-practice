## Create a game world

- Acknowldge global variables, mention coordinates, colour theory

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
In this step you will create the background for your game.
</div>
<div>
![The output area with sky coloured rectangle above a grass coloured rectangle to create the background.](images/background.png){:width="300px"}
</div>
</div>

<mark>define SKY constant, Draw sky and run(), color theory (collapse), coordinates (collapse) for rect</mark>

--- task ---

Open the [Python archery starter](https://trinket.io/python/bbcc44911d) project. Remix it.

--- save ---

--- /task ---

The first step in making your game is to draw the sky and grass backdrop. The starter already contains some colours you can use to do this.

--- task ---

Inside your `draw` function, set the colour you want to fill the sky with to `SKY` by using the `fill` function:

--- code ---
---
language: python
filename: main.py — draw
line_numbers: true
line_number_start: 14 
line_highlights: 24-26
---
def draw():
  # Things to do in every frame
  
  global GRASS, GREY, SKY, WOOD
  
  GRASS = color(149, 212, 122)
  GREY = color(236, 236, 236)
  SKY = color(92, 204, 206)
  WOOD = color(145, 96, 51)

  fill(SKY)


--- /code ---

**Tip:** When Python programmers won't be changing the value of a variable as the program is running, they name it with UPPERCASE LETTERS.

--- /task ---

--- task ---

Now, draw a sky blue rectangle by calling the `rect(x, y, width, height)` function after your `fill` code. 

The sky rectangle will start in the top-left corner of the screen at coordinates (0,0). The sky will have a width of `400` and a height of `250`.  

![A blue rectangle with a coordinates grid showing the position of the sky rectangle starting in the top corner, above a grey rectangle.](images/sky_coords.png)

--- code ---
---
language: python
filename: main.py — draw
line_numbers: true
line_number_start: 14 
line_highlights: 25
---
def draw():
  # Things to do in every frame
  
  global GRASS, GREY, SKY, WOOD
  
  GRASS = color(149, 212, 122)
  GREY = color(236, 236, 236)
  SKY = color(92, 204, 206)
  WOOD = color(145, 96, 51)

  fill(SKY)
  rect(0, 0, 400, 250) # x, y, width, height


--- /code ---

--- save ---

**Test:** Run your code to see the sky you've drawn.

--- /task ---

![A blue rectangle with a black border around it, above a grey rectangle.](images/sky_stroke.png)

That's a bit strange, there's a black line around your sky! This is because, when the program starts, it automatically sets a black border — called a **stroke** — around everything it draws.

--- task ---

Turn off the stroke by adding `no_stroke()` before you start drawing the sky. This function will turn off any stroke that may be active.

--- code ---
---
language: python
filename: main.py — draw
line_numbers: true
line_number_start: 14 
line_highlights: 24
---
def draw():
  # Things to do in every frame
  
  global GRASS, GREY, SKY, WOOD
  
  GRASS = color(149, 212, 122)
  GREY = color(236, 236, 236)
  SKY = color(92, 204, 206)
  WOOD = color(145, 96, 51)

  no_stroke()
  fill(SKY)
  rect(0, 0, 400, 250)


--- /code ---

--- save ---

**Test:** Check that the stroke is now gone.

--- /task ---

--- task ---

Now, change the `fill` colour to `GRASS` and add a `rect(x, y, width, height)`. 

This `rect` needs to be positioned below the sky `rect` at coordinates (0, 250). The first coordinate is the **x coordinate** and controls the horizontal position on the screen. The second coordinate is the **y coordinate** and controls the vertical postion on the screen. 

Set the grass `rect` to start at (0, 250) — so that it starts in the lower part of the screen.

--- code ---
---
language: python
filename: main.py — draw
line_numbers: true
line_number_start: 14 
line_highlights: 27-28
---
def draw():
  # Things to do in every frame
  
  global GRASS, GREY, SKY, WOOD
  
  GRASS = color(149, 212, 122)
  GREY = color(236, 236, 236)
  SKY = color(92, 204, 206)
  WOOD = color(145, 96, 51)

  no_stroke()
  fill(SKY)
  rect(0, 0, 400, 250) # x, y, width, height
  fill(GRASS)
  rect(0, 250, 400, 150) # x, y, width, height


--- /code ---

**Tip:** Shapes will always be drawn with the fill colour set the last time `fill` was called, even if that was in another function. This can sometimes be the cause of bugs!

--- save ---

**Test:** View your finished background

--- /task ---
