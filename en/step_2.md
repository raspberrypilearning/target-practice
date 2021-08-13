## Create a background
<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
In this step you will create the background for your game.
</div>
<div>
![The output area with sky coloured rectangle above a grass coloured rectangle to create the background.](images/background.png){:width="300px"}
</div>
</div>

--- task ---

Open the [Python archery starter](https://trinket.io/python/bbcc44911d){:target="_blank"} project. Click on the remix button.

--- save ---

--- /task ---

The first step in making your game is to draw the sky and grass background. The starter already contains some colours you can use to do this.

--- task ---

Inside your `draw()` function, add code to set the `fill()` colour to `BLUE`:

--- code ---
---
language: python
filename: main.py — draw()
line_numbers: true
line_number_start: 17
line_highlights: 28-30
---
def draw():
  # Things to do in every frame
  
  global GREEN, GREY, BLUE, BROWN, WHITE
  
  GREEN = color(149, 212, 122)
  GREY = color(236, 236, 236)
  BLUE = color(92, 204, 206)
  BROWN = color(145, 96, 51)
  WHITE = color(255,255,255)
  
  fill(BLUE)


--- /code ---

**Tip:** When Python programmers won't be changing the value of a variable as the program is running, they name it with UPPERCASE LETTERS.

--- /task ---

--- task ---

Now, draw rectangle by calling the `rect(x_coordinate, y_coordinate, width, height)` function after your `fill()` code.

The rectangle will start in the top-left corner of the screen at coordinates (0,0): 
+ The **x_coordinate** controls the horizontal position 
+ The **y_coordinate** controls the vertical postion 

The rectangle will have a width of `400` and a height of `250`.

![A blue rectangle with a coordinates grid showing the position of the sky rectangle starting in the top corner, above a grey rectangle.](images/sky_coords.png)

--- code ---
---
language: python
filename: main.py — draw()
line_numbers: true
line_number_start: 17 
line_highlights: 29
---
def draw():
  # Things to do in every frame
  
  global GREEN, GREY, BLUE, BROWN, WHITE
  
  GREEN = color(149, 212, 122)
  GREY = color(236, 236, 236)
  BLUE = color(92, 204, 206)
  BROWN = color(145, 96, 51)
  WHITE = color(255,255,255)
  
  fill(BLUE)
  rect(0, 0, 400, 250) # x, y, width, height


--- /code ---

**Tip:** Shapes will always be drawn with the fill colour set the last time `fill()` was called.

--- save ---

--- /task ---

--- task ---

**Test:** Run your code to see the sky you've drawn.

![A blue rectangle with a black border around it, above a grey rectangle.](images/sky_stroke.png){:width="300px"}

That's a bit strange, there's a black line around your sky! This is because, when the program starts, it automatically sets a black border — called a **stroke** — around everything it draws.

--- /task ---

--- task ---

Turn off the stroke by adding `no_stroke()` before you start drawing the sky.

--- code ---
---
language: python
filename: main.py — draw()
line_numbers: true
line_number_start: 26
line_highlights: 28
---
  WHITE = color(255,255,255)

  no_stroke()
  fill(BLUE)
  rect(0, 0, 400, 250) # x, y, width, height


--- /code ---

--- save ---

--- /task ---

--- task ---

**Test:** Run your project again to check that the stroke has gone.

--- /task ---

--- task ---

Now, change the `fill()` colour to `GREEN` and add another `rect(x, y, width, height)`. 

This rectangle needs to be positioned below the sky at coordinates (0, 250), so that it starts in the lower part of the screen.

--- code ---
---
language: python
filename: main.py — draw()
line_numbers: true
line_number_start: 26
line_highlights: 31-32
---
  WHITE = color(255,255,255)
  
  no_stroke()
  fill(BLUE)
  rect(0, 0, 400, 250) # x, y, width, height
  fill(GREEN)
  rect(0, 250, 400, 150)


--- /code ---

--- save ---

--- /task ---

--- task ---

**Test:** Run your project again to view the finished background.

--- /task ---
