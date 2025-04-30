## Questionnaire rapide

Réponds aux trois questions. Il y a des indices pour te guider vers la bonne réponse.

Lorsque tu as répondu à chaque question, clique sur **Vérifier ma réponse**.

Amuse-toi bien !

--- question ---
---
legend: Question 1 sur 3
---
Dans ton projet, tu as ajouté `randint(100, 300)` à ta fonction `tire_fleche()`. Que fait `randint(100, 300)` ?

--- code ---
---
language: python
---

def tire_fleche():
    global touche_couleur
    fleche_x = randint(100, 300)
    fleche_y = randint(100, 300)
  
--- /code ---

--- choices ---

- (x) Il choisit un nombre entier aléatoire entre 100 et 300.

  --- feedback ---

C'est correct ! Cela permet de choisir une coordonnée x aléatoire pour ta flèche.

  --- /feedback ---

- ( ) Cela fait bouger la flèche de manière aléatoire sur l'écran.

  --- feedback ---

Pas tout à fait. Ce code explique en partie comment la flèche se déplace de manière aléatoire, mais tu as besoin d'autres codes pour atteindre cet objectif.

  --- /feedback ---

- () Il s'agit de la couleur qui a été touchée par la flèche.

  --- feedback ---

  Pas tout à fait. La fonction get() est utilisée pour obtenir la couleur.

  --- /feedback ---

- ( ) Il dessine un cercle de taille aléatoire.

  --- feedback ---

  Pas tout à fait. La fonction circle() serait utilisée pour dessiner un cercle.

  --- /feedback ---

--- /choices ---

--- /question ---
