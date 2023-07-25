## تسجيل النقاط

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Your game will add scores based on where the arrow hits.
</div>
<div>

![الهدف ، مع ظهور السهم في مواضع مختلفة ، وتظهر النتائج كنص أسفل اللعبة.](images/points-scored.gif){:"width="300px}

</div>
</div>

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
نستخدم  <span style="color: #0faeb0; font-weight: bold;"> if … else </span> لاتخاذ القرارات. We could say 'if the pencil is blunt, then sharpen it'. Similarly, `if` conditions let us write code that do something different depending on whether a condition is true or false.
</p>

### Display the scores

--- task ---

Delete ❌ the `print('🎯')` line of code.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 9
line_highlights: 28
---
# The mouse_pressed function goes here
def draw():


--- /code ---

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
نحن نستخدم <span style="color: #0faeb0; font-weight: bold;"> شروط</span> طوال الوقت لاتخاذ القرارات. يمكننا أن نقول 'إذا كان القلم غير حاد ، فقم جعله حادا'. وبالمثل ، تتيح لنا شروط `if` كتابة رمز يقوم بشيء مختلف اعتمادًا على ما إذا كان الشرط صحيحًا أم خطأ.
</p>

--- task ---

`print` رسالة للدائرة الخارجية للهدف ، أضف رمزًا لوظيفة `mouse_pressed()` للتحقق مما إذا كانت `hit_color` هي `==` إلى `outer`.

كن حذرًا عند استخدام الرمز `=` في بايثون:

--- code ---
---
language: python filename: main.py - mouse_pressed() line_numbers: true line_number_start: 8
line_highlights: 10-11
---

# تذهب دالة mouse_pressed هنا
def mouse_pressed():    
if hit_color == outer:    
print('You hit the outer circle, 50 points!')    
elif hit_color == inner:    
print('You hit the inner circle, 200 points!')   
elif hit_color == bullseye:    
print('You hit the bullseye, 500 points!')

--- /code ---

**Tip:** 💡 If you changed the colour of your outer circle then you will need to replace `'blue'` with the colour name that you have chosen.

--- /task ---

--- task ---

**اختبار:** قم بتشغيل مشروعك. حاول إيقاف السهم الموجود على الدوائر الحمراء والصفراء لرؤية رسائلهم.

**نصيحة:** `frame_rate()`، في `setup()`، يتحكم في مدى سرعة رسم لعبتك. إذا كان الأمر سريعًا جدًا ، فاضبطه على رقم أقل.

![منطقة مخرجات مع سهم يلمس الدائرة الخارجية. تظهر عبارة طباعة النقاط في منطقة مخرجات.](images/blue-points.png)

**Debug:** 🐞 Check that you have used the American spelling of 'Color' (without a 'u') and that 'Color' is capitalised.

ما يجعل `elif` مختلفًا هو أنه سيتم فقط التحقق مما إذا كانت شروط `if` وأي `elif` قبل أن تكون `False`.

يستخدم لاختبار **تكافؤ** - مثل `hit_color == bullseye` - إذا كانت الأشياء على كلا الجانبين لها نفس القيمة ، فإن الاختبار هو `True`، وإلا فهو `False`

--- /task ---

لا يمكن استخدام `elif` إلا مع عبارة `if` ، ومثل `if`، يتحقق الشرط. These will be read from top to bottom. As soon as a **True** condition is found, it will be actioned. Any remaining conditions will be ignored.

--- task ---

Score points if the arrow lands on the `inner` or `middle` circles 🎯:

--- code ---
---
language: python filename: main.py - mouse_pressed() line_numbers: true line_number_start: 9
line_highlights: 12-15
---

def mouse_pressed(): if hit_colour == Color('blue').hex:   
print('You hit the outer circle, 50 points!') elif hit_colour == Color('red').hex: print('You hit the inner circle, 200 points!') elif hit_colour == Color('yellow').hex: print('You hit the middle, 500 points!')

--- /code ---

--- /task ---

--- task ---

**اختبار:** قم بتشغيل مشروعك. Try to fire the arrow on the inner and middle circles to see their messages.

![منطقة مخرجات مع سهم يلمس الدائرة الداخلية. تظهر عبارة طباعة النقاط في منطقة مخرجات.](images/yellow-points.png)

**تصحيح:** تأكد من تطابق التعليمات البرمجية تمامًا وقمت بوضع مسافة بادئة التعليمات البرمجية داخل عبارة `if`.

**التصحيح:** إذا رأيت رسالة حول `inner` or `bullseye` كونها 'غير محددة' ، فارجع إلى `draw()` وتأكد من أنها على السطر الذي يعلن عن المتغيرات عامة.

**تصحيح الأخطاء:** تأكد من أن `elif` في نفس مستوى المسافة البادئة مثل `if`، وأن الكود الموجود داخل `elif` في نفس مستوى الرمز الموجود داخل `if`.

يستخدم من أجل **تخصيص** - مثل `arrow_x = 200` لتعيين قيمة متغير

--- /task ---

### Missing the target

هناك قرار آخر يتعين عليك اتخاذه: ماذا يحدث إذا لم يسقط السهم على أي من الدوائر المستهدفة؟ ❌

لإجراء هذا الفحص الأخير ، يمكنك استخدام `else`.

--- task ---

أضف الكود إلى `print` رسالة `else` لم يتم استيفاء أي من عبارات `if` و `elif`.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 26
line_highlights: 16-17
---

def mouse_pressed():     
if hit_color == outer:      
print('You hit the outer circle, 50 points!') elif hit_colour == Color('red').hex: print('You hit the inner circle, 200 points!') elif hit_colour == Color('yellow').hex: print('You hit the middle, 500 points!') else:   
print('You missed! No points!')

--- /code ---

--- /task ---

--- task ---

**اختبار:** قم بتشغيل مشروعك. حاول إيقاف السهم في العشب أو السماء لرؤية الرسالة المفقودة.

**Choose:** 💭 Change the number of points scored for the different colours.

--- /task ---

--- save ---
