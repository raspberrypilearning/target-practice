## Draw the grass

--- task ---

Open the [Target practice starter](https://editor.raspberrypi.org/en/projects/target-practice-starter){:target="_blank"} project.

--- /task ---


--- task ---

**Add** code to draw a green rectangle at the bottom of the screen to represent the grass.

![The output area with a sky-coloured rectangle above a grass-coloured rectangle to create the background. The top left corner of the rectangle is marked as x=0, y=250 this is the origin of the rectangle. The width is highlighted as 400 and the height as 150. The code rect(0, 250, 400, 150) is shown.](images/green-grass.png){:width="400px"}

--- code ---
---
language: python line_numbers: true line_number_start: 17
line_highlights: 21-22
---
def draw(): # Things to do in every frame fill('cyan')  
rect(0, 0, 400, 250)  
fill('lightgreen')  
rect(0, 250, 400, 150) --- /code ---

--- /task ---

--- task ---

**Test:** Run your project to view the background.

![The output area with a sky-coloured rectangle above a grass-coloured rectangle to create the background.](images/background.png){:width="400px"}

--- /task ---

--- save ---
