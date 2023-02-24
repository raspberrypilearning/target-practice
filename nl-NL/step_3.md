## Teken je doelwit

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Your game needs a target to shoot arrows at.
</div>
<div>

![Het uitvoergebied met het doel en de standaard.](images/three-circles.png){:width="300px"}

</div>
</div>

### Draw a triangular stand

--- task ---

Set the fill colour to `wood` (brown).

Draw a triangle using the x and y coordinates for each of the corners.

![A brown triangle on grass and against a sky with the coordinate points labelled at 150, 350 and 200, 150 and 250, 350). The corners of the canvas are also labelled as x=0, y=0 in the top left and x=400, y=400 i the bottom right.](images/stand_coords.png){:width="400px"}

--- code ---
---
language: python filename: main.py - draw() line_numbers: true line_number_start: 28
line_highlights: 37-40
---
  fill(gras)   
rect(0, 250, 400, 150) #x, y, breedte, hoogte

--- /code ---

--- /task ---

--- task ---

**Test:** Voer je code uit om de standaard voor je doelwit te zien.

![Een bruine driehoek op gras en tegen een lucht.](images/target-stand.png){:width="400px"}

--- /task ---

### Draw the target circles

--- task ---

**Test:** Voer je code uit om de eerste grote blauwe cirkel te zien.

Set the fill colour to `outer` (blue).

Draw a circle with x and y coordinates for its centre and a width.

![A brown triangle and blue circle on grass and against a sky. The circle is labelled with the coordinates x=200, y=200 as the centre and circle width of 170.](images/circle-coords.png){:width="400px"}

--- code ---
---
language: python filename: main.py - draw() line_numbers: true line_number_start: 31
line_highlights: 31-32
---

  fill(hout) #Stel de vulkleur van de standaard in op bruin     
triangle(150, 350, 200, 150, 250, 350)

--- /code ---

--- /task ---

--- task ---

**Tip:** Om een cirkel te maken, moeten de **breedte** en **hoogte** gelijk zijn.

The blue circle was drawn after the stand so it is in front:

![Een bruine driehoek en blauwe cirkel op gras en tegen een lucht.](images/blue-circle.png){:width="400px"}

--- /task ---

--- task ---

Wijs kleuren toe aan de `binnenste` en `roos` variabelen met `color()`.

Maak twee nieuwe variabelen om de kleuren voor de resterende `binnenste` en `roos` cirkels op te slaan.

De functie `color()` verwacht drie getallen: één voor rood, groen en blauw.

--- code ---
---
language: python filename: main.py - draw() line_numbers: true line_number_start: 33
line_highlights: 33-34
---
lucht = color(92, 204, 206)   
gras = color(149, 212, 122)   
hout = color(145, 96, 51)   
buitenste = color(0, 120, 180) #Blauw    
binnenste = color(210, 60, 60) # Rood    
roos = color(220, 200, 0) # Geel

--- /code ---

--- /task ---

Het doel is gemaakt van cirkels van verschillende grootte met dezelfde centrale coördinaten (200, 200) - het midden van het scherm.

--- task ---

**Test:** Voer je project opnieuw uit om het doel met drie gekleurde cirkels te zien.

--- code ---
---
language: python filename: main.py - draw() line_numbers: true line_number_start: 18
line_highlights: 24-25
---
  fill(hout)    
triangle(150, 350, 200, 150, 250, 350) #Standaard    
fill(buitenste)   
ellipse(200, 200, 170, 170) #Buitenste cirkel   
fill(binnenste)   
ellipse(200, 200, 110, 110) #Binnenste cirkel   
fill(roos)   
ellipse(200, 200, 30, 30) #Roos

--- /code ---

--- /task ---

--- task ---

def draw():   
#Dingen om te doen in elk frame

![Een bruine driehoek met drie gekleurde cirkels op gras en tegen een lucht.](images/three-circles.png){:width="400px"}

**Debuggen:** Python gebruikt de Amerikaanse spelling van 'color' (zonder een 'u'), dus zorg ervoor dat jij dat ook doet.

--- /task ---

--- task ---

**Choose:** 💭 Change any of the colours.

[[[generic-theory-simple-colours]]]

![Een bruine driehoek op gras en tegen een lucht met de coördinaatpunten gelabeld. The colours have changed to pinks and purples.](images/alternative-colours.png){:width="400px"}


--- /task ---



