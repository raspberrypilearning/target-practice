## Zeichne das Gras

--- task ---

Öffne das Projekt [Zielübungsstarter](https://editor.raspberrypi.org/en/projects/target-practice-starter){:target="_blank"}.

--- /task ---


--- task ---

**Füge** Code hinzu, um ein grünes Rechteck am unteren Bildschirmrand zu zeichnen.

![Der Ausgabebereich mit einem himmelfarbenen Rechteck über einem grasfarbenen Rechteck, um den Hintergrund zu erstellen. Die obere linke Ecke des Rechtecks ist mit x=0, y=250 markiert. Dies ist der Ursprung des Rechtecks. Die Breite wird mit 400 und die Höhe mit 150 hervorgehoben. Der Code rect(0, 250, 400, 150) wird angezeigt.](images/green-grass.png){:width="400px"}

--- code ---
---
language: python filename: main.py — draw() line_numbers: true line_number_start: 14
line_highlights: 12
---
def draw(): # Things to do in every frame fill('cyan')  
rect(0, 0, 400, 250)  
fill('lightgreen')  
rect(0, 250, 400, 150) --- /code ---

--- /task ---

--- task ---

**Test:** 🔄 Führe dein Projekt erneut aus, um den fertigen Hintergrund anzuzeigen.

![Der Ausgabebereich mit einem himmelfarbenen Rechteck über einem grasfarbenen Rechteck, um den Hintergrund zu erstellen.](images/background.png){:width="400px"}

--- /task ---

--- save ---
