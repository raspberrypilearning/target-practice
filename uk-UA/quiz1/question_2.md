
--- question ---
---
legend: Питання 2 з 3
---

У твоєму проєкті використовувалися умови `if` , `elif`, та `else`, щоб перевірити, на який колір влучила стріла.

У наступному прикладі, змінна з назвою `speed` має число `6`, який вказано в ній. Коли інструкція `if` буде виконуватися, що буде надруковано в області виводу?

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
 print('Швидкість не розпізнано!')

--- /code ---

--- choices ---

- (x) `Дуже швидко`

  --- feedback ---

  Правильно! Змінній **speed** було присвоєно значення `6`, що робить умову `speed == 6` **True** та надрукує `Дуже швидко`.

  --- /feedback ---

- ( ) `Швидкість не розпізнано!`

  --- feedback ---

  Не зовсім так, подивись на значення, яке присвоєно змінній **speed**.

  --- /feedback ---

- ( ) Нічого не буде надруковано

  --- feedback ---

  Спробуй ще раз, `else` використовується лише в тому випадку, коли всі вищезазначені умови є хибними. Подивись ще раз на умови, чи відповідають вони істині?

  --- /feedback ---

--- /choices ---

--- /question ---
