
--- question ---
---
legend: Vraag 2 van 3
---

In je project heb je `if` , `elif`en `else` condities gebruikt om te controleren op welke kleur de pijl terechtkwam.

In the example below, a variable called `speed` has the number `6` stored in it. When this `if` statement is run, what would be printed in the output area?

--- code ---
---
language: python
---
snelheid = 6

if snelheid == 7: print('Super snel') elif snelheid == 5: print('Aardig snel') elif snelheid == 6: print('Zeer snel') else: print( 'Snelheid niet herkend!')

--- /code ---

--- choices ---

- (x) `Zeer snel`

  --- feedback ---

  Dat is correct! De **snelheid** variabele heeft de waarde `6`gekregen, waardoor de voorwaarde `snelheid == 6` **Waar** is en `Zeer snel` wordt afgedrukt.

  --- /feedback ---

- ( ) `Snelheid niet herkend!`

  --- feedback ---

  Niet helemaal, kijk naar de waarde die is toegewezen aan de variabele **snelheid**.

  --- /feedback ---

- ( ) Er wordt niets afgedrukt

  --- feedback ---

  Try again, `else` is used as a final option for when all the above conditions are false. Look through the conditions again, are any of the conditions true?

  --- /feedback ---

--- /choices ---

--- /question ---
