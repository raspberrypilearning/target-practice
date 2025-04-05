
--- question ---
---
legenda: Vraag 3 van 3
---

Een cirkel wordt getekend met behulp van de volgende code:

--- code ---
---
language: python
---

def setup():   
size(400, 400)   
fill(0, 255, 0)   
no_stroke()

def draw():   
circle(0, 0, 300)

run()

--- /code ---

Welke van de onderstaande afbeeldingen toont de juiste positie van deze cirkel in het uitvoergebied?

--- choices ---

- ( ) ![Een groene cirkel in het midden van de rechterbenedenhoek van het uitvoergebied.](images/bottom-right.png)

  --- feedback ---

  Niet helemaal, om de cirkel in de rechterbenedenhoek te centreren, zouden de coördinaten hetzelfde moeten zijn als de schermgrootte. In dit voorbeeld zou de ellips `circle(400, 400, 300)`zijn.

  --- /feedback ---

- ( ) ![Een groene cirkel in het midden van het uitvoergebied.](images/centre.png)

  --- feedback ---

  Niet helemaal, om de cirkel in het midden te centreren, zouden de coördinaten de helft van de schermgrootte moeten zijn. In dit voorbeeld `circle(200, 200, 300)`.

  --- /feedback ---

- (x) ![Een groene cirkel in het midden van de linkerbovenhoek van het uitvoergebied.](images/top-left.png)

  --- feedback ---

  Dat is correct! Deze cirkel is gecentreerd op coördinaten (0,0), de linkerbovenhoek van het scherm.

  --- /feedback ---

- ( ) ![Een groene cirkel gecentreerd bij de rechterbovenhoek van het uitvoergebied.](images/random-side.png)

  --- feedback ---

  Nee, deze cirkel zou de code `circle(350, 150, 300)` hebben om deze bij de rechterbovenhoek van het scherm te centreren. De `x` coördinaat is hoe ver naar rechts over het scherm de ellips is, en de `y` coördinaat is hoe ver het naar beneden op het scherm is.

  --- /feedback ---

--- /choices ---

--- /question ---
