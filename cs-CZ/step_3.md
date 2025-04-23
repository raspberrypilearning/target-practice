## Nakresli terč

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Vaše hra potřebuje cíl, na který budete střílet šípy.
</div>
<div>

![Výstupní oblast s cílem a stojanem.](images/three-circles.png){:width="300px"}

</div>
</div>

### Nakresli trojúhelníkový stojan

--- task ---

Nastav barvu výplně na `brown`.

Nakresli trojúhelník pomocí souřadnic x a y pro každý z rohů.

![Hnědý trojúhelník na trávě a proti obloze se souřadnicovými body označenými jako 150, 350 a 200, 150 a 250, 350). Rohy plátna jsou také označeny jako x=0, y=0 vlevo nahoře a x=400, y=400 vpravo dole.](images/stand_coords.png){:width="400px"}

--- code ---
---
language: python
line_numbers: true
line_number_start: 21
line_highlights: 23-24
---
    fill('lightgreen')  
    rect(0, 250, 400, 150)  
    fill('brown') 
    triangle(150, 350, 200, 150, 250, 350)  

--- /code ---

--- /task ---

--- task ---

**Test:** Spusťte svůj kód, abyste viděli stojan pro svůj cíl:

![Hnědý trojúhelník na trávě a proti obloze.](images/target-stand.png){:width="400px"}

--- /task ---

### Nakresli kruhy terče

--- task ---

Největší část terče je modrý **kruh**.

Nastav barvu výplně na `blue`.

Nakresli kružnici se souřadnicemi x a y pro její střed a šířku.

![Hnědý trojúhelník a modrý kruh na trávě a proti obloze. Kruh je označen souřadnicemi x=200, y=200 jako střed a šířka kruhu 170.](images/circle-coords.png){:width="400px"}

--- code ---
---
language: python
line_numbers: true
line_number_start: 23
line_highlights: 25-26
---
    fill('brown')  
    triangle(150, 350, 200, 150, 250, 350)  
    fill('blue')  
    circle(200, 200, 170)  
  
--- /code ---

--- /task ---

--- task ---

**Test:** Spusťte svůj kód a uvidíte první velký modrý kruh.

Modrý kruh byl nakreslen až když, byl nakreslen stojan, takže je vpředu.

![Hnědý trojúhelník a modrý kruh na trávě a proti obloze.](images/blue-circle.png){:width="400px"}

--- /task ---

Terč je vyroben z různě velkých kruhů se stejnými středovými souřadnicemi (200, 200).

--- task ---

**Přidejte** barevné kruhy pro vnitřní a střední části terče.

--- code ---
---
language: python
line_numbers: true
line_number_start: 25
line_highlights: 27-30
---

    fill('blue')  
    circle(200, 200, 170)  
    fill('red')  
    circle(200, 200, 110)  # Nakreslete vnitřní kruh
    fill('yellow')       
    circle(200, 200, 30)  # Nakreslete střední kruh

--- /code ---

--- /task ---

--- task ---

**Test:** Spusťte svůj projekt, abyste viděli cíl se třemi barevnými kruhy.

![Hnědý trojúhelník se třemi barevnými kruhy na trávě a proti obloze.](images/three-circles.png){:width="400px"}

--- /task ---

--- save ---
