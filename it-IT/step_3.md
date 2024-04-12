## Disegna il tuo bersaglio

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Il tuo gioco ha bisogno di un bersaglio contro il quale lanciare le frecce.
</div>
<div>

![L'area di output con il bersaglio e il supporto.](images/three-circles.png){:width="300px"}

</div>
</div>

### Disegna un supporto triangolare

--- task ---

Imposta il colore di riempimento su `sienna` (marrone).

Disegna un triangolo utilizzando le coordinate x e y per ciascuno degli angoli.

![Un triangolo marrone sull'erba, contro un cielo con i punti delle coordinate etichettati 150, 350 e 200, 150 e 250, 350). Anche gli angoli del nostro spazio sono etichettati come x=0, y=0 in alto a sinistra e x=400, y=400 in basso a destra.](images/stand_coords.png){:width="400px"}

--- code ---
---
language: python
filename: main.py - draw()
line_numbers: true
line_number_start: 18
line_highlights: 20, 21
---

    fill('lightgreen')  # Imposta il colore di riempimento dell'erba su verde chiaro
    rect(0, 250, 400, 150)  # Disegna un rettangolo per il cielo con questi valori per x, y, larghezza, altezza
    fill('sienna')  # Colore marrone
    triangle(150, 350, 200, 150, 250, 350)  # Disegna un triangolo per la posizione del bersaglio

--- /code ---

--- /task ---

--- task ---

**Test:** 🔄 Esegui il codice per vedere il supporto del tuo obiettivo:

![Un triangolo marrone sull'erba e contro il cielo.](images/target-stand.png){:width="400px"}

--- /task ---

### Disegna i cerchi bersaglio

--- task ---

La parte più grande del bersaglio è un **cerchio** blu.

Imposta il colore di riempimento su `blu`.

Disegna un cerchio con le coordinate x e y per il centro e una larghezza.

![Un triangolo marrone e un cerchio blu sull'erba e sopra il cielo. Il cerchio è etichettato con le coordinate x=200, y=200 come centro e la larghezza del cerchio pari a 170.](images/circle-coords.png){:width="400px"}

--- code ---
---
language: python
filename: main.py - draw()
line_numbers: true
line_number_start: 20
line_highlights: 22, 23
---

    fill('sienna')  # Colore marrone
    triangle(150, 350, 200, 150, 250, 350)  # Disegna un triangolo per la posizione del bersaglio
    fill('blue')  # Imposta il colore di riempimento del cerchio su blu
    circle(200, 200, 170)  # Disegna il cerchio esterno

--- /code ---

--- /task ---

--- task ---

**Test:** Esegui il codice per vedere il primo grande cerchio blu.

Il cerchio blu è stato disegnato dopo lo stand, quindi appare davanti.

![Un triangolo marrone e un cerchio blu sull'erba e sopra il cielo.](images/blue-circle.png){:width="400px"}

--- /task ---

Il bersaglio è composto da cerchi di diverse dimensioni ma con le stesse coordinate centrali (200, 200).

--- task ---

**Aggiungi** cerchi colorati per le parti interne e centrali del bersaglio.

--- code ---
---
language: python
filename: main.py - draw()
line_numbers: true
line_number_start: 20
line_highlights: 24, 25, 26, 27
---

    fill('sienna')  # Colore marrone
    triangle(150, 350, 200, 150, 250, 350)  # Disegna un triangolo per la posizione del bersaglio
    fill('blue')  # Imposta il colore di riempimento del cerchio su blu
    circle(200, 200, 170)  # Disegna il cerchio esterno
    fill('red')  # Imposta il colore di riempimento del cerchio su rosso
    circle(200, 200, 110)  # Disegna il cerchio interno usando x, y, larghezza
    fill('yellow')  # Imposta il colore di riempimento del cerchio su giallo
    circle(200, 200, 30)  # Disegna il cerchio interno usando x, y, larghezza

--- /code ---

--- /task ---

--- task ---

**Test:** 🔄 Esegui il tuo progetto per vedere il bersaglio con i tre cerchi colorati.

![Un triangolo marrone e tre cerchi colorati sull'erba e sopra il cielo.](images/three-circles.png){:width="400px"}

--- /task ---

--- task ---

**Scegli:** 💭 Cambia uno qualsiasi dei colori utilizzando un nome di colore diverso. Puoi trovare un elenco di tutti i nomi dei colori disponibili su [W3 Schools](https://www.w3schools.com/colors/colors_names.asp){:target="blank"}.

![Un triangolo marrone e tre cerchi colorati sull'erba e sopra il cielo. I colori sono cambiati in rosa e viola.](images/alternative-colours.png){:width="400px"}

--- collapse ---
---
title: Codice di esempio che utilizza colori diversi
---

--- code ---
---
language: python
filename: main.py - draw()
line_numbers: false
line_number_start: 14
line_highlights: 
---

def draw():
# Cose da fare in ogni fotogramma

    fill('BlueViolet')
    rect(0, 0, 400, 250)  # Cielo
    fill('DeepSkyBlue')
    rect(0, 250, 400, 150)  # Terra
    fill('FireBrick')
    triangle(150, 350, 200, 150, 250, 350)  # Supporto
    fill('LemonChiffon')
    circle(200, 200, 170)  # Cerchio esterno
    fill('DeepPink')
    circle(200, 200, 110)  # Cerchio interno
    fill('BlueViolet')
    circle(200, 200, 30)  # Cerchio centrale

--- /code ---

--- /collapse ---

--- /task ---

--- save ---
