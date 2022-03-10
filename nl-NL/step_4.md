## Schiet de pijl af

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Nu is het tijd om een pijl toe te voegen die willekeurig over het doelgebied beweegt.
</div>
<div>

![Het doelwit, met een bruine cirkelpijl die op verschillende posities verschijnt.](images/fire_arrow.gif){:width="300px"}

</div>
</div>

--- task ---

Zoek de opmerking **#De schiet_pijl functie komt hier** en daaronder voeg je code toe om je `schiet_pijl()`-functie te definiëren.

Voeg een kleine `ellips()` toe in het midden van het scherm om de pijl weer te geven.

--- code ---
---
language: python 
filename: main.py — shoot_arrow() 
line_numbers: true 
line_number_start: 10
line_highlights: 11-12
---

#De schiet_pijl functie komt hier
def schiet_pijl():   
  ellipse(200, 200, 15, 15)

--- /code ---

--- /task ---

--- task ---

Ga naar de `draw()` code die het doel maakt en voeg aan het einde code toe om de `fill()` tcode voor `hout` in te stellen, en roep dan je nieuwe `schiet_pijl()` functie aan.

--- code ---
---
language: python 
filename: main.py — draw() 
line_numbers: true 
line_number_start: 41
line_highlights: 44-45
---

  fill(roos)    
  ellipse(200, 200, 30, 30)

  fill(hout)   
  schiet_pijl()

--- /code ---

--- /task ---

--- task ---

**Test:** Voer je code uit en zie de pijl in de roos verschijnen.

![Het doelwit op de achtergrond met een bruine cirkelpijl erop.](images/arrow-middle.png)

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;"> Computerspelletjes, video's en animaties creëren het effect van beweging door veel afbeeldingen achter elkaar te laten zien. Elke afbeelding wordt een <span style="color: #0faeb0; font-weight: bold;"> frame </span>genoemd. De snelheid waarmee het beeld verandert, wordt de <span style="color: #800080;">frame rate</span> genoemd en wordt weergegeven in <span style="color: #800080;">fps</span> of frames per seconde.  
</p>

De `frame_rate(2)` regel in `setup()` stelt de frame snelheid in op 2 frames per seconde.

De `draw()` functie wordt in elk frame aangeroepen. Je gaat de pijl in een willekeurige positie weergeven, elke keer dat `draw()` wordt aangeroepen.

De achtergrond en het doel worden over de oude pijl getekend. Dit betekent dat je maar één pijl tegelijk ziet.

--- task ---

Zoek de `import`-statements, bovenaan je code, je gaat `randint` gebruiken uit de `random` bibliotheek.

--- code ---
---
language: python 
filename: main.py 
line_numbers: true
line_number_start: 3
---

#Bibliotheekcode importeren
from p5 import *    
from math import *    
from random import randint

--- /code ---

--- /task ---

--- task ---

Ga naar de functie `schiet_pijl()` en voeg twee nieuwe variabelen `pijl_x` en `pijl_y` toe om willekeurige getallen tussen `100` en `300` op te slaan.

Hierdoor zullen sommige schoten het doel missen, zonder dat ze helemaal naar de randen van je spel gaan.

Verander je `ellipse()` om de nieuwe variabelen te gebruiken om je pijl te positioneren.

![Een rechthoek met de coördinaten van het doelgebied in een semi-transparante rechthoek.](images/target_area.png)

--- code ---
---
language: python 
filename: main.py — shoot_arrow() 
line_numbers: true 
line_number_start: 10
line_highlights: 12-14
---

#De schiet_pijl functie komt hier
def schiet_pijl():    
  pijl_x = randint(100, 300)   
  pijl_y = randint(100, 300)    
  ellipse(pijl_x, pijl_y, 15, 15) #Update naar willekeurige coördinaten

--- /code ---

--- /task ---

### Bij welke kleur raakt de pijl het doel

De functie `get()` retourneert de kleur van een pixel.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Een <span style="color: #0faeb0; font-weight: bold;">pixel</span>, een afkorting van picture element, is een enkele gekleurde stip in een afbeelding. Afbeeldingen zijn opgebouwd uit veel gekleurde pixels.
</p>

--- task ---

Je moet de kleur waarop de pijl gericht is opslaan voordat je er een pijl op tekent.

Voeg code toe om de `raak_kleur` op te slaan. Gebruik de functie `get()` om de kleur van de pixel te vinden op de coördinaten `pijl_x` en `pijl_y` — het midden van de pijl.

--- code ---
---
language: python 
filename: main.py — shoot_arrow()
line_numbers: true 
line_number_start: 10
line_highlights: 14
---

#De schiet_pijl functie komt hier
def schiet_pijl():    
  pijl_x = randint(100, 300)    
  pijl_y = randint(100, 300)    
  raak_kleur = get(pijl_x, pijl_y) #Sla de kleur op voordat je de pijl tekent   
  ellipse(pijl_x, pijl_y, 15, 15)

--- /code ---

**Tip:** De code om de kleur op te halen en op te slaan moet **vóór** de code om de ellips te tekenen staan, anders bewaar je altijd de (hout) kleur van de pijl!

--- /task ---

De `p5` bibliotheek 'luistert' naar bepaalde gebeurtenissen, één daarvan is het indrukken van de muisknop. Wanneer het detecteert dat de muis knop is ingedrukt, zal het de code uitvoeren die het is gegeven in de `mouse_pressed()` functie.

--- task ---

Zoek het commentaar **#De mouse_pressed functie komt hier** en daaronder voeg je code toe om je `mouse_pressed()` functie te definiëren.

Voeg code toe om de hoeveelheden rood, groen en blauw af te drukken in de pixel waarop de pijl terechtkomt.

--- code ---
---
language: python 
filename: main.py - mouse_pressed() 
line_numbers: true 
line_number_start: 8
line_highlights: 9-10
---

#De mouse_pressed functie komt hier
def mouse_pressed():    
  print( red(raak_kleur), green(raak_kleur), blue(raak_kleur))

--- /code ---

--- /task ---

--- task ---

Je hebt twee functies gedefinieerd `schiet_pijl()` en `mouse_pressed()`, beide functies moeten de variabele `raak_kleur` gebruiken.

Een variabele die door het hele programma heen gebruikt moet worden, staat bekend als een **globale variabele**. Voeg code toe aan je `schiet_pijl()` functie om van `raak_kleur` een globale variabele te maken:

--- code ---
---
language: python 
filename: main.py - shoot_arrow() 
line_numbers: true 
line_number_start: 12
line_highlights: 14
---

#De schiet_pijl functie komt hier
def schiet_pijl():    
  global raak_kleur #Kan ook gebruikt worden in andere functies     
  pijl_x = randint(100, 300)     
  pijl_y = randint(100, 300)     
  raak_kleur = get(pijl_x, pijl_y) #Sla de kleur op voordat je de pijl tekent     
  ellipse(pijl_x, pijl_y, 15, 15)

--- /code ---

--- /task ---

--- task ---

**Test:** Voer je project uit. De pijl wordt opnieuw getekend op willekeurige coördinaten.

Het project haalt de `raak_kleur` op elke keer dat de pijl opnieuw wordt getekend en drukt de kleurwaarde af in het uitvoergebied onder het doel.

![Het doelwit, met een bruine cirkelpijl die in verschillende posities verschijnt.](images/fire_arrow.gif)

**Debuggen:** Als je een bericht ziet dat `raak_kleur` 'niet gedefinieerd' is, ga dan terug naar `schiet_pijl()` functie en controleer of je de regel `global raak_kleur` hebt.

**Debuggen:** Controleer de `print` regel heel goed op komma's en haakjes.

--- /task ---

--- save ---

