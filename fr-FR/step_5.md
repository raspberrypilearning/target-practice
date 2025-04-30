## Quelle est la couleur atteinte ?

Ensuite, tu ajouteras du code pour obtenir la couleur à l’emplacement de la flèche.

### Obtenir la couleur touchée par la flèche

--- task ---

Ajoute une nouvelle **variable globale** appelée `couleur_touchee`.

Ajoute du code pour `obtenir` la couleur au centre de la flèche et la stocker dans la variable `couleur_touchee`.


--- code ---
---
language: python
line_numbers: true
line_number_start: 9
line_highlights: 10, 13, 14
---
def shoot_arrow():
    global couleur_touchee  
    fleche_x = randint(100, 300)  
    fleche_y = randint(100, 300) 
    couleur_touchee = get(fleche_x, fleche_y).hex
    print(couleur_touchee)
    fill('brown')
    circle(fleche_x, fleche_y, 15)

--- /code ---

**Astuce :** le code pour `obtenir` la couleur doit être **avant** le code pour dessiner le `cercle` sinon tu garderas toujours la couleur brune de la flèche !

--- /task ---

--- task ---

**Test :** clique sur le bouton **Run** . Tu devrais voir les couleurs imprimées dans **Text output**, au format hexadécimal.

--- /task ---

### Exécuter le code lorsque la souris est pressée

--- task ---

Commente la ligne qui imprime la couleur. Cela signifie qu'elle ne s'exécuteras pas.

--- code ---
---
language: python
line_numbers: true
line_number_start: 13
line_highlights: 14
---
    couleur_touchee = get(fleche_x, fleche_y).hex
    # print(couleur_touchee)
    circle(fleche_x, fleche_y, 15)

--- /code ---

--- /task ---

--- task ---

Ajoute du code pour imprimer l'emoji cible 🎯 **quand la souris est cliquée**.

--- code ---
---
language: python
line_numbers: true
line_number_start: 5
line_highlights: 6-7
---
# La fonction souris_pressee vient ici
def mouse_pressed():    
    print('🎯')

--- /code ---

--- /task ---

--- task --- 

**Test :** clique sur le bouton **Run**. Tu dois voir le caractère 🎯 s'imprimer lorsque tu cliques sur la cible avec la souris.

![emoji cible imprimé lorsque l'on clique sur la souris](images/target_printed.gif)

--- /task ---

--- save ---