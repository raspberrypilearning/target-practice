## Add an arrow

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Add an even smaller circle to represent an arrow.
</div>
<div>

![Die Zielscheibe, mit einem braunen kreisförmigen Pfeil, der an verschiedenen Positionen erscheint.](images/fire_arrow.gif){:width="300px"}

</div>
</div>

### Where will you shoot?

--- task ---

Füge Code hinzu, um zufällig einen braunen Kreis innerhalb eines Zielbereichs zu zeichnen:

--- code ---
---
language: python filename: main.py — shoot_arrow() line_numbers: true line_number_start: 7
line_highlights: 8-12
---
# Die Funktion „schiess_pfeil“ kommt hierher
def schiess_pfeil(): global getroffene_farbe  # Kann in anderen Funktionen verwendet werden  
pfeil_x = randint(100, 300)  # Speichere eine zufällige Zahl zwischen 100 und 300 pfeil_y = randint(100, 300)  # Speichere eine zufällige Zahl zwischen 100 und 300 getroffene_farbe = get(pfeil_x, pfeil_y).hex  # Get the hit colour     
fill('sienna')  # Hol dir die getroffene Farbe circle(pfeil_x, pfeil_y, 15)  # Zeichne einen kleinen Kreis an zufälligen Koordinaten

--- /code ---

--- /task ---

--- task ---

Finde die Funktion `draw` (deutsch: „Zeichne“) und rufe dort deine neue Funktion `schiess_pfeil` auf.

--- code ---
---
language: python filename: main.py — draw() line_numbers: true line_number_start: 31
line_highlights: 33
---

    fill('yellow')  # Stelle die Farbe für die Kreisfüllung auf yellow (gelb) ein
    circle(200, 200, 30)  # Zeichne den mittleren Kreis mit x, y, Breite
    schiess_pfeil()

--- /code ---

--- /task ---

--- task ---

**Test:** 🔄 Führe dein Projekt aus. You should see the arrow in the centre.

![a brown arrow circle in the centre of the target](images/arrow-centre.png)


--- /task ---

The arrow needs to move randomly.


--- task ---

Change the `arrow_x`{:.language-python} and `arrow_y`{:.language-python} variables to choose a random number between 100 and 300.

--- code ---
---
language: python filename: main.py - mouse_pressed() line_numbers: true line_number_start: 5
line_highlights: 9, 12
---
def schiess_pfeil():   
pfeil_x = randint(100, 300)  # Speichere eine zufällige Zahl zwischen 100 und 300 pfeil_y = randint(100, 300)  # Speichere eine zufällige Zahl zwischen 100 und 300 fill('sienna')  # Stelle die Füllfarbe des Pfeils auf Braun ein circle(pfeil_x, pfeil_y, 15)  # Zeichne einen kleinen Kreis an zufälligen Koordinaten

--- /code ---

--- /task ---


--- task ---


**Test:** Click the **Run** button. You should see the arrow jump around the target.

![Eine Animation eines Ziels mit einem braunen Kreispfeil, der an verschiedenen Positionen erscheint.](images/fire_arrow.gif)

--- /task ---

--- save ---
