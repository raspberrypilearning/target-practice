## Wystrzel strzałkę

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Kiedy klikniesz lub stukniesz, strzałka wystrzeli w pozycję ruchomego koła docelowego. 
</div>
<div>

![Target, z brązową strzałką koła pojawiającą się w różnych pozycjach.](images/fire_arrow.gif){:width="300px"}

</div>
</div>

### Narysuj koło docelowe każdej klatce

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;"> Komputery tworzą efekt ruchu, wyświetlając wiele obrazów jeden po drugim. Każdy obraz jest nazywany <span style="color: #0faeb0; font-weight: bold;"> Frame </span>.   
</p>

--- task ---

Zdefiniuj swoją funkcję ` shoot_arrow()` pod komentarzem **# Funkcja shoot_arrow idzie tutaj **.

Dodaj kod, aby losowo narysować brązowe kółko w obszarze docelowym:

![Prostokąt pokazujący współrzędne obszaru docelowego w półprzezroczystym prostokącie. Obszar docelowy znajduje się między x=100 i y=100 do x=300 i y=300, więc obejmuje cały cel i szerszy.](images/target_area.png)

--- code ---
---
language: python filename: main.py — shoot_arrow() line_numbers: true line_number_start: 7
line_highlights: 8-12
---
# Pojawi się tutaj funkcja shoot_arrow
def shoot_arrow():   
arrow_x = randint(100, 300)  # Store a random number between 100 and 300    
arrow_y = randint(100, 300)  # Store a random number between 100 and 300    
fill('sienna')  # Set the arrow to fill colour to brown   
circle(arrow_x, arrow_y, 15)  # Draw a small circle at random coordinates

--- /code ---

--- /task ---

--- task ---

Przejdź do funkcji ` draw ` i wywołaj nową funkcję ` shoot_` .

--- code ---
---
language: python filename: main.py — draw() line_numbers: true line_number_start: 31
line_highlights: 33
---

    fill('yellow')  # Set the colour for the circle fill to yellow      
    circle(200, 200, 30)  # Draw the middle circle using x, y, width
    shoot_arrow()

--- /code ---

--- /task ---

--- task ---

Test **:** ? Uruchom swój kod i zobacz, jak strzałka pojawia się w losowej pozycji każdej klatki.

![Animacja celu z brązową strzałką koła pojawiającą się w różnych pozycjach.](images/fire_arrow.gif)

Tło i cel zostaną narysowane nad starą strzałką. Oznacza to, że widzisz tylko jedną strzałkę na raz.

--- /task ---

### Zdobądź kolor trafiony strzałką

Funkcja ` get()` zwraca kolor piksela.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
<span style="color: #0faeb0; font-weight: bold;"> </span>, skrót od elementu obrazu, to pojedyncza kolorowa kropka na obrazie. Obrazy składają się z wielu kolorowych pikseli.
</p>

--- task ---

Dodaj zmienną globalną ** ** o nazwie ` hit_`, która może być używana w całym kodzie.

Dodaj kod do ` ` kolor piksela na środku strzałki i zapisz go w zmiennej ` hit_`. Aby porównać kolory, musimy użyć kodu szesnastkowego. Można to zrobić za pomocą ciągu `.`.

--- code ---
---
language: python filename: main.py — shoot_arrow() line_numbers: true line_number_start: 7
line_highlights: 9, 12
---
# Pojawi się tutaj funkcja shoot_arrow
def shoot_arrow(): global hit_colour  # Can be used in other functions  
arrow_x = randint(100, 300)  # Store a random number between 100 and 300    
arrow_y = randint(100, 300)  # Store a random number between 100 and 300 hit_colour = get(arrow_x, arrow_y).hex  # Get the hit colour     
fill('sienna')  # Set the arrow to fill colour to brown   
circle(arrow_x, arrow_y, 15)  # Draw a small circle at random coordinates

--- /code ---

** Wskazówka:** ? Kod do ` ` Kolor musi być ** ** kod do narysowania koła ` ` w przeciwnym razie zawsze zapiszesz kolor drewna strzałki!

--- /task ---

### Wydrukuj kolor po naciśnięciu myszy

Biblioteka ` ` „słucha” niektórych zdarzeń, jednym z nich jest naciśnięcie przycisku myszy. Kiedy wykryje, że przycisk został naciśnięty, uruchomi dowolny kod, który został podany w funkcji ` mouse_`.

--- task ---

Zdefiniuj swoją funkcję ` mouse_pressed()` pod komentarzem **# Funkcja mouse_pressed pojawia się tutaj **.

Dodaj kod, aby wydrukować docelowe emoji? kiedy kliknięto mysz.

--- code ---
---
language: python filename: main.py - mouse_pressed() line_numbers: true line_number_start: 5
line_highlights: 6
---

# Tutaj pojawi się funkcja Mouse_pressed
def mouse_pressed():    
print('🎯')

--- /code ---

--- /task ---

--- task ---

Test **:** ? Uruchom swój projekt.

Projekt zostanie wydrukowany? za każdym razem, gdy strzałka jest rysowana ponownie.

![Animacja celu z brązową strzałką koła pojawiającą się w różnych pozycjach.](images/fire_arrow.gif)

Debugowanie **:** ? Jeśli widzisz komunikat o tym, że ` hit_` jest „niezdefiniowany”, wróć do ` shoot_arrow()` i sprawdź, czy uwzględniłeś linię ` Global hit_`.

Debugowanie **:** ? Sprawdź, czy linia ` ` nie zawiera przecinków i nawiasów.

--- /task ---

--- save ---
