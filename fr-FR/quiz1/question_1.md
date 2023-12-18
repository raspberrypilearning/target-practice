## Questionnaire rapide

Réponds aux trois questions. Il y a des indices pour te guider vers la bonne réponse.

Lorsque tu as répondu à chaque question, clique sur **Vérifier ma réponse**.

Amuse-toi bien !

--- question ---
---
legend : Question 1 sur 3
---
In your project you added no_stroke() to your setup function. What does the no_stroke() function do?

--- code ---
---
language: python
---

def setup():   
size(400, 400)      
no_stroke()

--- /code ---

--- choices ---

- ( ) It draws a shape using the coordinates given.

  --- feedback ---

Not quite. The size() function does this in this example.

  --- /feedback ---

- ( ) It fills the shape with a given colour.

  --- feedback ---

Not quite. The fill() function does this and will usually include a given colour.

  --- /feedback ---

- (x) It turns off the border(stroke) for all the shapes.

  --- feedback ---

  C'est correct ! A black border will be drawn around your shapes if you do not use this function.

  --- /feedback ---

- ( ) It will draw a circle shape in your program.

  --- feedback ---

  Not quite. The circle() function would be used to draw a circle.

  --- /feedback ---

--- /choices ---

--- /question ---
