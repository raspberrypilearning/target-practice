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

Ustaw kolor wypełnienia na ` ` (brązowy).

Narysuj trójkąt używając współrzędnych x i y dla każdego z rogów.

![Brązowy trójkąt na trawie i na niebie z punktami współrzędnych oznaczonymi jako 150, 350 i 200, 150 i 250, 350). Narożniki płótna są również oznaczone jako x=0, y=0 w lewym górnym rogu i x=400, y=400 w prawym dolnym rogu.](images/stand_coords.png){:width="400px"}

--- code ---
---
język: python nazwa pliku: main.py - draw() line_numbers: true line_number_start: 18
line_highlights: 20, 21
---

    fill('lightgreen')  # Set the fill colour for the grass to light green
    rect(0, 250, 400, 150)  # Draw a rectangle for the grass with these values for x, y, width, height
    fill('sienna')  # Brown colour
    triangle(150, 350, 200, 150, 250, 350)  # Draw a triangle for the target's stand

--- /code ---

--- /task ---

--- task ---

Test **:** ? Uruchom swój kod, aby zobaczyć stojak dla swojego celu:

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
language: python filename: main.py - draw() line_numbers: true line_number_start: 20
line_highlights: 22, 23
---

    fill('sienna')  # Brown colour
    triangle(150, 350, 200, 150, 250, 350)  # Draw a triangle for the target's stand 
    fill('blue')  # Set the circle fill colour to blue
    circle(200, 200, 170)  # Draw the outer circle

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
language: python filename: main.py - draw() line_numbers: true line_number_start: 20
line_highlights: 24, 25, 26, 27
---

    fill('sienna')  # Brown colour
    triangle(150, 350, 200, 150, 250, 350)  # Draw a triangle for the target's stand 
    fill('blue')  # Set the circle fill colour to blue
    circle(200, 200, 170)  # Draw the outer circle
    fill('red')  # Set the colour for the circle fill to red
    circle(200, 200, 110)  # Draw the inner circle using x, y, width
    fill('yellow')  # Set the colour for the circle fill to yellow      
    circle(200, 200, 30)  # Draw the middle circle using x, y, width

--- /code ---

--- /task ---

--- task ---

Test **:** ? Uruchom swój projekt, aby zobaczyć cel z trzema kolorowymi kółkami.

![Brązowy trójkąt z trzema kolorowymi kółkami na trawie i na tle nieba.](images/three-circles.png){:width="400px"}

--- /task ---

--- task ---

** Wybierz:** ? Zmień dowolny kolor używając innej nazwy koloru. Możesz znaleźć listę wszystkich nazw kolorów dostępnych w [ W3 ](https://www.w3schools.com/colors/colors_names.asp){:target="blank"}.

![Brązowy trójkąt z trzema kolorowymi kółkami na trawie i na tle nieba. Kolory zmieniły się na różowe i fioletowe.](images/alternative-colours.png){:width="400px"}

--- collapse ---
---
Title: Przykładowy kod używający różnych kolorów
---

--- code ---
---
language: python filename: main.py - draw() line_numbers: false line_number_start: 14
line_highlights:
---

def draw():
# Rzeczy do zrobienia w każdej klatce

    fill('BlueViolet')
    rect(0, 0, 400, 250)  # Sky
    fill('DeepSkyBlue')
    rect(0, 250, 400, 150)  # Ground
    fill('FireBrick')
    triangle(150, 350, 200, 150, 250, 350)  # Stand
    fill('LemonChiffon')
    circle(200, 200, 170)  # Outer circle
    fill('DeepPink')
    circle(200, 200, 110)  # Inner circle
    fill('BlueViolet')
    circle(200, 200, 30)  # Middle circle

--- /code ---

--- /collapse ---

--- /task ---

--- save ---
