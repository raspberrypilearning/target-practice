## Créer un arrière-plan

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Le ciel et l'herbe sont créés en écrivant du code pour dessiner des rectangles colorés.
</div>
<div>

![La zone de sortie avec un rectangle de couleur ciel au-dessus d'un rectangle de couleur herbe pour créer l'arrière-plan.](images/background.png){:width="300px"}

</div>
</div>

--- task ---

Ouvre le projet [Archery starter](https://trinket.io/python/cd149de1b6){:target="_blank"}.

Si tu as un compte Trinket, tu peux cliquer sur le bouton **Remix** pour enregistrer une copie dans ta bibliothèque `My Trinkets`.

--- /task ---

Le projet de démarrage contient du code déjà écrit pour que tu importes la bibliothèque `p5`, tu utiliseras cette bibliothèque pour créer ton jeu de tir à l'arc.

[[[p5-processing-library]]]

--- task ---

La fonction `fill()` définit la couleur intérieure des formes. Le projet de démarrage contient déjà des couleurs RVB que tu peux utiliser pour ce faire.

Trouve ta fonction `draw()` et prépare-toi à dessiner le ciel en ajoutant du code indenté pour définir la couleur `fill()` sur `ciel` :

--- code ---
---
language: python 
filename: main.py — draw() 
line_numbers: true 
line_number_start: 18
line_highlights: 25
---

def draw():     
  #Choses à faire dans chaque image     
  ciel = color(92, 204, 206) #Rouge = 92, Vert = 204, Bleu = 206     
  herbe = color(149, 212, 122)     
  bois = color(145, 96, 51)     
  exterieur = color(0, 120, 180)

  fill(ciel)

--- /code ---

--- /task ---

L'appel de fonction `size()` dans `setup()` définit la taille de l'écran à 400 pixels sur 400 pixels.

[[[p5-coordinates]]]

--- task ---

Après ton code `fill()` , dessine un `rect()` pour le ciel avec des coordonnées en haut à gauche (`0`,`0`), une largeur de `400` pour correspondre à la largeur de l'écran et une hauteur de `250`.

![Un rectangle bleu avec une grille de coordonnées indiquant la position du rectangle du ciel commençant dans le coin supérieur, au-dessus d'un rectangle gris.](images/sky_coords.png)

--- code ---
---
language: python 
filename: main.py — draw() 
line_numbers: true 
line_number_start: 25
line_highlights: 26
---

  fill(ciel) 
  rect(0, 0, 400, 250) #Départ x, départ y, largeur, hauteur

--- /code ---

--- /task ---

--- task ---

**Test :** Exécute ton code pour voir le ciel que tu as dessiné. Rappelle-toi qu'avec la bibliothèque `p5`, la fonction `run()` appelle la fonction `setup()` une fois, puis la fonction `draw()` à plusieurs reprises.

![Un rectangle bleu entouré d'une bordure noire, au-dessus d'un rectangle gris.](images/sky_stroke.png){:width="300px"}

C'est un peu étrange : il y a une ligne noire autour de ton ciel ! En effet, lorsque le programme démarre, il définit automatiquement une bordure noire - appelée **trait** - autour de tout ce qu'il dessine.

--- /task ---

--- task ---

Désactive le trait en ajoutant `no_stroke()` avant de commencer à dessiner le ciel.

--- code ---
---
language: python 
filename: main.py — draw() 
line_numbers: true 
line_number_start: 23
line_highlights: 25
---

  exterieur = color(0, 120, 180)

  no_stroke()   
  fill(ciel)   
  rect(0, 0, 400, 250) #x, y, largeur, hauteur

--- /code ---

--- /task ---

--- task ---

**Test :** Exécute à nouveau ton projet pour vérifier que le trait a disparu.

--- /task ---

--- task ---

`fill()` change la couleur de remplissage pour toutes les formes dessinées jusqu'à ce que `fill()` soit appelé à nouveau avec une nouvelle couleur.

Change la couleur `fill()` en `herbe` et ajoute encore `rect(x, y, largeur, hauteur)`.

Ce rectangle doit être positionné sous le ciel aux coordonnées (0, 250), de sorte qu'il commence dans la partie inférieure de l'écran.

--- code ---
---
language: python 
filename: main.py — draw() 
line_numbers: true 
line_number_start: 23
line_highlights: 28-29
---

  exterieur = color(0, 120, 180)

  no_stroke()     
  fill(ciel)     
  rect(0, 0, 400, 250) #x, y, largeur, hauteur    
  fill(herbe)    
  rect(0, 250, 400, 150)

--- /code ---

--- /task ---

--- task ---

**Test :** Exécute à nouveau ton projet pour afficher l'arrière-plan terminé.

--- /task ---

--- save ---
