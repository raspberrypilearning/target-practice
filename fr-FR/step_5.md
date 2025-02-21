## What colour did you hit?

Next, you will add some code to get the colour at the location of the arrow.

### Get the colour hit by the arrow

--- task ---

**Débogage :** 🐞 si tu vois un message indiquant que `touche_couleur` n'est pas « défini », reviens à `draw()` et vérifie que la ligne déclaration `touche_couleur` comme une variable globale.

Add code to `get` the colour at the centre of the arrow ,and store it in the `hit_colour` variable.


--- code ---
---
language: python line_numbers: true line_number_start: 9
line_highlights: 10, 13, 14
---
def shoot_arrow(): global hit_colour  
arrow_x = randint(100, 300)  
arrow_y = randint(100, 300) hit_colour = get(arrow_x, arrow_y).hex print(hit_colour) fill('brown') circle(arrow_x, arrow_y, 15)

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
language: python line_numbers: true line_number_start: 13
line_highlights: 14
---

    hit_colour = get(arrow_x, arrow_y).hex
    # print(hit_colour)
    circle(arrow_x, arrow_y, 15)
--- /code ---

--- /task ---

--- task --- Add code to print the target emoji 🎯 **when the mouse is clicked**.

--- code ---
---
language: python line_numbers: true line_number_start: 5
line_highlights: 6-7
---
# La fonction souris_pressee vient ici
def mouse_pressed():    
print('🎯') --- /code ---

--- /task ---

**Test :** 🔄 exécute ton projet. Essaie de tirer la flèche sur les cercles intérieurs et intermédiaires pour voir leurs messages.

![target emoji printed when mouse clicked](images/target_printed.gif) --- /task ---


--- save ---