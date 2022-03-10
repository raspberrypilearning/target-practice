## أطلق سهمك

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
حان الوقت الآن لإضافة سهم يتحرك بشكل عشوائي عبر المنطقة المستهدفة.
</div>
<div>

![الهدف بسهم دائري بني يظهر في عدة مواضع.](images/fire_arrow.gif){:"width="300px}

</div>
</div>

--- task ---

ابحث عن التعليق **# تنتقل دالة shoot_arrow هنا** وأدناه أضف التعليمات البرمجية لتعريف دالتك `shoot_arrow()`.

أضف صغير `()ellipse` في وسط الشاشة لتمثيل السهم.

--- code ---
---
language: python 
filename: main.py — shoot_arrow() 
line_numbers: true 
line_number_start: 10
line_highlights: 11-12
---

#تذهب دالة shoot_arrow هنا
def shoot_arrow():   
  ellipse(200, 200, 15, 15)

--- /code ---

--- /task ---

--- task ---

اذهب إلى الكود `draw()` الذي ينشئ الهدف وأضف الكود في النهاية لتعيين `fill()` إلى `wood`، ثم استدعي وظيفة `shoot_arrow()` الجديدة.

--- code ---
---
language: python 
filename: main.py — draw() 
line_numbers: true 
line_number_start: 41
line_highlights: 44-45
---

  fill(bullseye)    
  ellipse(200, 200, 30, 30)

  fill(wood)   
  shoot_arrow()

--- /code ---

--- /task ---

--- task ---

**اختبار:** قم بتشغيل التعليمات البرمجية الخاصة بك وشاهد السهم يظهر في مركز الهدف.

![الهدف على الخلفية مع سهم دائري بني عليه.](images/arrow-middle.png)

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;"> ألعاب الكمبيوتر ومقاطع الفيديو والرسوم المتحركة تخلق تأثير الحركة من خلال عرض الكثير من الصور واحدة تلو الأخرى. كل صورة تسمى <span style="color: #0faeb0; font-weight: bold;"> إطار </span>. تسمى السرعة التي تتغير بها الصورة  <span style="color: #800080;">معدل الإطارات</span> وتعطى بمعدل <span style="color: #800080;">إطارًا في الثانية</span> أو إطارات في الثانية.  
</p>

`frame_rate(2)` في سطر `setup()` يضبط معدل الإطارات على إطارين في الثانية.

دالة `draw()` تستدعى في كل اطار. ستقوم برسم السهم في موضع عشوائي في كل مرة يتم استدعاء `draw()`.

سيتم رسم الخلفية والهدف فوق السهم القديم. هذا يعني أنك ترى سهمًا واحدًا فقط في كل مرة.

--- task ---

ابحث عن عبارات `import` ، في الجزء العلوي من الكود الخاص بك ، ستستخدم `randint` من مكتبة `random`.

--- code ---
---
language: python 
filename: main.py 
line_numbers: true
line_number_start: 3
---

#استيراد مكتبة الشفرات البرمجية
from p5 import *    
from math import *    
from random import randint

--- /code ---

--- /task ---

--- task ---

انتقل إلى الدالة `shoot_arrow()` وأضف متغيرين جديدين `arrow_x` و `arrow_y` لتخزين الأرقام العشوائية بين `100` و `300`.

سيسمح هذا لبعض التسديدات بتفويت الهدف ، دون أن تصل إلى أطراف لعبتك.

قم بتغيير `ellipse()` لاستخدام المتغيرات الجديدة لموقع السهم الخاص بك.

![مستطيل يوضح إحداثيات المنطقة المستهدفة في مستطيل شبه شفاف.](images/target_area.png)

--- code ---
---
language: python 
filename: main.py — shoot_arrow() 
line_numbers: true 
line_number_start: 10
line_highlights: 12-14
---

#تذهب دالة shoot_arrow هنا
def shoot_arrow():    
  arrow_x = randint(100, 300)   
  arrow_y = randint(100, 300)    
  ellipse(arrow_x, arrow_y, 15, 15) #التحديث إلى الإحداثيات العشوائية

--- /code ---

--- /task ---

### احصل على اللون الذي يضربه السهم

ترجع الدالة `get()` لون البكسل.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
<span style="color: #0faeb0; font-weight: bold;">بكسل</span>، اختصار لعنصر الصورة ، هو نقطة ملونة واحدة داخل الصورة. تتكون الصور من الكثير من وحدات البكسل الملونة.
</p>

--- task ---

تحتاج إلى تخزين اللون الذي يستهدفه السهم قبل رسم سهم فوقه.

أضف رمزًا لتخزين `hit_color`. استخدم وظيفة `get()` ، للحصول على لون البكسل عند إحداثيات `arrow_x` و `arrow_y` - مركز السهم.

--- code ---
---
language: python 
filename: main.py — shoot_arrow() 
line_numbers: true 
line_number_start: 10
line_highlights: 14
---

#تذهب دالة shoot_arrow هنا
def shoot_arrow():    
  arrow_x = randint(100, 300)    
  arrow_y = randint(100, 300)    
  hit_color = get(arrow_x, arrow_y) #احفظ اللون قبل رسم السهم   
  ellipse(arrow_x, arrow_y, 15, 15)

--- /code ---

**نصيحة:** يجب أن يكون التعليمات البرمجية للحصول على اللون وحفظه هو **قبل** التعليمات البرمجية لرسم القطع الناقص وإلا ستحفظ دائمًا لون الخشب للسهم!

--- /task ---

مكتبة `p5` 'تستمع' لأحداث معينة ، أحد هذه الأحداث هو الضغط على زر الفأرة. عندما يكتشف أنه تم الضغط على الزر ، فإنه سيعمل على تشغيل أي كود تم تقديمه في دالة `mouse_pressed()`.

--- task ---

ابحث عن التعليق **# تنتقل دالة mouse_pressed هنا** وأدناه أضف رمزًا لتعريف دالة `mouse_pressed()`.

أضف رمزًا لطباعة كميات الأحمر والأخضر والأزرق في البكسل الذي يستقر عليه السهم.

--- code ---
---
language: python 
filename: main.py - mouse_pressed() 
line_numbers: true 
line_number_start: 8
line_highlights: 9-10
---

#تذهب دالة mouse_pressed هنا
def mouse_pressed():    
  print( red(hit_color), green(hit_color), blue(hit_color) )

--- /code ---

--- /task ---

--- task ---

لقد عينت دالتين `shoot_arrow()` و `mouse_pressed()`، كلتا دالتين تحتاجان إلى استخدام المتغير `hit_color`.

يُعرف المتغير الذي يجب استخدامه في جميع أنحاء البرنامج بــ**المتغير العام**. أضف الكود إلى الدالة `shoot_arrow()` لجعل `hit_color` متغيرًا عالميًا:

--- code ---
---
language: python 
filename: main.py - shoot_arrow() 
line_numbers: true 
line_number_start: 12
line_highlights: 14
---

#تذهب دالة shoot_arrow هنا
def shoot_arrow():    
  global hit_color #يمكن استخدامها في دالة أخرى     
  arrow_x = randint(100, 300)     
  arrow_y = randint(100, 300)     
  hit_color = get(arrow_x, arrow_y) #احفظ اللون قبل رسم السهم     
  ellipse(arrow_x, arrow_y, 15, 15)

--- /code ---

--- /task ---

--- task ---

**اختبار:** قم بتشغيل مشروعك. يتم إعادة رسم السهم في إحداثيات عشوائية.

يحصل المشروع على `hit_color` في كل مرة يتم فيها إعادة رسم السهم ويطبع قيمة اللون في منطقة المخرجات أسفل الهدف.

![الهدف ، مع سهم دائري بني يظهر في مواضع مختلفة.](images/fire_arrow.gif)

**التصحيح:** إذا كنت ترى رسالة حول `hit_colour` 'غير معرّف' ، فارجع إلى `shoot_arrow()` وتأكد من أن لديك سطر`global hit_color`.

**تصحيح الأخطاء:** تحقق من سطر `print` بعناية بحثًا عن الفواصل والأقواس.

--- /task ---

--- save ---

