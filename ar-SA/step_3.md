## ارسم هدفك

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Your game needs a target to shoot arrows at.
</div>
<div>

![منطقة المخرجات مع الهدف وحامل الهدف.] 
(images/three-circles.png) {"width="300px:}

</div>
</div>

### Draw a triangular stand

--- task ---

Set the fill colour to `wood` (brown).

Draw a triangle using the x and y coordinates for each of the corners.

![A brown triangle on grass and against a sky with the coordinate points labelled at 150, 350 and 200, 150 and 250, 350). The corners of the canvas are also labelled as x=0, y=0 in the top left and x=400, y=400 i the bottom right.](images/stand_coords.png){:width="400px"}

--- code ---
---
language: python filename: main.py - draw() line_numbers: true line_number_start: 28
line_highlights: 37-40
---
  fill(grass)   
rect(0, 250, 400, 150) #محور س, محور ص, العرض, الارتفاع

--- /code ---

--- /task ---

--- task ---

**اختبار:** قم بتشغيل التعليمات برمجية الخاص بك لمعرفة الحامل لهدفك.

![مثلث بني على العشب وقبالة السماء.](images/target-stand.png){:width="400px"}

--- /task ---

### ارسم الهدف

--- task ---

حامل الهدف هو شكل المثلث الهدف مكون من دوائر ملونة - الدوائر الأصغر تساوي نقاطًا أكثر من الدوائر الأكبر.

Set the fill colour to `outer` (blue).

Draw a circle with x and y coordinates for its centre and a width.

![A brown triangle and blue circle on grass and against a sky. The circle is labelled with the coordinates x=200, y=200 as the centre and circle width of 170.](images/circle-coords.png){:width="400px"}

--- code ---
---
language: python filename: main.py - draw() line_numbers: true line_number_start: 31
line_highlights: 31-32
---

  fill(wood) # اضبط لون تعبئة الحامل على البني     
triangle(150, 350, 200, 150, 250, 350)

--- /code ---

--- /task ---

--- task ---

**نصيحة:** لعمل دائرة ، يجب أن يكون **العرض** و **ارتفاع** هو نفسه.

The blue circle was drawn after the stand so it is in front:

![مثلث بني ودائرة زرقاء على العشب وقبالة السماء.](images/blue-circle.png){:width="400px"}

--- /task ---

--- task ---

قم بتعيين الألوان للمتغيرات `inner` و `bullseye` باستخدام `color()`.

قم بإنشاء متغيرين جديدين لتخزين الألوان `inner` و `bullseye` للدوائر المتبقية.

تتوقع الدالة `color()` ثلاثة أرقام: رقم واحد للأحمر والأخضر والأزرق.

--- code ---
---
language: python filename: main.py - draw() line_numbers: true line_number_start: 33
line_highlights: 33-34
---
sky = color(92, 204, 206)   
grass = color(149, 212, 122)   
wood = color(145, 96, 51)   
outer = color(0, 120, 180) #ازرق     
inner = color(210, 60, 60) # احمر     
bullseye = color(220, 200, 0) #أصفر

--- /code ---

--- /task ---

الهدف مكون من دوائر مختلفة الحجم بنفس إحداثيات المركز (200 ، 200) - منتصف الشاشة.

--- task ---

**اختبار:** قم بتشغيل مشروعك مرة أخرى لرؤية الهدف بثلاث دوائر ملونة.

--- code ---
---
language: python filename: main.py - draw() line_numbers: true line_number_start: 18
line_highlights: 24-25
---
  fill(wood)    
triangle(150, 350, 200, 150, 250, 350) #حامل الهدف    
fill(outer)   
ellipse(200, 200, 170, 170) #الدائرة الخارجية   
fill(inner)   
ellipse(200, 200, 110, 110) #الدائرة الداخلية    
fill(bullseye)   
ellipse(200, 200, 30, 30) #مركز الهدف

--- /code ---

--- /task ---

--- task ---

**اختبار:** قم بتشغيل التعليمات البرمجية الخاص بك لرؤية أول دائرة زرقاء كبيرة.

![مثلث بني به ثلاث دوائر ملونة على العشب ومقابل السماء.](images/three-circles.png){:width="400px"}

**تتبع الخطأ:** تستخدم Python التهجئة الأمريكية لـ "color" (بدون "u") لذا تأكد من فعل الشيء نفسه.

--- /task ---

--- task ---

استخدمنا الأرقام التي تعطي ألوانًا تقليدية لهدف الرماية ، ولكن يمكنك استخدام الألوان التي تريدها طالما أنها مختلفة عن بعضها البعض.

[[[generic-theory-simple-colours]]]

![مثلث بني على العشب وضد السماء مع تحديد نقاط الإحداثيات. The colours have changed to pinks and purples.](images/alternative-colours.png){:width="400px"}


--- /task ---



