
--- question ---
---
legend: Frage 2 von 3
---

In deinem Projekt hast du die Bedingungen `if`, `elif` und `else` verwendet, um zu überprüfen, welche Farbe der Pfeil erreicht hat.

Im folgenden Beispiel ist in einer Variablen namens `geschwindigkeit` die Zahl `6` gespeichert. Was würde im Ausgabebereich stehen, wenn diese `if`-Anweisung ausgeführt wird?

--- code ---
---
language: python
---
geschwindigkeit = 6

if geschwindigkeit == 7: print('Superschnell') elif geschwindigkeit == 5: print('Ziemlich schnell') elif geschwindigkeit == 6: print('Sehr schnell') else: print('Geschwindigkeit unbekannt!')

--- /code ---

--- choices ---

- (x) `Sehr schnell`

  --- feedback ---

  Richtig! Der Variablen **geschwindigkeit** wurde der Wert `6` zugewiesen, wodurch die Bedingung `geschwindigkeit == 6` **wahr** wird und `Sehr schnell` ausgegeben wird.

  --- /feedback ---

- ( ) `Geschwindigkeit unbekannt!`

  --- feedback ---

  Nicht ganz, schau dir den Wert an, der der Variablen **geschwindigkeit** zugewiesen ist.

  --- /feedback ---

- ( ) Es wird nichts ausgegeben

  --- feedback ---

  Versuch es erneut, `else` (deutsch: sonst) wird als letzte Option verwendet, wenn alle darüber gestellten Bedingungen falsch sind. Schau dir die Bedingungen noch einmal an. Sind einige der Bedingungen wahr?

  --- /feedback ---

--- /choices ---

--- /question ---
