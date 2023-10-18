## Schiet de pijl af

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
When you click or tap, an arrow will fire at the position of a moving target circle. 
</div>
<div>

![Het doelwit, met een bruine cirkelpijl die op verschillende posities verschijnt.](images/fire_arrow.gif){:width="300px"}

</div>
</div>

### Draw a target circle every frame

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;"> Computerspelletjes, video's en animaties creëren het effect van beweging door veel afbeeldingen achter elkaar te laten zien. Elke afbeelding wordt een <span style="color: #0faeb0; font-weight: bold;"> frame </span>genoemd.   
</p>

--- task ---

Zoek de opmerking **#De schiet_pijl functie komt hier** en daaronder voeg je code toe om je `schiet_pijl()`-functie te definiëren.

Add code to randomly draw a brown circle within a target area:

![Een rechthoek met de coördinaten van het doelgebied in een semi-transparante rechthoek. The target area is between x=100 and y=100 to x=300 and y=300 so covers the whole target and wider.](images/target_area.png)

--- code ---
---
language: python filename: main.py — schiet_pijl() line_numbers: true line_number_start: 10
line_highlights: 11-12
---
# De schiet_pijl functie komt hier
def schiet_pijl():    
pijl_x = randint(100, 300)    
pijl_y = randint(100, 300)    
raak_kleur = get(pijl_x, pijl_y) #Sla de kleur op voordat je de pijl tekent   
ellipse(pijl_x, pijl_y, 15, 15)

--- /code ---

--- /task ---

--- task ---

Ga naar de `draw()` code die het doel maakt en voeg aan het einde code toe om de `fill()` tcode voor `hout` in te stellen, en roep dan je nieuwe `schiet_pijl()` functie aan.

--- code ---
---
language: python filename: main.py — draw() line_numbers: true line_number_start: 41
line_highlights: 44-45
---

    fill('yellow')  # Set the colour for the circle fill to yellow      
    circle(200, 200, 30)  # Draw the middle circle using x, y, width
    shoot_arrow()

--- /code ---

--- /task ---

--- task ---

**Test:** Voer je code uit en zie de pijl in de roos verschijnen.

![Het doelwit op de achtergrond met een bruine cirkelpijl erop.](images/fire_arrow.gif)

De achtergrond en het doel worden over de oude pijl getekend. Dit betekent dat je maar één pijl tegelijk ziet.

--- /task ---

### Bij welke kleur raakt de pijl het doel

De functie `get()` retourneert de kleur van een pixel.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Een <span style="color: #0faeb0; font-weight: bold;">pixel</span>, een afkorting van picture element, is een enkele gekleurde stip in een afbeelding. Afbeeldingen zijn opgebouwd uit veel gekleurde pixels.
</p>

--- task ---

Je hebt twee functies gedefinieerd `schiet_pijl()` en `mouse_pressed()`, beide functies moeten de variabele `raak_kleur` gebruiken.

Voeg code toe om de `raak_kleur` op te slaan. Gebruik de functie `get()` om de kleur van de pixel te vinden op de coördinaten `pijl_x` en `pijl_y` — het midden van de pijl. In order to compare the colours, we need to use the hexadecimal code. This can be done with the `.hex` string.

--- code ---
---
language: python filename: main.py line_numbers: true
line_highlights: 9-10
---
# De schiet_pijl functie komt hier
def schiet_pijl():    
global raak_kleur #Kan ook gebruikt worden in andere functies     
pijl_x = randint(100, 300)     
pijl_y = randint(100, 300)     
raak_kleur = get(pijl_x, pijl_y) #Sla de kleur op voordat je de pijl tekent     
ellipse(pijl_x, pijl_y, 15, 15)

--- /code ---

**Tip:** De code om de kleur op te halen en op te slaan moet **vóór** de code om de ellips te tekenen staan, anders bewaar je altijd de (hout) kleur van de pijl!

--- /task ---

### Print the colour when the mouse is pressed

De `p5` bibliotheek 'luistert' naar bepaalde gebeurtenissen, één daarvan is het indrukken van de muisknop. Wanneer het detecteert dat de muis knop is ingedrukt, zal het de code uitvoeren die het is gegeven in de `mouse_pressed()` functie.

--- task ---

Zoek het commentaar **#De mouse_pressed functie komt hier** en daaronder voeg je code toe om je `mouse_pressed()` functie te definiëren.

Add code to print the target emoji 🎯 when the mouse is clicked.

--- code ---
---
language: python filename: main.py — schiet_pijl() line_numbers: true line_number_start: 10
line_highlights: 12-14
---

# De schiet_pijl functie komt hier
def mouse_pressed():    
print( red(raak_kleur), green(raak_kleur), blue(raak_kleur))

--- /code ---

--- /task ---

--- task ---

fill(hout)   
schiet_pijl()

The project prints 🎯 each time the arrow is redrawn.

![Het doelwit, met een bruine cirkelpijl die in verschillende posities verschijnt.](images/fire_arrow.gif)

**Debuggen:** Als je een bericht ziet dat `raak_kleur` 'niet gedefinieerd' is, ga dan terug naar `schiet_pijl()` functie en controleer of je de regel `global raak_kleur` hebt.

**Debuggen:** Controleer de `print` regel heel goed op komma's en haakjes.

--- /task ---

--- save ---
