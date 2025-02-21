## Kurzes Quiz

Beantworte die drei Fragen. Hinweise helfen dir beim Finden der richtigen Antwort.

Nach dem Beantworten der Fragen wähle **Meine Antwort prüfen**.

Viel Spaß!

--- question ---
---
legend: Frage 1 von 3
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

Richtig. Wenn du diese Funktion nicht verwendest, wird ein schwarzer Rand um deine Formen gezeichnet.

  --- /feedback ---

- ( ) It makes the arrow move randomly around the screen.

  --- feedback ---

Nicht ganz. This code part of how the arrow moves randomly but you need other code too to achieve that goal.

  --- /feedback ---

- () It gets the colour that was hit by the arrow.

  --- feedback ---

  Nicht ganz. Die Funktion fill() erledigt dies und enthält normalerweise eine bestimmte Farbe.

  --- /feedback ---

- ( ) Es wird eine Kreisform in das Programm gezeichnet.

  --- feedback ---

  Nicht ganz. Die Funktion „circle()“ wird zum Zeichnen eines Kreises verwendet.

  --- /feedback ---

--- /choices ---

--- /question ---
