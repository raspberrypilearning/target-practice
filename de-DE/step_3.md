## Zeichne deine Zielscheibe

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Dein Spiel braucht ein Ziel, auf das du mit Pfeilen schießen kannst.
</div>
<div>

![Der Ausgabebereich mit der Zielscheibe und dem Ständer.](images/ three-circles.png){:width="300px"}

</div>
</div>

### Zeichne einen dreieckigen Ständer

--- task ---

Stelle die Füllfarbe auf `sienna` (Braun) ein.

Zeichne ein Dreieck mit den x- und y-Koordinaten für jede Ecke.

![Ein braunes Dreieck auf Gras und vor einem Himmel mit den Koordinatenpunkten 150, 350 und 200, 150 und 250, 350). Die Ecken der Leinwand sind außerdem oben links mit x=0, y=0 und unten rechts mit x=400, y=400 beschriftet.](images/stand_coords.png){:width="400px"}

--- code ---
---
language: python filename: main.py - draw() line_numbers: true line_number_start: 18
line_highlights: 20, 21
---

    fill('lightgreen')  # Stelle die Füllfarbe für das Gras auf Hellgrün ein
    rect(0, 250, 400, 150)  # Zeichnet ein Rechteck für das Gras mit diesen Werten für x, y, Breite, Höhe
    fill('sienna')  # Braune Farbe
    triangle(150, 350, 200, 150, 250, 350)  # Zeichne ein Dreieck für den Zielstand

--- /code ---

--- /task ---

--- task ---

**Test:** 🔄 Führe deinen Code aus, um den Ständer für deine Zielscheibe zu sehen:

![Ein braunes Dreieck auf Gras und vor einem Himmel.](images/target-stand.png){:width="400px"}

--- /task ---

### Zeichne die Zielkreise

--- task ---

Der größte Teil der Zielscheibe ist ein blauer **Kreis** (engl.: „circle“).

Stelle die Füllfarbe auf `blue` (blau) ein.

Zeichne einen Kreis mit x- und y-Koordinaten als Mittelpunkt, und einer Breite.

![Ein braunes Dreieck und ein blauer Kreis auf Gras und vor einem Himmel. Der Kreis ist mit den Koordinaten x=200, y=200 als Mittelpunkt und der Kreisbreite 170 beschriftet.](images/circle-coords.png){:width="400px"}

--- code ---
---
language: python filename: main.py - draw() line_numbers: true line_number_start: 20
line_highlights: 22, 23
---

    fill('sienna')  # Braune Farbe
    triangle(150, 350, 200, 150, 250, 350)  # Zeichne ein Dreieck für den Zielstand
    fill('blue')  # Stelle die Füllfarbe auf blue (blau) ein
    circle(200, 200, 170)  # Zeichne den äußeren Kreis

--- /code ---

--- /task ---

--- task ---

**Test:** Führe deinen Code aus, um den ersten großen blauen Kreis zu sehen.

Der blaue Kreis wurde nach dem Ständer gezeichnet, sodass er davor liegt.

![Ein braunes Dreieck und ein blauer Kreis auf Gras und vor einem Himmel.](images/blue-circle.png){:width="400px"}

--- /task ---

Die Zielscheibe besteht aus unterschiedlich großen Kreisen mit denselben Mittelpunktskoordinaten (200, 200).

--- task ---

**Füge** farbige Kreise für den inneren und mittleren Teil der Zielscheibe hinzu.

--- code ---
---
language: python filename: main.py - draw() line_numbers: true line_number_start: 20
line_highlights: 24, 25, 26, 27
---

    fill('sienna')  # Braune Farbe
    triangle(150, 350, 200, 150, 250, 350)  # Zeichne ein Dreieck für den Zielstand
    fill('blue')  # Stelle die Füllfarbe auf blue (blau) ein
    circle(200, 200, 170)  # Zeichne den äußeren Kreis
    fill('red')  # Stelle die Farbe für die Kreisfüllung auf red (rot) ein
    circle(200, 200, 110)  # Zeichne den inneren Kreis mit x, y, Breite
    fill('yellow')  # Stelle die Farbe für die Kreisfüllung auf yellow (gelb) ein
    circle(200, 200, 30)  # Zeichne den mittleren Kreis mit x, y, Breite

--- /code ---

--- /task ---

--- task ---

**Test:** 🔄 Führe dein Projekt aus, um die Zielscheibe mit drei farbigen Kreisen zu sehen.

![Ein braunes Dreieck mit drei farbigen Kreisen auf Gras und vor einem Himmel.](images/three-circles.png){:width="400px"}

--- /task ---

--- save ---
