## Ajouter une flèche

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Ajoute un cercle encore plus petit pour représenter une flèche.
</div>
<div>

![La cible, avec une flèche circulaire marron apparaissant dans diverses positions.](images/fire_arrow.gif){:width="300px"}

</div>
</div>

### Où vas-tu tirer ?

--- task ---

Ajoute une fonction pour dessiner un cercle brun aux coordonnées `200`, `200`.

--- code ---
---
language: python
line_numbers: true
line_number_start: 8
line_highlights: 9-13
---
# La fonction tire_fleche vient ici
def tire_fleche():   
    fleche_x = 200
    fleche_y = 200
    fill('brown')
    circle(fleche_x, fleche_y, 15)

--- /code ---

--- /task ---

--- task ---

Appelle ta nouvelle fonction `tire_fleche()`{:.language-python} à la fin de ta fonction `draw()`{:.language-python}.

--- code ---
---
language: python
line_numbers: true
line_number_start: 33
line_highlights: 35
---
    fill('yellow')      
    circle(200, 200, 30)  
    tire_fleche()

--- /code ---

--- /task ---

--- task ---

**Test :** clique sur le bouton **Run**. Tu devrais voir la flèche au centre.

![un cercle de flèche brun au centre de la cible](images/arrow-centre.png)


--- /task ---

La flèche doit se déplacer de manière aléatoire.


--- task ---

Modifie les variables `fleche_x`{:.language-python} et `fleche_y`{:.language-python} pour choisir un nombre aléatoire entre 100 et 300.

--- code ---
---
language: python
line_numbers: true
line_number_start: 9
line_highlights: 10-11
---
def tire_fleche():
    fleche_x = randint(100, 300)
    fleche_y = randint(100, 300)
    fill('brown')
    circle(fleche_x, fleche_y, 15)

--- /code ---

--- /task ---


--- task ---


**Test :** clique sur le bouton **Run**. Tu devrais voir la flèche sauter autour de la cible.

![Une animation de cible avec une flèche circulaire marron apparaissant dans diverses positions.](images/fire_arrow.gif)

--- /task ---

--- save ---
