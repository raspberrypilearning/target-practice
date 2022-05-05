## Llunio eich targed
<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Siâp triongl yw stand y targed. Mae'r targed yn cael ei wneud â chylchoedd lliw — mae'r cylchoedd llai werth mwy o bwyntiau na'r rhai mwy. 
</div>
<div>

![Yr ardal allbwn gyda'r targed a'r stand.](images/three-circles.png){:width="300px"}

</div>
</div>

Mae siapiau'n cael eu llunio yn nhrefn rhedeg y llinellau cod. Mae'r stand pren triongl tu ôl cylchoedd y targed yn rhannol, felly rhaid ei lunio gyntaf.

Dychmygwch dorri'r holl siapiau allan o bapur. Yn dibynnu ar sut rydych chi'n trefnu ac yn croesi'r papur hwnnw, gallai'r canlyniad edrych yn wahanol iawn.

### Llunio'r stand

--- task ---

Pan fyddwch yn galw'r swyddogaeth `triangle()`, rhaid i chi ddarparu tair set o gyfesurynnau, `x1, y1, x2, y2, x3, y3` lle mae pob un yn cynrychioli un o gorneli'r triongl.

--- collapse ---
---
title: Cyfesurynnau triongl
---

  Dyma dri triongl enghreifftiol ac mae gan bob un set wahanol o gyfesurynnau. 'Drychwch ar safle grid pob un i weld sut mae'r cyfesurynnau `x` a `y` yn lleoli corneli'r trionglau:
  + Triongl gwyrdd: triongl(50, 50, 150, 50, 180, 100)
  + Triongl glas: triongl(210, 280, 300, 350, 380, 100)
  + Triongl brown: triongl(50, 150, 200, 250, 180, 350)

  ![Yr ardal allbwn gyda thri thriongl.](images/triangles-coords.png)

--- /collapse ---

Lluniwch `triangle()` ar gyfer y stand gyda'r corneli yn (150, 350), (200, 150), a (250, 350).

![Triongl brown ar wair ac yn erbyn awyr gyda'r pwyntiau cyfesurynnau wedi'u labelu.](images/stand_coords.png)

--- code ---
---
language: python filename: main.py - draw() line_numbers: true line_number_start: 28
line_highlights: 31-32
---

  fill(grass)   
rect(0, 250, 400, 150) #x, y, width, height

  fill(wood) #Set the stand fill colour to brown     
triangle(150, 350, 200, 150, 250, 350)


--- /code ---

**Cyngor:** Rydyn ni wedi ychwanegu sylwadau at ein cod, fel `#Gosod lliw llenwi'r stand ar frown`, i roi gwybod i chi beth mae'n ei wneud. Does dim rhaid i chi ychwanegu'r sylwadau hyn at eich cod, ond maen nhw'n gallu bod yn ddefnyddiol i'ch atgoffa beth mae llinellau cod yn ei wneud.

--- /task ---

--- task ---

**Profi:** Rhedwch eich cod i weld stand eich targed.

![Triongl brown ar wair ac yn erbyn awyr.](images/target-stand.png)

--- /task ---

### Llunio'r targed

--- task ---

Bydd y rhan fwyaf o'r targed yn **gylch** glas wedi'i wneud gan ddefnyddio'r swyddogaeth `ellipse()`. Siâp ag un ochr a dim corneli yw elips. Gall fod yn hirgrwn neu'n hollol grwn fel cylch.

Mae angen cyfesurynnau `x` ac `y`, lled ac uchder ar elips. Safle'r canol yw cyfesurynnau `x` ac `y` elips.

Bydd y cylch glas yn gorchuddio'r triongl brown lle maen nhw'n gorgyffwrdd, oherwydd bod y cylch wedi'i lunio'n ddiweddarach.

**Cyngor:** I wneud cylch, rhaid i'r **lled** a'r **uchder** fod yr un fath.

--- code ---
---
language: python filename: main.py - draw() line_numbers: true line_number_start: 31
line_highlights: 33-34
---

  fill(wood)   
triangle(150, 350, 200, 150, 250, 350)   
fill(outer)    
ellipse(200, 200, 170, 170) #Outer circle. 200, 200 yw canol y sgrin

--- /code ---

--- /task ---

--- task ---

**Profi:** Rhedwch eich cod i weld y cylch glas mawr cyntaf.

![Triongl brown a chylch glas ar wair ac yn erbyn awyr.](images/blue-circle.png)

--- /task ---

--- task ---

Ewch ati i greu dau newidyn newydd i storio'r lliwiau `mewnol` a `canol_y_nod` ar gyfer y cylchoedd sy'n weddill.

Neilltuwch liwiau i'r newidynnau `mewnol` a `canol_y_nod` gan ddefnyddio `color()`.

Mae'r swyddogaeth `color()` yn disgwyl tri rhif: un yr un i goch, gwyrdd a glas.

Rydyn ni wedi defnyddio rhifau sy'n creu lliwiau traddodiadol targed saethu, ond fe allwch chi ddefnyddio unrhyw liwiau mynnwch chi, cyhyd â'u bod yn wahanol i'w gilydd.

[[[generic-theory-simple-colours]]]

--- code ---
---
language: python filename: main.py - draw() line_numbers: true line_number_start: 18
line_highlights: 24-25
---

def draw():   
#Things to do in every frame

  sky = color(92, 204, 206)   
grass = color(149, 212, 122)   
wood = color(145, 96, 51)   
outer = color(0, 120, 180) #Blue    
inner = color(210, 60, 60) # Red    
bullseye = color(220, 200, 0) #Yellow

--- /code ---

--- /task ---

--- task ---

Mae'r targed wedi'i ffurffio o gylchoedd o wahanol faint gyda'r un cyfesurynnau canol (200, 200) — canol y sgrin.

Ychwanegwch ddau gylch arall i gynrychioli cylch mewnol a chanol y nod (y bullseye). Newidiwch `fill()` cyn llunio pob cylch.

--- code ---
---
language: python filename: main.py - draw() line_numbers: true line_number_start: 33
line_highlights: 37-40
---

  fill(wood)    
triangle(150, 350, 200, 150, 250, 350) #Stand    
fill(outer)   
ellipse(200, 200, 170, 170) #Outer circle   
fill(inner)   
ellipse(200, 200, 110, 110) #Inner circle   
fill(bullseye)   
ellipse(200, 200, 30, 30) #Bullseye

--- /code ---

--- /task ---

--- task ---

**Profi:** Rhedwch eich prosiect eto i weld y targed gyda thri chylch lliw. Newidiwch y lliwiau nes eich bod yn fodlon arnyn nhw.

![Triongl brown gyda thri chylch lliw ar wair ac yn erbyn awyr.](images/three-circles.png)

**Difa chwilod:** Mae Python yn defnyddio 'color', ar gyfer lliw, felly gwnewch yn siŵr eich bod chi'n gwneud hynny hefyd.

--- /task ---

--- save ---

