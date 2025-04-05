
--- question ---
---
legenda: Vraag 2 van 3
---

In je project heb je `if`, `elif`en `else` condities gebruikt om te controleren op welke kleur de pijl terechtkwam.

In het onderstaande voorbeeld is in een variabele met de naam `snelheid` het getal `6` opgeslagen. Als dit `if` commando wordt uitgevoerd, wat wordt er dan afgedrukt in het uitvoergebied?

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

  Probeer het opnieuw, `else` wordt gebruikt als laatste optie voor wanneer alle bovenstaande voorwaarden onwaar zijn. Kijk nog eens naar de voorwaarden. Is een van de voorwaarden waar?

  --- /feedback ---

--- /choices ---

--- /question ---
