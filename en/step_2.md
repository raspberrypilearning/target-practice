## Create a background

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
The sky and grass are made by writing code to draw coloured rectangles.
</div>
<div>
![The output area with a sky-coloured rectangle above a grass-coloured rectangle to create the background.](images/background.png){:width="300px"}
</div>
</div>

--- task ---
Open the [Archery starter](https://trinket.io/python/bbcc44911d){:target="_blank"} project. 

If you have a Trinket account, you can click on the **Remix** button to save a copy to your `My Trinkets` library.

--- /task ---

The starter project has some code already written for you to import the `p5` library, you will use this library to build your archery game. 

[[[p5-processing-library]]]

--- task ---

The `fill()` function sets the inside colour of shapes. The starter project already contains some RGB colours you can use to do this. 

Find your `draw()` function and prepare to draw the sky by adding indented code to set the `fill()` colour to `sky`:

--- code ---
---
language: python
filename: main.py — draw()
line_numbers: true
line_number_start: 17
line_highlights: 26
---
def draw():
  # Things to do in every frame
  sky = color(92, 204, 206) #Red = 92, Green = 204, Blue = 206
  grass = color(149, 212, 122)
  wood = color(145, 96, 51)
  outer = color(0, 120, 180) #Equal amounts of all colours
  
  fill(sky)

--- /code ---

--- /task ---

The `size()` function call in `setup()` sets the screen size to 400 pixels by 400 pixels.

[[[p5-coordinates.]]]

--- task ---

After your `fill()` code, draw a `rect()` for the sky with top-left coordinates (`0`,`0`), a width of `400` to match the width of the screen and a height of `250`.

![A blue rectangle with a coordinates grid showing the position of the sky rectangle starting in the top corner, above a grey rectangle.](images/sky_coords.png)

--- code ---
---
language: python
filename: main.py — draw()
line_numbers: true
line_number_start: 26 
line_highlights: 27
---
  fill(sky)
  rect(0, 0, 400, 250) #Start x, start y, width, height

--- /code ---

--- /task ---

--- task ---

**Test:** Run your code to see the sky you've drawn. Remember that with the `p5` library, the `run()` function calls the `setup()` function once, then the `draw()` function repeatedly.  

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
  outer = color(0, 120, 180) #Equal amounts of all colours

  no_stroke()   
  fill(sky)   
  rect(0, 0, 400, 250) #x, y, width, height

--- /code ---

--- /task ---

--- task ---

**Test:** Run your project again to check that the stroke has gone.

--- /task ---

--- task ---

`fill()` changes the fill colour for all shapes drawn until `fill()` is called again with a new colour.

Change the `fill()` colour to `grass` and add another `rect(x, y, width, height)`. 

This rectangle needs to be positioned below the sky at coordinates (0, 250), so that it starts in the lower part of the screen.

--- code ---
---
language: python
filename: main.py — draw()
line_numbers: true
line_number_start: 26
line_highlights: 31-32
---
  outer = color(0, 120, 180) #Equal amounts of all colours
  
  no_stroke()
  fill(sky)
  rect(0, 0, 400, 250) #x, y, width, height
  fill(grass)
  rect(0, 250, 400, 150)

--- /code ---

--- /task ---

--- task ---

**Test:** Run your project again to view the finished background.

--- /task ---

--- save ---
