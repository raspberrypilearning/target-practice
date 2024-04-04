## Utwórz tło

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Twoja gra potrzebuje kolorowego tła.
</div>
<div>

![Obszar wyjściowy z prostokątem w kolorze nieba nad prostokątem w kolorze trawy, aby utworzyć tło.](images/background.png){:width="300px"}

</div>
</div>

### Otwórz projekt startowy

--- task ---

Otwórz projekt [ Praktyka docelowa ](https://editor.raspberrypi.org/en/projects/target-practice-starter){:target="_blank"}. Edytor kodu otworzy się w innej karcie przeglądarki.

Jeśli masz konto Raspberry Pi, możesz kliknąć przycisk ** Saved ** , aby zapisać kopię w swoich projektach ** **.

--- /task ---

### Edytuj niebo

--- task ---

Projekt startowy ma już napisany dla Ciebie kod.

Kliknij **'Run'** , aby zobaczyć wypełniony niebieski prostokąt narysowany z x=` 0 `, y=` 0 ` (u góry ekranu). Ten prostokąt pikseli ` 400 ` x ` 250 ` to niebo.

![Niebieski prostokąt z czarną obwódką wokół niego, nad szarym prostokątem. Lewy górny róg płótna jest oznaczony jako x=0, y=0 to jest początek prostokąta. Szerokość jest podświetlona jako 400, a wysokość jako 250. Wyświetlany jest kod rect(0, 0, 400, 250).](images/sky_stroke.png){:width="400px"}

** Wskazówka:** ? Współrzędne zaczynają się od (x=0, y=0) w lewym górnym rogu. Może się to różnić od innych używanych układów współrzędnych.

--- /task ---

--- task ---

Niebo zostało narysowane czarną obwódką (obrys).

Aby wyłączyć obrys dla wszystkich kształtów, dodaj ` no_stroke()` do funkcji ` setup `:

--- code ---
---
language: python filename: main.py — setup() line_numbers: true line_number_start: 9
line_highlights: 12
---
def setup():
# Tutaj skonfiguruj swoją grę

    size(400, 400)  # Width and height of screen
    no_stroke()

--- /code ---

--- /task ---

--- task ---

** uruchom ponownie ** swój kod i zwróć uwagę? że obramowanie (obrys) zniknęło.

** Wskazówka:** ? Aby zatrzymać program, musisz nacisnąć klawisz ** Stop **. Spowoduje to ponowne wyświetlenie przycisku ** ** .

--- /task ---

### Narysuj trawę

--- task ---

** Dodano kod **, aby narysować zielony prostokąt u dołu ekranu.

![Obszar wyjściowy z prostokątem w kolorze nieba nad prostokątem w kolorze trawy, aby utworzyć tło. Lewy górny róg prostokąta jest oznaczony jako x=0, y=250 to jest początek początku prostokąta. Szerokość jest podświetlona jako 400, a wysokość jako 150. Wyświetlany jest kod rect(0, 250, 400, 150).](images/green-grass.png){:width="400px"}

--- code ---
---
language: python filename: main.py — draw() line_numbers: true line_number_start: 14
line_highlights: 18-19
---
def draw():
# Rzeczy do zrobienia w każdej klatce

    fill('cyan')  # Set the fill colour for the sky to cyan
    rect(0, 0, 400, 250)  # Draw a rectangle for the sky with these values for x, y, width, height
    fill('lightgreen')  # Set the fill colour for the grass to light green
    rect(0, 250, 400, 150)  # Draw a rectangle for the grass with these values for x, y, width, height

--- /code ---

** Wskazówka:** ? Dodaliśmy komentarze do naszego kodu, takie jak `# Ustaw kolor wypełnienia nieba na `, aby powiedzieć, co robi. Nie musisz dodawać komentarzy do kodu, ale są one pomocne, aby przypomnieć, co robią linie kodu.

--- /task ---

--- task ---

Test **:** ? Uruchom swój projekt ponownie, aby wyświetlić ukończone tło.

![Obszar wyjściowy z prostokątem w kolorze nieba nad prostokątem w kolorze trawy, aby utworzyć tło.](images/background.png){:width="400px"}

--- /task ---

--- save ---
