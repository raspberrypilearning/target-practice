## Scocca la tua freccia

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Add an even smaller circle to represent an arrow.
</div>
<div>

![Il bersaglio, con una freccia circolare marrone che appare in varie posizioni.](images/fire_arrow.gif){:width="300px"}

</div>
</div>

### Where will you shoot?

--- task ---

Aggiungi il codice per disegnare casualmente un cerchio marrone all'interno di un'area target:

--- code ---
---
language: python filename: main.py — shoot_arrow() line_numbers: true line_number_start: 7
line_highlights: 8-12
---
# La funzione shoot_arrow va qui
def shoot_arrow():   
arrow_x = randint(100, 300)  # Memorizza un numero a caso fra 100 e 300 arrow_y = randint(100, 300)  # Memorizza un numero a caso fra 100 e 300 fill('sienna')  # Imposta la freccia in modo che il colore di riempimento sia marrone circle(arrow_x, arrow_y, 15)  # Disegna un piccolo cerchio a coordinate casuali

--- /code ---

--- /task ---

--- task ---

Vai alla funzione `draw` e chiama la tua nuova funzione `shoot_arrow` .

--- code ---
---
language: python filename: main.py — draw() line_numbers: true line_number_start: 31
line_highlights: 33
---

    fill('yellow')  # Imposta il colore di riempimento del cerchio su giallo
    circle(200, 200, 30)  # Disegna il cerchio interno usando x, y, larghezza
    shoot_arrow()

--- /code ---

--- /task ---

--- task --- **Test:** Click the **Run** button. You should see the arrow in the centre.

![a brown arrow circle in the centre of the target](images/arrow-centre.png) --- /task ---

The arrow needs to move randomly.

language: python filename: main.py — shoot_arrow() line_numbers: true line_number_start: 7

--- code ---
---
language: python filename: main.py - mouse_pressed() line_numbers: true line_number_start: 5
line_highlights: 9, 12
---
def shoot_arrow(): global hit_colour  # Può essere utilizzato in altre funzioni arrow_x = randint(100, 300)  # Memorizza un numero a caso fra 100 e 300 arrow_y = randint(100, 300)  # Memorizza un numero a caso fra 100 e 300 hit_colour = get(arrow_x, arrow_y).hex  # Ottieni il colore colpito fill('sienna')  # Imposta la freccia in modo che il colore di riempimento sia marrone circle(arrow_x, arrow_y, 15)  # Disegna un piccolo cerchio a coordinate casuali

--- /code ---

--- /task ---


--- task ---


**Test:** 🔄 Esegui il tuo progetto. You should see the arrow jump around the target.

![Un'animazione del bersaglio con una freccia circolare marrone che appare in diverse posizioni.](images/fire_arrow.gif)

--- /task ---

--- save ---
