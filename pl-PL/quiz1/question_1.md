## Szybki quiz

Odpowiedz na trzy pytania. Istnieją wskazówki, które poprowadzą Cię do prawidłowej odpowiedzi.

Po udzieleniu odpowiedzi na każde pytanie kliknij ** Sprawdź moją odpowiedź **.

Miłej zabawy!

--- question ---
---
legend: Pytanie 1 z 3
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

Zgadza się. This chooses a random x coordinate for your arrow.

  --- /feedback ---

- ( ) It makes the arrow move randomly around the screen.

  --- feedback ---

Nie do końca. This code part of how the arrow moves randomly but you need other code too to achieve that goal.

  --- /feedback ---

- () It gets the colour that was hit by the arrow.

  --- feedback ---

  Nie do końca. The get() function would be used to get the colour.

  --- /feedback ---

- ( ) It draws a circle of a random size.

  --- feedback ---

  Nie do końca. Funkcja circle() zostanie użyta do narysowania koła.

  --- /feedback ---

--- /choices ---

--- /question ---
