## Créer un arrière-plan

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Ton jeu a besoin d'un arrière-plan coloré.
</div>
<div>

![La zone de sortie avec un rectangle de couleur ciel au-dessus d'un rectangle de couleur herbe pour créer l'arrière-plan.](images/background.png){:width="300px"}

</div>
</div>

### Ouvrir le projet de démarrage

--- task ---

Open the [Target practice starter](https://editor.raspberrypi.org/en/projects/target-practice-starter){:target="_blank"} project. The code editor will open in another browser tab.

If you have a Raspberry Pi account, you can click on the **Save** button to save a copy to your **Projects**.

--- /task ---

### Modifier le ciel

--- task ---

Le projet de démarrage contient du code déjà écrit pour toi.

Clique sur **« Run »** pour voir un rectangle rempli de bleu dessiné à partir de x=`0`, y=`0` (le haut de l'écran). Ce rectangle de `400` x `250` pixels représente le ciel.

![Un rectangle bleu entouré d'une bordure noire, au-dessus d'un rectangle gris. Le coin supérieur gauche du canevas est marqué par x=0, y=0 c'est l'origine du rectangle. La largeur est surlignée à 400 et la hauteur à 250. Le code rect(0, 0, 400, 250) s'affiche.](images/sky_stroke.png){:width="400px"}

**Astuce :** 💡 Les coordonnées commencent à partir de (x=0, y=0) dans le coin supérieur gauche. Cela peut être différent des autres systèmes de coordonnées que tu as utilisés.

--- /task ---

--- task ---

Le ciel a été dessiné avec une bordure noire (trait).

Pour désactiver le trait pour toutes les formes, ajoute `no_stroke()` à la fonction `configuration` :

--- code ---
---
language: python filename: main.py — draw() line_numbers: true line_number_start: 23
line_highlights: 25
---
def configuration():
# Configurer ton jeu ici

    size(400, 400)  # Width and height of screen
    no_stroke()

--- /code ---

--- /task ---

--- task ---

Change la couleur `fill()` en `herbe` et ajoute encore `rect(x, y, largeur, hauteur)`.

**Test :** Exécute à nouveau ton projet pour vérifier que le trait a disparu.

--- /task ---

### Dessiner l'herbe

--- task ---

**Ajoute** du code pour dessiner un rectangle vert en bas de l'écran.

![La zone de sortie avec un rectangle de couleur ciel au-dessus d'un rectangle de couleur herbe pour créer l'arrière-plan. Le coin supérieur gauche du rectangle est marqué x=0, y=250 ; c'est l'origine du rectangle. La largeur est surlignée à 400 et la hauteur à 150. Le code rect(0, 0, 400, 250) s'affiche.](images/green-grass.png){:width="400px"}

--- code ---
---
language: python filename: main.py — draw() line_numbers: true line_number_start: 18
line_highlights: 26
---
def dessin():
# Choses à faire dans chaque image

    fill('cyan')  # Set the fill colour for the sky to cyan
    rect(0, 0, 400, 250)  # Draw a rectangle for the sky with these values for x, y, width, height
    fill('lightgreen')  # Set the fill colour for the grass to light green
    rect(0, 250, 400, 150)  # Draw a rectangle for the grass with these values for x, y, width, height

--- /code ---

**Test :** Exécute ton code pour voir le ciel que tu as dessiné. You don't need to add comments to your code, but they are helpful to remind you what lines of code do.

--- /task ---

--- task ---

**Test :** Exécute à nouveau ton projet pour afficher l'arrière-plan terminé.

![Le ciel et l'herbe sont créés en écrivant du code pour dessiner des rectangles colorés.](images/background.png){:width="300px"}

--- /task ---

--- save ---
