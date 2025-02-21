## Narysuj swój cel

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Twoja gra potrzebuje celu do strzelania strzałkami.
</div>
<div>

![Obszar wyjściowy z obiektem docelowym i stojakiem.](images/three-cirles.png){:width="300px"}

</div>
</div>

### Narysuj stojak trójkątny

--- task ---

Set the fill colour to `brown`.

Narysuj trójkąt używając współrzędnych x i y dla każdego z rogów.

![Brązowy trójkąt na trawie i na niebie z punktami współrzędnych oznaczonymi jako 150, 350 i 200, 150 i 250, 350). Narożniki płótna są również oznaczone jako x=0, y=0 w lewym górnym rogu i x=400, y=400 w prawym dolnym rogu.](images/stand_coords.png){:width="400px"}

--- code ---
---
language: python line_numbers: true line_number_start: 21
line_highlights: 23-24
---

    fill('lightgreen')  
    rect(0, 250, 400, 150)  
    fill('brown') 
    triangle(150, 350, 200, 150, 250, 350)

--- /code ---

--- /task ---

--- task ---

**Test:** Run your code to see the stand for your target:

![Brązowy trójkąt na trawie i na tle nieba.](images/target-stand.png){:width="400px"}

--- /task ---

### Narysuj docelowe okręgi

--- task ---

Największa część celu to niebieski okrąg ** **.

Ustaw kolor wypełnienia na ` `.

Narysuj okrąg ze współrzędnymi x i y dla jego środka i szerokości.

![Brązowy trójkąt i niebieskie kółko na trawie i na niebie. Okrąg jest oznaczony współrzędnymi x=200, y=200 jako środek i szerokość okręgu 170.](images/circle-coords.png){:width="400px"}

--- code ---
---
language: python line_numbers: true line_number_start: 23
line_highlights: 25-26
---

    fill('brown')  
    triangle(150, 350, 200, 150, 250, 350)  
    fill('blue')  
    circle(200, 200, 170)

--- /code ---

--- /task ---

--- task ---

** Test:** Uruchom swój kod, aby zobaczyć pierwsze duże niebieskie kółko.

Niebieskie kółko zostało narysowane za stojakiem, więc jest z przodu.

![Brązowy trójkąt i niebieskie kółko na trawie i na niebie.](images/blue-circle.png){:width="400px"}

--- /task ---

Cel składa się z okręgów o różnych rozmiarach o tych samych współrzędnych środka (200, 200).

--- task ---

** ** kolorowe kółka dla wewnętrznej i środkowej części celu.

--- code ---
---
language: python line_numbers: true line_number_start: 25
line_highlights: 27-30
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

![Brązowy trójkąt z trzema kolorowymi kółkami na trawie i na tle nieba.](images/three-circles.png){:width="400px"}

--- /task ---

--- save ---
