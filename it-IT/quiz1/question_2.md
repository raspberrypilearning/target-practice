
--- question ---
---
legend: Domanda 2 di 3
---

Nel tuo progetto, hai utilizzato le condizioni `if` , `elif`e `else` per verificare su quale colore è atterrata la freccia.

Nell'esempio seguente, una variabile chiamata `speed` ha il numero `6` memorizzato al suo interno. Quando viene eseguita questa istruzione `if` , cosa verrà stampato nell'area di output?

--- code ---
---
language: python
---
speed = 6

if speed == 7: print('Super veloce') elif speed == 5: print('Abbastanza veloce') elif speed == 6: print('Molto veloce') else: print('Velocità non rilevata!')

--- /code ---

--- choices ---

- (x) `Molto veloce`

  --- feedback ---

  È corretto! Alla variabile **speed** è stato assegnato il valore </>6</code>, in modo che la condizione `speed==6` sia </strong>vera</0> a stampi `Molto veloce`

  --- /feedback ---

- ( ) `Velocità non riconosciuta!`

  --- feedback ---

  Non proprio, guarda il valore assegnato alla variabile **velocità** .

  --- /feedback ---

- ( ) Non viene stampato nulla

  --- feedback ---

  Riprova, `else` viene utilizzato come opzione finale quando tutte le condizioni di cui sopra sono false. Esamina nuovamente le condizioni: qualcuna di esse è vera?

  --- /feedback ---

--- /choices ---

--- /question ---
