
--- question ---
---
legend: Cwestiwn 2 o 3
---

Yn eich prosiect roeddech chi wedi defnyddio'r amodau `if` , `elif`, ac `else` i wirio ar ba liw glaniodd y saeth.

Pan fydd y cod hwn yn cael ei redeg, beth fyddai'n cael ei brintio yn yr ardal allbwn?

--- code ---
---
language: python
---

cyflymder = 6

if cyflymder == 7:
  print('Cyflym iawn iawn')
elif cyflymder == 5:
  print('Eithaf cyflym')
elif cyflymder == 6:
  print('Cyflym iawn')
else:
 print('Heb adnabod y cyflymder!')

--- /code ---

--- choices ---

- (x) `Cyflym iawn`

  --- feedback ---

  Cywir! Mae'r gwerth `6` wedi cael ei neilltuo i'r newidyn **cyflymder**, sy'n golygu mai **True** yw'r amod `cyflymder == 6` a bydd yn printio `Cyflym iawn`.

  --- /feedback ---

- ( ) `Heb adnabod y cyflymder!`

  --- feedback ---

  Ddim yn hollol, 'drychwch ar y gwerth sydd wedi'i neilltuo i'r newidyn **cyflymder**.

  --- /feedback ---

- ( ) Dim byd yn cael ei brintio

  --- feedback ---

  Na, mae'r datganiad else yn golygu y bydd rhywbeth yn wir bob amser. Felly, bydd allbwn yn cael ei brintio.

  --- /feedback ---

--- /choices ---

--- /question ---
