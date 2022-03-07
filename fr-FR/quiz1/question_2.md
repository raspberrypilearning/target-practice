
--- question ---
---
legend : Question 2 sur 3
---

Dans ton projet, tu as utilisé les conditions`if`, `elif`et `else` pour vérifier sur quelle couleur la flèche a atterri.

Lorsque ce code est exécuté, qu'est-ce qui sera imprimé dans la zone de sortie ?

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

  Non, avec l'instruction else, il y aura toujours quelque chose de vrai. Par conséquent, une sortie sera imprimée.

  --- /feedback ---

--- /choices ---

--- /question ---
