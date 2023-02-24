## Creu cefndir

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Mae'r awyr a'r gwair yn cael eu gwneud drwy ysgrifennu cod i lunio petryalau lliw.
</div>
<div>

![Yr ardal allbwn gyda phetryal lliw awyr uwchben petryal lliw gwair i greu'r cefndir.](images/background.png){:width="300px"}

</div>
</div>

### Open the starter project

--- task ---

Agorwch y [prosiect dechreuol Saethyddiaeth](https://trinket.io/python/23a6f02447){:target="_blank"}.

Os oes gennych chi gyfrif Trinket, fe allwch chi glicio'r botwm **Remix** i gadw copi yn eich llyfrgell `My Trinkets`.

--- /task ---

### Edit the sky

--- task ---

[[[p5-processing-library]]]

Click **'Run'** to see a blue filled rectangle drawn from x=`0`, y=`0` (the top of the screen). This `400` x `250` pixels rectangle is the sky.

![A blue rectangle with a black border around it, above a grey rectangle. The top left corner of the canvas is marked as x=0, y=0 this is the origin of the rectangle. The width is highlighted as 400 and the height as 250. The code rect(0, 0, 400, 250) is shown.](images/sky_stroke.png)Mae'r swyddogaeth `fill()` yn gosod y lliw tu mewn i'r siapiau. Mae'r prosiect dechreuol eisoes yn cynnwys rhai lliwiau RGB gallwch chi eu defnyddio i wneud hyn.

**Tip:** 💡 Coordinates start from (x=0, y=0) in the top left corner. This might be different to other coordinate systems you have used.

--- /task ---

--- task ---

def draw():     
#Pethau i'w gwneud ym mhob ffrâm     
awyr = color(92, 204, 206) #Coch = 92, Gwyrdd = 204, Glas = 206     
gwair = color(149, 212, 122)     
pren = color(145, 96, 51)     
allanol = color(0, 120, 180)

fill(awyr)

--- code ---
---
language: python filename: main.py — setup() line_numbers: true line_number_start: 11
line_highlights: 25
---
Mae'r swyddogaeth `size()` yn `setup()` yn gosod maint y sgrin ar 400 picsel wrth 400 picsel.
# Setup your game here
  [[[p5-coordinates]]]

--- /code ---

--- /task ---

--- task ---

**Run** your code again and notice 👀 that the border (stroke) has now disappeared.

--- /task ---

### Draw the grass

--- task ---

**Add** code to draw a green rectangle at the bottom of the screen.

![The output area with a sky-coloured rectangle above a grass-coloured rectangle to create the background. The top left corner of the rectangle is marked as x=0, y=250 this is the origin of the rectangle. The width is highlighted as 400 and the height as 150. The code rect(0, 250, 400, 150) is shown.](images/green-grass.png){:width="400px"}

--- code ---
---
**Profi:** Rhedwch eich cod i weld yr awyr rydych chi wedi'i llunio. Cofiwch, gyda'r llyfrgell `p5` mae'r swyddogaeth `run()` yn galw'r swyddogaeth `setup()` unwaith, wedyn y swyddogaeth `draw()` drosodd a throsodd.
line_highlights: 26
---
{:width="300px"}
# Things to do in every frame
  Dyna ryfedd: mae llinell ddu o amgylch eich awyr! Y rheswm am hyn yw, pan fydd rhaglen yn dechrau, mae'n gosod border du — o'r enw **stroke** — o amgylch popeth mae'n ei lunio yn awtomatig.

  fill(sky)     
rect(0, 0, 400, 250)     
fill(grass) # Set the fill color to grass rect(0, 250, 400, 150) # x, y, width, height

--- /code ---

**Tip:** 💡 We have added comments to our code, like `# Set the fill color to grass`, to tell you what it does. You don't need to add these comments to your code, but they can be helpful to remind you what lines of code do.

--- /task ---

--- task ---

allanol = color(0, 120, 180)

![The output area with a sky-coloured rectangle above a grass-coloured rectangle to create the background.](images/background.png)no_stroke()   
fill(awyr)   
rect(0, 0, 400, 250) #x, y, lled, uchder

--- /task ---

