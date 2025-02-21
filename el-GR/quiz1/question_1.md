## Αναστοχασμός

Answer the three questions. There are hints to guide you to the correct answer.

Απάντησε στις τρεις ερωτήσεις παρακάτω για να διαπιστώσεις τι έμαθες.

Have fun!

--- question ---
---
legend: Ερώτηση 1 από 3
---
In your project you added `randint(100, 300)` to your `shoot_arrow()` function. What does `randint(100, 300)` do?

Εδώ είναι ένα μπλε τετράγωνο, ποιες είναι οι τιμές RGB που θα το δημιουργήσουν;
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
