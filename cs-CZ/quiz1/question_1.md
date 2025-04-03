## Quick quiz

Answer the three questions. There are hints to guide you to the correct answer.

When you have answered each question, click on **Check my answer**.

Have fun!

--- question ---
---
legend: Question 1 of 3
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

That's correct. This chooses a random x coordinate for your arrow.

  --- /feedback ---

- ( ) It makes the arrow move randomly around the screen.

  --- feedback ---

Not quite. This code part of how the arrow moves randomly but you need other code too to achieve that goal.

  --- /feedback ---

- () It gets the colour that was hit by the arrow.

  --- feedback ---

  Not quite. The get() function would be used to get the colour.

  --- /feedback ---

- ( ) It draws a circle of a random size.

  --- feedback ---

  Not quite. The circle() function would be used to draw a circle.

  --- /feedback ---

--- /choices ---

--- /question ---
