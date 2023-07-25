## Tirer la flèche

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Lorsque tu cliques ou appuies, une flèche est tirée à la position d'un cercle cible en mouvement. 
</div>
<div>

![La cible, avec une flèche circulaire marron apparaissant dans diverses positions.](images/fire_arrow.gif){:width="300px"}

</div>
</div>

### Dessiner un cercle cible à chaque image

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;"> Les ordinateurs créent l'effet de mouvement en montrant beaucoup d'images les unes après les autres. Chaque image est appelée une <span style="color: #0faeb0; font-weight: bold;">frame</span>.   
</p>

--- task ---

Définis ta fonction `tire_fleche()` sous le commentaire **# La fonction tire_fleche vient ici**.

Ajoute du code pour dessiner au hasard un cercle marron dans une zone cible :

![Un rectangle montrant les coordonnées de la zone cible dans un rectangle semi-transparent. La zone cible est comprise entre x=100 et y=100 et x=300 et y=300, ce qui couvre toute la cible et même plus.](images/target_area.png)

--- code ---
---
language: python filename: main.py — tire_fleche() line_numbers: true line_number_start: 10
line_highlights: 11-12
---
# La fonction tire_fleche vient ici
def tire_fleche():    
fleche_x = randint(100, 300)    
fleche_y = randint(100, 300)    
touche_couleur = get(fleche_x, fleche_y) #Enregistrer la couleur avant de dessiner la flèche   
ellipse(fleche_x, fleche_y , 15, 15)

--- /code ---

--- /task ---

--- task ---

Va dans la fonction `dessin` et appelle ta nouvelle fonction `tire_fleche`.

--- code ---
---
language: python filename: main.py — draw() line_numbers: true line_number_start: 41
line_highlights: 44-45
---

    fill('yellow')  # Set the colour for the circle fill to yellow      
    circle(200, 200, 30)  # Draw the middle circle using x, y, width
    shoot_arrow()

--- /code ---

--- /task ---

--- task ---

**Test :** Exécute ton code et vois la flèche apparaître dans le centre.

![La cible sur l'arrière-plan avec une flèche de cercle marron dessus.](images/fire_arrow.gif)

L'arrière-plan et la cible seront dessinés sur l'ancienne flèche. Cela signifie que tu ne vois qu'une seule flèche à la fois.

--- /task ---

### Obtenir la couleur touchée par la flèche

La fonction `get()` renvoie la couleur d'un pixel.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Un <span style="color: #0faeb0; font-weight: bold;">pixel</span>, abréviation d'élément d'image, est un point coloré unique dans une image. Les images sont composées de beaucoup de pixels colorés.
</p>

--- task ---

Tu as défini deux fonctions `tire_fleche()` et `mouse_pressed()`, ces deux fonctions doivent utiliser la variable `couleur_touche`.

Ajoute du code pour stocker le `touche_couleur`. Utilise la fonction `get()` pour obtenir la couleur du pixel aux coordonnées `fleche_x` et `fleche_y` — le centre de la flèche.

--- code ---
---
language: python filename: main.py line_numbers: true
line_highlights: 9-10
---
# La fonction tire_fleche vient ici
def tire_fleche():    
global couleur_touche #Peut être utilisé dans d'autres fonctions     
fleche_x = randint(100, 300)     
fleche_y = randint(100, 300)     
couleur_touche = get(fleche_x, fleche_y) #Enregistrer la couleur avant de dessiner la flèche     
ellipse(fleche_x, fleche_y, 15, 15)

--- /code ---

**Astuce :** 💡 Le code pour `obtenir` la couleur doit être **avant** le code pour dessiner le `cercle` sinon tu enregistreras toujours la couleur bois de la flèche !

--- /task ---

### Imprimer la couleur lorsque la souris est pressée

La bibliothèque `p5` « écoute » certains événements, l'un d'eux est la pression du bouton de la souris. Lorsqu'elle détecte que le bouton a été pressé, elle exécute le code qui lui a été donné dans la fonction `souris_pressee`.

--- task ---

Définis ta fonction `souris_pressee()` sous le commentaire **# La fonction souris_pressee vient ici**.

Add code to print the target emoji 🎯 when the mouse is clicked.

--- code ---
---
language: python filename: main.py — tire_fleche() line_numbers: true line_number_start: 10
line_highlights: 12-14
---

# La fonction souris_pressee vient ici
def souris_pressee():    
print( red(couleur_touche), green(couleur_touche), blue(couleur_touche) )

--- /code ---

--- /task ---

--- task ---

**Test :** Exécute ton projet.

The project prints 🎯 each time the arrow is redrawn.

![La cible, avec une flèche circulaire marron apparaissant dans une variété de positions.](images/fire_arrow.gif)

**Débogage :** Si tu vois un message indiquant que `couleur_touche` n'est pas défini, reviens à `tire_fleche()` et vérifie que tu as bien la ligne `global couleur_touche`.

**Débogage :** Vérifie très attentivement la ligne `print` pour les virgules et les parenthèses.

--- /task ---

--- save ---
