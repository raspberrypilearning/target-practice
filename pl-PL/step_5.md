## Zdobądź punkty

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Twoja gra doda wyniki w zależności od tego, gdzie trafiła strzałka.
</div>
<div>

![animacja celu, ze strzałką pojawiającą się w różnych pozycjach, a wyniki wyświetlane jako tekst poniżej gry.](images/points-scored.gif){:width="300px"}

</div>
</div>

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Używamy <span style="color: #0faeb0; font-weight: bold;"> </span> cały czas do podejmowania decyzji. Moglibyśmy powiedzieć "jeśli ołówek jest tępy, to wyostrz go". Podobnie warunki „jeśli” pozwalają nam napisać kod, który robi coś innego w zależności od tego, czy warunek jest prawdziwy, czy fałszywy.
</p>

### Wyświetl wyniki

--- task ---

Usuń ❌ Linia kodu ` print('?')`.

--- code ---
---
język: python nazwa pliku: main.py line_numbers: true line_number_start: 5
line_highlights: 7
---
# Tutaj pojawi się funkcja Mouse_pressed
def mouse_pressed():


--- /code ---

--- /task ---

--- task ---

Wyświetl komunikat ** ** `_` jest równy kolorowi koła ` ` (niebieski) ?.

Uwaga ? że kod używa dwóch znaków równości `==`, aby oznaczać ** równe to **.

--- code ---
---
język: python nazwa pliku: main.py - mouse_pressed() line_numbers: true line_number_start: 5
line_highlights: 7, 8
---

# Tutaj pojawi się funkcja Mouse_pressed
def mouse_pressed():     
if hit_colour == Color('blue').hex:  # Like the code in functions, the code in 'if' statements is indented print('You hit the outer circle, 50 points!')

--- /code ---

** Wskazówka:** ? Jeśli zmieniłeś kolor zewnętrznego koła, będziesz musiał zastąpić `'blue'` wybraną nazwą koloru.

--- /task ---

--- task ---

Test **:** ? Uruchom swój projekt. Spróbuj wystrzelić strzałkę na niebieskim zewnętrznym kole, aby zobaczyć komunikat.

** Wskazówka:** ? ` frame_rate=2 `, w programie ` ` na dole kodu, kontroluje szybkość rysowania gry. Jeśli idzie zbyt szybko, ustaw go na niższą liczbę.

![Obszar wyjściowy ze strzałką dotykającą zewnętrznego okręgu. Komunikat Points jest wyświetlany w obszarze wyjściowym.](images/blue-points.png)

Debugowanie **:** ? Upewnij się, że użyłeś amerykańskiej pisowni „Color” (bez „u”) i że „Color” jest wielkie.

Debugowanie **:** ? Upewnij się, że kod jest dokładnie zgodny i wcięto kod wewnątrz instrukcji ` `.

Debugowanie **:** ? Upewnij się, że wprowadziłeś poprawną nazwę koloru użytą dla koła zewnętrznego ** **.

--- /task ---

za pomocą programu ` ` (else - if) można dodać więcej warunków do instrukcji ` `. Będą one odczytywane od góry do dołu. Jak tylko zostanie znaleziony warunek ** **, zostanie on zadziałał. Wszelkie pozostałe warunki zostaną zignorowane.

--- task ---

Zdobądź punkty, jeśli strzałka wyląduje na okręgach ` ` lub ` ` ?:

--- code ---
---
language: python filename: main.py - mouse_pressed() line_numbers: true line_number_start: 6
line_highlights: 9-12
---

def mouse_pressed(): if hit_colour == Color('blue').hex:   
print('You hit the outer circle, 50 points!') elif hit_colour == Color('red').hex: print('You hit the inner circle, 200 points!') elif hit_colour == Color('yellow').hex: print('You hit the middle, 500 points!')

--- /code ---

--- /task ---

--- task ---

Test **:** ? Uruchom swój projekt. Spróbuj wystrzelić strzałkę na wewnętrznym i środkowym kole, aby zobaczyć ich wiadomości.

![Obszar wyjściowy ze strzałką dotykającą wewnętrznego okręgu. Komunikat Points jest wyświetlany w obszarze wyjściowym.](images/yellow-points.png)

Debugowanie **:** ? Sprawdź, czy wcięcie pasuje do przykładu.

Debugowanie **:** ? Jeśli zobaczysz komunikat o tym, że ` hit_` jest 'niezdefiniowany', wróć do ` draw()` i sprawdź, czy linia deklaruje `_` jako zmienną globalną.

Debugowanie **:** ? Upewnij się, że wprowadziłeś poprawną nazwę koloru dla okręgów ** **.

Debugowanie **:** ? Upewnij się, że użyłeś ciągu `.` dla kolorów okręgu ** **.

--- /task ---

### Brak celu

Jest jeszcze jedna decyzja, którą musisz podjąć: Co się stanie, jeśli strzałka nie wyląduje na żadnym z kół docelowych? ❌

Aby wykonać to ostatnie sprawdzenie, użyj ` `.

--- task ---

Dodaj kod do ` wydrukuj ` Komunikat ` ` żadne z instrukcji ` ` i ` elilife ` nie zostały spełnione.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 6
line_highlights: 13-14
---

def mouse_pressed(): if hit_colour == Color('blue').hex:   
print('You hit the outer circle, 50 points!') elif hit_colour == Color('red').hex: print('You hit the inner circle, 200 points!') elif hit_colour == Color('yellow').hex: print('You hit the middle, 500 points!') else:   
print('You missed! No points!')

--- /code ---

--- /task ---

--- task ---

Test **:** ? Uruchom swój projekt. Wystrzel strzałkę na trawie lub niebie, aby zobaczyć komunikat o błędzie.

** Wybierz:** ? Zmień liczbę punktów zdobytych dla różnych kolorów.

--- /task ---

--- save ---
