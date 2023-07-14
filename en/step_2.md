## Create a background

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Your game needs a colourful background.
</div>
<div>

![The output area with a sky-coloured rectangle above a grass-coloured rectangle to create the background.](images/background.png){:width="300px"}

</div>
</div>

### Open the starter project

--- task ---

Open the [Target practice starter](https://editor.raspberrypi.org/en/projects/target-practice-starter){:target="_blank"} project. The code editor will open in another browser tab.

If you have a Raspberry Pi account, you can click on the **Save** button to save a copy to your **Projects**.

--- /task ---

### Edit the sky

--- task ---

The starter project has some code already written for you. 

Click **'Run'** to see a blue filled rectangle drawn from x=`0`, y=`0` (the top of the screen). This `400` x `250` pixels rectangle is the sky. 

![A blue rectangle with a black border around it, above a grey rectangle. The top left corner of the canvas is marked as x=0, y=0 this is the origin of the rectangle. The width is highlighted as 400 and the height as 250. The code rect(0, 0, 400, 250) is shown.](images/sky_stroke.png){:width="400px"}

**Tip:** 💡 Coordinates start from (x=0, y=0) in the top left corner. This might be different to other coordinate systems you have used. 

--- /task ---

--- task ---

The sky has been drawn with a black border (stroke). 

To turn the stroke off for all shapes add `no_stroke()` to the `setup` function:

--- code ---
---
language: python
filename: main.py — setup()
line_numbers: true
line_number_start: 9
line_highlights: 12
---
def setup():
# Setup your game here
    size(400, 400)  # Width and height of screen
    no_stroke()

--- /code ---

--- /task ---

--- task ---

**Run** your code again and notice 👀 that the border (stroke) has now disappeared.

**Tip:** 💡 You will need to press **Stop** to stop your program, this will make the **Run** button reappear. 

--- /task ---

### Draw the grass

--- task ---

**Add** code to draw a green rectangle at the bottom of the screen.

![The output area with a sky-coloured rectangle above a grass-coloured rectangle to create the background. The top left corner of the rectangle is marked as x=0, y=250 this is the origin of the rectangle. The width is highlighted as 400 and the height as 150. The code rect(0, 250, 400, 150) is shown.](images/green-grass.png){:width="400px"}

--- code ---
---
language: python
filename: main.py — draw()
line_numbers: true
line_number_start: 14
line_highlights: 18-19
---
def draw():
# Things to do in every frame
    fill('cyan')  # Set the fill colour for the sky to cyan
    rect(0, 0, 400, 250)  # Draw a rectangle for the sky with these values for x, y, width, height
    fill('lightgreen')  # Set the fill colour for the grass to light green
    rect(0, 250, 400, 150)  # Draw a rectangle for the grass with these values for x, y, width, height

--- /code ---

**Tip:** 💡 We have added comments to our code, like `# Set the fill colour for the sky to cyan`, to tell you what it does. You don't need to add comments to your code, but they are helpful to remind you what lines of code do.

--- /task ---

--- task ---

**Test:** 🔄 Run your project again to view the finished background. 

![The output area with a sky-coloured rectangle above a grass-coloured rectangle to create the background.](images/background.png){:width="400px"}

--- /task ---

--- save ---