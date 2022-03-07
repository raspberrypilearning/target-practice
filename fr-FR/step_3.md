## Dessiner ta cible
<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Le support cible est en forme de triangle. La cible est constituée de cercles colorés - les cercles plus petits valent plus de points que les plus grands. 
</div>
<div>

![La zone de sortie avec la cible et le support.](images/three-circles.png){:width="300px"}

</div>
</div>

Les formes sont dessinées dans l'ordre d'exécution des lignes de code. Le support triangulaire en bois se trouve en partie derrière les cercles cibles, il doit donc être dessiné en premier.

Imagine découper toutes les formes dans du papier. Selon la façon dont tu organises et superposes ce papier, le résultat final peut être très différent.

### Dessiner le support

--- task ---

Lorsque tu appelles la fonction `triangle()`, tu dois fournir trois ensembles de coordonnées, `x1, y1, x2, y2, x3, y3` représentant chacun la position de l'un des coins du triangle.

--- collapse ---
---
title: Coordonnées du triangle
---

  Voici trois exemples de triangles, chacun avec différents ensembles de coordonnées. Regarde la position de grille de chacun pour voir comment les coordonnées `x` et `y` positionnent les coins des triangles :
  + Triangle vert : triangle(50, 50, 150, 50, 180, 100)
  + Triangle bleu : triangle(210, 280, 300, 350, 380, 100)
  + Triangle marron : triangle(50, 150, 200, 250, 180, 350)

  ![La zone de sortie avec trois triangles.](images/triangles-coords.png)

--- /collapse ---

Dessine un `triangle()` pour le support avec des coins à (150, 350), (200, 150) et (250, 350).

![Un triangle marron sur l'herbe et contre un ciel avec les points de coordonnées étiquetés.](images/stand_coords.png)

--- code ---
---
language: python filename: main.py - draw() line_numbers: true line_number_start: 28
line_highlights: 31-32
---

  fill(herbe)   
rect(0, 250, 400, 150) #x, y, largeur, hauteur

  fill(bois) #Définir la couleur de remplissage du support sur marron     
triangle(150, 350, 200, 150, 250, 350)


--- /code ---

**Astuce :** Nous avons ajouté des commentaires à notre code, comme `#Définir la couleur de remplissage du support sur marron`, pour te dire ce qu'il fait. Tu n'as pas besoin d'ajouter ces commentaires à ton code, mais ils peuvent être utiles pour te rappeler ce que font les lignes de code.

--- /task ---

--- task ---

**Test :** Exécute ton code pour voir le support de ta cible.

![Un triangle marron sur l'herbe et contre un ciel.](images/target-stand.png)

--- /task ---

### Dessiner la cible

--- task ---

La plus grande partie de la cible sera un **cercle bleu** créé en utilisant la fonction `ellipse()`. Une ellipse est une forme avec un seul côté et sans coins. Elle peut être écrasée, comme un ovale, ou parfaitement ronde, comme un cercle.

Une ellipse nécessite des coordonnées `x` et `y` , largeur et hauteur. Les coordonnées `x` et `y` d'une ellipse sont la position centrale.

Le cercle bleu couvrira le triangle marron où ils se chevauchent, car le cercle a été dessiné plus tard.

**Astuce :** Pour faire un cercle, les **largeur** et **hauteur** doivent être identiques.

--- code ---
---
language: python filename: main.py - draw() line_numbers: true line_number_start: 31
line_highlights: 33-34
---

  fill(bois)   
triangle(150, 350, 200, 150, 250, 350)   
fill(exterieur)    
ellipse(200, 200, 170, 170) #Cercle extérieur. 200, 200 est le milieu de l'écran

--- /code ---

--- /task ---

--- task ---

**Test :** Exécute ton code pour voir le premier grand cercle bleu.

![Un triangle marron et un cercle bleu sur l'herbe et contre un ciel.](images/blue-circle.png)

--- /task ---

--- task ---

Crée deux nouvelles variables pour stocker les couleurs `intérieur` et `centre` pour les cercles restants.

Attribue des couleurs aux variables `intérieure` et `centre` en utilisant `color()`.

La fonction `color()` attend trois nombres : un pour le rouge, le vert et le bleu.

Nous avons utilisé des chiffres qui donnent les couleurs traditionnelles des cibles de tir à l'arc, mais tu peux utiliser les couleurs que tu aimes tant qu'elles sont différentes les unes des autres.

[[[generic-theory-simple-colours]]]

--- code ---
---
language: python filename: main.py - draw() line_numbers: true line_number_start: 18
line_highlights: 24-25
---

def dessin():   
#Choses à faire dans chaque image

  ciel = color(92, 204, 206)   
herbe = color(149, 212, 122)   
bois = color(145, 96, 51)   
exterieur = color(0, 120, 180) #Bleu    
interieur = color(210, 60, 60) #Rouge    
centre = color(220, 200, 0) #Jaune

--- /code ---

--- /task ---

--- task ---

La cible est constituée de cercles de tailles différentes avec les mêmes coordonnées centrales (200, 200) - le milieu de l'écran.

Ajoute deux autres cercles pour représenter un cercle intérieur et le centre. Change le `fill()` avant de dessiner chaque cercle.

--- code ---
---
language: python filename: main.py - draw() line_numbers: true line_number_start: 33
line_highlights: 37-40
---

  fill(bois)    
triangle(150, 350, 200, 150, 250, 350) #Support    
fill(exterieur)   
ellipse(200, 200, 170, 170) #Cercle extérieur   
fill(interieur)   
ellipse(200, 200, 110, 110) #Cercle interieur   
fill(centre)   
ellipse(200, 200, 30, 30) #Centre

--- /code ---

--- /task ---

--- task ---

**Test :** Exécute à nouveau ton projet pour voir la cible avec trois cercles colorés. Change les couleurs jusqu'à ce que tu en sois satisfait.

![Un triangle marron avec trois cercles colorés sur l'herbe et contre un ciel.](images/three-circles.png)

**Débogage:** Python utilise l'orthographe américaine de « color » (sans "u") alors assure-toi de faire de même.

--- /task ---

--- save ---

