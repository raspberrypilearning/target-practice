## Create a background

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Draw the sky and grass using coloured rectangles. 
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

The `fill` function sets the colour for the inside of a shape.

Go to the `draw` function and set the `fill` colour to `grass` then add another rectangle.

The code for a rectangle is `rect(x, y, width, height)` The grass rectangle will be drawn from x=`0`, y=`250` and be `400` x `150` pixels in size. 

![The output area with a sky-coloured rectangle above a grass-coloured rectangle to create the background.](images/background.png)

--- code ---
---
language: python
filename: main.py — draw()
line_numbers: true
line_number_start: 24
line_highlights: 26-27
---
  fill(sky)     
  rect(0, 0, 400, 250) # x, y, width, height    
  fill(grass)    
  rect(0, 250, 400, 150) # x, y, width, height     

--- /code ---

--- /task ---

--- task ---

**Test:** Run your project again to view the finished background. 

--- /task ---

--- save ---
