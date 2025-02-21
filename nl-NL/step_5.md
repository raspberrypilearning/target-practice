## What colour did you hit?

Next, you will add some code to get the colour at the location of the arrow.

### Get the colour hit by the arrow

--- task ---

**Debuggen:** 🐞 Als je een bericht ziet over `raak_kleur` die 'niet gedefinieerd' is, ga dan terug naar `draw()` en controleer de regel waarin `raak_kleur` als globale variabele gedeclareerd is.

Add code to `get` the colour at the centre of the arrow ,and store it in the `hit_colour` variable.


--- code ---
---
language: python filename: main.py - mouse_pressed() line_numbers: true line_number_start: 6
line_highlights: 7
---
def mouse_pressed(): if hit_kleur == Color('blue').hex:   
print('Je raakt de buitenste cirkel, 50 punten!') elif hit_kleur == Color('red').hex: print('Je hebt de binnenste cirkel geraakt, 200 punten!') elif hit_kleur == Color('yellow').hex: print('Je raakt het midden, 500 punten!')

--- /code ---

**Debug:** 🐞 Zorg ervoor dat je de `.hex` string hebt gebruikt voor **jouw** cirkelkleuren.

--- /task ---

--- task ---

**Test:** 🔄 Voer je project uit. **Debuggen:** 🐞 Zorg ervoor dat je de juiste kleurnaam hebt ingevoerd voor **jouw** cirkels.

--- /task ---

### Run code when the mouse is pressed

--- task --- Comment out the line that prints the colour. This means it will not run.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 6
line_highlights: 7, 8
---

    def mouse_pressed():<br x-id="5" />
        if raak_kleur == Color('blue').hex: # Net als bij functies worden 'if'-instructies ingesprongen
            print('Je hebt de buitenste cirkel geraakt, 50 punten!')
--- /code ---

--- /task ---

--- task --- Add code to print the target emoji 🎯 **when the mouse is clicked**.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 5
line_highlights: 9-12
---
# De mouse_pressed functie komt hier
def mouse_pressed():

--- /task ---

**Test:** 🔄 Voer je project uit. You should see the 🎯 character printed when you click the mouse on the target.

![target emoji printed when mouse clicked](images/target_printed.gif) --- /task ---


--- save ---