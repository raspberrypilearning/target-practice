
--- question ---
---
legend: Питання 2 з 3
---

У твоєму проєкті використовувалися умови `if`, `elif` та `else`, щоб перевірити, на який колір влучила стріла.

У наступному прикладі змінна з назвою `speed` зберігає число `6`. Що буде надруковано в області виводу, коли ми запустимо умову `if`?

--- code ---
---
language: python
---
speed = 6

if speed == 7:
    print('Надзвичайно швидко')
elif speed == 5:
    print('Досить швидко')
elif speed == 6:
    print('Дуже швидко')
else:
    print('Не вдається розпізнати швидкість!') 

--- /code ---

--- choices ---

- (x) `Дуже швидко`

  --- feedback ---

  Правильно! Змінній **speed** було присвоєно значення `6`. Це означає, що умова `speed == 6` **справджується** (True), і код виведе на екран `Дуже швидко`.

  --- /feedback ---

- ( ) `Не вдається розпізнати швидкість!`

  --- feedback ---

  Не зовсім так. Подивися на значення, присвоєне змінній **speed**.

  --- /feedback ---

- ( ) Нічого не буде надруковано

  --- feedback ---

  Спробуй ще раз. `else` використовується тоді, коли всі попередні умови є хибними. Подивись ще раз на умови, чи справджуються вони?

  --- /feedback ---

--- /choices ---

--- /question ---
