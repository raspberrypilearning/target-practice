## Schiet de pijl af

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Wanneer je klikt of tikt, zal er een pijl worden afgevuurd op de positie van een bewegende doelcirkel. 
</div>
<div>

![Het doelwit, met een bruine cirkelpijl die op verschillende posities verschijnt.](images/fire_arrow.gif){:width="300px"}

</div>
</div>

### Teken elk frame een doelcirkel

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;"> Computerspelletjes, video's en animaties creëren het effect van beweging door veel afbeeldingen achter elkaar te laten zien. Elke afbeelding wordt een <span style="color: #0faeb0; font-weight: bold;"> frame </span>genoemd.   
</p>

--- task ---

Definieer je `schiet_pijl()` functie onder de opmerking **# De schiet_pijl functie komt hier**.

Voeg code toe om een bruine cirkel binnen een doelgebied willekeurig te tekenen:

![Een rechthoek met de coördinaten van het doelgebied in een semi-transparante rechthoek. Het doelgebied ligt tussen x=100 en y=100 tot x=300 en y=300 dus beslaat het hele doel en breder.](images/target_area.png)

--- code ---
---
language: python filename: main.py — shoot_arrow() line_numbers: true line_number_start: 7
line_highlights: 8-12
---
# De schiet_pijl functie komt hier
def schiet_pijl():   
pijl_x = randint(100, 300) # Bewaar een willekeurig getal tussen 100 en 300    
pijl_y = randint(100, 300) # Bewaar een willekeurig getal tussen 100 en 300    
fill('sienna') # Stel vulkeur van de pijl in op bruin   
cicle(pijl_x, pijl_y, 15) # Teken een kleine cirkel op willekeurige coördinaten

--- /code ---

--- /task ---

--- task ---

Ga naar de functie `draw` en roep je nieuwe `schiet_pijl` functie aan.

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

**Test:** 🔄 Voer je code uit en zie de pijl in elk frame op een willekeurige positie verschijnen.

![Het doelwit op de achtergrond met een bruine cirkelpijl erop.](images/fire_arrow.gif)

De achtergrond en het doel worden over de oude pijl getekend. Dit betekent dat je maar één pijl tegelijk ziet.

--- /task ---

### Bij welke kleur raakt de pijl het doel

De functie `get()` retourneert de kleur van een pixel.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Een <span style="color: #0faeb0; font-weight: bold;">pixel</span>, een afkorting van picture element, is een enkele gekleurde stip in een afbeelding. Afbeeldingen zijn opgebouwd uit veel gekleurde pixels.
</p>

--- task ---

Voeg een **globale variabele** toe met de naam `raak_kleur` die in je hele code kan worden gebruikt.

Voeg code toe om de `raak_kleur` op te slaan. Gebruik de functie `get()` om de kleur van de pixel te vinden op de coördinaten `pijl_x` en `pijl_y` — het midden van de pijl. Om de kleuren te vergelijken, moeten we de hexadecimale code gebruiken. Dit kan gedaan worden met de string `.hex`.

--- code ---
---
language: python filename: main.py — shoot_arrow() line_numbers: true line_number_start: 7
line_highlights: 9, 12
---
# De schiet_pijl functie komt hier
def schiet_pijl(): global raak_kleur # Kan ook gebruikt worden in andere functies  
pijl_x = randint(100, 300) # Bewaar een willekeurig getal tussen 100 en 300    
pijl_y = randint(100, 300) # Bewaar een willekeurig getal tussen 100 en 300 raak_kleur = get(pijl_x, pijl_y) # Haal de geraakte kleur op     
fill('sienna') # Stel vulkeur van de pijl in op bruin   
circle(pijl_x, pijl_y, 15) # Teken een kleine cirkel op willekeurige coördinaten

--- /code ---

**Tip:** De `get`-code om de kleur op te halen en op te slaan moet **vóór** de code om de `cirkel` te tekenen staan, anders bewaar je altijd de (hout) kleur van de pijl!

--- /task ---

### Druk de kleur af wanneer de muis wordt ingedrukt

De `p5` bibliotheek 'luistert' naar bepaalde gebeurtenissen, één daarvan is het indrukken van de muisknop. Wanneer het detecteert dat de muis knop is ingedrukt, zal het de code uitvoeren die het is gegeven in de `mouse_pressed()` functie.

--- task ---

Definieer je `mouse_pressed()` functie onder de opmerking **# De mouse_pressed functie komt hier**.

Voeg code toe om de doel-emoji 🎯 af te drukken wanneer met de muis wordt geklikt.

--- code ---
---
language: python filename: main.py - mouse_pressed() line_numbers: true line_number_start: 5
line_highlights: 6
---

# De mouse_pressed functie komt hier
def mouse_pressed():    
print('🎯')

--- /code ---

--- /task ---

--- task ---

**Test:** 🔄 Voer je project uit.

Het project drukt 🎯 af telkens wanneer de pijl opnieuw wordt getekend.

![Een animatie van een doelwit met een bruine cirkelpijl die in verschillende posities verschijnt.](images/fire_arrow.gif)

**Debuggen:** Als je een bericht ziet dat `raak_kleur` 'niet gedefinieerd' is, ga dan terug naar `schiet_pijl()` functie en controleer of je de regel `global raak_kleur` hebt.

**Debuggen:** Controleer de `print` regel heel goed op komma's en haakjes.

--- /task ---

--- save ---
