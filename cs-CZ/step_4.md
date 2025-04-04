## Přidejte šíp

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Přidejte ještě menší kruh, který bude představovat šíp.
</div>
<div>

![Cíl s hnědou kruhovou šipkou objevující se v různých pozicích.](images/fire_arrow.gif){:width="300px"}

</div>
</div>

### Kam budeš střílet?

--- task ---

Přidej funkci pro nakreslení hnědého kruhu na souřadnicích `200`, `200`.

--- code ---
---
language: python line_numbers: true line_number_start: 8
line_highlights: 9-13
---
# The shoot_arrow function goes here
def shoot_arrow():   
arrow_x = 200 arrow_y = 200 fill('brown') circle(arrow_x, arrow_y, 15)

--- /code ---

--- /task ---

--- task ---

Na konci funkce `draw()`{:.language-python} zavolejte svou novou funkci `shoot_arrow()`{:.language-python}.

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

**Test:** Click the **Run** button. Měli byste vidět šíp uprostřed.


**Test:** Klikněte na tlačítko **Spustit**. Měli byste vidět šíp uprostřed.

![kruh s hnědou šipkou ve středu terče](images/arrow-centre.png)


--- /task ---

Šíp se musí pohybovat náhodně.


--- task ---

Změňte proměnné `arrow_x`{:.language-python} a `arrow_y`{:.language-python} a vyberte náhodné číslo mezi 100 a 300.

--- code ---
---
language: python line_numbers: true line_number_start: 9
line_highlights: 10-11
---
def shoot_arrow(): arrow_x = randint(100, 300) arrow_y = randint(100, 300) fill('brown') circle(arrow_x, arrow_y, 15)

--- /code ---

--- /task ---


--- task ---


**Test:** Klikněte na tlačítko **Spustit**. Měl bys vidět, jak šíp přeskakuje kolem cíle.

![Animace cíle s hnědou kruhovou šipkou objevující se v různých pozicích.](images/fire_arrow.gif)

--- /task ---

--- save ---
