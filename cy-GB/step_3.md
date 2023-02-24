## Llunio eich targed

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Siâp triongl yw stand y targed. Mae'r targed yn cael ei wneud â chylchoedd lliw — mae'r cylchoedd llai werth mwy o bwyntiau na'r rhai mwy.
</div>
<div>

![Yr ardal allbwn gyda'r targed a'r stand.](images/three-circles.png){:width="300px"}

</div>
</div>

### Llunio'r stand

--- task ---

Dychmygwch dorri'r holl siapiau allan o bapur. Yn dibynnu ar sut rydych chi'n trefnu ac yn croesi'r papur hwnnw, gallai'r canlyniad edrych yn wahanol iawn.

Draw a triangle using the x and y coordinates for each of the corners.

![A brown triangle on grass and against a sky with the coordinate points labelled at 150, 350 and 200, 150 and 250, 350). The corners of the canvas are also labelled as x=0, y=0 in the top left and x=400, y=400 i the bottom right.](images/stand_coords.png)Pan fyddwch yn galw'r swyddogaeth `triangle()`, rhaid i chi ddarparu tair set o gyfesurynnau, `x1, y1, x2, y2, x3, y3` lle mae pob un yn cynrychioli un o gorneli'r triongl.

--- code ---
---
Dyma dri triongl enghreifftiol ac mae gan bob un set wahanol o gyfesurynnau. 'Drychwch ar safle grid pob un i weld sut mae'r cyfesurynnau `x` a `y` yn lleoli corneli'r trionglau:
title: Cyfesurynnau triongl
---
  --- /collapse ---

--- /code ---

--- /task ---

--- task ---

language: python filename: main.py - draw() line_numbers: true line_number_start: 28

![A brown triangle on grass and against a sky.](images/target-stand.png)fill(gwair)   
rect(0, 250, 400, 150) #x, y, lled, uchder

--- /task ---

### Llunio'r targed

--- task ---

**Cyngor:** Rydyn ni wedi ychwanegu sylwadau at ein cod, fel `#Gosod lliw llenwi'r stand ar frown`, i roi gwybod i chi beth mae'n ei wneud. Does dim rhaid i chi ychwanegu'r sylwadau hyn at eich cod, ond maen nhw'n gallu bod yn ddefnyddiol i'ch atgoffa beth mae llinellau cod yn ei wneud.

Set the fill colour to `outer` (blue).

Draw a circle with x and y coordinates for its centre and a width.

![A brown triangle and blue circle on grass and against a sky. The circle is labelled with the coordinates x=200, y=200 as the centre and circle width of 170.](images/circle-coords.png)**Profi:** Rhedwch eich cod i weld stand eich targed.

--- code ---
---
language: python filename: main.py - draw() line_numbers: true line_number_start: 29
line_highlights: 31-32
---

  fill(wood)   
triangle(150, 350, 200, 150, 250, 350)   
fill(outer) # Set the circle fill colour to outer    
circle(200, 200, 170) # x, y, width of the circle

--- /code ---

--- /task ---

--- task ---

**Cyngor:** I wneud cylch, rhaid i'r **lled** a'r **uchder** fod yr un fath.

The blue circle was drawn after the stand so it is in front:

![A brown triangle and blue circle on grass and against a sky.](images/blue-circle.png){:width="400px"}

--- /task ---

--- task ---

👀 Find your colour variables in the `draw` function.

Create two variables called `inner` and `middle` to store colours for the other circles.

**Profi:** Rhedwch eich cod i weld y cylch glas mawr cyntaf.

--- code ---
---
language: python filename: main.py - draw() line_numbers: true line_number_start: 17
line_highlights: 33-34
---
def draw():   
# Things to do in every frame global wood sky = color(92, 204, 206)   
grass = color(149, 212, 122)   
wood = color(145, 96, 51)   
outer = color(0, 120, 180) # Blue    
inner = color(210, 60, 60) # Red    
middle = color(220, 200, 0) # Yellow

--- /code ---

--- /task ---

Mae'r swyddogaeth `color()` yn disgwyl tri rhif: un yr un i goch, gwyrdd a glas.

--- task ---

**Add** coloured circles for the inner and middle parts of the target.

--- code ---
---
language: python filename: main.py - draw() line_numbers: true line_number_start: 31
line_highlights: 24-25
---
  def draw():   
#Pethau i'w gwneud ym mhob ffrâm

--- /code ---

--- /task ---

--- task ---

**Test:** 🔄 Run your project to see the target with three coloured circles.

![A brown triangle with three coloured circles on grass and against a sky.](images/three-circles.png)Mae'r targed wedi'i ffurffio o gylchoedd o wahanol faint gyda'r un cyfesurynnau canol (200, 200) — canol y sgrin.

Ychwanegwch ddau gylch arall i gynrychioli cylch mewnol a chanol y nod (y canol_y_nod). Newidiwch `fill()` cyn llunio pob cylch.

--- /task ---

--- task ---

fill(pren)    
triangle(150, 350, 200, 150, 250, 350) #Stand    
fill(allanol)   
ellipse(200, 200, 170, 170) #Cylch allanol   
fill(mewnol)   
ellipse(200, 200, 110, 110) #Cylch mewnol   
fill(canol_y_nod)   
ellipse(200, 200, 30, 30) #Canol y nod

[[[generic-theory-simple-colours]]]

![A brown triangle with three coloured circles on grass and against a sky. The colours have changed to pinks and purples.](images/alternative-colours.png){:width="400px"}


--- /task ---



