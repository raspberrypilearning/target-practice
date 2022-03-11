## قم بإنشاء خلفية

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
تتكون السماء والعشب من خلال كتابة كود لرسم مستطيلات ملونة.
</div>
<div>

! [منطقة مخرجات مع مستطيل بلون السماء فوق مستطيل بلون العشب لإنشاء الخلفية.] (images / background.png) {: "width = "300px}

</div>
</div>

--- task ---

افتح مشروع [بداية الرماية](https://trinket.io/python/9973649e5c){: "target = "_ blank}.

إذا كان لديك حساب Trinket ، فيمكنك النقر فوق الزر **Remix** لحفظ نسخة في مكتبة `My Trinkets`.

--- /task ---

يحتوي مشروع البداية على بعض التعليمات البرمجية المكتوبة بالفعل لاستيراد مكتبة `p5` ، وسوف تستخدم هذه المكتبة لبناء لعبة الرماية الخاصة بك.

[[[p5-processing-library]]]

--- task ---

تقوم دالة `fill()` بتعيين اللون الداخلي للأشكال. يحتوي مشروع مبتدئ بالفعل على بعض ألوان RGB التي يمكنك استخدامها للقيام بذلك.

ابحث عن دالة `()draw` واستعد لرسم السماء عن طريق إضافة تعليمات البرمجية ذي مسافة بادئة لتعيين ` ()fill` لون إلى `سماء`:

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

  fill(sky)

--- /code ---

--- /task ---

دالة `()size` تستدعى في `()setup` يعين حجم الشاشة على 400 بكسل × 400 بكسل.

[[[p5-coordinates]]]

--- task ---

بعد `() fill` التعليمات البرمجية ، ارسم `() rect` للسماء مع الإحداثيات العلوية اليسرى (`0`،`0`) ، بعرض</code> `عرض الشاشة والارتفاع من`250`.</p>

<p spaces-before="0"><img src="images/sky_coords.png" alt="مستطيل أزرق مع شبكة إحداثيات توضح موضع مستطيل السماء بدءًا من الزاوية العلوية ، فوق مستطيل رمادي." /></p>

<p spaces-before="0">--- code ---</p>

<hr />

<p spaces-before="0">language: python
filename: main.py — draw()
line_numbers: true
line_number_start: 25 </p>

<h2 spaces-before="0">line_highlights: 26</h2>

<p spaces-before="2">fill(sky)
  rect(0, 0, 400, 250) #ابداء محور س, ابداء محور ص, عرض, ارتفاع</p>

<p spaces-before="0">--- /code ---</p>

<p spaces-before="0">--- /task ---</p>

<p spaces-before="0">--- task ---</p>

<p spaces-before="0"><strong x-id="1">اختبار:</strong> قم بتشغيل الكود الخاص بك لرؤية السماء التي رسمتها. تذكر أنه مع مكتبة <code>p5` ، تستدعي وظيفة `() run ` وظيفة `() setup ` مرة واحدة ، ثم دالة `() draw ` بشكل متكرر.

![مستطيل أزرق حوله حدود سوداء وفوق مستطيل رمادي.](images/sky_stroke.png){:width="300px"}

هذا غريب بعض الشيء: هناك خط أسود حول السماء! هذا لأنه ، عندما يبدأ البرنامج ، يقوم تلقائيًا بتعيين حد أسود - يسمى **ضربة** - حول كل شيء يرسمه.

--- /task ---

--- task ---

قم بإيقاف تشغيل الحد بإضافة `()no_stroke ` قبل أن تبدأ في رسم السماء.

--- code ---
---
language: python filename: main.py — draw() line_numbers: true line_number_start: 23
line_highlights: 25
---

  outer = color(0, 120, 180)

  no_stroke()   
fill(sky)   
rect(0, 0, 400, 250) #x, y, width, height

--- /code ---

--- /task ---

--- task ---

**اختبار:** قم بتشغيل مشروعك مرة أخرى لعرض الخلفية النهائية.

--- /task ---

--- task ---

` () fill` يغير لون التعبئة لجميع الأشكال المرسومة حتى يتم استدعاء ` () fill` مرة أخرى بلون جديد.

قم بتغيير لون التعبئة ` ()fill` إلى `grass` وأضف `rect(x, y, width, height)`.

يجب وضع هذا المستطيل أسفل السماء عند الإحداثيات (0 ، 250) ، بحيث يبدأ في الجزء السفلي من الشاشة.

--- code ---
---
language: python filename: main.py — draw() line_numbers: true line_number_start: 23
line_highlights: 28-29
---

  outer = color(0, 120, 180)

  no_stroke()     
fill(sky)     
rect(0, 0, 400, 250) #محور س, محور ص, العرض, الارتفاع    
fill(grass)    
rect(0, 250, 400, 150)

--- /code ---

--- /task ---

--- task ---

**اختبار:** قم بتشغيل مشروعك مرة أخرى لعرض الخلفية النهائية.

--- /task ---

--- save ---
