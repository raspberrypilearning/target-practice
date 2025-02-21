## Beth nesaf?

Answer the three questions. There are hints to guide you to the correct answer.

Atebwch y tri chwestiwn isod i fyfyrio ar yr hyn rydych chi wedi'i ddysgu.

Ar ôl bob cwestiwn, pwyswch **cyflwyno**. Byddi di'n cael dy dywys i'r ateb cywir. Galli di wneud hyn gymaint ag y mynni.

--- question ---
---
legend: Cwestiwn 1 o 3
---
In your project you added `randint(100, 300)` to your `shoot_arrow()` function. What does `randint(100, 300)` do?

Dyma sgŵar glas. Beth yw'r gwerthoedd RGB a fydd yn ei greu?
---
language: python
---

def shoot_arrow(): global hit_colour arrow_x = randint(100, 300) arrow_y = randint(100, 300)

--- /code ---

--- choices ---

- ( ) (0, 0, 0)

  --- feedback ---

That's correct. This chooses a random x coordinate for your arrow.

  --- /feedback ---

- ( ) (255, 0, 0)

  --- feedback ---

Not quite. This code part of how the arrow moves randomly but you need other code too to achieve that goal.

  --- /feedback ---

- (x) (0, 0, 255)

  --- feedback ---

  Not quite. The get() function would be used to get the colour.

  --- /feedback ---

- ( ) (255, 255, 255)

  --- feedback ---

  Not quite. The circle() function would be used to draw a circle.

  --- /feedback ---

--- /choices ---

--- /question ---
