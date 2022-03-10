## Punten scoren

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
In deze stap voeg je scores toe afhankelijk van waar de pijl raakt.
</div>
<div>

![Het doel, met de pijl die op verschillende posities verschijnt, en scores die als tekst onder het spel verschijnen.](images/points-scored.gif){:width="300px"}

</div>
</div>

--- task ---

De kleurvariabelen in de functie `draw()` worden gebruikt om de score in de functie `mouse_pressed()` te controleren. Om dit te kunnen doen, moeten ze worden ingesteld als globale variabelen:

--- code ---
---
language: python 
filename: main.py 
line_numbers: true 
line_number_start: 26
line_highlights: 28
---

def draw():
#Dingen om te doen in elk frame
  global buitenste, binnenste, roos    
  lucht = color(92, 204, 206) #Rood = 92, Groen = 204, Blauw = 206    
  gras = color(149, 212, 122)    
  hout = color(145, 96, 51)    
  buitenste = color(0, 120, 180)    
  binnenste = color(210, 60, 60)   
  roos = color(220, 200, 0)

--- /code ---

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
We gebruiken voortdurende <span style="color: #0faeb0; font-weight: bold;"> voorwaarden</span> om beslissingen te nemen. We zouden kunnen zeggen 'als het potlood bot is, slijp het dan'. Evenzo laten `if`-voorwaarden ons code schrijven die iets anders doet, afhankelijk van of een voorwaarde waar of onwaar is.
</p>

--- task ---

Om een bericht voor de buitenste cirkel van het doel `weer te geven`, voeg je code toe aan je `mouse_pressed()` functie om te controleren of de `raak_kleur` `==` is aan de `buitenste`.

Wees voorzichtig bij het gebruik van het `=` symbool in Python:
 + `=` wordt gebruikt voor een **toewijzing** — zoals `pijl_x = 200` om de waarde van een variabele in te stellen
 + `==` wordt gebruikt om **gelijkheid** te testen — zoals `raak_kleur == roos` — als beide kanten dezelfde waarde hebben, dan is de test `True` (Waar), anders is het `False` (Niet waar)

Wijzig de code in `print()` om een score te geven:

--- code ---
---
language: python 
filename: main.py - mouse_pressed() 
line_numbers: true 
line_number_start: 8
line_highlights: 10-11
---

#De mouse_pressed functie komt hier
def mouse_pressed():     
  if raak_kleur == buitenste:      
    print('Je raakt de buitenste cirkel, 50 punten!') #Net als functions zijn 'if'-instructies ingesprongen

--- /code ---

--- /task ---

--- task ---

**Test:** Voer je project uit. Probeer de pijl op de blauwe buitenste cirkel te laten landen om je bericht te zien. De kleur van de pixel in het midden van de pijl is de kleur die is opgeslagen en gecontroleerd.

**Tip:** `frame_rate()`, in `setup()`, bepaalt hoe snel je spel gaat. Als het te snel gaat, stel het dan in op een lager getal.

![Het uitvoergebied met de pijl die de buitenste cirkel raakt. De punten worden getoond in het uitvoergebied.](images/blue-points.png)

**Debuggen:** Zorg ervoor dat je code exact overeenkomt en dat de code in je `if`-statement is ingesprongen. De inspringing vertelt Python dat de code alleen moet worden uitgevoerd als de voorwaarde `Waar`is.

--- /task ---

Aangezien er punten worden gescoord als de pijl ook op de `binnenste` of `roos` cirkels terechtkomt, is `buitenste` niet de enige cirkel die je moet controleren. Gebruik hiervoor `elif` (een verkorte versie van else - if).

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
We gebruiken <span style="color: #0faeb0; font-weight: bold;"> else - if </span> om beslissingen in het echte leven te nemen. Wanneer je een afbeelding van de lucht schildert, kun je controleren of er een gele verf voor de zon is. Anders, als er geen gele verf is, zoek je naar oranje. Anders, als er geen gele of oranje verf is, zou je rood kunnen gebruiken - heel licht!
</p>

--- task ---

Een `elif` kan alleen gebruikt worden met een `if` statement en, net als een `if`, controleert het een voorwaarde. Als de voorwaarde `Waar`is, voert de `elif` wat code uit.

Wat `elif` anders maakt, is dat het die controle alleen zal uitvoeren als de voorwaarden van de `if` en elke `elif` ervoor `Niet waar`zijn.

Voeg `elif` statements toe voor `binnenste` en `roos`.

--- code ---
---
language: python 
filename: main.py - mouse_pressed() 
line_numbers: true 
line_number_start: 9
line_highlights: 12-15
---

def mouse_pressed():    
  if raakt_kleur == buitenste:    
    print('Je raakt de buitenste cirkel, 50 punten!')    
  elif raak_kleur == binnenste:    
    print('Je raakt de binnenste cirkel, 200 punten!')   
  elif raak_kleur == roos:    
    print('Je raakt de roos, 500 punten!')

--- /code ---

--- /task ---

--- task ---

**Test:** Voer je project uit. Probeer de pijl op de rode en gele cirkels te laten landen om hun berichten te zien.

![Het uitvoergebied met de pijl die de binnenste cirkel raakt. De punten worden getoond in het uitvoergebied.](images/yellow-points.png)

**Debuggen:** Zorg ervoor dat `elif` zich op hetzelfde inspringniveau bevindt als je `if`, en dat de code in je `elif` zich op hetzelfde niveau bevindt als de code in je `if`.

**Debuggen:** Als je een bericht ziet over `binnenste` of `roos` die 'niet gedefinieerd' zijn, ga dan terug naar `draw()` en controleer of ze als globale variabele declareert zijn.

```python
global buitenste, binnenste, roos
```

--- /task ---

Er is nog een beslissing die je moet nemen: wat gebeurt er als de pijl niet op een van de doelcirkels landt? Om deze laatste controle uit te voeren, gebruik je `else`.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
We gebruiken <span style="color: #0faeb0; font-weight: bold;"> if ... else</span> om beslissingen te nemen. Als je wakker wordt, controleer je en als het ochtend is sta je op, anders ga je weer slapen. Kun je een 'if ... else'  beslissing bedenken? 
</p>

--- task ---

Voeg code toe om een bericht `te tonen` `als` aan geen van de `if` en `elif` voorwaarden is voldaan.

--- code ---
---
language: python 
filename: main.py 
line_numbers: true 
line_number_start: 9
line_highlights: 16-17
---

def mouse_pressed():    
  if raak_kleur == buitenste:   
    print('Je raakt de buitenste cirkel, 50 punten!')   
  elif raak_kleur == binnenste:   
    print('Je raakt de binnenste cirkel, 200 punten!')   
  elif raak_kleur == roos:    
    print('Je hebt de roos, 500 punten!')   
  else:   
    print('Je hebt gemist! Geen punten!')

--- /code ---

--- /task ---

--- task ---

**Test:** Voer je project uit. Probeer de pijl in het gras of de lucht te laten landen om het bericht 'Gemist' te zien. Wijzig desgewenst het aantal gescoorde punten voor de verschillende kleuren.

![Het uitvoergebied met een pijl die het doel mist. De punten worden getoond in het uitvoergebied.](images/missed-points.png)

--- /task ---

--- save ---
