
--- question ---
---
legend: Pregunta 2 de 3
---

En su proyecto, usaste condiciones `if`, `elif` y `else` para verificar en qué color aterrizó la flecha.

En el siguiente ejemplo, una variable llamada `velocidad` `6` almacena el número 6. Cuando se ejecuta esta instrucción `if`, ¿qué se imprimirá en el área de salida?

--- code ---
---
language: python
---
velocidad = 6

if velocidad == 7:
  print('Súper rápido')
elif velocidad == 5:
  print('Bastante rápido')
elif velocidad == 6:
  print('Muy rápido')
else:
 print('¡Velocidad no reconocida!') 

--- /code ---

--- choices ---

- (x) `Muy rápido`

  --- feedback ---

  ¡Correcto! A la variable **velocidad** se le ha asignado el valor `6`, lo que hace que la `velocidad == 6` Sea **Verdadero** e imprima `Muy rápido`.

  --- /feedback ---

- ( ) `¡Velocidad no reconocida!`

  --- feedback ---

  No del todo, mira el valor asignado a la variable **velocidad**.

  --- /feedback ---

- ( ) No se imprime nada

  --- feedback ---

  Inténtalo de nuevo, `else` se usa como una opción final para cuando todas las condiciones anteriores son falsas. Mira nuevamente las condiciones, ¿alguna de las condiciones es verdadera?

  --- /feedback ---

--- /choices ---

--- /question ---
