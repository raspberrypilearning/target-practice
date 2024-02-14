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
language: python filename: main.py - draw() line_numbers: true line_number_start: 18
line_highlights: 24-25
---

    fill('lightgreen')  # Set the fill colour for the grass to light green
    rect(0, 250, 400, 150)  # Draw a rectangle for the grass with these values for x, y, width, height
    fill('sienna')  # Brown colour
    triangle(150, 350, 200, 150, 250, 350)  # Draw a triangle for the target's stand

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
language: python filename: main.py - draw() line_numbers: true line_number_start: 33
line_highlights: 31-32
---

    fill('sienna') # Bruine kleur
    triangle(150, 350, 200, 150, 250, 350) # Teken een driehoek voor de stand van het doelwit 
    fill('blue') # Stel de vulkleur van cirkel naar blauw
    circle(200, 200, 170) # Teken de buitenste cirkel

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
language: python filename: main.py - draw() line_numbers: true line_number_start: 28
line_highlights: 33-34
---

    fill('sienna')  # Brown colour
    triangle(150, 350, 200, 150, 250, 350)  # Draw a triangle for the target's stand 
    fill('blue')  # Set the circle fill colour to blue
    circle(200, 200, 170)  # Draw the outer circle
    fill('red')  # Set the colour for the circle fill to red
    circle(200, 200, 110)  # Draw the inner circle using x, y, width
    fill('yellow')  # Set the colour for the circle fill to yellow      
    circle(200, 200, 30)  # Draw the middle circle using x, y, width

--- /code ---

--- /task ---

--- task ---

**Test:** 🔄 Voer je project uit om het doel met drie gekleurde cirkels te zien.

![Een bruine driehoek met drie gekleurde cirkels op gras en tegen een lucht.](images/three-circles.png){:width="400px"}

--- /task ---

--- task ---

**Kies:** 💭 Verander een van de kleuren met een andere kleurnaam. Je kunt een lijst met alle beschikbare kleurnamen vinden op [W3 Schools](https://www.w3schools.com/colors/colors_names.asp){:target="blank"}.

![Een bruine driehoek op gras en tegen een lucht met de coördinaatpunten gelabeld. De kleuren zijn veranderd in verschilende tinten roze en paars.](images/alternative-colours.png){:width="400px"}

--- collapse ---
---
title: Voorbeeldcode met verschillende kleuren
---

--- code ---
---
language: python filename: main.py - draw() line_numbers: true line_number_start: 31
line_highlights: 37-40
---

def draw():
# Dingen om te doen in elk frame

    fill('BlueViolet')
    rect(0, 0, 400, 250)  # Sky
    fill('DeepSkyBlue')
    rect(0, 250, 400, 150)  # Ground
    fill('FireBrick')
    triangle(150, 350, 200, 150, 250, 350)  # Stand
    fill('LemonChiffon')
    circle(200, 200, 170)  # Outer circle
    fill('DeepPink')
    circle(200, 200, 110)  # Inner circle
    fill('BlueViolet')
    circle(200, 200, 30)  # Middle circle

--- /code ---

--- /collapse ---

--- /task ---

--- save ---
