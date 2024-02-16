
--- question ---
---
legend: Question 3 sur 3
---

Un cercle est dessiné en utilisant le code suivant :

--- code ---
---
language: python
---

def setup():   
  size(400, 400)   
  fill(0, 255, 0)   
  no_stroke()

def draw():   
  circle(0, 0, 300)

run()

--- /code ---

Laquelle des images ci-dessous montre la position correcte de ce cercle dans la zone de sortie ?

--- choices ---

- ( ) ![Un cercle vert centré dans le coin inférieur droit de la zone de sortie.](images/bottom-right.png)

  --- feedback ---

  Pas tout à fait, pour centrer le cercle dans le coin inférieur droit, les coordonnées doivent être identiques à la taille de l'écran. Dans cet exemple, le cercle serait `circle(400, 400, 300)`.

  --- /feedback ---

- ( ) ![Un cercle vert centré au milieu de la zone de sortie.](images/centre.png)

  --- feedback ---

  Pas tout à fait, pour centrer le cercle au centre, les coordonnées devraient être la moitié de la taille de l'écran. Dans cet exemple, `circle(200, 200, 300)`.

  --- /feedback ---

- (x) ![Un cercle vert centré dans le coin supérieur gauche de la zone de sortie.](images/top-left.png)

  --- feedback ---

  C'est correct ! Ce cercle est centré aux coordonnées (0,0), le coin supérieur gauche de l'écran.

  --- /feedback ---

- ( ) ![Un cercle vert centré vers le côté supérieur droit de la zone de sortie.](images/random-side.png)

  --- feedback ---

  Non, cette ellipse aurait le code `circle(350, 150, 300)` pour le centrer vers le haut à droite de l'écran. La coordonnée `x` est la distance horizontale entre l'ellipse et le bord de l'écran, et la coordonnée `y` est la distance verticale sur l'écran.

  --- /feedback ---

--- /choices ---

--- /question ---
