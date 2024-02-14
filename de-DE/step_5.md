## Punkten

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Dein Spiel vergibt Punkte je nachdem, wo der Pfeil auftrifft.
</div>
<div>

![Eine Animation der Zielscheibe, wobei der Pfeil an verschiedenen Positionen erscheint und Punkte als Text unter dem Spiel angezeigt werden.](images/points-scored.gif){:width="300px"}

</div>
</div>

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Wir verwenden ständig <span style="color: #0faeb0; font-weight: bold;"> Bedingungen</span>, um Entscheidungen zu treffen. Wir könnten sagen: „Wenn der Bleistift stumpf ist, dann spitzt Du ihn“. In ähnlicher Weise können wir mit „if“-Bedingungen (deutsch „Wenn“) Code schreiben, der etwas anderes tut, je nachdem, ob eine Bedingung wahr oder falsch ist.
</p>

### Punkte anzeigen

--- task ---

Lösche ❌ die Codezeile `print('🎯')`.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 5
line_highlights: 7
---
# Die Funktion „mouse_pressed“ kommt hierher
def mouse_pressed():


--- /code ---

--- /task ---

--- task ---

Zeigt eine Meldung **wenn** die `getroffene_farbe` gleich der `äußeren` Kreisfarbe (blue, deutsch: blau) ist 🎯.

Beachte 👀, dass im Code zwei Gleichheitszeichen `==` verwendet werden, um **gleich** zu bedeuten.

--- code ---
---
language: python filename: main.py - mouse_pressed() line_numbers: true line_number_start: 5
line_highlights: 7, 8
---

# Die Funktion „mouse_pressed“ kommt hierher
def mouse_pressed():     
if hit_colour == Color('blue').hex:  # Like the code in functions, the code in 'if' statements is indented print('You hit the outer circle, 50 points!')

--- /code ---

**Tipp:** 💡 Wenn du die Farbe deines äußeren Kreises geändert hast, musst du `„blue“` durch den von dir gewählten Farbnamen ersetzen.

--- /task ---

--- task ---

**Test:** 🔄 Führe dein Projekt aus. Versuche, den Pfeil auf den blauen äußeren Kreis abzufeuern, um die Ausgabe zu sehen.

**Tipp:** 💡 Mit dem Argument `frame_rate=2` (deutsch: Einzelbildrate), in `run` am Ende deines Codes kannst du steuern, wie schnell das Spiel die Bilder zeichnet. Wenn es zu schnell geht, stell eine niedrigere Zahl ein.

![Der Ausgabebereich mit Pfeil, der den äußeren Kreis berührt. Die Punktemeldung wird im Ausgabebereich angezeigt.](images/blue-points.png)

**Debug:** 🐞 Stelle sicher, dass dein Code genau übereinstimmt und dass du den Code innerhalb deiner `if` -Anweisung eingerückt hast.

**Debug:** 🐞 Stelle sicher, dass du den richtigen Farbnamen eingegeben hast, den du für **deinen** äußeren Kreis verwendet hast.

--- /task ---

`elif` (kurz für else - if, deutsch: sonst - wenn) kann verwendet werden, um deiner `if`-Anweisung weitere Bedingungen hinzuzufügen. Diese werden von oben nach unten gelesen. Sobald eine **wahre**-Bedingung gefunden wird, wird der entsprechende eingerückte Code darunter ausgeführt. Alle verbleibenden Bedingungen werden ignoriert.

--- task ---

Erziele Punkte, wenn der Pfeil auf den `inneren` oder `mittleren` Kreisen landet 🎯:

--- code ---
---
language: python filename: main.py - mouse_pressed() line_numbers: true line_number_start: 6
line_highlights: 9-12
---

def mouse_pressed(): if hit_colour == Color('blue').hex:   
print('You hit the outer circle, 50 points!') elif hit_colour == Color('red').hex: print('You hit the inner circle, 200 points!') elif hit_colour == Color('yellow').hex: print('You hit the middle, 500 points!')

--- /code ---

--- /task ---

--- task ---

**Test:** 🔄 Führe dein Projekt aus. Versuche, den Pfeil auf den inneren und den mittleren Kreis abzufeuern, um die jeweiligen Ausgaben zu sehen.

![Der Ausgabebereich mit Pfeil, der den inneren Kreis berührt. Die Punktemeldung wird im Ausgabebereich angezeigt.](images/yellow-points.png)

**Debug:** 🐞 Überprüfe, ob deine Einrückungen mit dem Beispiel übereinstimmt.

**Debug:** 🐞 Wenn du eine Meldung siehst, dass `getroffene_farbe` „not defined“ (deutsch: „nicht definiert“) ist, gehe zurück zu `draw()` und überprüfe, ob die Zeile `getroffene_farbe` als eine globale Variable deklariert.

**Debug:** 🐞 Stelle sicher, dass du den richtigen Farbnamen eingegeben hast, die du für **deine** Kreise verwendet hast.

**Debug:** 🐞 Stelle sicher, dass du die `.hex`-Zeichenfolge für **deine** Kreisfarben verwendet hast.

--- /task ---

### Das Ziel verfehlen

Du musst noch eine weitere Entscheidung treffen: Was passiert, wenn der Pfeil auf keinem der Zielkreise landet? ❌

Um diese letzte Bedingung zu überprüfen, verwendest du `else` (deutsch: sonst).

--- task ---

Füge Code für eine `print`-Asugabe hinzu, wenn `else (sonst)` keine der Bedingungen von `if` und `elif` erfüllt werden.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 6
line_highlights: 13-14
---

def mouse_pressed(): if hit_colour == Color('blue').hex:   
print('You hit the outer circle, 50 points!') elif hit_colour == Color('red').hex: print('You hit the inner circle, 200 points!') elif hit_colour == Color('yellow').hex: print('You hit the middle, 500 points!') else:   
print('You missed! No points!')

--- /code ---

--- /task ---

--- task ---

**Test:** 🔄 Führe dein Projekt aus. Schieß den Pfeil ins Gras oder in den Himmel, um die Verfehlt-Ausgabe zu sehen.

**Wählen aus:** 💭 Ändere die Anzahl der Punkte, die für die verschiedenen Farben erzielt werden.

--- /task ---

--- save ---
