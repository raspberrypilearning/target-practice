## Crea uno sfondo

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Il tuo gioco ha bisogno di uno sfondo colorato.
</div>
<div>

![L'area di output con un rettangolo color cielo sopra un rettangolo color erba per creare lo sfondo.](images/ background.png){:width="300px"}

</div>
</div>

### Apri il progetto iniziale

--- task ---

Apri il progetto [Target Practice Starter](https://editor.raspberrypi.org/it-IT/projects/target-practice-starter){:target="_blank"}. L'editor si aprirà in un'altra scheda del browser.

Se disponi di un account Raspberry Pi, puoi fare clic sul pulsante **Salva** per salvarne una copia nei tuoi **Progetti**.

--- /task ---

### Modifica il cielo

--- task ---

Il progetto iniziale ha del codice già scritto per te.

Fai clic su **'Run'** per vedere un rettangolo riempito di blu disegnato da x=`0`, y=`0` (la parte superiore dello schermo). Questo rettangolo che misura `400` x `250` pixel è il cielo.

![Un rettangolo blu con un bordo nero attorno, sopra un rettangolo grigio. L'angolo in alto a sinistra della tela è contrassegnato come x=0, y=0 questa è l'origine del rettangolo. La larghezza è evidenziata come 400 e l'altezza come 250. Viene visualizzato il codice rect(0, 0, 400, 250).](images/sky_stroke.png){:width="400px"}

**Suggerimento:** 💡 Le coordinate iniziano da (x=0, y=0) nell'angolo in alto a sinistra. Questo sistema potrebbe essere diverso da altri sistemi di coordinate che hai già utilizzato.

--- /task ---

--- task ---

Il cielo è stato disegnato con un bordo nero (stroke).

Per disattivare il tratto per tutte le forme aggiungi `no_stroke()` alla funzione `setup` :

--- code ---
---
language: python
filename: main.py — setup()
line_numbers: true
line_number_start: 9
line_highlights: 12
---
def setup():
# Imposta il tuo gioco qui

    size(400, 400)  # Larghezza e altezza dello schermo
    no_stroke()

--- /code ---

--- /task ---

--- task ---

**Esegui** nuovamente il tuo codice e nota 👀 che il bordo (tratto) ora è scomparso.

**Suggerimento:** 💡 Dovrai premere **Stop** per interrompere il programma, in questo modo il pulsante **Run** sarà nuovamente visibile.

--- /task ---

### Disegna l'erba

--- task ---

**Aggiungi** il codice per disegnare un rettangolo verde nella parte inferiore dello schermo.

![L'area di output con un rettangolo color cielo sopra un rettangolo color erba per creare lo sfondo. L'angolo in alto a sinistra del rettangolo è contrassegnato dalle coordinate x=0, y=250; questa è l'origine del rettangolo. La larghezza è indicata come 400 e l'altezza come 150. Viene visualizzato il codice rect(0, 250, 400, 150).](images/green-grass.png){:width="400px"}

--- code ---
---
language: python
filename: main.py — draw()
line_numbers: true
line_number_start: 14
line_highlights: 18-19
---
def draw():
# Cose da fare in ogni fotogramma

    fill('cyan')  # Imposta il colore di riempimento del cielo su ciano
    rect(0, 0, 400, 250)  # Disegna un rettangolo per il cielo con questi valori per x, y, larghezza, altezza
    fill('lightgreen')  # Imposta il colore di riempimento dell'erba su verde chiaro
    rect(0, 250, 400, 150)  # Disegna un rettangolo per il cielo con questi valori per x, y, larghezza, altezza

--- /code ---

**Suggerimento:** 💡 Abbiamo aggiunto commenti al nostro codice, come `# Imposta il colore di riempimento del cielo su ciano`, per dirti cosa fa. Non è necessario aggiungere commenti al codice, ma sono utili per ricordarti cosa fanno le righe di codice.

--- /task ---

--- task ---

**Test:** 🔄 Esegui nuovamente il progetto per visualizzare lo sfondo finito.

![L'area di output con un rettangolo color cielo sopra un rettangolo color erba per creare lo sfondo.](images/background.png){:width="400px"}

--- /task ---

--- save ---
