## Snelle quiz

Beantwoord de drie vragen. Je wordt naar het juiste antwoord geleid.

Klik na het beantwoorden van elke vraag op **Controleer mijn antwoord**.

Veel plezier!

--- question ---
---
legend: Vraag 1 van 3
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

Dat klopt. This chooses a random x coordinate for your arrow.

  --- /feedback ---

- ( ) It makes the arrow move randomly around the screen.

  --- feedback ---

Niet helemaal. This code part of how the arrow moves randomly but you need other code too to achieve that goal.

  --- /feedback ---

- () It gets the colour that was hit by the arrow.

  --- feedback ---

  Niet helemaal. De functie fill() doet dit en bevat meestal een bepaalde kleur.

  --- /feedback ---

- ( ) Er wordt een cirkelvorm in jouw programma getekend.

  --- feedback ---

  Niet helemaal. De functie circle() zou worden gebruikt om een cirkel te tekenen.

  --- /feedback ---

--- /choices ---

--- /question ---
