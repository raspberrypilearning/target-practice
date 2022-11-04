## Create a background

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Your game needs a colourful background.
</div>
<div>

![The output area with a sky-coloured rectangle above a grass-coloured rectangle to create the background.](images/background.png){:width="300px"}

</div>
</div>

--- task ---

Open the [Target practice starter](https://trinket.io/python/9973649e5c){:target="_blank"} project. 

If you have a Trinket account, you can click on the **Remix** button to save a copy to your **My Trinkets** library.

--- /task ---

--- task ---

The starter project has some code already written for you. 

Click **'Run'** to see a blue filled rectangle drawn from x=`0`, y=`0` (the top of the screen). This `400` x `250` pixels rectangle is the sky. 

![A blue rectangle with a black border around it, above a grey rectangle.](images/sky_stroke.png){:width="300px"}

**Tip:** Coordinates start from (x=0, y=0) in the top left corner. This might be different to other coordinate systems you have used. 

--- /task ---



--- task ---

The sky has been drawn with a black border (stroke). 

To turn the stroke off for all shapes add `no_stroke()` to the `setup` function:

--- code ---
---
language: python
filename: main.py — setup()
line_numbers: true
line_number_start: 11
line_highlights: 15
---
def setup():
# Setup your game here
  size(400, 400) # width and height of screen
  frame_rate(2)
  no_stroke()

--- /code ---

--- /task ---

--- task ---

**Run** your code again and notice 👀 that the border (stroke) has now disappeared. 

--- /task ---

### Draw the grass

--- task ---

**Add** code to draw a green rectangle at the bottom of the screen.

![The output area with a sky-coloured rectangle above a grass-coloured rectangle to create the background.](images/background.png)

--- code ---
---
language: python
filename: main.py — draw()
line_numbers: true
line_number_start: 24
line_highlights: 33, 34
---
def draw():
# Things to do in every frame
  sky = color(92, 204, 206) # Red = 92, Green = 204, Blue = 206
  grass = color(149, 212, 122)
  wood = color(145, 96, 51)
  outer = color(0, 120, 180) 

  fill(sky)     
  rect(0, 0, 400, 250)     
  fill(grass) # Set the fill color to grass
  rect(0, 250, 400, 150) # x, y, width, height     

--- /code ---

**Tip:** We have added comments to our code, like `# Set the stand fill colour to brown`, to tell you what it does. You don't need to add these comments to your code, but they can be helpful to remind you what lines of code do.

--- /task ---

--- collapse ---
---
title: How does the `rectangle` function work?
---

The `rectangle` function call takes **four** numbers (arguments). 

`rect(0, 0, 400, 250)` will draw a rectangle that starts in the **top left** corner at `(0, 0)` and is `400` pixels wide and `250` pixels tall. 

+ The first two numbers are `0, 0` and refer to the `x` and `y` coordinates of the **top left** corner of the rectangle
+ `400` refers to the width (w) of the rectangle
+ `250` refers to the height (h) of the rectangle

![A diagram demonstrating what the four numbers in the rectangle function call mean. Part one focuses on the first number, which is 0. 0 refers to the x value and is located in the top left corner of the screen. Part two focuses on the second number, which is 0. This 0 refers to the y value and is also located in the top left corner. Part three focuses on the third number, which is 400. 400 refers to the width of the rectangle. The fourth part refers to the fourth number, which is 250. 250 refers to the height of the rectangle.](images/rectangle-diagram.png)

--- /collapse ---

--- task ---

**Test:** Run your project again to view the finished background. 

--- /task ---

