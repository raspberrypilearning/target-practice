## Een achtergrond maken

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Je spel heeft een kleurrijke achtergrond nodig.
</div>
<div>

![Het uitvoergebied met een luchtkleurige rechthoek boven een graskleurige rechthoek om de achtergrond te maken.](images/background.png){:width="300px"}

</div>
</div>

### Open het startproject

--- task ---

Open het project [Doelpraktijk-start](https://editor.raspberrypi.org/en/projects/target-practice-starter){:target="_blank"}. De code-editor wordt geopend in een ander browsertabblad.

Als je een Raspberry Pi-account hebt, kun je op de knop **Save** klikken om een kopie op te slaan in je **Projecten**.

--- /task ---

### Bewerk de lucht

--- task ---

Het startproject heeft al wat code voor je geschreven.

Klik op **'Run'** om een blauw gevulde rechthoek te zien die is getekend van x=`0`, y=`0` (de bovenkant van het scherm). Deze rechthoek van `400` x `250` pixels is de lucht.

![Een blauwe rechthoek met een zwarte rand eromheen, daarboven een grijze rechthoek. De linkerbovenhoek van het canvas is gemarkeerd als x=0, y=0 dit is de oorsprong van de rechthoek. De breedte wordt gemarkeerd als 400 en de hoogte als 250. De code rect(0, 0, 400, 250) wordt weergegeven.](images/sky_stroke.png){:width="300px"}

**Tip:** 💡 Coördinaten beginnen vanaf (x=0, y=0) in de linkerbovenhoek. Dit kan anders zijn dan andere coördinatenstelsels die je hebt gebruikt.

--- /task ---

--- task ---

De lucht is getekend met een zwarte rand (lijn).

Om de lijn voor alle vormen uit te schakelen, voeg je `no_stroke()` toe aan de `setup` functie:

--- code ---
---
language: python filename: main.py — draw() line_numbers: true line_number_start: 9
line_highlights: 12
---
def setup():
# Stel je spel hier in

    size(400, 400)  # Width and height of screen
    no_stroke()

--- /code ---

--- /task ---

--- task ---

**Run** je code opnieuw en merk 👀 op dat de rand (lijn) nu is verdwenen.

**Tip:** 💡 Je moet op **Stop** drukken om je programma te stoppen. Hierdoor zal de **Run** knop opnieuw verschijnen.

--- /task ---

### Teken het gras

--- task ---

**Voeg** code toe om een groene rechthoek onder aan het scherm te tekenen.

![Het uitvoergebied met een luchkleurige rechthoek boven een graskleurige rechthoek om de achtergrond te creëren. De linkerbovenhoek van de rechthoek is gemarkeerd als x=0, y=250 dit is de oorsprong van de rechthoek. De breedte wordt gemarkeerd als 400 en de hoogte als 150. De code rect(0, 250, 400, 150) wordt weergegeven.](images/green-grass.png){:width="400px"}

--- code ---
---
language: python filename: main.py — draw() line_numbers: true line_number_start: 18
line_highlights: 26
---
def draw():
# Dingen om te doen in elk frame

    fill('cyan')  # Set the fill colour for the sky to cyan
    rect(0, 0, 400, 250)  # Draw a rectangle for the sky with these values for x, y, width, height
    fill('lightgreen')  # Set the fill colour for the grass to light green
    rect(0, 250, 400, 150)  # Draw a rectangle for the grass with these values for x, y, width, height

--- /code ---

**Tip:** 💡 We hebben opmerkingen aan onze code toegevoegd, zoals `# Stel de vulkleur voor de lucht in op cyaan`, om je te vertellen wat dit doet. Je hoeft deze opmerkingen niet aan je code toe te voegen, maar ze zijn nuttig om je eraan te herinneren wat coderegels doen.

--- /task ---

--- task ---

**Test:** 🔄 Voer je project opnieuw uit om de voltooide achtergrond te bekijken.

![Het uitvoergebied met een luchtkleurige rechthoek boven een graskleurige rechthoek om de achtergrond te creëren.](images/background.png){:width="400px"}

--- /task ---

--- save ---
