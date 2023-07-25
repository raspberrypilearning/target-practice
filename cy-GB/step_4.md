## Saethu

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Nawr mae'n amser ychwanegu saeth sy'n symud ar hap ar draws yr ardal targed. 
</div>
<div>

![Y targed, gyda chylch brown, y saeth, yn ymddangos mewn amrywiaeth o safleoedd.](images/fire_arrow.gif){:width="300px"}

</div>
</div>

### Cael y lliw mae'r saeth yn ei daro

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;"> Computers create the effect of movement by showing lots of images one after another. Each image is called a <span style="color: #0faeb0; font-weight: bold;"> frame </span>.   
</p>

--- task ---

Ychwanegwch `ellipse()` bach yng nghanol y sgrin i gynrychioli'r saeth.

Add code to randomly draw a brown circle within a target area:

![A rectangle showing the target area coordinates in a semi transparent rectangle. The target area is between x=100 and y=100 to x=300 and y=300 so covers the whole target and wider.](images/target_area.png)

--- code ---
---
language: python filename: main.py — shoot_arrow() line_numbers: true line_number_start: 7
line_highlights: 11-12
---
# Mae'r swyddogaeth saethu_saeth yn mynd fan hyn
def shoot_arrow():   
arrow_x = randint(100, 300)  # Store a random number between 100 and 300    
arrow_y = randint(100, 300)  # Store a random number between 100 and 300    
fill('sienna')  # Set the arrow to fill colour to brown   
circle(arrow_x, arrow_y, 15)  # Draw a small circle at random coordinates

--- /code ---

--- /task ---

--- task ---

language: python filename: main.py — draw() line_numbers: true line_number_start: 41

--- code ---
---
fill(pren)   
saethu_saeth()
line_highlights: 44-45
---

    fill('yellow')  # Set the colour for the circle fill to yellow      
    circle(200, 200, 30)  # Draw the middle circle using x, y, width
    shoot_arrow()

--- /code ---

--- /task ---

--- task ---

**Profi:** Rhedwch eich cod a gweld y saeth yn ymddangos yng nghanol y nod.

![Y targed ar gefndir gyda chylch brown, y saeth, arno.](images/fire_arrow.gif)

The background and target will be drawn over the old arrow. This means you only see one arrow at a time.

--- /task ---

### Get the colour hit by the arrow

Mae'r llinell `frame_rate(2)` yn `setup()` yn gosod y gyfradd fframiau ar 2 ffrâm yr eiliad.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
A <span style="color: #0faeb0; font-weight: bold;">pixel</span>, short for picture element, is a single coloured dot within an image. Images are made up of lots of coloured pixels.
</p>

--- task ---

Add a **global variable** called `hit_colour` that can be used throughout your code.

Add code to `get` the colour of the pixel at the centre of the arrow and store it in the `hit_colour` variable. In order to compare the colours, we need to use the hexadecimal code this can be done with the `.hex` string.

--- code ---
---
language: python filename: main.py line_numbers: true
line_number_start: 3
---
# Import library code
from p5 import *    
from math import *    
from random import randint

--- /code ---

**Tip:** 💡 The code to `get` the colour needs to be **before** the code to draw the `circle` otherwise you will always save the wood colour of the arrow!

--- /task ---

### Print the colour when the mouse is pressed

The `p5` library 'listens' for certain events, one of these is the press of the mouse button. When it detects that the button has been pressed, it will run whatever code it has been given in the `mouse_pressed` function.

--- task ---

Newidiwch eich `ellipse()` i ddefnyddio'r newidynnau newidd i leoli eich saeth.

Add code to print the target emoji 🎯 when the mouse is clicked.

--- code ---
---
language: python filename: main.py — saethu_saeth() line_numbers: true line_number_start: 10
line_highlights: 12-14
---

# Mae'r swyddogaeth saethu_saeth yn mynd fan hyn
def saethu_saeth():    
saeth_x = randint(100, 300)   
saeth_y = randint(100, 300)    
ellipse(saeth_x, saeth_y, 15, 15) #Diweddaru i gyfesurynnau ar hap

--- /code ---

--- /task ---

--- task ---

Ystyr <span style="color: #0faeb0; font-weight: bold;">picsel</span>, sy'n deillio o 'picture element' yn Saesneg, yw un dot lliw mewn delwedd. Mae delweddau wedi'u ffurfio o lawer o bicselau lliw.

The project prints 🎯 each time the arrow is redrawn.

![An animation of target with a brown circle arrow appearing in a variety of positions.](images/fire_arrow.gif)

Ychwanegwch god i storio'r `lliw_taro`. Defnyddiwch y swyddogaeth `get()` i gael lliw'r picsel yn y cyfesurynnau `saeth_x` a `saeth_y` — canol y saeth.

**Debug:** 🐞 Check the `print` line really carefully for commas and brackets.

--- /task ---

--- save ---
