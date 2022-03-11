
--- question ---
---
legend: السؤال 2 من 3
---

في مشروعك ، استخدمت `if` و `elif`و `else` للتحقق من اللون الذي سقط عليه السهم.

عند تشغيل هذا التعليمات البرمجية ، ما الذي سيتم طباعته في منطقة المخرجات ؟

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

  لا ، مع عبارة else ، سيكون هناك دائمًا شيء صحيح. لذلك ، ستتم طباعة المخرجات.

  --- /feedback ---

--- /choices ---

--- /question ---
