## Add an arrow

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Add an even smaller circle to represent an arrow.
</div>
<div>

! [الهدف بسهم دائري بني يظهر في عدة مواضع.] (images/fire_arrow.gif){:width="300px"}

</div>
</div>

### Where will you shoot?

--- task ---

Add a function to draw a brown circle at coordinates `200`, `200`.

--- code ---
---
language: python filename: main.py - mouse_pressed() line_numbers: true line_number_start: 8
line_highlights: 11-12
---
# تذهب دالة shoot_arrow هنا
def shoot_arrow():    
global hit_color #يمكن استخدامها في دالة أخرى     
arrow_x = randint(100, 300)     
arrow_y = randint(100, 300)     
hit_color = get(arrow_x, arrow_y) #احفظ اللون قبل رسم السهم     
ellipse(arrow_x, arrow_y, 15, 15)

--- /code ---

--- /task ---

--- task ---

اذهب إلى الكود `draw()` الذي ينشئ الهدف وأضف الكود في النهاية لتعيين `fill()` إلى `wood`، ثم استدعي وظيفة `shoot_arrow()` الجديدة.

--- code ---
---
language: python filename: main.py — draw() line_numbers: true line_number_start: 41
line_highlights: 44-45
---

    def shoot_arrow():<br x-id="3" />
      ellipse(200, 200, 15, 15)

--- /code ---

--- /task ---

**اختبار:** قم بتشغيل مشروعك. يتم إعادة رسم السهم في إحداثيات عشوائية.

![a brown arrow circle in the centre of the target](images/arrow-centre.png) --- /task ---

The arrow needs to move randomly.

انتقل إلى الدالة `shoot_arrow()` وأضف متغيرين جديدين `arrow_x` و `arrow_y` لتخزين الأرقام العشوائية بين `100` و `300`.

--- code ---
---
language: python filename: main.py line_numbers: true
line_highlights: 9-10
---
def shoot_arrow():    
arrow_x = randint(100, 300)    
arrow_y = randint(100, 300)    
hit_color = get(arrow_x, arrow_y) #احفظ اللون قبل رسم السهم   
ellipse(arrow_x, arrow_y, 15, 15)

--- /code ---

--- /task ---


--- task ---


ابحث عن التعليق **# تنتقل دالة mouse_pressed هنا** وأدناه أضف رمزًا لتعريف دالة `mouse_pressed()`. You should see the arrow jump around the target.

![الهدف ، مع سهم دائري بني يظهر في مواضع مختلفة.](images/fire_arrow.gif)

--- /task ---

--- save ---
