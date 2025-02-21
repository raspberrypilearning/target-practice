## Narysuj trawę

--- task ---

Otwórz projekt [ Praktyka docelowa ](https://editor.raspberrypi.org/en/projects/target-practice-starter){:target="_blank"}.

--- /task ---

--- task ---

**Add** code to draw a green rectangle at the bottom of the screen to represent the grass.

![Obszar wyjściowy z prostokątem w kolorze nieba nad prostokątem w kolorze trawy, aby utworzyć tło. Lewy górny róg prostokąta jest oznaczony jako x=0, y=250 to jest początek początku prostokąta. Szerokość jest podświetlona jako 400, a wysokość jako 150. Wyświetlany jest kod rect(0, 250, 400, 150).](images/green-grass.png){:width="400px"}

--- code ---
---
language: python line_numbers: true line_number_start: 17
line_highlights: 21-22
---
def draw(): # Things to do in every frame fill('cyan')  
rect(0, 0, 400, 250)  
fill('lightgreen')  
rect(0, 250, 400, 150)

--- /code ---

--- /task ---

--- task ---

**Test:** Run your project to view the background.

![Obszar wyjściowy z prostokątem w kolorze nieba nad prostokątem w kolorze trawy, aby utworzyć tło.](images/background.png){:width="400px"}

--- /task ---

--- save ---
