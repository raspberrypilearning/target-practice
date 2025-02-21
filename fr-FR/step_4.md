## Tirer la flèche

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Add an even smaller circle to represent an arrow.
</div>
<div>

![La cible, avec une flèche circulaire marron apparaissant dans diverses positions.](images/fire_arrow.gif){:width="300px"}

</div>
</div>

### Where will you shoot?

--- task ---

Ajoute du code pour dessiner au hasard un cercle marron dans une zone cible :

--- code ---
---
language: python filename: main.py — shoot_arrow() line_numbers: true line_number_start: 7
line_highlights: 8-12
---
# La fonction tire_fleche vient ici
def tire_fleche():    
global couleur_touche #Peut être utilisé dans d'autres fonctions     
fleche_x = randint(100, 300)     
fleche_y = randint(100, 300)     
couleur_touche = get(fleche_x, fleche_y) #Enregistrer la couleur avant de dessiner la flèche     
ellipse(fleche_x, fleche_y, 15, 15)

--- /code ---

--- /task ---

--- task ---

Va dans la fonction `draw` et appelle ta nouvelle fonction `tire_fleche`.

--- code ---
---
language: python filename: main.py — draw() line_numbers: true line_number_start: 31
line_highlights: 33
---

    fill('yellow')  # Définis la couleur du remplissage du cercle sur jaune     
    circle(200, 200, 30)  # Dessine le cercle du milieu en utilisant x, y, largeur
    tire_fleche()

--- /code ---

--- /task ---

--- task --- **Test:** Click the **Run** button. You should see the arrow in the centre.

![a brown arrow circle in the centre of the target](images/arrow-centre.png) --- /task ---

The arrow needs to move randomly.

--- task --- Change the `arrow_x`{:.language-python} and `arrow_y`{:.language-python} variables to choose a random number between 100 and 300.

--- code ---
---
language: python filename: main.py - mouse_pressed() line_numbers: true line_number_start: 5
line_highlights: 9, 12
---
def tire_fleche():    
fleche_x = randint(100, 300)    
fleche_y = randint(100, 300)    
touche_couleur = get(fleche_x, fleche_y) #Enregistrer la couleur avant de dessiner la flèche   
ellipse(fleche_x, fleche_y , 15, 15)

--- /code ---

--- /task ---


--- task ---


**Test :** 🔄 exécute ton projet. You should see the arrow jump around the target.

![Une animation de cible avec une flèche circulaire marron apparaissant dans diverses positions.](images/fire_arrow.gif)

--- /task ---

--- save ---
