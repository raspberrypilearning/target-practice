## Scocca la tua freccia

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Quando fai clic o tocchi, una freccia sarà lanciata verso la posizione di un bersaglio rotondo in movimento. 
</div>
<div>

![Il bersaglio, con una freccia circolare marrone che appare in varie posizioni.](images/fire_arrow.gif){:width="300px"}

</div>
</div>

### Disegna un obiettivo rotondo in ogni fotogramma

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;"> I computer creano l'effetto del movimento mostrando molte immagini una dopo l'altra. Ogni immagine è chiamata <span style="color: #0faeb0; font-weight: bold;"> frame </span>.   
</p>

--- task ---

Definisci la tua funzione `shoot_arrow()` sotto il commento **# La funzione shoot_arrow() va qui**.

Aggiungi il codice per disegnare casualmente un cerchio marrone all'interno di un'area target:

![Un rettangolo che mostra le coordinate dell'area target in un rettangolo semitrasparente. L'area target è compresa tra x=100 e y=100 fino a x=300 e y=300, quindi copre l'intero target e anche oltre.](images/target_area.png)

--- code ---
---
language: python
filename: main.py — shoot_arrow()
line_numbers: true
line_number_start: 7
line_highlights: 8-12
---
# La funzione shoot_arrow va qui
def shoot_arrow():   
    arrow_x = randint(100, 300)  # Memorizza un numero a caso fra 100 e 300
    arrow_y = randint(100, 300)  # Memorizza un numero a caso fra 100 e 300
    fill('sienna')  # Imposta la freccia in modo che il colore di riempimento sia marrone 
    circle(arrow_x, arrow_y, 15)  # Disegna un piccolo cerchio a coordinate casuali

--- /code ---

--- /task ---

--- task ---

Vai alla funzione `draw` e chiama la tua nuova funzione `shoot_arrow` .

--- code ---
---
language: python
filename: main.py — draw()
line_numbers: true
line_number_start: 31
line_highlights: 33
---

    fill('yellow')  # Imposta il colore di riempimento del cerchio su giallo
    circle(200, 200, 30)  # Disegna il cerchio interno usando x, y, larghezza
    shoot_arrow()

--- /code ---

--- /task ---

--- task ---

**Test:** 🔄 Esegui il codice e osserva la freccia apparire in una posizione casuale in ogni fotogramma.

![Un'animazione del bersaglio con una freccia circolare marrone che appare in diverse posizioni.](images/fire_arrow.gif)

Lo sfondo e il bersaglio verranno disegnati sopra la vecchia freccia. Ciò significa che vedi solo una freccia alla volta.

--- /task ---

### Ottieni il colore colpito dalla freccia

La funzione `get()` restituisce il colore di un pixel.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Un <span style="color: #0faeb0; font-weight: bold;">pixel</span>, abbreviazione di picture element, è un singolo punto colorato all'interno di un'immagine. Le immagini sono composte da molti pixel colorati.
</p>

--- task ---

Aggiungi una  **variabile globale** chiamata `hit_color` che può essere utilizzata in tutto il codice.

Aggiungi il codice per `ottenere` il colore del pixel al centro della freccia e memorizzalo nella variabile `hit_color`. Per confrontare i colori dobbiamo utilizzare il codice esadecimale. Questo può essere fatto con la stringa `.hex` .

--- code ---
---
language: python
filename: main.py — shoot_arrow() 
line_numbers: true
line_number_start: 7
line_highlights: 9, 12
---
# La funzione shoot_arrow va qui
def shoot_arrow():
    global hit_colour  # Può essere utilizzato in altre funzioni 
    arrow_x = randint(100, 300)  # Memorizza un numero a caso fra 100 e 300
    arrow_y = randint(100, 300)  # Memorizza un numero a caso fra 100 e 300
    hit_colour = get(arrow_x, arrow_y).hex  # Ottieni il colore colpito
    fill('sienna')  # Imposta la freccia in modo che il colore di riempimento sia marrone
    circle(arrow_x, arrow_y, 15)  # Disegna un piccolo cerchio a coordinate casuali

--- /code ---

**Suggerimento** 💡Il codice per `ottenere (get)` i colori deve essere inserito **prima** del codice per disegnare il `cerchio` altrimenti salverai sempre il color legno della freccia!

--- /task ---

### Stampa il colore quando si preme il mouse

La libreria `p5` 'ascolta' determinati eventi, uno di questi è la pressione del pulsante del mouse. Quando rileva che il pulsante è stato premuto, eseguirà qualunque codice sia stato inserito nella funzione `mouse_pressed` .

--- task ---

Definisci la tua funzione `mouse_pressed()` sotto il commento **# La funzione mouse_pressed va qui**.

Aggiungi il codice per stampare l'emoji target 🎯 quando si fa clic con il mouse.

--- code ---
---
language: python
filename: main.py - mouse_pressed()
line_numbers: true
line_number_start: 5
line_highlights: 6
---

# La funzione mouse_pressed va qui
def mouse_pressed():    
    print('🎯')

--- /code ---

--- /task ---

--- task --- 

**Test:** 🔄 Esegui il tuo progetto.

Il progetto stampa 🎯 ogni volta che la freccia viene ridisegnata.

![Un'animazione del bersaglio con una freccia circolare marrone che appare in diverse posizioni.](images/fire_arrow.gif)

**Debug:** 🐞Se vedi un messaggio `hit_colour` being 'not defined', torna indietro alla funzione `shoot_arrow()` e controlla di aver incluso la riga `global hit_colour` .

**Debug:** 🐞 Controlla con molta attenzione le virgole e le parentesi alla riga `print` .

--- /task ---

--- save ---
