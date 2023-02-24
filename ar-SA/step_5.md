## تسجيل النقاط

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Your game will add scores based on where the arrow hits.
</div>
<div>

! [الهدف ، مع ظهور السهم في مواضع مختلفة ، وتظهر النتائج كنص أسفل اللعبة.](images/points-scored.gif){:width="300px"}

</div>
</div>

--- task ---

Go to the `draw()` function and add `, outer, inner, middle` to the list of global variables.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 26
line_highlights: 28
---

def draw():
# أشياء للقيام بها في كل إطار
  global outer, inner, bullseye    
sky = color(92, 204, 206) #احمر = 92, اخضر = 204, ازرق = 206    
grass = color(149, 212, 122)    
wood = color(145, 96, 51)    
outer = color(0, 120, 180)    
inner = color(210, 60, 60)   
bullseye = color(220, 200, 0)

--- /code ---

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
نحن نستخدم <span style="color: #0faeb0; font-weight: bold;"> شروط</span> طوال الوقت لاتخاذ القرارات. يمكننا أن نقول 'إذا كان القلم غير حاد ، فقم جعله حادا'. وبالمثل ، تتيح لنا شروط `if` كتابة رمز يقوم بشيء مختلف اعتمادًا على ما إذا كان الشرط صحيحًا أم خطأ.
</p>

### Display the scores

--- task ---

Delete ❌ the `print( red(hit_color), green(hit_color), blue(hit_color) )` line of code.

--- code ---
---
قم بتغيير التعليمات البرمجية الموجود في `print()` لإعطاء درجة:
line_highlights: 10-11
---
# تذهب دالة mouse_pressed هنا
def mouse_pressed():


--- /code ---

--- /task ---

--- task ---

`print` رسالة للدائرة الخارجية للهدف ، أضف رمزًا لوظيفة `mouse_pressed()` للتحقق مما إذا كانت `hit_color` هي `==` إلى `outer`.

يستخدم لاختبار **تكافؤ** - مثل `hit_color == bullseye` - إذا كانت الأشياء على كلا الجانبين لها نفس القيمة ، فإن الاختبار هو `True`، وإلا فهو `False`

--- code ---
---
language: python filename: main.py - mouse_pressed() line_numbers: true line_number_start: 9
line_highlights: 12-15
---

# The mouse_pressed function goes here
def mouse_pressed():     
if hit_color == outer:      
print('You hit the outer circle, 50 points!') #Like دالة ، يتم وضع مسافة بادئة لعبارات 'if'

--- /code ---

--- /task ---

--- task ---

**اختبار:** قم بتشغيل مشروعك. حاول إيقاف السهم الموجود على الدوائر الحمراء والصفراء لرؤية رسائلهم.

**نصيحة:** `frame_rate()`، في `setup()`، يتحكم في مدى سرعة رسم لعبتك. إذا كان الأمر سريعًا جدًا ، فاضبطه على رقم أقل.

![منطقة مخرجات مع سهم يلمس الدائرة الخارجية. تظهر عبارة طباعة النقاط في منطقة مخرجات.](images/blue-points.png)

**تصحيح الأخطاء:** تأكد من أن `elif` في نفس مستوى المسافة البادئة مثل `if`، وأن الكود الموجود داخل `elif` في نفس مستوى الرمز الموجود داخل `if`.

--- /task ---

لا يمكن استخدام `elif` إلا مع عبارة `if` ، ومثل `if`، يتحقق الشرط. These will be read from top to bottom. As soon as a **True** condition is found, it will be actioned. The remaining conditions will be ignored.

--- task ---

Score points if the arrow lands on the `inner` or `middle` circles 🎯:

--- code ---
---
language: python filename: main.py - mouse_pressed() line_numbers: true line_number_start: 8
line_highlights: 16-17
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

**اختبار:** قم بتشغيل مشروعك. حاول إيقاف السهم الموجود على الدائرة الخارجية الزرقاء لرؤية رسالتك.

![منطقة مخرجات مع سهم يلمس الدائرة الداخلية. تظهر عبارة طباعة النقاط في منطقة مخرجات.](images/yellow-points.png)

**تصحيح:** تأكد من تطابق التعليمات البرمجية تمامًا وقمت بوضع مسافة بادئة التعليمات البرمجية داخل عبارة `if`.

**التصحيح:** إذا رأيت رسالة حول `inner` or `bullseye` كونها 'غير محددة' ، فارجع إلى `draw()` وتأكد من أنها على السطر الذي يعلن عن المتغيرات عامة.

--- /task ---

### Missing the target

هناك قرار آخر يتعين عليك اتخاذه: ماذا يحدث إذا لم يسقط السهم على أي من الدوائر المستهدفة؟ ❌

لإجراء هذا الفحص الأخير ، يمكنك استخدام `else`.

--- task ---

أضف الكود إلى `print` رسالة `else` لم يتم استيفاء أي من عبارات `if` و `elif`.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 9
line_highlights: 15, 16
---

def mouse_pressed():    
if hit_color == outer:   
print('You hit the outer circle, 50 points!')   
elif hit_color == inner:   
print('You hit the inner circle, 200 points!')   
elif hit_color == bullseye:    
print('You hit the bullseye, 500 points!')   
else:   
print('You missed! No points!')

--- /code ---

--- /task ---

--- task ---

**اختبار:** قم بتشغيل مشروعك. حاول إيقاف السهم في العشب أو السماء لرؤية الرسالة المفقودة.

قم بتغيير عدد النقاط المسجلة للألوان المختلفة إذا أردت.

![منطقة مخرجات بسهم يفتقد الهدف. تظهر عبارة طباعة النقاط في منطقة مخرجات.](images/missed-points.png)

--- /task ---

