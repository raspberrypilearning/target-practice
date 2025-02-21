## Draw the grass

--- task ---

افتح مشروع [بداية الرماية](https://trinket.io/python/eb67937f99){:target="_blank}.

--- /task ---


--- task ---

**Add** code to draw a green rectangle at the bottom of the screen to represent the grass.

![The output area with a sky-coloured rectangle above a grass-coloured rectangle to create the background. The top left corner of the rectangle is marked as x=0, y=250 this is the origin of the rectangle. The width is highlighted as 400 and the height as 150. The code rect(0, 250, 400, 150) is shown.](images/green-grass.png)no_stroke()   
fill(sky)   
rect(0, 0, 400, 250) #محور س, محور ص, العرض, الارتفاع

--- code ---
---
language: python filename: main.py — draw() line_numbers: true line_number_start: 18
line_highlights: 25
---
def draw():     
#أشياء للقيام بها في كل إطار     
sky = color(92, 204, 206) #احمر = 92, اخضر = 204, ازرق = 206     
grass = color(149, 212, 122)     
wood = color(145, 96, 51)     
outer = color(0, 120, 180)

--- /task ---

--- task ---

**اختبار:** قم بتشغيل مشروعك مرة أخرى لعرض الخلفية النهائية.

![![منطقة مخرجات مع مستطيل بلون السماء فوق مستطيل بلون العشب لإنشاء الخلفية.](images/background.png){:"width="300px}](images/background.png)دالة `size()` تستدعى في `setup()` يعين حجم الشاشة على 400 بكسل × 400 بكسل.

--- /task ---

--- save ---
