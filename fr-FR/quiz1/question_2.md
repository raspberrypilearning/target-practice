
--- question ---
---
legend : Question 2 sur 3
---

Dans ton projet, tu as utilisé les conditions`if`, `elif` et `else` pour vérifier sur quelle couleur la flèche a atterri.

Dans l'exemple ci-dessous, une variable appelée `vitesse` contient le nombre `6` stocké. Lorsque cette instruction `if` est exécutée, que serait imprimé dans la zone de sortie ?

--- code ---
---
language: python
---
vitesse = 6

if vitesse == 7: print('Super rapide') elif speed == 5: print('Assez rapide') elif speed == 6: print('Très rapide') else: print('Vitesse non reconnue !')

--- /code ---

--- choices ---

- (x) `Très rapide`

  --- feedback ---

  C'est correct ! La variable **vitesse** a reçu la valeur `6`, ce qui rend la condition `vitesse == 6` **True** et imprime `Très rapide`.

  --- /feedback ---

- ( ) `Vitesse non reconnue !`

  --- feedback ---

  Pas tout à fait, regarde la valeur attribuée à la variable **vitesse**.

  --- /feedback ---

- ( ) Rien ne s'imprime

  --- feedback ---

  Réessaie, `else` est utilisé comme option finale lorsque toutes les conditions ci-dessus sont fausses. Regarde à nouveau les conditions, est-ce que l'une d'entre elles est vraie ?

  --- /feedback ---

--- /choices ---

--- /question ---
