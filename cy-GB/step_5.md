## Sgorio pwyntiau

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Yn y cam hwn, byddwch chi'n ychwanegu sgoriau ar sail lle mae'r saeth yn taro.
</div>
<div>

![Y targed, gyda'r saeth yn ymddangos mewn amrywiaeth o safleoedd a sgoriau'n ymddangos fel testun o dan y gêm.](images/points-scored.gif){:width="300px"}

</div>
</div>

--- task ---

Bydd y newidynnau lliw yn y swyddogaeth `draw()` yn cael eu defnyddio i wirio'r sgôr yn y swyddogaeth `mouse_pressed()`. I wneud hyn, bydd angen eu gosod fel newidynnau cyffredinol:

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 26
line_highlights: 28
---

def draw():
# Pethau i'w gwneud ym mhob ffrâm
  global outer, inner, bullseye    
sky = color(92, 204, 206) #Red = 92, Green = 204, Blue = 206    
grass = color(149, 212, 122)    
wood = color(145, 96, 51)    
outer = color(0, 120, 180)    
inner = color(210, 60, 60)   
bullseye = color(220, 200, 0)

--- /code ---

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Rydyn ni'n defnyddio <span style="color: #0faeb0; font-weight: bold;">amodau</span> i wneud penderfyniadau drwy'r amser. Pethau fel 'os nad oes min ar y pensil, mae angen ei finio'. Yn debyg, mae amodau `if` yn gadael i ni ysgrifennu cod sy'n gwneud pethau gwahanol yn dibynnu a yw'r amod yn wir neu ddim.
</p>

--- task ---

I brintio neges ar gyfer cylch allanol y targed, ychwanegwch god at eich swyddogaeth `mouse_pressed()` i wneud yn siŵr bod y `lliw_taro` `==` to `allanol`.

Byddwch yn ofalus wrth ddefnyddio'r symbol `=` yn Python:
 + `=` yn cael ei ddefnyddio i **neilltuo** — fel `saeth_x= 200` i osod gwerth newidyn
 + `==` yn cael ei ddefnyddio i brofi **cywerthedd** — fel `lliw_taro == canol_y_nod` — os oes gan y pethau ar y naill ochr a'r llall yr un gwerth, mae'r prawf yn `True`, fel arall mae'n `False`

Newidiwch y cod yn eich `print()` i roi sgôr:

--- code ---
---
language: python filename: main.py - mouse_pressed() line_numbers: true line_number_start: 8
line_highlights: 10-11
---

# Mae'r swyddogaeth mouse_pressed yn mynd fan hyn
def mouse_pressed():     
if hit_color == outer:      
print('You hit the outer circle, 50 points!') #Fel swyddogethau, mae datganiadau 'if' wedi'u mewnoli

--- /code ---

--- /task ---

--- task ---

**Profi:** Rhedwch eich prosiect. Ceisiwch stopio'r saeth ar y cylch allanol glas i weld eich neges. Lliw'r picsel ar ganol y saeth yw'r lliw sy'n cael ei gadw a'i wirio.

**Cyngor:** Mae `frame_rate()` yn `setup()` yn rheoli pa mor gyflym mae eich gêm yn llunio. Os yw'n mynd yn rhy gyflym, rhowch rif is.

![Yr ardal allbwn gyda saeth yn cyffwrdd y cylch allanol. Mae'r datganiad print pwyntiau yn ymddangos yn yr ardal allbwn.](images/blue-points.png)

**Difa chwilod:** Gwnewch yn siŵr bod eich cod yn cyfateb yn union a'ch bod wedi mewnoli'r cod yn eich datganiad `if`. Mae mewnoli yn dweud wrth Python mai dim ond os yw'r amod yn `True` y dylai'r cod redeg.

--- /task ---

Oherwydd bydd pwyntiau'n cael eu sgorio os bydd y saeth yn glanio ar y cylchoedd `mewnol` neu `canol_y_nod` hefyd, nid `allanol` yw'r unig gylch mae'n rhaid i chi ei wirio. I wneud hyn, defnyddiwch `elif` (fersiwn wedi'i byrhau o else - if).

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Rydyn ni'n defnyddio <span style="color: #0faeb0; font-weight: bold;"> else - if </span> i wneud penderfyniadau mewn bywyd go iawn. Pan fyddwch chi'n paentio llun o'r awyr, efallai byddwch chi'n gweld a oes paent melyn ar gyfer yr haul. Fel arall, os nad oes paent melyn, rydych chi'n chwilio am baent oren. Fel arall, os nad oes paent melyn nac oren, fe allech chi ddefnyddio coch — yn ysgafn iawn!
</p>

--- task ---

Dim ond gyda datganiad `if` gellir defnyddio `elif` ac, fel `if`, mae'n gwirio amod. Os yw'r amod yn `True`, mae'r `elif` yn rhedeg cod.

Yr hyn sy'n gwneud `elif` yn wahanol yw y bydd yn gwirio dim ond os yw amodau `if` ac unrhyw `elif` o'i flaen yn `False`.

Ychwanegwch ddatganiadau `elif` ar gyfer `mewnol` a `canol_y_nod`.

--- code ---
---
language: python filename: main.py - mouse_pressed() line_numbers: true line_number_start: 9
line_highlights: 12-15
---

def mouse_pressed():    
if hit_color == outer:    
print('You hit the outer circle, 50 points!')    
elif hit_color == inner:    
print('You hit the inner circle, 200 points!')   
elif hit_color == bullseye:    
print('You hit the bullseye, 500 points!')

--- /code ---

--- /task ---

--- task ---

**Profi:** Rhedwch eich prosiect. Ceisiwch stopio'r saeth ar y cylchoedd coch a melyn i weld eu negeseuon.

![Yr ardal allbwn gyda'r saeth yn cyffwrdd y cylch mewnol. Mae'r datganiad print pwyntiau yn ymddangos yn yr ardal allbwn.](images/yellow-points.png)

**Difa chwilod:** Gwnewch yn siŵr bod eich `elif` ar yr un lefel mewnoli â'ch `if`, a bod y cod tu mewn i'ch `elif` ar yr un lefel â'r cod tu mewn i'ch `if`.

**Difa chwilod:** Os gwelwch chi neges yn dweud bod y `mewnol` neu `canol_y_nod` 'not defined', ewch yn ôl i `draw()` a gwneud yn siŵr eu bod ar y llinell sy'n datgan bod y newidynnau'n rhai cyffredinol (global).

```python
global outer, inner, bullseye
```

--- /task ---

Mae un penderfyniad arall i chi ei wneud: beth sy'n digwydd os nad yw'r saeth yn glanio ar unrhyw un o gylchoedd y targed? Rydych chi'n defnyddio `else` i wneud y gwiriad olaf hwn.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Rydyn ni'n defnyddio <span style="color: #0faeb0; font-weight: bold;"> os (if) … fel arall (else) </span> i wneud penderfyniadau. Pan fyddwch chi'n deffro, rydych chi'n gweld a yw hi'n fore ac os felly, yn deffro. Fel arall, rydych chi'n mynd yn ôl i gysgu. Allwch chi feddwl am unrhyw benderfyniadau os ... fel arall rydych chi'n eu gwneud? 
</p>

--- task ---

Ychwanegwch god i brintio neges `else` os nad yw unrhyw un o'r datganiadau `if` ac `elif` wedi'u bodloni.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 9
line_highlights: 16-17
---

def mouse_pressed():    
if hit_color == outer:   
print('You hit the outer circle, 50 points!')   
elif hit_color == inner:   
print('You hit the inner circle, 200 points!')   
elif hit_color == bullseye:    
print('You hit the bullseye, 500 points!')   
else:   
print('You missed! Dim pwyntiau!')

--- /code ---

--- /task ---

--- task ---

**Profi:** Rhedwch eich prosiect. Ceisiwch stopio'r saeth ar y gwair neu yn yr awyr i weld y neges methu. Newidiwch nifer y pwyntiau sy'n cael eu sgorio am y gwahanol liwiau os hoffech chi.

![Yr ardal allbwn gyda saeth yn methu'r targed. Mae'r datganiad print pwyntiau yn ymddangos yn yr ardal allbwn.](images/missed-points.png)

--- /task ---

--- save ---
