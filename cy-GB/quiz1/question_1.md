## Beth nesaf?

Answer the three questions. There are hints to guide you to the correct answer.

Atebwch y tri chwestiwn isod i fyfyrio ar yr hyn rydych chi wedi'i ddysgu.

Ar ôl bob cwestiwn, pwyswch **cyflwyno**. Byddi di'n cael dy dywys i'r ateb cywir. Galli di wneud hyn gymaint ag y mynni.

--- question ---
---
legend: Cwestiwn 1 o 3
---
In your project you added no_stroke() to your setup function. What does the no_stroke() function do?

Dyma sgŵar glas. Beth yw'r gwerthoedd RGB a fydd yn ei greu?
---
language: python
---

def setup():   
size(400, 400)      
no_stroke()

--- /code ---

--- choices ---

- ( ) (0, 0, 0)

  --- feedback ---

Not quite. The size() function does this in this example.

  --- /feedback ---

- ( ) (255, 0, 0)

  --- feedback ---

Not quite. The fill() function does this and will usually include a given colour.

  --- /feedback ---

- (x) (0, 0, 255)

  --- feedback ---

  That's correct. A black border will be drawn around your shapes if you do not use this function.

  --- /feedback ---

- ( ) (255, 255, 255)

  --- feedback ---

  Not quite. The circle() function would be used to draw a circle.

  --- /feedback ---

--- /choices ---

--- /question ---
