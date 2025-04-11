## Rychlý kvíz

Odpovězte na tři otázky. Existují tipy, které vás dovedou ke správné odpovědi.

Po zodpovězení každé otázky klikněte na **Zkontrolujte moji odpověď**.

Příjemnou zábavu!

--- question ---
---
legend: Otázka 1 ze 3
---
Ve svém projektu jsi přidal `randint(100, 300)` do funkce `shoot_arrow()`. Co dělá `randint(100, 300)`?

--- code ---
---
language: python
---

def shoot_arrow():
    global hit_colour
    arrow_x = randint(100, 300)
    arrow_y = randint(100, 300)
  
--- /code ---

--- choices ---

- (x) Vybere náhodné celé číslo mezi 100 a 300.

  --- feedback ---

Správně. Tím vyberete náhodnou souřadnici x pro vaši šipku.

  --- /feedback ---

- ( ) Způsobí, že se šipka náhodně pohybuje po obrazovce.

  --- feedback ---

Ne tak docela. Tento kód je součástí toho, jak se šipka pohybuje náhodně, ale k dosažení tohoto cíle potřebujete také jiný kód.

  --- /feedback ---

- () Získá barvu, kterou zasáhla šipka.

  --- feedback ---

  Ne tak docela. K získání barvy by se použila funkce get().

  --- /feedback ---

- ( ) Nakreslí kruh náhodné velikosti.

  --- feedback ---

  Ne tak docela. K nakreslení kruhu lze použít funkci circle().

  --- /feedback ---

--- /choices ---

--- /question ---
