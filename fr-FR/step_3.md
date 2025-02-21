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

**Test :** exécute ton code pour voir le premier grand cercle bleu.

Le cercle bleu a été dessiné après le support donc il est devant.

![Un triangle marron et un cercle bleu sur l'herbe et sur fond de ciel.](images/blue-circle.png){:width="400px"}

--- /task ---

La cible est constituée de cercles de tailles différentes ayant les mêmes coordonnées centrales (200, 200).

--- task ---

**Ajoute** des cercles de couleur pour les parties intérieure et centrale de la cible.

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

**Test :** 🔄 exécute ton projet pour voir la cible avec trois cercles colorés.

![Un triangle marron avec trois cercles colorés sur de l'herbe et sur fond de ciel.](images/three-circles.png){:width="400px"}

--- /task ---

--- save ---
