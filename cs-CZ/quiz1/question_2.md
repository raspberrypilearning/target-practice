
--- question ---
---
legend: Otázka 2 ze 3
---

Ve svém projektu jsi použil `if` , `elif` and `else` , abys zkontroloval, na kterou barvu šipka přistála.

V níže uvedeném příkladu má proměnná s názvem `speed` uloženu hodnotu `6`. Když je spuštěn příkaz `if`, co se vytiskne ve výstupní oblasti?

--- code ---
---
language: python
---
speed = 6

if speed == 7: print('Super rychlá') elif speed == 5: print('Docela rychlá') elif speed == 6: print('Velmi rychlá') else: print('Rychlost nebyla rozpoznána!')

--- /code ---

--- choices ---

- (x) `Velmi rychlá`

  --- feedback ---

  Správně! Proměnné **speed** byla přiřazena hodnota `6`. Podmínka `speed == 6` bude vyhodnocena jako **True** a tím pádem bude vytisknuto `Very fast`.

  --- /feedback ---

- ( ) `Rychlost nebyla rozpoznána!`

  --- feedback ---

  Ne tak docela. Podívej se na hodnotu přiřazenou proměnné **speed**.

  --- /feedback ---

- ( ) Nic se nevytiskne

  --- feedback ---

  Zkus to znovu, `else` se použije jako poslední možnost, když jsou všechny výše uvedené podmínky nepravdivé. Prohlédni si znovu podmínky, jsou některé z podmínek pravdivé?

  --- /feedback ---

--- /choices ---

--- /question ---
