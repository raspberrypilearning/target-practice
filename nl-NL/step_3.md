## Teken je doelwit

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Je spel heeft een doel nodig om pijlen op te schieten.
</div>
<div>

![Het uitvoergebied met het doel en de standaard.](images/three-circles.png){:width="300px"}

</div>
</div>

### Teken een driehoekige standaard

--- task ---

Stel de vulkleur in op `sienna` (bruin).

Teken een driehoek met de x- en y-coördinaten voor elk van de hoeken.

![Een bruine driehoek op gras en tegen een lucht met de coördinatenpunten gelabeld op 150, 350 en 200, 150 en 250, 350). De hoeken van het canvas zijn ook gelabeld als x=0, y=0 linksboven en x=400, y=400 rechtsonder.](images/stand_coords.png){:width="400px"}

--- code ---
---
language: python line_numbers: true line_number_start: 21
line_highlights: 23-24
---

    fill('lightgreen')  
    rect(0, 250, 400, 150)  
    fill('brown') 
    triangle(150, 350, 200, 150, 250, 350)

--- /code ---

--- /task ---

--- task ---

**Test:** 🔄 Voer je code uit om de standaard voor je doelwit te zien:

![Een bruine driehoek op gras en tegen een lucht.](images/target-stand.png){:width="400px"}

--- /task ---

### Teken de doelcirkels

--- task ---

Het grootste deel van het doel is een blauwe **cirkel**.

Stel de vulkleur in op `blue` (blauw).

Teken een cirkel met x- en y-coördinaten voor het midden en de breedte.

![Een bruine driehoek en blauwe cirkel op gras en tegen een lucht. De cirkel is gelabeld met de coördinaten x=200, y=200 als het midden en de cirkelbreedte van 170.](images/circle-coords.png){:width="400px"}

--- code ---
---
language: python line_numbers: true line_number_start: 23
line_highlights: 25-26
---

    fill('brown')  
    triangle(150, 350, 200, 150, 250, 350)  
    fill('blue')  
    circle(200, 200, 170)

--- /code ---

--- /task ---

--- task ---

**Test:** Voer je code uit om de eerste grote blauwe cirkel te zien.

De blauwe cirkel is na de standaard getekend, dus deze staat vooraan.

![Een bruine driehoek en blauwe cirkel op gras en tegen een lucht.](images/blue-circle.png){:width="400px"}

--- /task ---

Het doel is gemaakt van cirkels van verschillende grootte met dezelfde centrale coördinaten (200, 200).

--- task ---

**Voeg** gekleurde cirkels toe voor de binnenste en middelste delen van het doel.

--- code ---
---
language: python line_numbers: true line_number_start: 25
line_highlights: 27-30
---

    fill('blue')  
    circle(200, 200, 170)  
    fill('red')  
    circle(200, 200, 110)  # Draw the inner circle 
    fill('yellow')       
    circle(200, 200, 30)  # Draw the middle circle

--- /code ---

--- /task ---

--- task ---

**Test:** 🔄 Voer je project uit om het doel met drie gekleurde cirkels te zien.

![Een bruine driehoek met drie gekleurde cirkels op gras en tegen een lucht.](images/three-circles.png){:width="400px"}

--- /task ---

--- save ---
