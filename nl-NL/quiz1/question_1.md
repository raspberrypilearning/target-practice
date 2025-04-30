## Snelle quiz

Beantwoord de drie vragen. Je wordt naar het juiste antwoord geleid.

Klik na het beantwoorden van elke vraag op **Controleer mijn antwoord**.

Veel plezier!

--- question ---
---
legend: Vraag 1 van 3
---
In je project heb je `randint(100, 300)` toegevoegd aan je `schiet_pijl()` functie. Wat doet `randint(100, 300)`?

--- code ---
---
language: python
---

def shoot_arrow(): global hit_colour arrow_x = randint(100, 300) arrow_y = randint(100, 300)

--- /code ---

--- choices ---

- (x) Er wordt een willekeurig geheel getal tussen 100 en 300 gekozen.

  --- feedback ---

Dat klopt. Hiermee kies je een willekeurige x-coördinaat voor jouw pijl.

  --- /feedback ---

- ( ) Hierdoor beweegt de pijl willekeurig over het scherm.

  --- feedback ---

Niet helemaal. Deze code bepaalt gedeeltelijk hoe de pijl willekeurig beweegt, maar om dat doel te bereiken, heb je ook nog andere code nodig.

  --- /feedback ---

- () Het haalt de kleur op die door de pijl werd geraakt.

  --- feedback ---

  Niet helemaal. De get()-functie wordt gebruikt om de kleur op te halen.

  --- /feedback ---

- ( ) Er wordt een cirkelvorm in jouw programma getekend.

  --- feedback ---

  Niet helemaal. De functie circle() zou worden gebruikt om een cirkel te tekenen.

  --- /feedback ---

--- /choices ---

--- /question ---
