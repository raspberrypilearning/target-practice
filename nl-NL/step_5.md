## Welke kleur heb je geraakt?

Vervolgens voeg je wat code toe om de kleur op de plek van de pijl op te halen.

### Haal de kleur op die door de pijl wordt geraakt

--- task ---

Voeg een nieuwe **globale variabele** toe met de naam `raak_kleur`.

Voeg code toe om de kleur in het midden van de pijl `op te halen` en sla deze op in de variabele `raak_kleur`.


--- code ---
---
language: python
line_numbers: true
line_number_start: 9
line_highlights: 10, 13, 14
---
def schiet_pijl():
    global raak_kleur  
    pijl_x = randint(100, 300)  
    pijl_y = randint(100, 300) 
    raak_kleur = get(pijl_x, pijl_y).hex
    print(raak_kleur)
    fill('brown')
    circle(pijl_x, pijl_y, 15)

--- /code ---

**Tip:** 💡 De `get`-code om de kleur op te halen en op te slaan moet **vóór** de code om de `cirkel` te tekenen staan, anders bewaar je altijd de bruin kleur van de pijl!

--- /task ---

--- task ---

**Test:** Klik op de knop **Run**. Je zou kleuren moeten zien afgedrukt in de **Tekstuitvoer**, in hexadecimaal formaat.

--- /task ---

### Code uitvoeren wanneer de muis wordt ingedrukt

--- task ---

Maak een comment van de regel die de kleur print. Dit betekent dat het niet zal werken.

--- code ---
---
language: python
line_numbers: true
line_number_start: 13
line_highlights: 14
---
    raak_kleur = get(pijl_x, pijl_y).hex
    # print(raak_kleur)
    circle(pijl_x, pijl_y, 15)

--- /code ---

--- /task ---

--- task ---

Voeg code toe om de doel-emoji 🎯 af te drukken **wanneer met de muis wordt geklikt**.

--- code ---
---
language: python
line_numbers: true
line_number_start: 5
line_highlights: 6-7
---
# De mouse_pressed functie komt hier  
def mouse_pressed():    
    print('🎯')

--- /code ---

--- /task ---

--- task --- 

**Test:** Klik op de knop **Run**. Wanneer je met de muis op het doel klikt, zou je het teken 🎯 moeten zien.

![doel-emoji geprint wanneer met de muis wordt geklikt](images/target_printed.gif)

--- /task ---

--- save ---