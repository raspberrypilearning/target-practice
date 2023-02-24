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

Ouvre le [projet de démarrage Tir à l'arc](https://trinket.io/python/9973649e5c){:target="_blank"}.

Si tu as un compte Trinket, tu peux cliquer sur le bouton **Remix** pour enregistrer une copie dans ta bibliothèque `My Trinkets`.

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
language: python filename: main.py — configuration() line_numbers: true line_number_start: 11
line_highlights: 25
---
def configuration():
# Configurer ton jeu ici
  size(400, 400) # largeur et hauteur de l'écran frame_rate(2) no_stroke()

--- /code ---

--- /task ---

--- task ---

**Exécute** à nouveau ton projet pour vérifier 👀 que la bordure (trait) a disparue.

--- /task ---

### Dessiner l'herbe

--- task ---

**Ajoute** du code pour dessiner un rectangle vert en bas de l'écran.

![La zone de sortie avec un rectangle de couleur ciel au-dessus d'un rectangle de couleur herbe pour créer l'arrière-plan. Le coin supérieur gauche du rectangle est marqué x=0, y=250 ; c'est l'origine du rectangle. La largeur est surlignée à 400 et la hauteur à 150. Le code rect(0, 0, 400, 250) s'affiche.](images/green-grass.png){:width="400px"}

--- code ---
---
language: python filename: main.py — dessin() line_numbers: true line_number_start: 17
line_highlights: 27, 28
---
def dessin():
# Choses à faire dans chaque image
  global bois ciel= color(92, 204, 206) # Rouge = 92, Vert = 204, Bleu = 206 herbe = color(149, 212, 122) bois = color(145, 96, 51) exterieur = color(0, 120, 180)

  fill(ciel)     
rect(0, 0, 400, 250)     
fill(herbe) # Défini la couleur de remplissage de l'herbe rect(0, 250, 400, 150) # x, y, largeur, hauteur

--- /code ---

**Astuce :** 💡 Nous avons ajouté des commentaires à notre code, comme `# Définir la couleur de remplissage à l'herbe`, pour t'indiquer ce qu'il fait. Tu n'as pas besoin d'ajouter ces commentaires à ton code, mais ils peuvent être utiles pour te rappeler ce que font les lignes de code.

--- /task ---

--- task ---

**Test :** 🔄 Exécute à nouveau ton projet pour afficher l'arrière-plan terminé.

![La zone de sortie avec un rectangle de couleur ciel au-dessus d'un rectangle de couleur herbe pour créer l'arrière-plan.](images/background.png){:width="400px"}

--- /task ---

