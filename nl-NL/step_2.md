## Teken het gras

--- task ---

Open het project [Doelpraktijk-start](https://editor.raspberrypi.org/en/projects/target-practice-starter){:target="_blank"}.

--- /task ---

--- task ---

**Voeg** code toe om een groene rechthoek onder aan het scherm te tekenen.

![Het uitvoergebied met een luchkleurige rechthoek boven een graskleurige rechthoek om de achtergrond te creëren. De linkerbovenhoek van de rechthoek is gemarkeerd als x=0, y=250 dit is de oorsprong van de rechthoek. De breedte wordt gemarkeerd als 400 en de hoogte als 150. De code rect(0, 250, 400, 150) wordt weergegeven.](images/green-grass.png){:width="400px"}

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

**Test:** 🔄 Voer je project opnieuw uit om de voltooide achtergrond te bekijken.

![Het uitvoergebied met een luchtkleurige rechthoek boven een graskleurige rechthoek om de achtergrond te creëren.](images/background.png){:width="400px"}

--- /task ---

--- save ---
