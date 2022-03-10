## Een achtergrond maken

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
De lucht en het gras worden gemaakt door code te schrijven om gekleurde rechthoeken te tekenen.
</div>
<div>

![Het uitvoergebied met een luchtkleurige rechthoek boven een graskleurige rechthoek om de achtergrond te maken.](images/background.png){:width="300px"}

</div>
</div>

--- task ---

Open het [Boogschieten starter](https://trinket.io/python/ed9eefbca2){:target="_blank"} project.

Als je een Trinket-account hebt, kun je op de knop **Remix** klikken om een kopie op te slaan in je `My Trinkets`-bibliotheek.

--- /task ---

Het startproject heeft al code voor je geschreven om de `p5` -bibliotheek te importeren, je gaat deze bibliotheek gebruiken om je boogschietspel te bouwen.

[[[p5-processing-library]]]

--- task ---

De functie `fill()` stelt de binnenkleur van vormen in. Het startproject bevat al enkele RGB-kleuren die je hiervoor kunt gebruiken.

Zoek je `draw()` functie en bereid je voor om de lucht te tekenen door ingesprongen code toe te voegen om de `fill()` kleur in te stellen op `lucht`:

--- code ---
---
language: python 
filename: main.py — draw() 
line_numbers: true 
line_number_start: 18
line_highlights: 25
---

def draw():     
  #Dingen die je in elk frame moet doen     
  lucht = color(92, 204, 206) #Rood = 92, Groen = 204, Blauw = 206     
  gras = color(149, 212, 122)     
  hout = color(145, 96, 51)     
  buitenste = color(0, 120, 180)

  fill(lucht)

--- /code ---

--- /task ---

De `size()` functie in `setup()` stelt de schermgrootte in op 400 pixels bij 400 pixels.

[[[p5-coordinates]]]

--- task ---

Teken na je `fill()`-code een `rect()` voor de lucht met coördinaten linksboven (`0`,`0`), een breedte van `400` die overeenkomt met de breedte van het scherm en een hoogte van `250`.

![Een blauwe rechthoek met een coördinatenraster die de positie van de luchtrechthoek toont, beginnend in de bovenhoek, boven een grijze rechthoek.](images/sky_coords.png)

--- code ---
---
language: python 
filename: main.py — draw() 
line_numbers: true 
line_number_start: 25
line_highlights: 26
---

  fill(lucht) 
  rect(0, 0, 400, 250) #Start x, start y, breedte, hoogte

--- /code ---

--- /task ---

--- task ---

**Test:** Voer je code uit om de lucht te zien die je hebt getekend. Onthoud dat met de `p5` bibliotheek, de `run()` functie de `setup()` functie eenmaal aanroept, daarna de `draw()` functie herhaaldelijk.

![Een blauwe rechthoek met een zwarte rand eromheen, daarboven een grijze rechthoek.](images/sky_stroke.png){:width="300px"}

Dat is een beetje vreemd: er staat een zwarte lijn om je lucht! Dit komt omdat, wanneer het programma start, het automatisch een zwarte rand plaatst — een zogenaamde **stroke** — rond alles wat het tekent.

--- /task ---

--- task ---

Schakel de lijn uit door `no_stroke()` toe te voegen voordat je de lucht begint te tekenen.

--- code ---
---
language: python 
filename: main.py — draw() 
line_numbers: true 
line_number_start: 23
line_highlights: 25
---

  buitenste = color(0, 120, 180)

  no_stroke()   
  fill(lucht)   
  rect(0, 0, 400, 250) #x, y, breedte, hoogte

--- /code ---

--- /task ---

--- task ---

**Test:** Voer je project opnieuw uit om te controleren of de lijn is verdwenen.

--- /task ---

--- task ---

`fill()` verandert de vulkleur voor alle getekende vormen totdat `fill()` opnieuw wordt aangeroepen met een nieuwe kleur.

Verander de `fill()` kleur in `gras` en voeg nog eens `rect(x, y, breedte, hoogte)`toe.

Deze rechthoek moet op coördinaten (0, 250) onder de lucht worden geplaatst, zodat deze in het onderste deel van het scherm begint.

--- code ---
---
language: python 
filename: main.py — draw() 
line_numbers: true 
line_number_start: 23
line_highlights: 28-29
---

  buitenste = color(0, 120, 180)

  no_stroke()     
  fill(lucht)     
  rect(0, 0, 400, 250) #x, y, breedte, hoogte    
  fill(gras)    
  rect(0, 250, 400, 150)

--- /code ---

--- /task ---

--- task ---

**Test:** Voer je project opnieuw uit om de voltooide achtergrond te bekijken.

--- /task ---

--- save ---
