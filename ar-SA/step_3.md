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

قم بتعيين الألوان للمتغيرات `inner` و `bullseye` باستخدام `color()`.

Draw a triangle using the x and y coordinates for each of the corners.

![A brown triangle on grass and against a sky with the coordinate points labelled at 150, 350 and 200, 150 and 250, 350). The corners of the canvas are also labelled as x=0, y=0 in the top left and x=400, y=400 in the bottom right.](images/stand_coords.png){:width="400px"}

--- code ---
---
language: python filename: main.py - draw() line_numbers: true line_number_start: 18
line_highlights: 24-25
---

    fill('lightgreen')  # Set the fill colour for the grass to light green
    rect(0, 250, 400, 150)  # Draw a rectangle for the grass with these values for x, y, width, height
    fill('sienna')  # Brown colour
    triangle(150, 350, 200, 150, 250, 350)  # Draw a triangle for the target's stand

--- /code ---

--- /task ---

--- task ---

**اختبار:** قم بتشغيل التعليمات برمجية الخاص بك لمعرفة الحامل لهدفك.

![مثلث بني على العشب وقبالة السماء.](images/target-stand.png){:width="400px"}

--- /task ---

### ارسم الهدف

--- task ---

**نصيحة:** لعمل دائرة ، يجب أن يكون **العرض** و **ارتفاع** هو نفسه.

قم بإنشاء متغيرين جديدين لتخزين الألوان `inner` و `bullseye` للدوائر المتبقية.

Draw a circle with x and y coordinates for its centre and a width.

![A brown triangle and blue circle on grass and against a sky. The circle is labelled with the coordinates x=200, y=200 as the centre and circle width of 170.](images/circle-coords.png){:width="400px"}

--- code ---
---
language: python filename: main.py - draw() line_numbers: true line_number_start: 33
line_highlights: 31-32
---

    fill(wood)<br x-id="3" />
      triangle(150, 350, 200, 150, 250, 350)<br x-id="3" />
      fill(outer)<br x-id="4" />
      ellipse(200, 200, 170, 170) #الدائرة الخارجية.

--- /code ---

--- /task ---

--- task ---

**اختبار:** قم بتشغيل التعليمات البرمجية الخاص بك لرؤية أول دائرة زرقاء كبيرة.

The blue circle was drawn after the stand so it is in front.

![مثلث بني ودائرة زرقاء على العشب وقبالة السماء.](images/blue-circle.png){:width="400px"}

--- /task ---

الهدف مكون من دوائر مختلفة الحجم بنفس إحداثيات المركز (200 ، 200) - منتصف الشاشة.

--- task ---

**اختبار:** قم بتشغيل مشروعك مرة أخرى لرؤية الهدف بثلاث دوائر ملونة.

--- code ---
---
language: python filename: main.py - draw() line_numbers: true line_number_start: 28
line_highlights: 33-34
---

    fill('sienna')  # Brown colour
    triangle(150, 350, 200, 150, 250, 350)  # Draw a triangle for the target's stand 
    fill('blue')  # Set the circle fill colour to blue
    circle(200, 200, 170)  # Draw the outer circle
    fill('red')  # Set the colour for the circle fill to red
    circle(200, 200, 110)  # Draw the inner circle using x, y, width
    fill('yellow')  # Set the colour for the circle fill to yellow      
    circle(200, 200, 30)  # Draw the middle circle using x, y, width

--- /code ---

--- /task ---

--- task ---

**تتبع الخطأ:** تستخدم Python التهجئة الأمريكية لـ "color" (بدون "u") لذا تأكد من فعل الشيء نفسه.

![مثلث بني به ثلاث دوائر ملونة على العشب ومقابل السماء.](images/three-circles.png){:width="400px"}

--- /task ---

--- task ---

**Choose:** 💭 Change any of the colours using a different colour name. You can find a list of all of the available colour names on [W3 Schools](https://www.w3schools.com/colors/colors_names.asp){:target="blank"}.

![مثلث بني على العشب وضد السماء مع تحديد نقاط الإحداثيات. The colours have changed to pinks and purples.](images/alternative-colours.png){:width="400px"}

--- collapse ---
---
title: Example code using different colours
---

--- code ---
---
language: python filename: main.py - draw() line_numbers: true line_number_start: 31
line_highlights: 37-40
---

def draw():
# أشياء يجب القيام بها في كل إطار

    fill('BlueViolet')
    rect(0, 0, 400, 250)  # Sky
    fill('DeepSkyBlue')
    rect(0, 250, 400, 150)  # Ground
    fill('FireBrick')
    triangle(150, 350, 200, 150, 250, 350)  # Stand
    fill('LemonChiffon')
    circle(200, 200, 170)  # Outer circle
    fill('DeepPink')
    circle(200, 200, 110)  # Inner circle
    fill('BlueViolet')
    circle(200, 200, 30)  # Middle circle

--- /code ---

--- /collapse ---

--- /task ---

--- save ---
