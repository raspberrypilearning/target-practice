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

![A brown triangle on grass and against a sky with the coordinate points labelled at 150, 350 and 200, 150 and 250, 350). The corners of the canvas are also labelled as x=0, y=0 in the top left and x=400, y=400 in the bottom right.](images/stand_coords.png)Pan fyddwch yn galw'r swyddogaeth `triangle()`, rhaid i chi ddarparu tair set o gyfesurynnau, `x1, y1, x2, y2, x3, y3` lle mae pob un yn cynrychioli un o gorneli'r triongl.

--- code ---
---
language: python filename: main.py - draw() line_numbers: true line_number_start: 18
title: Cyfesurynnau triongl
---

    fill('lightgreen')  # Set the fill colour for the grass to light green
    rect(0, 250, 400, 150)  # Draw a rectangle for the grass with these values for x, y, width, height
    fill('sienna')  # Brown colour
    triangle(150, 350, 200, 150, 250, 350)  # Draw a triangle for the target's stand

--- /code ---

--- /task ---

--- task ---

**Test:** 🔄 Run your code to see the stand for your target:

![A brown triangle on grass and against a sky.](images/target-stand.png)language: python filename: main.py - draw() line_numbers: true line_number_start: 28

--- /task ---

### Llunio'r targed

--- task ---

The largest part of the target is a blue **circle**.

**Cyngor:** Rydyn ni wedi ychwanegu sylwadau at ein cod, fel `#Gosod lliw llenwi'r stand ar frown`, i roi gwybod i chi beth mae'n ei wneud. Does dim rhaid i chi ychwanegu'r sylwadau hyn at eich cod, ond maen nhw'n gallu bod yn ddefnyddiol i'ch atgoffa beth mae llinellau cod yn ei wneud.

Draw a circle with x and y coordinates for its centre and a width.

![A brown triangle and blue circle on grass and against a sky. The circle is labelled with the coordinates x=200, y=200 as the centre and circle width of 170.](images/circle-coords.png){:width="400px"}

--- code ---
---
language: python filename: main.py - draw() line_numbers: true line_number_start: 20
line_highlights: 31-32
---

    fill('sienna')  # Brown colour
    triangle(150, 350, 200, 150, 250, 350)  # Draw a triangle for the target's stand 
    fill('blue')  # Set the circle fill colour to blue
    circle(200, 200, 170)  # Draw the outer circle

--- /code ---

--- /task ---

--- task ---

Mae angen cyfesurynnau `x` ac `y`, lled ac uchder ar elips. Safle'r canol yw cyfesurynnau `x` ac `y` elips.

Bydd y cylch glas yn gorchuddio'r triongl brown lle maen nhw'n gorgyffwrdd, oherwydd bod y cylch wedi'i lunio'n ddiweddarach.

![A brown triangle and blue circle on grass and against a sky.](images/blue-circle.png)**Cyngor:** I wneud cylch, rhaid i'r **lled** a'r **uchder** fod yr un fath.

--- /task ---

language: python filename: main.py - draw() line_numbers: true line_number_start: 31

--- task ---

**Add** coloured circles for the inner and middle parts of the target.

--- code ---
---
language: python filename: main.py - draw() line_numbers: true line_number_start: 20
line_highlights: 33-34
---

    fill('sienna')  # Brown colour
    triangle(150, 350, 200, 150, 250, 350)  # Draw a triangle for the target's stand 
    fill('blue')  # Set the circle fill colour to blue
    circle(200, 200, 170)  # Draw the outer circle
    fill('red')  # Set the colour for the circle fill to red
    circle(200, 200, 110)  # Draw the inner circle using x, y, width
    fill('yellow')  # Set the colour for the circle fill to yellow      
    circle(200, 200, 30)  # Draw the middle circle using x, y, width

--- /code ---

--- /task ---

--- task ---

**Test:** 🔄 Run your project to see the target with three coloured circles.

![A brown triangle with three coloured circles on grass and against a sky.](images/three-circles.png)Ewch ati i greu dau newidyn newydd i storio'r lliwiau `mewnol` a `canol_y_nod` ar gyfer y cylchoedd sy'n weddill.

--- /task ---

--- task ---

**Choose:** 💭 Change any of the colours using a different colour name. You can find a list of all of the available colour names on [W3 Schools](https://www.w3schools.com/colors/colors_names.asp){:target="blank"}.

![A brown triangle with three coloured circles on grass and against a sky. The colours have changed to pinks and purples.](images/alternative-colours.png)[[[generic-theory-simple-colours]]]

--- collapse ---
---
line_highlights: 24-25
---

--- code ---
---
def draw():   
#Pethau i'w gwneud ym mhob ffrâm
line_highlights: 37-40
---

awyr = color(92, 204, 206)   
gwair = color(149, 212, 122)   
pren = color(145, 96, 51)   
allanol = color(0, 120, 180) #Glas    
mewnol = color(210, 60, 60) # Coch    
canol_y_nod = color(220, 200, 0) #Melyn
# Things to do in every frame

    fill('BlueViolet')
    rect(0, 0, 400, 250)  # Sky
    fill('DeepSkyBlue')
    rect(0, 250, 400, 150)  # Ground
    fill('FireBrick')
    triangle(150, 350, 200, 150, 250, 350)  # Stand
    fill('LemonChiffon')
    circle(200, 200, 170)  # Outer circle
    fill('DeepPink')
    circle(200, 200, 110)  # Inner circle
    fill('BlueViolet')
    circle(200, 200, 30)  # Middle circle

--- /code ---

--- /collapse ---

--- /task ---

--- save ---
