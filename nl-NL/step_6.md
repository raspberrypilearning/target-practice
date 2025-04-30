## Punten scoren

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Afhankelijk van waar de pijl terechtkomt, wordt er een score toegekend.
</div>
<div>

![Een animatie van het doel, waarbij de pijl in verschillende posities verschijnt en de scores als tekst onder het spel verschijnen.](images/points-scored.gif){:width="300px"}

</div>
</div>

--- task ---

Maak een comment van de regel die het teken 🎯 print, zodat deze niet meer wordt uitgevoerd.

--- code ---
---
language: python
line_numbers: true
line_number_start: 6
line_highlights: 7
---
def mouse_pressed():
    # print('🎯')

--- /code ---

--- /task ---

--- task ---

Geef een bericht weer **als** de `raak_kleur`{:.language-python} gelijk is aan de `buitenste` cirkelkleur (blauw).

--- code ---
---
language: python
line_numbers: true
line_number_start: 6
line_highlights: 8-9
---
def mouse_pressed():    
    # print('🎯')
    if raak_kleur == Color('blue').hex:
        print('Je raakt de buitenste cirkel, 50 punten!')

--- /code ---

**Tip:** Als je de kleur van je buitenste cirkel hebt gewijzigd, moet je `'blue'` vervangen door de kleurnaam die je hebt gekozen.

--- /task ---

--- task ---

**Test:** Klik op de knop **Run**. Wacht tot de pijl in de blauwe cirkel terechtkomt en klik vervolgens op de linkermuisknop.
![punten gescoord toen op de blauwe cirkel werd geklikt](images/blue_circle_points.gif)

--- /task ---

`elif`{:.language-python} kan worden gebruikt om meer voorwaarden toe te voegen aan je `if`{:.language-python} statement.

--- task ---

Voeg wat meer code toe om punten te scoren als de pijl op de **binnenste** of **middelste** cirkel terechtkomt.

--- code ---
---
language: python
line_numbers: true
line_number_start: 6
line_highlights: 10-14
---

def mouse_pressed():
    # print('🎯')
    if raak_kleur == Color('blue').hex:
        print('Je raakt de buitenste cirkel, 50 punten!')
    elif raak_kleur == Color('red').hex:
        print('Je hebt de binnenste cirkel geraakt, 200 punten!')
    elif raak_kleur == Color('yellow').hex:
        print('Je raakt het midden, 500 punten!')

--- /code ---

--- /task ---

--- task ---

**Test:** Klik op de knop **Run**. Je zou punten moeten scoren wanneer je het doel raakt.

![punten die op een willekeurig gebied van het doel worden gescoord](images/yellow-points.png)

--- /task ---

### Het doel missen

Er is nog een beslissing die je moet nemen: wat gebeurt er als de pijl niet op een van de doelcirkels landt?

Om deze laatste controle uit te voeren, gebruikt je `else`{:.language-python}.

--- task ---

Voeg code toe aan het `print` commando om een bericht weer te geven wanneer geen van de `if` en `elif` statements waar zijn.

--- code ---
---
language: python
line_numbers: true
line_number_start: 12
line_highlights: 14-15
---

    elif raak_kleur == Color('yellow').hex:
        print('Je raakt het midden, 500 punten!')
    else:   
        print('Je hebt gemist! Geen punten!')

--- /code ---

--- /task ---

--- task ---

**Test:** Klik op de knop **Run**. Probeer de pijl in het gras of de lucht te laten landen om het gemist bericht te zien.

![geen punten weergegeven wanneer buiten het doelgebied](images/missed_no_points.gif)

--- /task ---

--- save ---
