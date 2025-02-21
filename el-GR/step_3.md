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

Set the fill colour to `brown`.

Draw a triangle using the x and y coordinates for each of the corners.

![A brown triangle on grass and against a sky with the coordinate points labelled at 150, 350 and 200, 150 and 250, 350). The corners of the canvas are also labelled as x=0, y=0 in the top left and x=400, y=400 in the bottom right.](images/stand_coords.png)Όταν καλείς τη συνάρτηση `triangle()`, πρέπει να παρέχεις τρία σύνολα συντεταγμένων, `x1, y1, x2, y2, x3, y3` που το καθένα αντιπροσωπεύει τη θέση μιας από τις κορυφές του τριγώνου.

--- code ---
---
language: python line_numbers: true line_number_start: 21
title: Συντεταγμένες τριγώνων
---

    fill('lightgreen')  
    rect(0, 250, 400, 150)  
    fill('brown') 
    triangle(150, 350, 200, 150, 250, 350)

--- /code ---

--- /task ---

--- task ---

**Test:** Run your code to see the stand for your target:

![A brown triangle on grass and against a sky.](images/target-stand.png)language: python filename: main.py - draw() line_numbers: true line_number_start: 28

--- /task ---

### Σχεδίασε τον στόχο

--- task ---

The largest part of the target is a blue **circle**.

Set the fill colour to `blue`.

Draw a circle with x and y coordinates for its centre and a width.

![A brown triangle and blue circle on grass and against a sky. The circle is labelled with the coordinates x=200, y=200 as the centre and circle width of 170.](images/circle-coords.png){:width="400px"}

--- code ---
---
language: python line_numbers: true line_number_start: 23
line_highlights: 31-32
---

    fill('brown')  
    triangle(150, 350, 200, 150, 250, 350)  
    fill('blue')  
    circle(200, 200, 170)

--- /code ---

--- /task ---

--- task ---

**Test:** Run your code to see the first large blue circle.

Ο μπλε κύκλος θα καλύψει το καφέ τρίγωνο όπου επικαλύπτονται, επειδή ο κύκλος σχεδιάστηκε αργότερα.

![A brown triangle and blue circle on grass and against a sky.](images/blue-circle.png)**Συμβουλή:** Για να φτιάξεις έναν κύκλο, το **πλάτος** και το **ύψος** πρέπει να είναι τα ίδια.

--- /task ---

language: python filename: main.py - draw() line_numbers: true line_number_start: 31

--- task ---

**Add** coloured circles for the inner and middle parts of the target.

--- code ---
---
language: python line_numbers: true line_number_start: 25
line_highlights: 33-34
---

    fill('blue')  
    circle(200, 200, 170)  
    fill('red')  
    circle(200, 200, 110)  # Draw the inner circle 
    fill('yellow')       
    circle(200, 200, 30)  # Draw the middle circle

--- /code ---

--- /task ---

--- task ---

**Test:** Run your project to see the target with three coloured circles.

![A brown triangle with three coloured circles on grass and against a sky.](images/three-circles.png)Δημιούργησε δύο νέες μεταβλητές για να αποθηκεύσεις τα χρώματα `inner` και `bullseye` για τους υπόλοιπους κύκλους.

--- /task ---

--- save ---
