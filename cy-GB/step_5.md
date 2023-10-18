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
We use <span style="color: #0faeb0; font-weight: bold;"> conditions</span> all the time to make decisions. We could say 'if the pencil is blunt, then sharpen it'. Similarly, `if` conditions let us write code that does something different depending on whether a condition is true or false.
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

--- task ---

Display a message **if** the `hit_colour` is equal to the `outer` circle colour (blue) 🎯.

I brintio neges ar gyfer cylch allanol y targed, ychwanegwch god at eich swyddogaeth `mouse_pressed()` i wneud yn siŵr bod y `lliw_taro` `==` to `allanol`.

--- code ---
---
Newidiwch y cod yn eich `print()` i roi sgôr:
line_highlights: 10-11
---

# Mae'r swyddogaeth mouse_pressed yn mynd fan hyn
def mouse_pressed():     
if hit_colour == Color('blue').hex:  # Like the code in functions, the code in 'if' statements is indented print('You hit the outer circle, 50 points!')

--- /code ---

def mouse_pressed():     
if lliw_taro == allanol:      
print('Ti wedi taro'r cylch allanol, 50 pwynt!') #Fel swyddogaethau, mae datganiadau 'if' yn cael eu mewnoli

--- /task ---

--- task ---

**Test:** 🔄 Run your project. Try to fire the arrow on the blue outer circle to see the message.

**Tip:** 💡 `frame_rate=2`, in `run` at the bottom of your code, controls how fast your game draws. If it's going too fast, set it to a lower number.

![The output area with arrow touching the outer circle. The points message is displayed in the output area.](images/blue-points.png)

**Debug:** 🐞 Check that you have used the American spelling of 'Color' (without a 'u') and that 'Color' is capitalised.

**Difa chwilod:** Gwnewch yn siŵr bod eich cod yn cyfateb yn union a'ch bod wedi mewnoli'r cod yn eich datganiad `if`. Mae mewnoli yn dweud wrth Python mai dim ond os yw'r amod yn `True` y dylai'r cod redeg.

**Debug:** 🐞 Make sure that you have entered the correct colour name you used for **your** outer circle.

--- /task ---

`elif` (else - if) can be used to add more conditions to your `if` statement. These will be read from top to bottom. As soon as a **True** condition is found, it will be actioned. Any remaining conditions will be ignored.

--- task ---

Dim ond gyda datganiad `if` gellir defnyddio `elif` ac, fel `if`, mae'n gwirio amod. Os yw'r amod yn `True`, mae'r `elif` yn rhedeg cod.

--- code ---
---
Ychwanegwch ddatganiadau `elif` ar gyfer `mewnol` a `canol_y_nod`.
line_highlights: 12-15
---

def mouse_pressed(): if hit_colour == Color('blue').hex:   
print('You hit the outer circle, 50 points!') elif hit_colour == Color('red').hex: print('You hit the inner circle, 200 points!') elif hit_colour == Color('yellow').hex: print('You hit the middle, 500 points!')

--- /code ---

--- /task ---

--- task ---

**Test:** 🔄 Run your project. Try to fire the arrow on the inner and middle circles to see their messages.

![The output area with arrow touching the inner circle. The points message is displayed in the output area.](images/yellow-points.png)

**Profi:** Rhedwch eich prosiect. Ceisiwch stopio'r saeth ar y cylchoedd coch a melyn i weld eu negeseuon.

**Debug:** 🐞 If you see a message about `hit_colour` being 'not defined', then go back to `draw()` and check that the line declares `hit_colour` as a global variable.

**Difa chwilod:** Gwnewch yn siŵr bod eich `elif` ar yr un lefel mewnoli â'ch `if`, a bod y cod tu mewn i'ch `elif` ar yr un lefel â'r cod tu mewn i'ch `if`.

**Difa chwilod:** Os gwelwch chi neges yn dweud bod y `mewnol` neu `canol_y_nod` 'not defined', ewch yn ôl i `draw()` a gwneud yn siŵr eu bod ar y llinell sy'n datgan bod y newidynnau'n rhai cyffredinol (global).

--- /task ---

### Missing the target

There is one more decision you need to make: what happens if the arrow does not land on any of the target circles? ❌

Rydyn ni'n defnyddio <span style="color: #0faeb0; font-weight: bold;"> os (if) … fel arall (else) </span> i wneud penderfyniadau. Pan fyddwch chi'n deffro, rydych chi'n gweld a yw hi'n fore ac os felly, yn deffro. Fel arall, rydych chi'n mynd yn ôl i gysgu. Allwch chi feddwl am unrhyw benderfyniadau os ... fel arall rydych chi'n eu gwneud?

--- task ---

Ychwanegwch god i brintio neges `else` os nad yw unrhyw un o'r datganiadau `if` ac `elif` wedi'u bodloni.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 9
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
