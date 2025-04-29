
--- question ---
---
legend: Otázka 3 ze 3
---

Kruh se nakreslí pomocí následujícího kódu:

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

Který z obrázků níže ukazuje správnou polohu tohoto kruhu ve výstupní oblasti?

--- choices ---

- ( ) ![Zelený kruh se středem v pravém dolním rohu výstupní oblasti.](images/bottom-right.png)

  --- feedback ---

  Ne tak docela, pro vycentrování kruhu v pravém dolním rohu by souřadnice musely být stejné jako velikost obrazovky. V tomto příkladu by elipsa byla `circle(400, 400, 300)`.

  --- /feedback ---

- ( ) ![Zelený kruh uprostřed oblasti výstupu.](images/centre.png)

  --- feedback ---

  Ne tak docela, aby se kruh vycentroval na střed, souřadnice by musely být poloviční velikosti obrazovky. V tomto příkladu `circle(200, 200, 300)`.

  --- /feedback ---

- (x) ![Zelený kruh se středem v levém horním rohu výstupní oblasti.](images/top-left.png)

  --- feedback ---

  Správně! Tento kruh je vycentrován na souřadnicích (0,0), v levém horním rohu obrazovky.

  --- /feedback ---

- ( ) ![Zelený kruh se středem směrem k pravé horní straně výstupní oblasti.](images/random-side.png)

  --- feedback ---

  Ne, tento kruh by měl kód `circle(350, 150, 300)`, aby byl vycentrován směrem k pravé horní části obrazovky. Souřadnice `x` udává, jak daleko přes obrazovku je elipsa, a souřadnice `y` je, jak daleko je na obrazovce.

  --- /feedback ---

--- /choices ---

--- /question ---
