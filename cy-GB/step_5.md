## Sgorio pwyntiau

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Yn y cam hwn, byddwch chi'n ychwanegu sgoriau ar sail lle mae'r saeth yn taro.
</div>
<div>

![Y targed, gyda'r saeth yn ymddangos mewn amrywiaeth o safleoedd a sgoriau'n ymddangos fel testun o dan y gêm.](images/points-scored.gif){:width="300px"}

</div>
</div>

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
We use <span style="color: #0faeb0; font-weight: bold;"> conditions</span> all the time to make decisions. We could say 'if the pencil is blunt, then sharpen it'. Similarly, `if` conditions let us write code that do something different depending on whether a condition is true or false.
</p>

### Display the scores

--- task ---

Delete ❌ the `print('🎯')` line of code.

--- code ---
---
def draw():
line_highlights: 28
---
# Pethau i'w gwneud ym mhob ffrâm
global allanol, mewnol, canol_y_nod    
awyr = color(92, 204, 206) #Coch = 92, Gwyrdd = 204, Glas = 206    
gwair = color(149, 212, 122)    
pren = color(145, 96, 51)    
allanol = color(0, 120, 180)    
mewnol = color(210, 60, 60)   
canol_y_nod = color(220, 200, 0)


--- /code ---

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Rydyn ni'n defnyddio <span style="color: #0faeb0; font-weight: bold;">amodau</span> i wneud penderfyniadau drwy'r amser. Pethau fel 'os nad oes min ar y pensil, mae angen ei finio'. Similarly, `if` conditions let us write code that do something different depending on whether a condition is true or false.
</p>

--- task ---

I brintio neges ar gyfer cylch allanol y targed, ychwanegwch god at eich swyddogaeth `mouse_pressed()` i wneud yn siŵr bod y `lliw_taro` `==` to `allanol`.

Byddwch yn ofalus wrth ddefnyddio'r symbol `=` yn Python:

--- code ---
---
language: python filename: main.py - mouse_pressed() line_numbers: true line_number_start: 5
line_highlights: 10-11
---

# Mae'r swyddogaeth mouse_pressed yn mynd fan hyn
language: python filename: main.py - mouse_pressed() line_numbers: true line_number_start: 8

--- /code ---

**Tip:** 💡 If you changed the colour of your outer circle then you will need to replace `'blue'` with the colour name that you have chosen.

--- /task ---

--- task ---

**Test:** 🔄 Run your project. Try to fire the arrow on the blue outer circle to see the message.

**Tip:** 💡 `frame_rate=2`, in `run` at the bottom of your code, controls how fast your game draws. If it's going too fast, set it to a lower number.

![The output area with arrow touching the outer circle. The points message is displayed in the output area.](images/blue-points.png)

**Difa chwilod:** Gwnewch yn siŵr bod eich cod yn cyfateb yn union a'ch bod wedi mewnoli'r cod yn eich datganiad `if`. Mae mewnoli yn dweud wrth Python mai dim ond os yw'r amod yn `True` y dylai'r cod redeg.

**Debug:** 🐞 Make sure your code matches exactly and you indented the code inside your `if` statement.

Oherwydd bydd pwyntiau'n cael eu sgorio os bydd y saeth yn glanio ar y cylchoedd `mewnol` neu `canol_y_nod` hefyd, nid `allanol` yw'r unig gylch mae'n rhaid i chi ei wirio. I wneud hyn, defnyddiwch `elif` (fersiwn wedi'i byrhau o else - if).

--- /task ---

`elif` (else - if) can be used to add more conditions to your `if` statement. These will be read from top to bottom. As soon as a **True** condition is found, it will be actioned. Any remaining conditions will be ignored.

--- task ---

Yr hyn sy'n gwneud `elif` yn wahanol yw y bydd yn gwirio dim ond os yw amodau `if` ac unrhyw `elif` o'i flaen yn `False`.

--- code ---
---
language: python filename: main.py - mouse_pressed() line_numbers: true line_number_start: 6
line_highlights: 12-15
---

def mouse_pressed(): if hit_colour == Color('blue').hex:   
print('You hit the outer circle, 50 points!') elif hit_colour == Color('red').hex: print('You hit the inner circle, 200 points!') elif hit_colour == Color('yellow').hex: print('You hit the middle, 500 points!')

--- /code ---

--- /task ---

--- task ---

**Test:** 🔄 Run your project. Try to fire the arrow on the inner and middle circles to see their messages.

![The output area with arrow touching the inner circle. The points message is displayed in the output area.](images/yellow-points.png)

**Debug:** 🐞 Check your indentation matches the example.

**Difa chwilod:** Gwnewch yn siŵr bod eich `elif` ar yr un lefel mewnoli â'ch `if`, a bod y cod tu mewn i'ch `elif` ar yr un lefel â'r cod tu mewn i'ch `if`.

**Difa chwilod:** Os gwelwch chi neges yn dweud bod y `mewnol` neu `canol_y_nod` 'not defined', ewch yn ôl i `draw()` a gwneud yn siŵr eu bod ar y llinell sy'n datgan bod y newidynnau'n rhai cyffredinol (global).

**Debug:** 🐞 Make sure that you have used the `.hex` string for **your** circle colours.

--- /task ---

### Missing the target

There is one more decision you need to make: what happens if the arrow does not land on any of the target circles? ❌

To do this last check, you use `else`.

--- task ---

Add code to `print` a message `else` none of the `if` and `elif` statements have been met.

--- code ---
---
def mouse_pressed():    
if lliw_taro == allanol:   
print('Ti wedi taro'r cylch allanol, 50 pwynt!')   
elif lliw_taro == mewnol:   
print('Ti wedi taro'r cylch mewnol, 200 pwynt!')   
elif lliw_taro == canol_y_nod:    
print('Canol y nod! 500 pwynt!')   
else:   
print('Ti wedi methu! Dim pwyntiau!')
line_highlights: 16-17
---

def mouse_pressed(): if hit_colour == Color('blue').hex:   
print('You hit the outer circle, 50 points!') elif hit_colour == Color('red').hex: print('You hit the inner circle, 200 points!') elif hit_colour == Color('yellow').hex: print('You hit the middle, 500 points!') else:   
print('You missed! No points!')

--- /code ---

--- /task ---

--- task ---

**Test:** 🔄 Run your project. Fire the arrow in the grass or sky to see the miss message.

**Choose:** 💭 Change the number of points scored for the different colours.

--- /task ---

--- save ---
