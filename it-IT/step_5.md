## What colour did you hit?

Next, you will add some code to get the colour at the location of the arrow.

### Get the colour hit by the arrow

--- task ---

**Debug:** 🐞Se vedi un messaggio `hit_colour` being 'not defined', torna indietro alla funzione `draw()` e controlla la riga che dichiara `hit_colour` come variabile globale.

Add code to `get` the colour at the centre of the arrow ,and store it in the `hit_colour` variable.


--- code ---
---
language: python filename: main.py - mouse_pressed() line_numbers: true line_number_start: 6
line_highlights: 7
---
def mouse_pressed():     
if hit_colour == Color('blue').hex:  # Come il codice delle funzioni, il codice delle istruzioni 'if' è rientrato print('Hai colpito il cerchio esterno, 50 punti!')

--- /code ---

**Debug:** 🐞 Assicurati di aver utilizzato la stringa `.hex` per i colori del **tuo cerchio**.

--- /task ---

--- task ---

**Test:** 🔄 Esegui il tuo progetto. Prova a lanciare la freccia sul cerchio esterno blu per vedere il messaggio.

--- /task ---

### Run code when the mouse is pressed

--- task --- Comment out the line that prints the colour. This means it will not run.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 6
line_highlights: 7, 8
---

    Visualizza un messaggio <strong x-id="1">if</strong> il <code>hit_color è uguale al colore del cerchio esterno (blu) 🎯.
    </code>
--- /code ---

--- /task ---

--- task --- Add code to print the target emoji 🎯 **when the mouse is clicked**.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 5
line_highlights: 9-12
---
# La funzione mouse_pressed va qui
def mouse_pressed():

--- /task ---

**Test:** 🔄 Esegui il tuo progetto. Prova a lanciare la freccia sul cerchio interno e su quello esterno per vedere il messaggio.

![target emoji printed when mouse clicked](images/target_printed.gif) --- /task ---


--- save ---