## Creu cefndir

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Mae'r awyr a'r gwair yn cael eu gwneud drwy ysgrifennu cod i lunio petryalau lliw.
</div>
<div>

![Yr ardal allbwn gyda phetryal lliw awyr uwchben petryal lliw gwair i greu'r cefndir.](images/background.png){:width="300px"}

</div>
</div>

--- task ---

Agorwch y [prosiect dechreuol Saethyddiaeth](https://trinket.io/python/23a6f02447){:target="_blank"}.

Os oes gennych chi gyfrif Trinket, fe allwch chi glicio'r botwm **Remix** i gadw copi yn eich llyfrgell `My Trinkets`.

--- /task ---

Mae rhywfaint o god wedi'i ysgrifennu i chi yn barod yn y prosiect dechreuol er mwyn i chi fewngludo'r llyfrgell `p5`. Byddwch yn defnyddio'r llyfrgell hon i adeiladu eich gêm saethyddiaeth.

[[[p5-processing-library]]]

--- task ---

Mae'r swyddogaeth `fill()` yn gosod y lliw tu mewn i'r siapiau. Mae'r prosiect dechreuol eisoes yn cynnwys rhai lliwiau RGB gallwch chi eu defnyddio i wneud hyn.

Dewch o hyd i'ch swyddogaeth `draw()` a pharatoi i lunio'r awyr drwy ychwanegu cod wedi'i fewnoli i osod y lliw `fill()` ar `awyr`:

--- code ---
---
language: python 
filename: main.py — draw() 
line_numbers: true 
line_number_start: 18
line_highlights: 25
---

def draw():     
  #Pethau i'w gwneud ym mhob ffrâm     
  awyr = color(92, 204, 206) #Coch = 92, Gwyrdd = 204, Glas = 206     
  gwair = color(149, 212, 122)     
  pren = color(145, 96, 51)     
  allanol = color(0, 120, 180)     
  
  fill(awyr)

--- /code ---

--- /task ---

Mae'r swyddogaeth `size()` yn `setup()` yn gosod maint y sgrin ar 400 picsel wrth 400 picsel.

[[[p5-coordinates]]]

--- task ---

Ar ôl eich cod `fill()` lluniwch betryal - `rect()` - ar gyfer yr awyr gyda'r cyfesurynnau chwith uchaf (`0`,`0`), lled o `400` i gyfateb i led y sgrin ac uchder o `250`.

![Petryal glas gyda grid cyfesurynnau yn dangos safle'r petryal awyr yn dechrau yn y gornel uchaf, uwchben petryal llwyd.](images/awyr_coords.png)

--- code ---
---
language: python
filename: main.py — draw()
line_numbers: true
line_number_start: 25 
line_highlights: 26
---

  fill(awyr)
  rect(0, 0, 400, 250) #x dechrau, y dechrau, lled, uchder

--- /code ---

--- /task ---

--- task ---

**Profi:** Rhedwch eich cod i weld yr awyr rydych chi wedi'i llunio. Cofiwch, gyda'r llyfrgell `p5` mae'r swyddogaeth `run()` yn galw'r swyddogaeth `setup()` unwaith, wedyn y swyddogaeth `draw()` drosodd a throsodd.

![Petryal glas gyda border du o'i amgylch, uwchben petryal llwyd.](images/sky_stroke.png){:width="300px"}

Dyna ryfedd: mae llinell ddu o amgylch eich awyr! Y rheswm am hyn yw, pan fydd rhaglen yn dechrau, mae'n gosod border du — o'r enw **stroke** — o amgylch popeth mae'n ei lunio yn awtomatig.

--- /task ---

--- task ---

I gael gwared ar y strôc, ychwanegwch `no_stroke()` cyn dechrau llunio'r awyr.

--- code ---
---
language: python
filename: main.py — draw()
line_numbers: true
line_number_start: 23
line_highlights: 25
---

  allanol = color(0, 120, 180) 

  no_stroke()   
  fill(awyr)   
  rect(0, 0, 400, 250) #x, y, lled, uchder

--- /code ---

--- /task ---

--- task ---

**Profi:** Rhedwch eich prosiect eto i wneud yn siŵr bod y strôc wedi diflannu.

--- /task ---

--- task ---

Mae `fill()` yn newid y lliw llenwi ar gyfer pob siâp sy'n cael ei lunio nes bod `fill()` yn cael ei galw eto gyda lliw newydd.

Newidiwch y lliw `fill()` i `gwair` ac ychwanegu `rect(x, y, lled, uchder)` arall.

Mae angen i'r petryal hwn fod o dan yr awyr ar y cyfesurynnau (0, 250) er mwyn iddo ddechrau yn y rhan isaf o'r sgrin.

--- code ---
---
language: python
filename: main.py — draw()
line_numbers: true
line_number_start: 23
line_highlights: 28-29
---

  allanol = color(0, 120, 180) 
  
  no_stroke()     
  fill(awyr)     
  rect(0, 0, 400, 250) #x, y, lled, uchder    
  fill(gwair)    
  rect(0, 250, 400, 150) 

--- /code ---

--- /task ---

--- task ---

**Profi:** Rhedwch eich prosiect eto i weld y cefndir gorffenedig.

--- /task ---

--- save ---
