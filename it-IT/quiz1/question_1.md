## Quiz veloce

Rispondi alle tre domande. Ci sono alcuni suggerimenti per aiutarti a trovare la risposta corretta.

Dopo aver risposto a ciascuna domanda, fai clic su **Controlla la mia risposta**.

Divertiti!

--- question ---
---
legend: Domanda 1 di 3
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

È corretto. Se non utilizzi questa funzione verrà disegnato un bordo nero attorno alle tue forme.

  --- /feedback ---

- ( ) It makes the arrow move randomly around the screen.

  --- feedback ---

Non proprio. This code part of how the arrow moves randomly but you need other code too to achieve that goal.

  --- /feedback ---

- ( ) Riempie la forma con un dato colore.

  --- feedback ---

  Non proprio. La funzione fill() fa questo e di solito includerà un dato colore.

  --- /feedback ---

- ( ) It draws a circle of a random size.

  --- feedback ---

  Non proprio. La funzione circle() verrebbe utilizzata per disegnare un cerchio.

  --- /feedback ---

--- /choices ---

--- /question ---
