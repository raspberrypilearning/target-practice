## Schiet de pijl af

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Voeg een nog kleinere cirkel toe die een pijlt voorstelt.
</div>
<div>

![Het doelwit, met een bruine cirkelpijl die op verschillende posities verschijnt.](images/fire_arrow.gif){:width="300px"}

</div>
</div>

### Waar ga je schieten?

--- task ---

Voeg een functie toe om een bruine cirkel te tekenen op de coördinaten `200`, `200`.

--- code ---
---
language: python line_numbers: true line_number_start: 8
line_highlights: 9-13
---
# De schiet_pijl functie komt hier
def shoot_arrow():   
arrow_x = 200 arrow_y = 200 fill('brown') circle(arrow_x, arrow_y, 15)

--- /code ---

--- /task ---

--- task ---

Roep je nieuwe `schiet_pijl()`{:.language-python} functie aan het einde van jouw `draw()`{:.language-python} functie aan.

--- code ---
---
language: python line_numbers: true line_number_start: 33
line_highlights: 35
---

    fill('yellow')      
    circle(200, 200, 30)  
    shoot_arrow()

--- /code ---

--- /task ---

--- task ---

**Test:** Klik op de knop **Run**. Je zou de pijl in het midden moeten zien.

![een bruine pijlcirkel in het midden van het doel](images/arrow-centre.png)


--- /task ---

De pijl moet willekeurig bewegen.


--- task ---

Wijzig de `pijl_x`{:.language-python} en `pijl_y`{:.language-python} variabelen om een willekeurig getal tussen 100 en 300 te kiezen.

--- code ---
---
language: python line_numbers: true line_number_start: 9
line_highlights: 10-11
---
def shoot_arrow(): arrow_x = randint(100, 300) arrow_y = randint(100, 300) fill('brown') circle(arrow_x, arrow_y, 15)

--- /code ---

--- /task ---


--- task ---


**Test:** Klik op de knop **Run**. Je zou de pijl rond het doel moeten zien springen.

![Een animatie van een doelwit met een bruine cirkelpijl die in verschillende posities verschijnt.](images/fire_arrow.gif)

--- /task ---

--- save ---
