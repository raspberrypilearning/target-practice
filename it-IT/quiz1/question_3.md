
--- question ---
---
legend: Domanda 3 di 3
---

Viene disegnato un cerchio utilizzando il seguente codice:

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

Quale delle immagini seguenti mostra la posizione corretta di questo cerchio nell'area di output?

--- choices ---

- ( ) ![Un cerchio verde centrato nell'angolo inferiore destro dell'area di output.](images/bottom-right.png)

  --- feedback ---

  Non proprio, per centrare il cerchio nell'angolo in basso a destra, le coordinate dovrebbero essere le stesse della dimensione dello schermo. In questo esempio, l'ellisse sarebbe `circle(400, 400, 300)`.

  --- /feedback ---

- ( ) ![Un cerchio verde centrato nella zona intermedia dell'area di output.](images/centre.png)

  --- feedback ---

  Non proprio, per centrare il cerchio intermedio, le coordinate dovrebbero essere la metà della dimensione dello schermo. In questo esempio, `circle(200, 200, 300)`.

  --- /feedback ---

- (x) ![Un cerchio verde centrato nell'angolo superiore sinistro dell'area di output.](images/top-left.png)

  --- feedback ---

  È corretto! Questo cerchio è centrato nelle coordinate (0,0), nell'angolo in alto a sinistra dello schermo.

  --- /feedback ---

- ( ) ![Un cerchio verde centrato nell'angolo superiore destro dell'area di output.](images/random-side.png)

  --- feedback ---

  No, per centrarlo verso l'angolo in alto a destra dello schermo, questo cerchio avrebbe il codice `circle(350, 150, 300)` . La coordinata `x` indica la distanza dell'ellisse rispetto a margine sinistro dello schermo, mentre la coordinata `y` indica dal margine superiore.

  --- /feedback ---

--- /choices ---

--- /question ---
