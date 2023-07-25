## Marquer des points

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Ton jeu ajoutera des scores en fonction de l'endroit où la flèche frappe.
</div>
<div>

![La cible, avec la flèche apparaissant dans diverses positions et les scores apparaissant sous forme de texte sous le jeu.](images/points-scored.gif){:width="300px"}

</div>
</div>

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Nous utilisons <span style="color: #0faeb0; font-weight: bold;"> si … sinon </span> pour prendre des décisions. We could say 'if the pencil is blunt, then sharpen it'. Similarly, `if` conditions let us write code that do something different depending on whether a condition is true or false.
</p>

### Afficher les scores

--- task ---

Delete ❌ the `print('🎯')` line of code.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 9
line_highlights: 28
---
# The mouse_pressed function goes here
def mouse_pressed():


--- /code ---

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Nous utilisons des <span style="color: #0faeb0; font-weight: bold;">conditions</span> tout le temps pour prendre des décisions. On pourrait dire « si le crayon est émoussé, alors taille-le ». De même, les conditions « if » nous permettent d'écrire du code qui fait quelque chose de différent selon qu'une condition est vraie ou fausse.
</p>

--- task ---

Pour `imprimer` un message pour le cercle extérieur de la cible, ajoute du code à ta fonction `mouse_pressed()` pour vérifier si le `couleur_touche` est `==` à `exterieur`.

Sois prudent lorsque tu utilise le symbole `=` en Python :

--- code ---
---
language: python filename: main.py - mouse_pressed() line_numbers: true line_number_start: 8
line_highlights: 10-11
---

# La fonction souris_pressee vient ici
def mouse_pressed():     
if couleur_touche == exterieur:      
print('tu as touché le cercle extérieur, 50 points !') #Comme les fonctions, les instructions "if" sont indentées

--- /code ---

**Tip:** 💡 If you changed the colour of your outer circle then you will need to replace `'blue'` with the colour name that you have chosen.

--- /task ---

--- task ---

**Test :** Exécute ton projet. Essaye d'arrêter la flèche sur les cercles rouges et jaunes pour voir leurs messages.

**Astuce :** `frame_rate()`, dans `setup()`, contrôle la vitesse à laquelle ton jeu dessine. S'il va trop vite, régle-le sur un nombre inférieur.

![La zone de sortie avec une flèche touchant le cercle extérieur. L'instruction d'impression des points apparaît dans la zone de sortie.](images/blue-points.png)

**Debogage :** Assure-toi que ton code correspond exactement et que tu as indenté le code dans ton instruction `if`.

Ajoute `elif` déclarations pour `intérieur` et `centre`.

est utilisé pour tester **équivalence** — comme `couleur_touche == centre` — si les choses de chaque côté ont la même valeur, alors le test est `True`, sinon c'est `False`

--- /task ---

Un `elif` ne peut être utilisé qu'avec une instruction `if` et, comme un `if`, il vérifie une condition. Si la condition est `True`, le `elif` exécute du code. These will be read from top to bottom. As soon as a **True** condition is found, it will be actioned. Any remaining conditions will be ignored.

--- task ---

Comme des points seront marqués si la flèche atterrit également sur les cercles `intérieur` ou `centre`, `extérieur` n'est pas le seul cercle que tu dois vérifier. Pour ce faire, utilise `elif` (une version abrégée de else - if).

--- code ---
---
language: python filename: main.py - mouse_pressed() line_numbers: true line_number_start: 9
line_highlights: 12-15
---

def mouse_pressed(): if hit_colour == Color('blue').hex:   
print('You hit the outer circle, 50 points!') elif hit_colour == Color('red').hex: print('You hit the inner circle, 200 points!') elif hit_colour == Color('yellow').hex: print('You hit the middle, 500 points!')

--- /code ---

--- /task ---

--- task ---

**Test :** Exécute ton projet. Essaye d'arrêter la flèche sur le cercle extérieur bleu pour voir ton message.

![La zone de sortie avec une flèche touchant le cercle intérieur. L'instruction d'impression des points apparaît dans la zone de sortie.](images/yellow-points.png)

**Debogage :** Assure-toi que ton `elif` est au même niveau d'indentation que ton `if`, et que le code à l'intérieur de ton `elif` est au même niveau que le code à l'intérieur de ton `if`.

**Débogage :** Si tu vois un message indiquant que `interieur` ou `centre` sont « non définis », reviens à `draw()` et vérifie qu'ils se trouvent sur la ligne qui déclare les variables globales.

def mouse_pressed():    
if couleur_touche == exterieur:    
print('Tu as touché le cercle extérieur, 50 points !')    
elif couleur_touche == interieur:    
print('Tu as touché le cercle intérieur, 200 points !')   
elif couleur_touche == centre:    
print('Tu as touché le centre, 500 points !')

est utilisé pour **affectation** — comme `fleche_x = 200` pour définir la valeur d'une variable

--- /task ---

### Manquer la cible

Il te reste une décision à prendre : que se passe-t-il si la flèche n'atterrit sur aucun des cercles cibles ? ❌

Pour faire cette dernière vérification, tu utilises `else`.

--- task ---

Ajoute du code à `print` un message `else` si aucune des déclarations `if` et `elif` n'ont été remplies.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 26
line_highlights: 16-17
---

def mouse_pressed():    
if couleur_touche == exterieur:   
print('Tu as touché le cercle extérieur, 50 points !')   
elif couleur_touche == interieur:   
print('Tu as touché le cercle intérieur, 200 points !')   
elif couleur_touche == centre:    
print('Tu as touché le centre, 500 points !') else:   
print('Tu as loupé la cible ! Aucun point !') elif hit_colour == Color('red').hex: print('You hit the inner circle, 200 points!') elif hit_colour == Color('yellow').hex: print('You hit the middle, 500 points!') else:   
print('You missed! No points!')

--- /code ---

--- /task ---

--- task ---

**Test :** Exécute ton projet. Essaye d'arrêter la flèche dans l'herbe ou le ciel pour voir le message manqué.

**Choose:** 💭 Change the number of points scored for the different colours.

--- /task ---

--- save ---
