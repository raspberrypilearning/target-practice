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

Définir la couleur de remplissage sur `bois` (marron).

Dessine un triangle en utilisant les coordonnées x et y de chacun des angles.

![Un triangle marron sur de l'herbe et sur un ciel dont les points de coordonnées sont marqués 150, 350 et 200, 150 et 250, 350). Les coins du canevas sont également marqués x=0, y=0 en haut à gauche et x=400, y=400 en bas à droite.](images/stand_coords.png){:width="400px"}

--- code ---
---
language: python filename: main.py - dessin() line_numbers: true line_number_start: 27
line_highlights: 29, 30
---
  fill(herbe)   
rect(0, 250, 400, 150) fill(bois) # Défini la couleur de remplissage du support sur bois     
triangle(150, 350, 200, 150, 250, 350)

--- /code ---

--- /task ---

--- task ---

**Test :** 🔄 Exécute ton code pour voir le support de ta cible :

![Un triangle marron sur l'herbe et contre un ciel.](images/target-stand.png){:width="400px"}

--- /task ---

### Dessiner les cibles

--- task ---

La plus grande partie de la cible est un **cercle** bleu.

Définis la couleur de remplissage sur `extérieur` (bleu).

Dessine un cercle avec des coordonnées x et y pour son centre et une largeur.

![Un triangle marron et un cercle bleu sur de l'herbe et contre un ciel. Le cercle est nommé avec les coordonnées x=200, y=200 comme centre et une largeur de cercle de 170.](images/circle-coords.png){:width="400px"}

--- code ---
---
language: python filename: main.py - dessin() line_numbers: true line_number_start: 29
line_highlights: 31, 32
---

  fill(bois)   
triangle(150, 350, 200, 150, 250, 350)   
fill(exterieur) # Défini la couleur de remplissage du cercle sur extérieur    
circle(200, 200, 170) # x, y, largeur du cercle

--- /code ---

--- /task ---

--- task ---

**Test:** Exécute ton code pour voir le premier grand cercle bleu.

Le cercle bleu a été dessiné après le support donc il est devant :

![Un triangle marron et un cercle bleu sur l'herbe et contre un ciel.](images/blue-circle.png){:width="400px"}

--- /task ---

--- task ---

👀 Trouve tes variables de couleur dans la fonction `dessine`.

Crée deux variables appelées `interieur` et `centre` pour stocker les couleurs des autres cercles.

La fonction `color()` attend trois nombres : un pour le rouge, le vert et le bleu.

--- code ---
---
language: python filename: main.py - dessin() line_numbers: true line_number_start: 17
line_highlights: 24, 25
---
def dessin():   
# Choses à faire dans chaque image global bois ciel = color(92, 204, 206)   
herbe = color(149, 212, 122)   
bois = color(145, 96, 51)   
exterieur = color(0, 120, 180) # Bleu    
interieur = color(210, 60, 60) # Rouge    
centre = color(220, 200, 0) # Jaune

--- /code ---

--- /task ---

La cible est constituée de cercles de tailles différentes ayant les mêmes coordonnées centrales (200, 200).

--- task ---

**Ajoute** des cercles de couleur pour les parties intérieure et centrale de la cible.

--- code ---
---
language: python filename: main.py - dessin() line_numbers: true line_number_start: 31
line_highlights: 35, 36, 37, 38
---
  fill(bois)    
triangle(150, 350, 200, 150, 250, 350)  
fill(exterieur)   
circle(200, 200, 170) fill(interieur) # Défini la couleur de remplissage du cercle sur intérieur      
circle(200, 200, 110) # Cercle intérieur - x, y, largeur du cercle  
fill(centre) # Défini la couleur de remplissage du cercle sur centre      
circle(200, 200, 30) # Cercle intérieur - x, y, largeur du cercle

--- /code ---

--- /task ---

--- task ---

**Test :** 🔄 Exécute ton projet pour voir la cible avec trois cercles colorés.

![Un triangle marron avec trois cercles colorés sur l'herbe et contre un ciel.](images/three-circles.png){:width="400px"}

**Débogage :** 🐞 Vérifie que tu as utilisé le mot américain « color » (sans "u").

--- /task ---

--- task ---

**Choisir :** 💭 Change n'importe laquelle des couleurs.

[[[generic-theory-simple-colours]]]

![Un triangle marron avec trois cercles de couleur sur de l'herbe et sur un ciel. Les couleurs ont changé sur rose et violet.](images/alternative-colours.png){:width="400px"}


--- /task ---



