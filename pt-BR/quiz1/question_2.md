
--- question ---
---
legend: Pergunta 2 de 3
---

Em seu projeto, você usou as condições `if` , `elif` e `else` para verificar em qual cor a flecha acertou.

No exemplo abaixo, uma variável chamada `velocidade` possui o número `6` armazenado nela. Quando esta instrução `if` for executada, o que será impresso na área de saída?

--- code ---
---
language: python
---
velocidade = 6

if velocidade == 7: print('Super rápido') elif velocidade == 5: print('Bem rápido') elif velocidade == 6: print('Muito rápido') else: print('Velocidade não reconhecida!')

--- /code ---

--- choices ---

- (x) `Muito rápida`

  --- feedback ---

  Está correto! A variável **velocidade** recebeu o valor `6`, o que torna a condição `velocidade == 6` **Verdadeira** e imprime `Muito rápida`.

  --- /feedback ---

- ( ) `Velocidade não reconhecida!`

  --- feedback ---

  Não necessariamente. Veja o valor atribuído à variável **velocidade**.

  --- /feedback ---

- ( ) Nada é impresso

  --- feedback ---

  Tente novamente. `else` é usado como uma opção final para quando todas as condições acima forem falsas. Examine as condições novamente, algumas das condições são verdadeiras?

  --- /feedback ---

--- /choices ---

--- /question ---
