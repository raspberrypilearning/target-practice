## Punten scoren

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
In deze stap voeg je scores toe afhankelijk van waar de pijl raakt.
</div>
<div>

![Het doel, met de pijl die op verschillende posities verschijnt, en scores die als tekst onder het spel verschijnen.](images/points-scored.gif){:width="300px"}

</div>
</div>

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
We gebruiken steeds <span style="color: #0faeb0; font-weight: bold;"> voorwaarden</span> om beslissingen te nemen. We zouden kunnen zeggen 'als het potlood bot is, slijp het dan'. Net zo laten `if`-voorwaarden ons code schrijven die iets anders doet, afhankelijk van of een voorwaarde waar of onwaar is.
</p>

### Geef de scores weer

--- task ---

Verwijder ❌ de coderegel `print('🎯')`.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 5
line_highlights: 7
---
# De mouse_pressed functie komt hier
def mouse_pressed():


--- /code ---

--- /task ---

--- task ---

Geef een bericht weer **als** de `raak_kleur` gelijk is aan de `buitenste` cirkelkleur (blauw) 🎯.

Merk op 👀 dat de code twee gelijktekens `==` gebruikt om **gelijk aan** aan te duiden.

--- code ---
---
language: python
filename: main.py - mouse_pressed()
line_numbers: true
line_number_start: 5
line_highlights: 7, 8  
---

# De muis_ingedrukt functie komt hier
def mouse_pressed():     
    if raak_kleur == Color('blue').hex: # Net als bij functies worden 'if'-instructies ingesprongen
        print('Je hebt de buitenste cirkel geraakt, 50 punten!')

--- /code ---

**Tip:** 💡 Als je de kleur van je buitenste cirkel hebt gewijzigd, moet je `'blue'` vervangen door de kleurnaam die je hebt gekozen.

--- /task ---

--- task ---

**Test:** 🔄 Voer je project uit. Probeer de pijl op de blauwe buitenste cirkel af te vuren om het bericht te zien.

**Tip:** 💡 `frame_rate=2`, in `run` onderaan je code uit, bepaalt hoe snel je spel tekent. Als het te snel gaat, stel het dan in op een lager getal.

![Het uitvoergebied met de pijl die de buitenste cirkel raakt. De punten worden getoond in het uitvoergebied.](images/blue-points.png)

**Debug:** 🐞 Controleer of je de Amerikaanse spelling van 'Color' hebt gebruikt (zonder 'u') en of 'Color' met een hoofdletter is geschreven.

**Debug:** 🐞 Zorg ervoor dat je code exact overeenkomt en dat je de code hebt ingesprongen in je `if`-instructie.

**Debug:** 🐞 Zorg ervoor dat je de juiste kleurnaam hebt ingevoerd die je hebt gebruikt voor je **buitenste** cirkel.

--- /task ---

`elif` (else - if) kan worden gebruikt om meer voorwaarden toe te voegen aan je `if`-instructie. Deze worden van boven naar beneden gelezen. Zodra een **True** voorwaarde wordt gevonden, wordt hierop actie ondernomen. Eventuele resterende voorwaarden worden genegeerd.

--- task ---

Scoor punten als de pijl op de `binnenste` of `middelste` cirkels terechtkomt 🎯:

--- code ---
---
language: python
filename: main.py - mouse_pressed()
line_numbers: true
line_number_start: 6
line_highlights: 9-12
---

def mouse_pressed():
    if hit_kleur == Color('blue').hex:   
        print('Je raakt de buitenste cirkel, 50 punten!')
    elif hit_kleur == Color('red').hex:
        print('Je hebt de binnenste cirkel geraakt, 200 punten!')
    elif hit_kleur == Color('yellow').hex:
        print('Je raakt het midden, 500 punten!')

--- /code ---

--- /task ---

--- task ---

**Test:** 🔄 Voer je project uit. Probeer de pijl op de binnenste en middelste cirkels te schieten om hun berichten te zien.

![Het uitvoergebied met de pijl die de binnenste cirkel raakt. De punten worden getoond in het uitvoergebied.](images/yellow-points.png)

**Debug:** 🐞 Controleer of je inspringing overeenkomt met het voorbeeld.

**Debuggen:** 🐞 Als je een bericht ziet over `raak_kleur` die 'niet gedefinieerd' is, ga dan terug naar `draw()` en controleer de regel waarin `raak_kleur` als globale variabele gedeclareerd is.

**Debuggen:** 🐞 Zorg ervoor dat je de juiste kleurnaam hebt ingevoerd voor **jouw** cirkels.

**Debug:** 🐞 Zorg ervoor dat je de `.hex` string hebt gebruikt voor **jouw** cirkelkleuren.

--- /task ---

### Het doel missen

Er is nog een beslissing die je moet nemen: wat gebeurt er als de pijl niet op een van de doelcirkels landt? ❌

Om deze laatste controle uit te voeren, gebruik je `else`.

--- task ---

Voeg code toe om een bericht `te tonen` `als` aan geen van de `if` en `elif` voorwaarden is voldaan.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 6
line_highlights: 13-14
---

def mouse_pressed():
    if hit_kleur == Color('blue').hex:   
        print('Je raakt de buitenste cirkel, 50 punten!')
    elif hit_kleur == Color('red').hex:
        print('Je hebt de binnenste cirkel geraakt, 200 punten!')
    elif hit_kleur == Color('yellow').hex:
        print('Je raakt het midden, 500 punten!')
    else:   
        print('You missed! Geen punten!')

--- /code ---

--- /task ---

--- task ---

**Test:** 🔄 Voer je project uit. Probeer de pijl in het gras of de lucht te laten landen om het bericht 'Gemist' te zien.

**Kies:** 💭 Verander het aantal punten dat voor de verschillende kleuren wordt gescoord.

--- /task ---

--- save ---
