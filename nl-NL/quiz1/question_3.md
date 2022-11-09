
--- question ---
---
legend: Vraag 3 van 3
---

A circle is drawn using the following code:

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

Which of the images below show the correct position of this circle in the output area?

--- choices ---

- ( ) ![Een groene cirkel in het midden van de rechterbenedenhoek van het uitvoergebied.](images/bottom-right.png)

  --- feedback ---

  Niet helemaal, om de cirkel in de rechterbenedenhoek te centreren, zouden de coördinaten hetzelfde moeten zijn als de schermgrootte. In this example, the ellipse would be `circle(400, 400, 300)`.

  --- /feedback ---

- ( ) ![Een groene cirkel in het midden van het uitvoergebied.](images/centre.png)

  --- feedback ---

  Niet helemaal, om de cirkel in het midden te centreren, zouden de coördinaten de helft van de schermgrootte moeten zijn. In this example, `circle(200, 200, 300)`.

  --- /feedback ---

- (x) ![Een groene cirkel in het midden van de linkerbovenhoek van het uitvoergebied.](images/top-left.png)

  --- feedback ---

  Dat is correct! Deze cirkel is gecentreerd op coördinaten (0,0), de linkerbovenhoek van het scherm.

  --- /feedback ---

- ( ) ![Een groene cirkel gecentreerd bij de rechterbovenhoek van het uitvoergebied.](images/random-side.png)

  --- feedback ---

  No, this circle would have code of `circle(350, 150, 300)` to centre it towards the top-right of the screen. De `x` coördinaat is hoe ver naar rechts over het scherm de ellips is, en de `y` coördinaat is hoe ver het naar beneden op het scherm is.

  --- /feedback ---

--- /choices ---

--- /question ---
