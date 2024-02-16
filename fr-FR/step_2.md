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

Ouvre le [projet de démarrage Tir sur cible](https://editor.raspberrypi.org/fr-FR/projects/target-practice-starter){:target="_blank"}. Le Code Editor s'ouvrira dans un autre onglet du navigateur.

Si tu as un compte Raspberry Pi, tu peux cliquer sur le bouton **Enregistrer** pour enregistrer une copie dans tes **Projets**.

--- /task ---

### Modifier le ciel

--- task ---

Le projet de démarrage contient du code déjà écrit pour toi.

Clique sur **« Run »** pour voir un rectangle rempli de bleu dessiné à partir de x=`0`, y=`0` (le haut de l'écran). Ce rectangle de `400` x `250` pixels représente le ciel.

![Un rectangle bleu entouré d'une bordure noire, au-dessus d'un rectangle gris. Le coin supérieur gauche du canevas est marqué par x=0, y=0 c'est l'origine du rectangle. La largeur est surlignée à 400 et la hauteur à 250. Le code rect(0, 0, 400, 250) s'affiche.](images/sky_stroke.png){:width="400px"}

**Astuce :** 💡 les coordonnées commencent à partir de (x=0, y=0) dans le coin supérieur gauche. Cela peut être différent des autres systèmes de coordonnées que tu as utilisés.

--- /task ---

--- task ---

Le ciel a été dessiné avec une bordure noire (trait).

Pour désactiver le trait pour toutes les formes, ajoute `no_stroke()` à la fonction `setup` :

--- code ---
---
language: python
filename: main.py — setup()
line_numbers: true
line_number_start: 9
line_highlights: 12
---
def setup():
# Configurer ton jeu ici

    size(400, 400)  # largeur et hauteur de l'écran
    no_stroke()

--- /code ---

--- /task ---

--- task ---

**Exécute** à nouveau ton projet pour vérifier 👀 que la bordure (trait) a disparue.

**Astuce :** 💡 tu devras appuyer sur **Stop** pour arrêter ton programme, cela fera réapparaître le bouton **Run**.

--- /task ---

### Dessiner l'herbe

--- task ---

**Ajoute** du code pour dessiner un rectangle vert en bas de l'écran.

![La zone de sortie avec un rectangle de couleur ciel au-dessus d'un rectangle de couleur herbe pour créer l'arrière-plan. Le coin supérieur gauche du rectangle est marqué x=0, y=250 ; c'est l'origine du rectangle. La largeur est surlignée à 400 et la hauteur à 150. Le code rect(0, 0, 400, 250) s'affiche.](images/green-grass.png){:width="400px"}

--- code ---
---
language: python
filename: main.py — draw()
line_numbers: true
line_number_start: 14
line_highlights: 18-19
---
def draw():
# Choses à faire dans chaque frame

    fill('cyan')  # Définis la couleur de remplissage du ciel sur cyan
    rect(0, 0, 400, 250)  # Dessine un rectangle pour le ciel avec ces valeurs pour x, y, largeur, hauteur
    fill('lightgreen')  # Définis la couleur de remplissage de l'herbe sur vert clair
    rect(0, 250, 400, 150)  # Dessine un rectangle pour l'herbe avec ces valeurs pour x, y, largeur, hauteur

--- /code ---

**Astuce :** 💡 nous avons ajouté des commentaires à notre code, comme `# Définir la couleur de remplissage du ciel en cyan`, pour t'indiquer ce qu'il fait. Tu n'as pas besoin d'ajouter des commentaires à ton code, mais ils peuvent être utiles pour te rappeler ce que font les lignes de code.

--- /task ---

--- task ---

**Test :** 🔄 exécute à nouveau ton projet pour voir l'arrière-plan terminé.

![La zone de sortie avec un rectangle de couleur ciel au-dessus d'un rectangle de couleur herbe pour créer l'arrière-plan.](images/background.png){:width="300px"}

--- /task ---

--- save ---
