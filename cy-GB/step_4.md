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
language: python filename: main.py — shoot_arrow() line_numbers: true line_number_start: 9
line_highlights: 11-12
---
# Mae'r swyddogaeth saethu_saeth yn mynd fan hyn
def shoot_arrow():   
arrow_x = randint(100, 300) # Store a random number between 100 and 300    
arrow_y = randint(100, 300) # Store a random number between 100 and 300    
fill(wood) # Set the arrow to fill colour to wood   
circle(arrow_x, arrow_y, 15) # Draw a small circle at random coordinates

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
  fill(middle)    
circle(200, 200, 30)    
shoot_arrow()

--- /code ---

--- /task ---

--- task ---

**Test:** 🔄 Run you code and see the arrow appear in a random position each frame.

![The target, with a brown circle arrow appearing in a variety of positions.](images/fire_arrow.gif)

The background and target will be drawn over the old arrow. This means you only see one arrow at a time.

--- /task ---

### Get the colour hit by the arrow

Mae'r swyddogaeth `draw()` yn cael ei galw bob ffrâm. Byddwch chi'n llunio'r saeth mewn safle ar hap bob tro mae `draw()` yn cael ei galw.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
A <span style="color: #0faeb0; font-weight: bold;">pixel</span>, short for picture element, is a single coloured dot within an image. Images are made up of lots of coloured pixels.
</p>

--- task ---

Dewch o hyd i'r datganiadau `import` ar frig eich cod. Byddwch chi'n defnyddio `randint` o'r llyfrgell `random`.

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

Add code to print the amounts of red, green, and blue in the pixel the arrow lands on.

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

--- code ---
---
Mae angen i chi storio'r lliw mae'r saeth yn anelu ato cyn llunio saeth ar ei ben.
line_highlights: 14
---
# Mae'r swyddogaeth saethu_saeth yn mynd fan hyn
Ychwanegwch god i storio'r `lliw_taro`. Defnyddiwch y swyddogaeth `get()` i gael lliw'r picsel yn y cyfesurynnau `saeth_x` a `saeth_y` — canol y saeth.

--- /code ---

--- /task ---

--- task ---

**Test:** 🔄 Run your project.

**Cyngor:** Mae angen i'r cod i gael y lliw a'i gadw fod **cyn** y cod i lunio'r elips neu byddwch chi'n cadw lliw pren y saeth bob tro!

![The target, with a brown circle arrow appearing in a variety of positions.](images/fire_arrow.gif)

Mae'r llyfrgell `p5` yn 'gwrando' am rai digwyddiadau. Un o'r rhain yw botwm y llygoden yn cael ei bwyso. Pan fydd yn synhwyro bod y botwm wedi'i bwyso, bydd yn rhedeg pa god bynnag sydd wedi'i roi iddi yn y swyddogaeth `mouse_pressed()`.

**Debug:** 🐞 Check the `print` line really carefully for commas and brackets.

--- /task ---


