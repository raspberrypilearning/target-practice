## Dessiner l'herbe

--- task ---

Ouvre le [projet de démarrage Tir sur cible](https://editor.raspberrypi.org/en/projects/target-practice-starter){:target="_blank"}.

--- /task ---


--- task ---

**Ajoute** du code pour dessiner un rectangle vert en bas de l'écran.

![La zone de sortie avec un rectangle de couleur ciel au-dessus d'un rectangle de couleur herbe pour créer l'arrière-plan. Le coin supérieur gauche du rectangle est marqué x=0, y=250 ; c'est l'origine du rectangle. La largeur est surlignée à 400 et la hauteur à 150. Le code rect(0, 0, 400, 250) s'affiche.](images/green-grass.png){:width="400px"}

--- code ---
---
language: python filename: main.py — draw() line_numbers: true line_number_start: 14
line_highlights: 12
---
def draw(): # Things to do in every frame fill('cyan')  
rect(0, 0, 400, 250)  
fill('lightgreen')  
rect(0, 250, 400, 150) --- /code ---

--- /task ---

--- task ---

**Test :** 🔄 exécute à nouveau ton projet pour voir l'arrière-plan terminé.

![La zone de sortie avec un rectangle de couleur ciel au-dessus d'un rectangle de couleur herbe pour créer l'arrière-plan.](images/background.png){:width="400px"}

--- /task ---

--- save ---
