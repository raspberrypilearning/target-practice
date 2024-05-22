## Erstelle einen Hintergrund

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Dein Spiel braucht einen farbenfrohen Hintergrund.
</div>
<div>

![Der Ausgabebereich mit einem himmelfarbenen Rechteck über einem grasfarbenen Rechteck, um den Hintergrund zu erstellen.](images/background.png){:width="300px"}

</div>
</div>

### Öffne das Starterprojekt

--- task ---

Öffne das Projekt [Zielübungsstarter](https://editor.raspberrypi.org/de-DE/projects/target-practice-starter){:target="_blank"}. Der Code Editor wird in einem anderen Tab im Browser geöffnet.

Wenn du ein Raspberry Pi Konto hast, kannst du auf **Speichern** klicken, um eine Kopie in deinen **Projekten** zu speichern.

--- /task ---

### Bearbeite den Himmel

--- task ---

Für das Starterprojekt ist bereits Code geschrieben.

Klicke auf **„Ausführen“**, um ein blau gefülltes Rechteck zu sehen, das bei x=`0`, y=`0` (oben auf dem Bildschirm) beginnt. Dieses `400` x `250` Pixel große Rechteck ist der Himmel.

![Ein blaues Rechteck mit einem schwarzen Rand darüber, darüber ein graues Rechteck. Die obere linke Ecke der Leinwand ist mit x=0, y=0 markiert. Dies ist der Ursprung des Rechtecks. Die Breite wird mit 400 und die Höhe mit 250 hervorgehoben. Der Code rect(0, 0, 400, 250) wird angezeigt.](images/sky_stroke.png){:width="400px"}

**Tipp:** 💡 Die Koordinaten beginnen bei (x=0, y=0) in der oberen linken Ecke. Dies kann sich von anderen Koordinatensystemen unterscheiden, die Du mal verwendet hast.

--- /task ---

--- task ---

Der Himmel wurde mit einem schwarzen Rand (Strich, engl.: „stroke“) gezeichnet.

Um den Strich für alle Formen auszuschalten, füge `no_stroke()` zur `aufsetzen` Funktion hinzu:

--- code ---
---
language: python
filename: main.py — setup()
line_numbers: true
line_number_start: 9
line_highlights: 12
---
def setup():
# Richte hier Dein Spiel ein
    size(400, 400)  # Breite und Höhe des Bildschirms
    no_stroke()

--- /code ---

--- /task ---

--- task ---

Führe mit **Ausführen** deinen Code erneut aus und beachte 👀, dass der Rand (stroke) jetzt verschwunden ist.

**Tipp:** 💡 Du musst **Stopp** drücken, um dein Programm zu stoppen. Dadurch wird die Schaltfläche **Ausführen** wieder erscheinen.

--- /task ---

### Zeichne das Gras

--- task ---

**Füge** Code hinzu, um ein grünes Rechteck am unteren Bildschirmrand zu zeichnen.

![Der Ausgabebereich mit einem himmelfarbenen Rechteck über einem grasfarbenen Rechteck, um den Hintergrund zu erstellen. Die obere linke Ecke des Rechtecks ist mit x=0, y=250 markiert. Dies ist der Ursprung des Rechtecks. Die Breite wird mit 400 und die Höhe mit 150 hervorgehoben. Der Code rect(0, 250, 400, 150) wird angezeigt.](images/green-grass.png){:width="400px"}

--- code ---
---
language: python
filename: main.py — draw()
line_numbers: true
line_number_start: 14
line_highlights: 18-19
---
def draw():
# Dinge die in jedem Frame passieren
    fill('cyan')  # Setzt die Füllfarbe für den Himmel auf Cyan
    rect(0, 0, 400, 250)  # Zeichnet ein Rechteck für den Himmel mit diesen Werten für x, y, Breite, Höhe
    fill('lightgreen')  # Stelle die Füllfarbe für das Gras auf Hellgrün ein
    rect(0, 250, 400, 150)  # Zeichnet ein Rechteck für das Gras mit diesen Werten für x, y, Breite, Höhe

--- /code ---

**Tipp:** 💡 Wir haben Kommentare zu unserem Code hinzugefügt, wie etwa `# Setzt die Füllfarbe für den Himmel auf Cyan`, um dir zu sagen, was es bewirkt. Du musst deinem Code keine Kommentare hinzufügen, aber sie sind hilfreich, um dich daran zu erinnern, was Codezeilen bewirken.

--- /task ---

--- task ---

**Test:** 🔄 Führe dein Projekt erneut aus, um den fertigen Hintergrund anzuzeigen.

![Der Ausgabebereich mit einem himmelfarbenen Rechteck über einem grasfarbenen Rechteck, um den Hintergrund zu erstellen.](images/background.png){:width="400px"}

--- /task ---

--- save ---
