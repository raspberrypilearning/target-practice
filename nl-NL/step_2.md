## Een achtergrond maken

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Your game needs a colourful background.
</div>
<div>

![Het uitvoergebied met een luchtkleurige rechthoek boven een graskleurige rechthoek om de achtergrond te maken.](images/background.png){:width="300px"}

</div>
</div>

### Open the starter project

--- task ---

Open het [Boogschieten starter](https://trinket.io/python/ed9eefbca2){:target="_blank"} project.

Als je een Trinket-account hebt, kun je op de knop **Remix** klikken om een kopie op te slaan in je `My Trinkets`-bibliotheek.

--- /task ---

### Edit the sky

--- task ---

The starter project has some code already written for you.

Click **'Run'** to see a blue filled rectangle drawn from x=`0`, y=`0` (the top of the screen). This `400` x `250` pixels rectangle is the sky.

![Een blauwe rechthoek met een zwarte rand eromheen, daarboven een grijze rechthoek. The top left corner of the canvas is marked as x=0, y=0 this is the origin of the rectangle. The width is highlighted as 400 and the height as 250. The code rect(0, 0, 400, 250) is shown.](images/sky_stroke.png){:width="300px"}

**Tip:** 💡 Coordinates start from (x=0, y=0) in the top left corner. This might be different to other coordinate systems you have used.

--- /task ---

--- task ---

The sky has been drawn with a black border (stroke).

To turn the stroke off for all shapes add `no_stroke()` to the `setup` function:

--- code ---
---
language: python filename: main.py — draw() line_numbers: true line_number_start: 23
line_highlights: 25
---
def setup():
# Setup your game here
  size(400, 400) # width and height of screen frame_rate(2) no_stroke()

--- /code ---

--- /task ---

--- task ---

**Test:** Voer je project opnieuw uit om te controleren of de lijn is verdwenen.

--- /task ---

### Draw the grass

--- task ---

**Add** code to draw a green rectangle at the bottom of the screen.

![The output area with a sky-coloured rectangle above a grass-coloured rectangle to create the background. The top left corner of the rectangle is marked as x=0, y=250 this is the origin of the rectangle. The width is highlighted as 400 and the height as 150. The code rect(0, 250, 400, 150) is shown.](images/green-grass.png)no_stroke()   
fill(lucht)   
rect(0, 0, 400, 250) #x, y, breedte, hoogte

--- code ---
---
language: python filename: main.py — draw() line_numbers: true line_number_start: 18
line_highlights: 26
---
def draw():
# Things to do in every frame
  global wood sky = color(92, 204, 206) # Red = 92, Green = 204, Blue = 206 grass = color(149, 212, 122) wood = color(145, 96, 51) outer = color(0, 120, 180)

  no_stroke()     
fill(lucht)     
rect(0, 0, 400, 250) #x, y, breedte, hoogte    
fill(gras)    
rect(0, 250, 400, 150)

--- /code ---

**Test:** Voer je code uit om de lucht te zien die je hebt getekend. You don't need to add these comments to your code, but they can be helpful to remind you what lines of code do.

--- /task ---

--- task ---

**Test:** Voer je project opnieuw uit om de voltooide achtergrond te bekijken.

![De lucht en het gras worden gemaakt door code te schrijven om gekleurde rechthoeken te tekenen.](images/background.png)De `size()` functie in `setup()` stelt de schermgrootte in op 400 pixels bij 400 pixels.

--- /task ---

