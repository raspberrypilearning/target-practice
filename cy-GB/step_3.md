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
Dyma dri triongl enghreifftiol ac mae gan bob un set wahanol o gyfesurynnau. 'Drychwch ar safle grid pob un i weld sut mae'r cyfesurynnau `x` a `y` yn lleoli corneli'r trionglau:
title: Cyfesurynnau triongl
---

    fill('lightgreen')  
    rect(0, 250, 400, 150)  
    fill('brown') 
    triangle(150, 350, 200, 150, 250, 350)

--- /code ---

--- /task ---

--- task ---

**Test:** Run your code to see the stand for your target:

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
language: python line_numbers: true line_number_start: 23
line_highlights: 31-32
---

    fill('brown')  
    triangle(150, 350, 200, 150, 250, 350)  
    fill('blue')  
    circle(200, 200, 170)

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
language: python line_numbers: true line_number_start: 25
line_highlights: 33-34
---

    fill('blue')  
    circle(200, 200, 170)  
    fill('red')  
    circle(200, 200, 110)  # Draw the inner circle 
    fill('yellow')       
    circle(200, 200, 30)  # Draw the middle circle

--- /code ---

--- /task ---

--- task ---

**Test:** Run your project to see the target with three coloured circles.

![A brown triangle with three coloured circles on grass and against a sky.](images/three-circles.png)Ewch ati i greu dau newidyn newydd i storio'r lliwiau `mewnol` a `canol_y_nod` ar gyfer y cylchoedd sy'n weddill.

--- /task ---

--- save ---
