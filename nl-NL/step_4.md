## Schiet de pijl af

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Add an even smaller circle to represent an arrow.
</div>
<div>

![Het doelwit, met een bruine cirkelpijl die op verschillende posities verschijnt.](images/fire_arrow.gif){:width="300px"}

</div>
</div>

### Where will you shoot?

--- task ---

Voeg code toe om een bruine cirkel binnen een doelgebied willekeurig te tekenen:

--- code ---
---
language: python filename: main.py — shoot_arrow() line_numbers: true line_number_start: 7
line_highlights: 8-12
---
# De schiet_pijl functie komt hier
def schiet_pijl(): global raak_kleur # Kan ook gebruikt worden in andere functies  
pijl_x = randint(100, 300) # Bewaar een willekeurig getal tussen 100 en 300    
pijl_y = randint(100, 300) # Bewaar een willekeurig getal tussen 100 en 300 raak_kleur = get(pijl_x, pijl_y).hex # Haal de geraakte kleur op     
fill('sienna') # Stel vulkeur van de pijl in op bruin   
circle(pijl_x, pijl_y, 15) # Teken een kleine cirkel op willekeurige coördinaten

--- /code ---

--- /task ---

--- task ---

Ga naar de functie `draw` en roep je nieuwe `schiet_pijl` functie aan.

--- code ---
---
language: python filename: main.py — draw() line_numbers: true line_number_start: 31
line_highlights: 33
---

    fill('yellow')  # Stel de kleur voor de cirkel in op geel      
    circle(200, 200, 30)  # Teken de middelste cirkel met x, y, breedte
    schiet_pijl()

--- /code ---

--- /task ---

--- task --- **Test:** Click the **Run** button. You should see the arrow in the centre.

![a brown arrow circle in the centre of the target](images/arrow-centre.png) --- /task ---

The arrow needs to move randomly.

--- task --- Change the `arrow_x`{:.language-python} and `arrow_y`{:.language-python} variables to choose a random number between 100 and 300.

--- code ---
---
language: python filename: main.py - mouse_pressed() line_numbers: true line_number_start: 5
line_highlights: 9, 12
---
def schiet_pijl():   
pijl_x = randint(100, 300) # Bewaar een willekeurig getal tussen 100 en 300    
pijl_y = randint(100, 300) # Bewaar een willekeurig getal tussen 100 en 300    
fill('sienna') # Stel vulkeur van de pijl in op bruin   
circle(pijl_x, pijl_y, 15) # Teken een kleine cirkel op willekeurige coördinaten

--- /code ---

--- /task ---


--- task ---


**Test:** 🔄 Voer je project uit. You should see the arrow jump around the target.

![Het doelwit op de achtergrond met een bruine cirkelpijl erop.](images/fire_arrow.gif)

--- /task ---

--- save ---
