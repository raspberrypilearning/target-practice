
--- question ---
---
legend: Frage 3 von 3
---

Ein Kreis wird mit dem folgenden Code gezeichnet:

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

Welches der folgenden Bilder zeigt die korrekte Position dieses Kreises im Ausgabebereich?

--- choices ---

- ( ) ![Ein grüner Kreis in der Mitte der unteren rechten Ecke des Ausgabebereichs.](images/bottom-right.png)

  --- feedback ---

  Nicht ganz. Um den Kreis in der unteren rechten Ecke zu zentrieren, müssten die Koordinaten mit der Bildschirmgröße übereinstimmen. In diesem Beispiel wäre die Ellipse `circle(400, 400, 300)`.

  --- /feedback ---

- ( ) ![Ein grüner Kreis in der Mitte des Ausgabebereichs.](images/centre.png)

  --- feedback ---

  Nicht ganz. Um den Kreis in der Mitte zu zentrieren, müssten die Koordinaten die Hälfte der Bildschirmgröße betragen. In diesem Beispiel `circle(200, 200, 300)`.

  --- /feedback ---

- (x) ![Ein grüner Kreis in der Mitte der oberen linken Ecke des Ausgabebereichs.](images/top-left.png)

  --- feedback ---

  Richtig! Der Mittelpunkt dieses Kreises liegt auf den Koordinaten (0,0), der oberen linken Ecke des Bildschirms.

  --- /feedback ---

- ( ) ![Ein grüner Kreis mit der Mitte oben rechts im Ausgabebereich.](images/random-side.png)

  --- feedback ---

  Nein, dieser Kreis entspräche dem Code `circle(350, 150, 300)`, um ihn oben rechts auf dem Bildschirm zu zentrieren. Die Koordinate `x` gibt an, wie weit die Ellipse über den Bildschirm verläuft, und die Koordinate `y` gibt an, wie weit unten auf dem Bildschirm sie liegt.

  --- /feedback ---

--- /choices ---

--- /question ---
