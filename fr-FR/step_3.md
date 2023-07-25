## Dessiner ta cible

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Ton jeu a besoin d'une cible pour tirer des flèches.
</div>
<div>

![La zone de sortie avec la cible et le support.](images/three-circles.png){:width="300px"}

</div>
</div>

### Dessiner un support triangulaire

--- task ---

Set the fill colour to `sienna` (brown).

Dessine un triangle en utilisant les coordonnées x et y de chacun des angles.

![Un triangle marron sur de l'herbe et sur un ciel dont les points de coordonnées sont marqués 150, 350 et 200, 150 et 250, 350). The corners of the canvas are also labelled as x=0, y=0 in the top left and x=400, y=400 in the bottom right.](images/stand_coords.png){:width="400px"}

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

**Test :** Exécute ton code pour voir le support de ta cible.

![Un triangle marron sur l'herbe et contre un ciel.](images/target-stand.png){:width="400px"}

--- /task ---

### Dessiner les cibles

--- task ---

**Astuce :** Pour faire un cercle, les **largeur** et **hauteur** doivent être identiques.

Set the fill colour to `blue`.

Draw a circle with x and y coordinates for its centre and a width.

![A brown triangle and blue circle on grass and against a sky. The circle is labelled with the coordinates x=200, y=200 as the centre and circle width of 170.](images/circle-coords.png){:width="400px"}

--- code ---
---
language: python filename: main.py - draw() line_numbers: true line_number_start: 33
line_highlights: 31-32
---

    fill(bois)<br x-id="3" />
      triangle(150, 350, 200, 150, 250, 350)<br x-id="3" />
      fill(exterieur)<br x-id="4" />
      ellipse(200, 200, 170, 170) #Cercle extérieur.

--- /code ---

--- /task ---

--- task ---

**Test :** Exécute ton code pour voir le premier grand cercle bleu.

Le cercle bleu couvrira le triangle marron où ils se chevauchent, car le cercle a été dessiné plus tard.

![Un triangle marron et un cercle bleu sur l'herbe et contre un ciel.](images/blue-circle.png){:width="400px"}

--- /task ---

La cible est constituée de cercles de tailles différentes avec les mêmes coordonnées centrales (200, 200) - le milieu de l'écran.

--- task ---

**Test :** Exécute à nouveau ton projet pour voir la cible avec trois cercles colorés.

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

**Débogage:** Python utilise l'orthographe américaine de « color » (sans "u") alors assure-toi de faire de même.

![Un triangle marron avec trois cercles colorés sur l'herbe et contre un ciel.](images/three-circles.png){:width="400px"}

--- /task ---

--- task ---

**Choose:** 💭 Change any of the colours using a different colour name. You can find a list of all of the available colour names on [W3 Schools](https://www.w3schools.com/colors/colors_names.asp){:target="blank"}.

![Un triangle marron sur l'herbe et contre un ciel avec les points de coordonnées étiquetés. The colours have changed to pinks and purples.](images/alternative-colours.png){:width="400px"}

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
