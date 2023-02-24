## Σχεδίασε τον στόχο σου

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Your game needs a target to shoot arrows at.
</div>
<div>

![Η περιοχή εξόδου με τον στόχο και τη βάση.](images/three-circles.png){:width="300px"}

</div>
</div>

### Σχεδίασε τη βάση

--- task ---

Set the fill colour to `wood` (brown).

Draw a triangle using the x and y coordinates for each of the corners.

![A brown triangle on grass and against a sky with the coordinate points labelled at 150, 350 and 200, 150 and 250, 350). The corners of the canvas are also labelled as x=0, y=0 in the top left and x=400, y=400 i the bottom right.](images/stand_coords.png)Όταν καλείς τη συνάρτηση `triangle()`, πρέπει να παρέχεις τρία σύνολα συντεταγμένων, `x1, y1, x2, y2, x3, y3` που το καθένα αντιπροσωπεύει τη θέση μιας από τις κορυφές του τριγώνου.

--- code ---
---
language: python filename: main.py - draw() line_numbers: true line_number_start: 27
title: Συντεταγμένες τριγώνων
---
  --- /collapse ---

--- /code ---

--- /task ---

--- task ---

language: python filename: main.py - draw() line_numbers: true line_number_start: 28

![A brown triangle on grass and against a sky.](images/target-stand.png)fill(grass)   
rect(0, 250, 400, 150) #x, y, πλάτος, ύψος

--- /task ---

### Σχεδίασε τον στόχο

--- task ---

The largest part of the target is a blue **circle**.

Set the fill colour to `outer` (blue).

Draw a circle with x and y coordinates for its centre and a width.

![A brown triangle and blue circle on grass and against a sky. The circle is labelled with the coordinates x=200, y=200 as the centre and circle width of 170.](images/circle-coords.png)**Δοκιμή:** Εκτέλεσε τον κώδικά σου για να δεις την βάση για τον στόχο σου.

--- code ---
---
language: python filename: main.py - draw() line_numbers: true line_number_start: 29
line_highlights: 31-32
---

  fill(wood)   
triangle(150, 350, 200, 150, 250, 350)   
fill(outer) # Set the circle fill colour to outer    
circle(200, 200, 170) # x, y, width of the circle

--- /code ---

--- /task ---

--- task ---

**Συμβουλή:** Για να φτιάξεις έναν κύκλο, το **πλάτος** και το **ύψος** πρέπει να είναι τα ίδια.

The blue circle was drawn after the stand so it is in front:

![A brown triangle and blue circle on grass and against a sky.](images/blue-circle.png)language: python filename: main.py - draw() line_numbers: true line_number_start: 31

--- /task ---

--- task ---

👀 Find your colour variables in the `draw` function.

Create two variables called `inner` and `middle` to store colours for the other circles.

**Δοκιμή:** Εκτέλεσε τον κώδικά σου για να δεις τον πρώτο μεγάλο μπλε κύκλο.

--- code ---
---
language: python filename: main.py - draw() line_numbers: true line_number_start: 17
line_highlights: 33-34
---
def draw():   
# Things to do in every frame global wood sky = color(92, 204, 206)   
grass = color(149, 212, 122)   
wood = color(145, 96, 51)   
outer = color(0, 120, 180) # Blue    
inner = color(210, 60, 60) # Red    
middle = color(220, 200, 0) # Yellow

--- /code ---

--- /task ---

Η συνάρτηση `color()` χρειάζεται τρεις αριθμούς: έναν για το κόκκινο, έναν για το πράσινο κι έναν για το μπλε.

--- task ---

**Add** coloured circles for the inner and middle parts of the target.

--- code ---
---
language: python filename: main.py - draw() line_numbers: true line_number_start: 18
line_highlights: 24-25
---
  def draw():   
#Πράγματα που πρέπει να κάνεις σε κάθε καρέ

--- /code ---

--- /task ---

--- task ---

**Test:** 🔄 Run your project to see the target with three coloured circles.

![A brown triangle with three coloured circles on grass and against a sky.](images/three-circles.png)Ο στόχος αποτελείται από κύκλους διαφορετικού μεγέθους με τις ίδιες συντεταγμένες του κέντρου (200, 200) — το μέσο της οθόνης.

**Debug:** 🐞 Check that you have used the American spelling of 'color' (without a 'u').

--- /task ---

--- task ---

fill(wood)    
triangle(150, 350, 200, 150, 250, 350) #Βάση    
fill(outer)   
ellipse(200, 200, 170, 170) #Εξωτερικός κύκλος   
fill(inner)   
ellipse(200, 200, 110, 110) #Εσωτερικός κύκλος   
fill(bullseye)   
ellipse(200, 200, 30, 30) #Κέντρο στόχου

[[[generic-theory-simple-colours]]]

![A brown triangle with three coloured circles on grass and against a sky. The colours have changed to pinks and purples.](images/alternative-colours.png){:width="400px"}


--- /task ---



