## Feuere deinen Pfeil ab

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Wenn du klickst oder tippst, wird ein Pfeil auf die Position eines sich bewegenden Zielkreises abgefeuert. 
</div>
<div>

![Die Zielscheibe, mit einem braunen kreisförmigen Pfeil, der an verschiedenen Positionen erscheint.](images/fire_arrow.gif){:width="300px"}

</div>
</div>

### Zeichne in jedem Frame einen Zielkreis

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;"> Computer erzeugen den Bewegungseffekt, indem sie viele Bilder nacheinander anzeigen. Jedes Bild wird als <span style="color: #0faeb0; font-weight: bold;"> Frame </span> (deutsch: „Einzelbild“) bezeichnet.   
</p>

--- task ---

Definiere deine Funktion `schiess_pfeil()` unter dem Kommentar **# Die Funktion „schiess_pfeil“ kommt hierher**.

Füge Code hinzu, um zufällig einen braunen Kreis innerhalb eines Zielbereichs zu zeichnen:

![Ein Rechteck, das die Koordinaten des Zielbereichs in einem halbtransparenten Rechteck anzeigt. Der Zielbereich liegt zwischen x=100 und y=100 bis x=300 und y=300, deckt also die gesamte Zielscheibe und darüber hinaus ab.](images/target_area.png)

--- code ---
---
language: python
filename: main.py — shoot_arrow()
line_numbers: true
line_number_start: 7
line_highlights: 8-12
---
# Die Funktion „schiess_pfeil“ kommt hierher
def schiess_pfeil():   
    pfeil_x = randint(100, 300)  # Speichere eine zufällige Zahl zwischen 100 und 300
    pfeil_y = randint(100, 300)  # Speichere eine zufällige Zahl zwischen 100 und 300
    fill('sienna')  # Stelle die Füllfarbe des Pfeils auf Braun ein
    circle(pfeil_x, pfeil_y, 15)  # Zeichne einen kleinen Kreis an zufälligen Koordinaten

--- /code ---

--- /task ---

--- task ---

Finde die Funktion `draw` (deutsch: „Zeichne“) und rufe dort deine neue Funktion `schiess_pfeil` auf.

--- code ---
---
language: python
filename: main.py — draw()
line_numbers: true
line_number_start: 31
line_highlights: 33
---
    fill('yellow')  # Stelle die Farbe für die Kreisfüllung auf yellow (gelb) ein
    circle(200, 200, 30)  # Zeichne den mittleren Kreis mit x, y, Breite
    schiess_pfeil()

--- /code ---

--- /task ---

--- task ---

**Test:** 🔄 Führe deinen Code aus und sieh, wie der Pfeil in jedem Frame an einer zufälligen Position erscheint.

![Eine Animation eines Ziels mit einem braunen Kreispfeil, der an verschiedenen Positionen erscheint.](images/fire_arrow.gif)

Der Hintergrund und die Zielscheibe werden über den alten Pfeil gezeichnet. Das bedeutet, dass du immer nur einen Pfeil siehst.

--- /task ---

### Hol dir die Farbe, die vom Pfeil getroffen wird

Die Funktion `get()` (deutsch: „holen“) gibt die Farbe eines Pixels zurück.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Ein <span style="color: #0faeb0; font-weight: bold;">Pixel</span> ist ein einzelner farbiger Punkt innerhalb eines Bildes. Bilder bestehen aus vielen farbigen Pixeln.
</p>

--- task ---

Füge eine **globale Variable** mit dem Namen `getroffene_farbe` hinzu, die im gesamten Code verwendet werden kann.

Füge Code zu `get` hinzu, um die Farbe des Pixels in der Mitte des Pfeils zu erhalten, und sie in der Variablen `getroffene_farbe` zu speichern. Um die Farben vergleichen zu können, müssen wir den Hexadezimalcode verwenden. Dies kann mit der Zeichenfolge `.hex` erfolgen.

--- code ---
---
language: python
filename: main.py — shoot_arrow() 
line_numbers: true
line_number_start: 7
line_highlights: 9, 12
---
# Die Funktion „schiess_pfeil“ kommt hierher
def schiess_pfeil():
    global getroffene_farbe  # Kann in anderen Funktionen verwendet werden  
    pfeil_x = randint(100, 300)  # Speichere eine zufällige Zahl zwischen 100 und 300
    pfeil_y = randint(100, 300)  # Speichere eine zufällige Zahl zwischen 100 und 300
    getroffene_farbe = get(pfeil_x, pfeil_y).hex  # Get the hit colour     
    fill('sienna')  # Hol dir die getroffene Farbe
    circle(pfeil_x, pfeil_y, 15)  # Zeichne einen kleinen Kreis an zufälligen Koordinaten
  
--- /code ---

​**Tipp:** 💡 Der Code in `get` zum Abrufen der Farbe muss **vor** dem Code zum Zeichnen des `circle` (deutsch: „Kreis“) stehen, sonst speicherst du immer die Holzfarbe des Pfeils!

--- /task ---

### Gib die Farbe aus, wenn die Maus gedrückt wird

Die `p5`-Bibliothek „horcht“ auf bestimmte Ereignisse, eines davon ist das Drücken der Maustaste. Wenn sie erkennt, dass die Taste gedrückt wurde, führt es den Code aus, die ihr in der Funktion `mouse_pressed` (deutsch: mouse = Maus, pressed = gedrückt) gegeben wurde.

--- task ---

Definiere deine Funktion `mouse_pressed()` unter dem Kommentar **# Die Funktion „mouse_pressed“ kommt hierher**.

Füge Code hinzu, um das Ziel-Emoji 🎯 auszudrucken, wenn mit der Maus geklickt wird.

--- code ---
---
language: python
filename: main.py - mouse_pressed()
line_numbers: true
line_number_start: 5
line_highlights: 6
---

# Die Funktion „mouse_pressed“ kommt hierher
def mouse_pressed():    
    print('🎯')

--- /code ---

--- /task ---

--- task --- 

**Test:** 🔄 Führe dein Projekt aus.

Das Projekt gibt jedes Mal 🎯 aus, wenn der Pfeil neu gezeichnet wird.

![Eine Animation eines Ziels mit einem braunen Kreispfeil, der an verschiedenen Positionen erscheint.](images/fire_arrow.gif)

**Debug:** 🐞 Wenn du eine Meldung siehst, dass `getroffene_farbe` „not defined“ (deutsch: „nicht definiert“) ist, gehe zurück zu `schiess_pfeil()` und überprüfe, ob du die Zeile `global getroffene_farbe` hinzugefügt hast.

**Debug:** 🐞 Überprüfe die `print`-Zeile sehr sorgfältig auf Kommas und Klammern.

--- /task ---

--- save ---
