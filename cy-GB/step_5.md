## Sgorio pwyntiau

Next, you will add some code to get the colour at the location of the arrow.

### Get the colour hit by the arrow

--- task ---

Add a new **global variable** called `hit_colour`.

language: python filename: main.py line_numbers: true line_number_start: 26


--- code ---
---
global allanol, mewnol, canol_y_nod    
awyr = color(92, 204, 206) #Coch = 92, Gwyrdd = 204, Glas = 206    
gwair = color(149, 212, 122)    
pren = color(145, 96, 51)    
allanol = color(0, 120, 180)    
mewnol = color(210, 60, 60)   
canol_y_nod = color(220, 200, 0)
line_highlights: 28
---
def shoot_arrow(): global hit_colour  
arrow_x = randint(100, 300)  
arrow_y = randint(100, 300) hit_colour = get(arrow_x, arrow_y).hex print(hit_colour) fill('brown') circle(arrow_x, arrow_y, 15)

--- /code ---

Rydyn ni'n defnyddio <span style="color: #0faeb0; font-weight: bold;">amodau</span> i wneud penderfyniadau drwy'r amser. Pethau fel 'os nad oes min ar y pensil, mae angen ei finio'. Yn debyg, mae amodau `if` yn gadael i ni ysgrifennu cod sy'n gwneud pethau gwahanol yn dibynnu a yw'r amod yn wir neu ddim.

--- /task ---

--- task ---

**Test:** Click the **Run** button. You should see colours being printed in the **Text output**, in hexadecimal format.

--- /task ---

### Run code when the mouse is pressed

--- task ---

Comment out the line that prints the colour. This means it will not run.

--- code ---
---
def mouse_pressed():     
if lliw_taro == allanol:      
print('Ti wedi taro'r cylch allanol, 50 pwynt!') #Fel swyddogaethau, mae datganiadau 'if' yn cael eu mewnoli
line_highlights: 10-11
---

    global allanol, mewnol, canol_y_nod

--- /code ---

--- /task ---

--- task ---

Add code to print the target emoji 🎯 **when the mouse is clicked**.

--- code ---
---
**Cyngor:** Mae `frame_rate()` yn `setup()` yn rheoli pa mor gyflym mae eich gêm yn llunio. Os yw'n mynd yn rhy gyflym, rhowch rif is.
line_highlights: 12-15
---
# Pethau i'w gwneud ym mhob ffrâm
def mouse_pressed():    
print('🎯')

--- /code ---

--- /task ---

--- task ---

**Test:** Click the **Run** button. You should see the 🎯 character printed when you click the mouse on the target.

![target emoji printed when mouse clicked](images/target_printed.gif)

--- /task ---

--- save ---