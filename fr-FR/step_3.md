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

Définis la couleur de remplissage sur `sienna` (marron).

Dessine un triangle en utilisant les coordonnées x et y de chacun des angles.

![Un triangle marron sur de l'herbe et sur un ciel dont les points de coordonnées sont marqués 150, 350 et 200, 150 et 250, 350). Les coins du canevas sont également marqués x=0, y=0 en haut à gauche et x=400, y=400 en bas à droite.](images/stand_coords.png){:width="400px"}

--- code ---
---
language: python filename: main.py - dessin() line_numbers: true line_number_start: 18
line_highlights: 24-25
---

    fill('lightgreen')  # Set the fill colour for the grass to light green
    rect(0, 250, 400, 150)  # Draw a rectangle for the grass with these values for x, y, width, height
    fill('sienna')  # Brown colour
    triangle(150, 350, 200, 150, 250, 350)  # Draw a triangle for the target's stand

--- /code ---

--- /task ---

--- task ---

**Test :** 🔄 exécute ton code pour voir le support de ta cible :

![Un triangle marron sur l'herbe et sur fond de ciel.](images/target-stand.png){:width="400px"}

--- /task ---

### Dessiner les cibles

--- task ---

La plus grande partie de la cible est un **cercle** bleu.

Définis la couleur de remplissage sur `blue`.

Dessine un cercle avec des coordonnées x et y pour son centre et une largeur.

![Un triangle marron et un cercle bleu sur l'herbe et sur fond de ciel. Le cercle est nommé avec les coordonnées x=200, y=200 comme centre et une largeur de cercle de 170.](images/circle-coords.png){:width="400px"}

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

**Test :** exécute ton code pour voir le premier grand cercle bleu.

Le cercle bleu a été dessiné après le support donc il est devant.

![Un triangle marron et un cercle bleu sur l'herbe et sur fond de ciel.](images/blue-circle.png){:width="400px"}

--- /task ---

La cible est constituée de cercles de tailles différentes ayant les mêmes coordonnées centrales (200, 200).

--- task ---

**Ajoute** des cercles de couleur pour les parties intérieure et centrale de la cible.

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

**Test :** 🔄 exécute ton projet pour voir la cible avec trois cercles colorés.

![Un triangle marron avec trois cercles colorés sur de l'herbe et sur fond de ciel.](images/three-circles.png){:width="400px"}

--- /task ---

--- task ---

**Choisir :** 💭 modifie l'une des couleurs en utilisant un nom de couleur différent. Tu peux trouver une liste de tous les noms de couleurs disponibles sur [W3 Schools](https://www.w3schools.com/colors/colors_names.asp){:target="blank"}.

![Un triangle marron avec trois cercles colorés sur l'herbe et sur fond de ciel. Les couleurs sont devenues roses et violettes.](images/alternative-colours.png){:width="400px"}

--- collapse ---
---
title: Exemple de code utilisant différentes couleurs
---

--- code ---
---
language: python filename: main.py - draw() line_numbers: true line_number_start: 31
line_highlights: 37-40
---

def draw():
# Choses à faire dans chaque frame

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
