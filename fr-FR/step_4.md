## Tirer la flèche

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Il est maintenant temps d'ajouter une flèche qui se déplace de manière aléatoire sur la zone cible.
</div>
<div>

![La cible, avec une flèche circulaire marron apparaissant dans diverses positions.](images/fire_arrow.gif){:width="300px"}

</div>
</div>

--- task ---

Trouve le commentaire **La fonction tire_fleche vient ici** et en dessous ajoute du code pour définir ta `fonction tire_fleche()`.

Ajoute une petite `ellipse()` au centre de l'écran pour représenter la flèche.

--- code ---
---
language: python 
filename: main.py — shoot_arrow() 
line_numbers: true 
line_number_start: 10
line_highlights: 11-12
---

#La fonction tire_fleche vient ici
def tire_fleche():   
  ellipse(200, 200, 15, 15)

--- /code ---

--- /task ---

--- task ---

Va au code `draw()` qui crée la cible et ajoute du code à la fin pour définir le `fill()` à `bois`, puis appelle ta nouvelle fonction `tire_fleche()`.

--- code ---
---
language: python 
filename: main.py — draw() 
line_numbers: true 
line_number_start: 41
line_highlights: 44-45
---

  fill(centre)    
  ellipse(200, 200, 30, 30)

  fill(bois)   
  tire_fleche()

--- /code ---

--- /task ---

--- task ---

**Test :** Exécute ton code et vois la flèche apparaître dans le centre.

![La cible sur l'arrière-plan avec une flèche de cercle marron dessus.](images/arrow-middle.png)

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;"> Les jeux informatiques, les vidéos et les animations créent l'effet de mouvement en montrant de nombreuses images les unes après les autres. Chaque image est appelée une <span style="color: #0faeb0; font-weight: bold;">image</span>. La vitesse à laquelle l'image change est appelée <span style="color: #800080;">frame rate</span> et est donnée en <span style="color: #800080;">fps</span> ou images par seconde.  
</p>

La ligne `frame_rate(2)` dans `setup()` définit la fréquence d'images à 2 images par seconde.

La fonction `draw()` est appelée à chaque image. Tu vas dessiner la flèche dans une position aléatoire à chaque fois que `draw()` est appelé.

L'arrière-plan et la cible seront dessinés sur l'ancienne flèche. Cela signifie que tu ne vois qu'une seule flèche à la fois.

--- task ---

Trouve les instructions `import`, en haut de ton code, tu vas utiliser `randint` de la bibliothèque `random`.

--- code ---
---
language: python 
filename: main.py 
line_numbers: true
line_number_start: 3
---

#Importer le code de la bibliothèque
from p5 import *    
from math import *    
from random import randint

--- /code ---

--- /task ---

--- task ---

Va à ta fonction `tire_fleche()` et ajoute deux nouvelles variables `fleche_x` et `fleche_y` pour stocker des nombres aléatoires entre `100` et `300`.

Cela permettra à certains tirs de manquer la cible, sans qu'ils n'aillent jusqu'aux bords de ton jeu.

Change ton `ellipse()` pour utiliser les nouvelles variables pour positionner ta flèche.

![Un rectangle montrant les coordonnées de la zone cible dans un rectangle semi-transparent.](images/target_area.png)

--- code ---
---
language: python 
filename: main.py — shoot_arrow() 
line_numbers: true 
line_number_start: 10
line_highlights: 12-14
---

#La fonction tire_fleche vient ici
def tire_fleche():    
  fleche_x = randint(100, 300)   
  fleche_y = randint(100, 300)    
  ellipse(fleche_x, fleche_y, 15, 15) #Mise à jour des coordonnées aléatoires

--- /code ---

--- /task ---

### Obtiens la couleur que la flèche frappe

La fonction `get()` renvoie la couleur d'un pixel.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Un <span style="color: #0faeb0; font-weight: bold;">pixel</span>, abréviation d'élément d'image, est un point coloré unique dans une image. Les images sont composées de beaucoup de pixels colorés.
</p>

--- task ---

Tu dois stocker la couleur visée par la flèche avant de dessiner une flèche dessus.

Ajoute du code pour stocker le `touche_couleur`. Utilise la fonction `get()` pour obtenir la couleur du pixel aux coordonnées `fleche_x` et `fleche_y` — le centre de la flèche.

--- code ---
---
language: python 
filename: main.py — shoot_arrow() 
line_numbers: true 
line_number_start: 10
line_highlights: 14
---

#La fonction tire_fleche vient ici
def tire_fleche():    
  fleche_x = randint(100, 300)    
  fleche_y = randint(100, 300)    
  touche_couleur = get(fleche_x, fleche_y) #Enregistrer la couleur avant de dessiner la flèche   
  ellipse(fleche_x, fleche_y , 15, 15)

--- /code ---

**Astuce :** Le code pour obtenir la couleur et l'enregistrer doit être **avant** le code pour dessiner l'ellipse sinon tu enregistreras toujours la couleur du bois de la flèche !

--- /task ---

La bibliothèque `p5` « écoute » certains événements, l'un d'eux est la pression du bouton de la souris. Lorsqu'il détecte que le bouton a été enfoncé, il exécute le code qui lui a été donné dans la fonction `mouse_pressed()`.

--- task ---

Trouve le commentaire **# La fonction souris_pressee vient ici** et en dessous ajoute du code pour définir ta fonction `mouse_pressed()`.

Ajoute du code pour imprimer les quantités de rouge, de vert et de bleu dans le pixel sur lequel la flèche atterrit.

--- code ---
---
language: python 
filename: main.py - mouse_pressed() 
line_numbers: true 
line_number_start: 8
line_highlights: 9-10
---

#La fonction souris_pressee vient ici
def souris_pressee():    
  print( red(couleur_touche), green(couleur_touche), blue(couleur_touche) )

--- /code ---

--- /task ---

--- task ---

Tu as défini deux fonctions `tire_fleche()` et `mouse_pressed()`, ces deux fonctions doivent utiliser la variable `couleur_touche`.

Une variable qui doit être utilisée tout au long d'un programme est connue sous le nom de **variable globale**. Ajoute du code à ta fonction `tire_fleche()` pour faire de `couleur_touche` une variable globale :

--- code ---
---
language: python 
filename: main.py - shoot_arrow() 
line_numbers: true 
line_number_start: 12
line_highlights: 14
---

#La fonction tire_fleche vient ici
def tire_fleche():    
  global couleur_touche #Peut être utilisé dans d'autres fonctions     
  fleche_x = randint(100, 300)     
  fleche_y = randint(100, 300)     
  couleur_touche = get(fleche_x, fleche_y) #Enregistrer la couleur avant de dessiner la flèche     
  ellipse(fleche_x, fleche_y, 15, 15)

--- /code ---

--- /task ---

--- task ---

**Test :** Exécute ton projet. La flèche est redessinée à des coordonnées aléatoires.

Le projet obtient le `couleur_touche` chaque fois que la flèche est redessinée et imprime la valeur de couleur dans la zone de sortie sous la cible.

![La cible, avec une flèche circulaire marron apparaissant dans une variété de positions.](images/fire_arrow.gif)

**Débogage :** Si tu vois un message indiquant que `couleur_touche` n'est pas défini, reviens à `tire_fleche()` et vérifie que tu as bien la ligne `global couleur_touche`.

**Débogage :** Vérifie très attentivement la ligne `print` pour les virgules et les parenthèses.

--- /task ---

--- save ---

