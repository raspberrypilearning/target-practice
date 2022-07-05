## Saethu

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Nawr mae'n amser ychwanegu saeth sy'n symud ar hap ar draws yr ardal targed.
</div>
<div>

![Y targed, gyda chylch brown, y saeth, yn ymddangos mewn amrywiaeth o safleoedd.](images/fire_arrow.gif){:width="300px"}

</div>
</div>

--- task ---

Dewch o hyd i'r sylw **#Mae'r swyddogaeth saethu_saeth yn mynd fan hyn** ac ychwanegu cod oddi tano i ddiffinio eich swyddogaeth `saethu_saeth()`.

Ychwanegwch `ellipse()` bach yng nghanol y sgrin i gynrychioli'r saeth.

--- code ---
---
language: python
filename: main.py — saethu_saeth()
line_numbers: true
line_number_start: 10
line_highlights: 11-12
---

#Mae'r swyddogaeth saethu_saeth yn mynd fan hyn    
def saethu_saeth():   
  ellipse(200, 200, 15, 15)

--- /code ---

--- /task ---

--- task ---

Ewch i'r cod `draw()` sy'n creu'r targed ac ychwanegu cod ar y diwedd i osod `fill()` ar `pren`, ac yna galw eich swyddogaeth `saethu_saeth()` newydd.

--- code ---
---
language: python
filename: main.py — draw()
line_numbers: true
line_number_start: 41
line_highlights: 44-45
---

  fill(canol_y_nod)    
  ellipse(200, 200, 30, 30)    
  
  fill(pren)   
  saethu_saeth()

--- /code ---

--- /task ---

--- task ---

**Profi:** Rhedwch eich cod a gweld y saeth yn ymddangos yng nghanol y nod.

![Y targed ar gefndir gyda chylch brown, y saeth, arno.](images/arrow-middle.png)

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;"> Mae gemau cyfrifiadur, fideos ac animeiddiadau'n creu effaith symud drwy ddangos llawer o ddelweddau un ar ôl y llall. <span style="color: #0faeb0; font-weight: bold;">Ffrâm</span> yw enw pob delwedd. <span style="color: #800080;">Cyfradd fframiau</span> yw enw'r cyflymder mae'r ddelwedd yn newid ac mae'n cael ei rhoi mewn <span style="color: #800080;">fps</span>, sef fframiau yr eiliad (frames per second).  
</p>

Mae'r llinell `frame_rate(2)` yn `setup()` yn gosod y gyfradd fframiau ar 2 ffrâm yr eiliad.

Mae'r swyddogaeth `draw()` yn cael ei galw bob ffrâm. Byddwch chi'n llunio'r saeth mewn safle ar hap bob tro mae `draw()` yn cael ei galw.

Bydd y cefndir a'r targed yn cael eu llunio dros yr hen saeth. Mae hyn yn golygu mai dim ond un saeth sydd i'w gweld ar y tro.

--- task ---

Dewch o hyd i'r datganiadau `import` ar frig eich cod. Byddwch chi'n defnyddio `randint` o'r llyfrgell `random`.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 3
---

#Import library code    
from p5 import *    
from math import *    
from random import randint

--- /code ---

--- /task ---

--- task ---

Ewch i'ch sywddogaeth `saethu_saeth()` ac ychwanegu dau newidyn newydd, `saeth_x` a `saeth_y` i storio rhifau ar hap rhwng `100` a `300`.

Bydd hyn yn golygu bod rhai saethiadau'n methu'r targed heb fynd yr holl ffordd i ymylon eich gêm.

Newidiwch eich `ellipse()` i ddefnyddio'r newidynnau newidd i leoli eich saeth.

![Petryal yn dangos cyfesurynnau'r ardal targed mewn petryal lled-dryloyw.](images/target_area.png)

--- code ---
---
language: python
filename: main.py — saethu_saeth()
line_numbers: true
line_number_start: 10
line_highlights: 12-14
---

#Mae'r swyddogaeth saethu_saeth yn mynd fan hyn    
def saethu_saeth():    
  saeth_x = randint(100, 300)   
  saeth_y = randint(100, 300)    
  ellipse(saeth_x, saeth_y, 15, 15) #Diweddaru i gyfesurynnau ar hap

--- /code ---

--- /task ---

### Cael y lliw mae'r saeth yn ei daro

Mae'r swyddogaeth `get()` yn dychwelyd lliw picsel.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Ystyr <span style="color: #0faeb0; font-weight: bold;">picsel</span>, sy'n deillio o 'picture element' yn Saesneg, yw un dot lliw mewn delwedd. Mae delweddau wedi'u ffurfio o lawer o bicselau lliw.
</p>

--- task ---

Mae angen i chi storio'r lliw mae'r saeth yn anelu ato cyn llunio saeth ar ei ben.

Ychwanegwch god i storio'r `lliw_taro`. Defnyddiwch y swyddogaeth `get()` i gael lliw'r picsel yn y cyfesurynnau `saeth_x` a `saeth_y` — canol y saeth.

--- code ---
---
language: python
filename: main.py — saethu_saeth() 
line_numbers: true
line_number_start: 10
line_highlights: 14
---

#Mae'r swyddogaeth saethu_saeth yn mynd fan hyn     
def saethu_saeth():    
  saeth_x = randint(100, 300)    
  saeth_y = randint(100, 300)    
  lliw_taro = get(saeth_x, saeth_y) #Cadw'r lliw cyn llunio'r saeth   
  ellipse(saeth_x, saeth_y, 15, 15)

--- /code ---

**Cyngor:** Mae angen i'r cod i gael y lliw a'i gadw fod **cyn** y cod i lunio'r elips neu byddwch chi'n cadw lliw pren y saeth bob tro!

--- /task ---

Mae'r llyfrgell `p5` yn 'gwrando' am rai digwyddiadau. Un o'r rhain yw botwm y llygoden yn cael ei bwyso. Pan fydd yn synhwyro bod y botwm wedi'i bwyso, bydd yn rhedeg pa god bynnag sydd wedi'i roi iddi yn y swyddogaeth `mouse_pressed()`.

--- task ---

Dewch o hyd i'r sylw **#Mae'r swyddogaeth mouse_pressed yn mynd fan hyn** ac ychwanegu cod oddi tano i ddiffinio eich swyddogaeth `mouse_pressed()`.

Ychwanegwch god i brintio faint o goch, gwyrdd a glas sydd yn y picsel mae'r saeth yn glanio arno.

--- code ---
---
language: python
filename: main.py - mouse_pressed()
line_numbers: true
line_number_start: 8
line_highlights: 9-10
---

#Mae'r swyddogaeth mouse_pressed yn mynd fan hyn    
def mouse_pressed():    
  print( red(lliw_taro), green(lliw_taro), blue(lliw_taro) )

--- /code ---

--- /task ---

--- task ---

Rydych chi wedi diffinio dwy swyddogaeth, `saethu_saeth()` a `mouse_pressed()`. Mae angen i'r ddwy swyddogaeth hyn ddefnyddio'r newidyn `lliw_taro`.

Mae newidyn sydd angen ei ddefnyddio drwy raglen gyfan yn cael ei galw'n **newidyn cyffredinol**. Ychwanegwch god at eich swyddogaeth `saethu_saeth()` i wneud `lliw_taro` yn newidyn cyffredinol:

--- code ---
---
language: python
filename: main.py - saethu_saeth()
line_numbers: true
line_number_start: 12
line_highlights: 14
---

#Mae'r swyddogaeth saethu_saeth yn mynd fan hyn    
def saethu_saeth():    
  global lliw_taro #Gellir ei ddefnyddio mewn swyddogaethau eraill     
  saeth_x = randint(100, 300)     
  saeth_y = randint(100, 300)     
  lliw_taro = get(saeth_x, saeth_y) #Cadw'r lliw cyn llunio'r saeth     
  ellipse(saeth_x, saeth_y, 15, 15)    

--- /code ---

--- /task ---

--- task ---

**Profi:** Rhedwch eich prosiect. Mae'r saeth yn cael ei hail-lunio ar gyfesurynnau ar hap.

Mae'r prosiect yn cael y `lliw_taro` bob tro mae'r saeth yn cael ei hail-lunio ac yn printio'r gwerth lliw yn yr ardal allbwn o dan y targed.

![Y targed gyda chylch brown, y saeth, yn ymddangos mewn amrywiaeth o safleoedd.](images/fire_arrow.gif)

**Difa chwilod:** Os ydych chi'n gweld neges yn dweud `lliw_taro` 'not defined', ewch yn ôl i `saeth_saethu()` a gwneud yn siŵr bod gennych chi'r llinell `global lliw_taro`.

**Difa chwilod:** Gwiriwch y comas a'r cromfachau yn y llinell `print` yn ofalus iawn.

--- /task ---

--- save ---

