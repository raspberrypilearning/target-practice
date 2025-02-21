## Ρίξε το βέλος σου

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Τώρα ήρθε η ώρα να προσθέσεις ένα βέλος που κινείται τυχαία στην περιοχή του στόχου.
</div>
<div>

![Ο στόχος, με ένα καφέ κυκλικό βέλος να εμφανίζεται σε διάφορες θέσεις.](images/fire_arrow.gif){:width="300px"}

</div>
</div>

### Μάθε το χρώμα που χτυπά το βέλος

--- task ---

Βρες το σχόλιο **#Η συνάρτηση shoot_arrow πηγαίνει εδώ** και από κάτω πρόσθεσε κώδικα για να ορίσεις τη συνάρτηση `shoot_arrow()`.

--- code ---
---
language: python line_numbers: true line_number_start: 8
line_highlights: 11-12
---
# Η συνάρτηση shoot_arrow πηγαίνει εδώ
language: python filename: main.py — shoot_arrow() line_numbers: true line_number_start: 10

--- /code ---

--- /task ---

--- task ---

Call your new `shoot_arrow()`{:.language-python} function at the end of your `draw()`{:.language-python} function.

--- code ---
---
language: python line_numbers: true line_number_start: 33
line_highlights: 44-45
---

    fill('yellow')      
    circle(200, 200, 30)  
    shoot_arrow()

--- /code ---

--- /task ---

--- task --- **Test:** Click the **Run** button. You should see the arrow in the centre.

![a brown arrow circle in the centre of the target](images/arrow-centre.png) --- /task ---

The arrow needs to move randomly.

--- task --- Change the `arrow_x`{:.language-python} and `arrow_y`{:.language-python} variables to choose a random number between 100 and 300.

--- code ---
---
language: python line_numbers: true line_number_start: 9
line_number_start: 3
---
def shoot_arrow(): arrow_x = randint(100, 300) arrow_y = randint(100, 300) fill('brown') circle(arrow_x, arrow_y, 15)

--- /code ---

--- /task ---


--- task ---


**Test:** Click the **Run** button. You should see the arrow jump around the target.

![Ο στόχος στο φόντο με ένα καφέ κυκλικό βέλος πάνω του.](images/fire_arrow.gif)

--- /task ---

--- save ---
