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

Set the fill colour to `sienna` (brown).

Draw a triangle using the x and y coordinates for each of the corners.

![A brown triangle on grass and against a sky with the coordinate points labelled at 150, 350 and 200, 150 and 250, 350). The corners of the canvas are also labelled as x=0, y=0 in the top left and x=400, y=400 in the bottom right.](images/stand_coords.png){:width="400px"}

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

**Test:** Voer je code uit om de standaard voor je doelwit te zien.

![Een bruine driehoek op gras en tegen een lucht.](images/target-stand.png){:width="400px"}

--- /task ---

### Draw the target circles

--- task ---

**Tip:** Om een cirkel te maken, moeten de **breedte** en **hoogte** gelijk zijn.

Set the fill colour to `blue`.

Draw a circle with x and y coordinates for its centre and a width.

![A brown triangle and blue circle on grass and against a sky. The circle is labelled with the coordinates x=200, y=200 as the centre and circle width of 170.](images/circle-coords.png){:width="400px"}

--- code ---
---
language: python filename: main.py - draw() line_numbers: true line_number_start: 33
line_highlights: 31-32
---

    fill(hout)<br x-id="3" />
      triangle(150, 350, 200, 150, 250, 350)<br x-id="3" />
      fill(buitenste)<br x-id="4" />
      ellipse(200, 200, 170, 170) #Buitenste cirkel.

--- /code ---

--- /task ---

--- task ---

**Test:** Voer je code uit om de eerste grote blauwe cirkel te zien.

The blue circle was drawn after the stand so it is in front.

![Een bruine driehoek en blauwe cirkel op gras en tegen een lucht.](images/blue-circle.png){:width="400px"}

--- /task ---

Het doel is gemaakt van cirkels van verschillende grootte met dezelfde centrale coördinaten (200, 200) - het midden van het scherm.

--- task ---

Maak twee nieuwe variabelen om de kleuren voor de resterende `binnenste` en `roos` cirkels op te slaan.

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

**Debuggen:** Python gebruikt de Amerikaanse spelling van 'color' (zonder een 'u'), dus zorg ervoor dat jij dat ook doet.

![Een bruine driehoek met drie gekleurde cirkels op gras en tegen een lucht.](images/three-circles.png){:width="400px"}

--- /task ---

--- task ---

**Test:** Voer je project opnieuw uit om het doel met drie gekleurde cirkels te zien. Verander de kleuren totdat je er tevreden mee bent. You can find a list of all of the available colour names on [W3 Schools](https://www.w3schools.com/colors/colors_names.asp){:target="blank"}.

![Een bruine driehoek op gras en tegen een lucht met de coördinaatpunten gelabeld. The colours have changed to pinks and purples.](images/alternative-colours.png){:width="400px"}

--- collapse ---
---
title: Example code using different colours
---

--- code ---
---
language: python filename: main.py - draw() line_numbers: true line_number_start: 31
line_highlights: 37-40
---

def draw():
# Things to do in every frame

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
