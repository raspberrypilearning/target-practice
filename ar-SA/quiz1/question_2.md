
--- question ---
---
legend: السؤال 2 من 3
---

في مشروعك ، استخدمت `if` و `elif`و `else` للتحقق من اللون الذي سقط عليه السهم.

In the example below, a variable called `speed` has the number `6` stored in it. عند تشغيل هذا التعليمات البرمجية ، ما الذي سيتم طباعته في منطقة المخرجات ؟

--- code ---
---
language: python
---
speed = 6

if speed == 7: print('Super fast') elif speed == 5: print('Pretty quick') elif speed == 6: print('Very fast') else: print('Speed not recognised!')

--- /code ---

--- choices ---

- سريع جدًا

  --- feedback ---

  هذا صحيح! تم تخصيص متغير **speed** للقيمة `6`، مما يجعل `speed == 6` شرط **صحيح** ويطبع `سريع جدًا`.

  --- /feedback ---

- ( ) `لا يمكن تمييز السرعة!`

  --- feedback ---

  ليس تمامًا ، انظر إلى القيمة المخصصة للمتغير **speed**.

  --- /feedback ---

- لا تتم طباعة أي شيء

  --- feedback ---

  Try again, `else` is used as a final option for when all the above conditions are false. Look through the conditions again, are any of the conditions true?

  --- /feedback ---

--- /choices ---

--- /question ---
