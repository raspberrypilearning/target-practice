## Creu cefndir

--- task ---

Agorwch y [prosiect dechreuol Saethyddiaeth](https://trinket.io/python/23a6f02447){:target="_blank"}.

--- /task ---


--- task ---

Mae rhywfaint o god wedi'i ysgrifennu i chi yn barod yn y prosiect dechreuol er mwyn i chi fewngludo'r llyfrgell `p5`. Byddwch yn defnyddio'r llyfrgell hon i adeiladu eich gêm saethyddiaeth.

![The output area with a sky-coloured rectangle above a grass-coloured rectangle to create the background. The top left corner of the rectangle is marked as x=0, y=250 this is the origin of the rectangle. The width is highlighted as 400 and the height as 150. The code rect(0, 250, 400, 150) is shown.](images/green-grass.png)Mae'r swyddogaeth `fill()` yn gosod y lliw tu mewn i'r siapiau. Mae'r prosiect dechreuol eisoes yn cynnwys rhai lliwiau RGB gallwch chi eu defnyddio i wneud hyn.

--- code ---
---
Mae'r swyddogaeth `fill()` yn gosod y lliw tu mewn i'r siapiau. Mae'r prosiect dechreuol eisoes yn cynnwys rhai lliwiau RGB gallwch chi eu defnyddio i wneud hyn.
line_highlights: 25
---
Dewch o hyd i'ch swyddogaeth `draw()` a pharatoi i lunio'r awyr drwy ychwanegu cod wedi'i fewnoli i osod y lliw `fill()` ar `awyr`:

--- /task ---

--- task ---

def draw():     
#Pethau i'w gwneud ym mhob ffrâm     
awyr = color(92, 204, 206) #Coch = 92, Gwyrdd = 204, Glas = 206     
gwair = color(149, 212, 122)     
pren = color(145, 96, 51)     
allanol = color(0, 120, 180)

![The output area with a sky-coloured rectangle above a grass-coloured rectangle to create the background.](images/background.png){:width="400px"}

--- /task ---

--- save ---
