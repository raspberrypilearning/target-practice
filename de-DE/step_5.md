## What colour did you hit?

Next, you will add some code to get the colour at the location of the arrow.

### Get the colour hit by the arrow

--- task ---

**Debug:** 🐞 Wenn du eine Meldung siehst, dass `getroffene_farbe` „not defined“ (deutsch: „nicht definiert“) ist, gehe zurück zu `draw()` und überprüfe, ob die Zeile `getroffene_farbe` als eine globale Variable deklariert.

Add code to `get` the colour at the centre of the arrow ,and store it in the `hit_colour` variable.


--- code ---
---
language: python filename: main.py - mouse_pressed() line_numbers: true line_number_start: 6
line_highlights: 7
---
def mouse_pressed():     
if getroffene_farbe == Color('blue').hex:  # Wie der Code in Funktionen ist der Code auch in 'if'-Anweisungen eingerückt print('Du hast den äußeren Kreis getroffen, 50 Punkte!')

--- /code ---

**Debug:** 🐞 Stelle sicher, dass du die `.hex`-Zeichenfolge für **deine** Kreisfarben verwendet hast.

--- /task ---

--- task ---

**Test:** 🔄 Führe dein Projekt aus. Versuche, den Pfeil auf den blauen äußeren Kreis abzufeuern, um die Ausgabe zu sehen.

--- /task ---

### Run code when the mouse is pressed

--- task ---

Comment out the line that prints the colour. This means it will not run.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 6
line_highlights: 7, 8
---

    def mouse_pressed():
        if getroffene_farbe == Color('blue').hex:<br x-id="3" />
            print('Du hast den äußeren Kreis getroffen, 50 Punkte!')
        elif getroffene_farbe == Color('red').hex:
            print('Du hast den inneren Kreis getroffen, 200 Punkte!')
        elif getroffene_farbe == Color('yellow').hex:
            print('Du hast die Mitte getroffen, 500 Punkte!')

--- /code ---

--- /task ---

--- task ---

Add code to print the target emoji 🎯 **when the mouse is clicked**.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 5
line_highlights: 9-12
---
# Die Funktion „mouse_pressed“ kommt hierher
def mouse_pressed():    
print('🎯')

--- /code ---

--- /task ---

--- task ---

**Test:** 🔄 Führe dein Projekt aus. You should see the 🎯 character printed when you click the mouse on the target.

![target emoji printed when mouse clicked](images/target_printed.gif)

--- /task ---

--- save ---