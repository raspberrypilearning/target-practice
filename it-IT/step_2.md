## Disegna l'erba

--- task ---

Apri il progetto [Target Practice Starter](https://editor.raspberrypi.org/en/projects/target-practice-starter){:target="_blank"}.

--- /task ---

--- task ---

**Aggiungi** il codice per disegnare un rettangolo verde nella parte inferiore dello schermo.

![L'area di output con un rettangolo color cielo sopra un rettangolo color erba per creare lo sfondo. L'angolo in alto a sinistra del rettangolo è contrassegnato dalle coordinate x=0, y=250; questa è l'origine del rettangolo. La larghezza è indicata come 400 e l'altezza come 150. Viene visualizzato il codice rect(0, 250, 400, 150).](images/green-grass.png){:width="400px"}

--- code ---
---
language: python filename: main.py — draw() line_numbers: true line_number_start: 14
line_highlights: 12
---
def draw(): # Things to do in every frame fill('cyan')  
rect(0, 0, 400, 250)  
fill('lightgreen')  
rect(0, 250, 400, 150)

--- /code ---

--- /task ---

--- task ---

**Test:** 🔄 Esegui nuovamente il progetto per visualizzare lo sfondo finito.

![L'area di output con un rettangolo color cielo sopra un rettangolo color erba per creare lo sfondo.](images/background.png){:width="400px"}

--- /task ---

--- save ---
