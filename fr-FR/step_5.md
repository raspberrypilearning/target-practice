## What colour did you hit?

Next, you will add some code to get the colour at the location of the arrow.

### Get the colour hit by the arrow

--- task ---

**Débogage :** 🐞 si tu vois un message indiquant que `touche_couleur` n'est pas « défini », reviens à `draw()` et vérifie que la ligne déclaration `touche_couleur` comme une variable globale.

Add code to `get` the colour at the centre of the arrow ,and store it in the `hit_colour` variable.


--- code ---
---
language: python filename: main.py - mouse_pressed() line_numbers: true line_number_start: 6
line_highlights: 7
---
def mouse_pressed():     
if touche_couleur == Color('blue').hex: #Comme les fonctions, les instructions "if" sont indentées   
print('tu as touché le cercle extérieur, 50 points !')

--- /code ---

**Débogage :** 🐞 assure-toi d'avoir utilisé la chaîne `.hex` pour **tes** couleurs de cercle.

--- /task ---

--- task ---

**Test :** 🔄 exécute ton projet. Essaie de tirer la flèche sur le cercle extérieur bleu pour voir le message.

--- /task ---

### Run code when the mouse is pressed

--- task --- Comment out the line that prints the colour. This means it will not run.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 6
line_highlights: 7, 8
---

    def mouse_pressed():
        if touche_couleur == Color('blue').hex:<br x-id="3" />
            print('Tu as touché le cercle extérieur, 50 points !')
        elif touche_couleur == Color('red').hex:
            print('Tu as touché le cercle intérieur, 200 points !')
        elif touche_couleur == Color('yellow').hex:
            print('Tu as touché le centre, 500 points !')
--- /code ---

--- /task ---

--- task --- Add code to print the target emoji 🎯 **when the mouse is clicked**.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 5
line_highlights: 9-12
---
# La fonction souris_pressee vient ici
def mouse_pressed():

--- /task ---

**Test :** 🔄 exécute ton projet. Essaie de tirer la flèche sur les cercles intérieurs et intermédiaires pour voir leurs messages.

![target emoji printed when mouse clicked](images/target_printed.gif) --- /task ---


--- save ---