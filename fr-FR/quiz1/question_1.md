## Questionnaire rapide

Réponds aux trois questions. Il y a des indices pour te guider vers la bonne réponse.

Lorsque tu as répondu à chaque question, clique sur **Vérifier ma réponse**.

Amuse-toi bien !

--- question ---
---
legend : Question 1 sur 3
---
In your project you added `randint(100, 300)` to your `shoot_arrow()` function. What does `randint(100, 300)` do?

--- code ---
---
language: python
---

def shoot_arrow(): global hit_colour arrow_x = randint(100, 300) arrow_y = randint(100, 300)

--- /code ---

--- choices ---

- (x) It chooses a random whole number between 100 and 300.

  --- feedback ---

C'est correct ! Une bordure noire sera dessinée autour de tes formes si tu n'utilises pas cette fonction.

  --- /feedback ---

- ( ) It makes the arrow move randomly around the screen.

  --- feedback ---

Pas tout à fait. This code part of how the arrow moves randomly but you need other code too to achieve that goal.

  --- /feedback ---

- ( ) Elle remplit la forme avec une couleur donnée.

  --- feedback ---

  Pas tout à fait. La fonction fill() fait cela et inclura généralement une couleur donnée.

  --- /feedback ---

- ( ) Elle dessinera une forme de cercle dans ton programme.

  --- feedback ---

  Pas tout à fait. La fonction circle() serait utilisée pour dessiner un cercle.

  --- /feedback ---

--- /choices ---

--- /question ---
