## Examen rápido

Contesta las tres preguntas. Hay sugerencias que te guían hacia la respuesta correcta.

Cuando hayas respondido a cada pregunta, haz clic en **Revisar mi respuesta**.

¡Qué te diviertas!

--- pregunta ---
---
legend: Pregunta 1 de 3
---
En tu proyecto agregaste `randint(100, 300)` a tu función `shoot_arrow()`. ¿Qué hace `randint(100, 300)`?

--- code ---
---
language: python
---

def shoot_arrow(): global hit_colour arrow_x = randint(100, 300) arrow_y = randint(100, 300)

--- /code ---

--- opciones ---

- (x) Elige un número entero aleatorio entre 100 y 300.

  --- feedback ---

That's correct. Esto elige una coordenada x aleatoria para tu flecha.

  --- /retroalimentación ---

- ( ) Hace que la flecha se mueva aleatoriamente por la pantalla.

  --- feedback ---

Not quite. Esta parte del código muestra cómo la flecha se mueve aleatoriamente, pero también necesitas otro código para que alcance el objetivo.

  --- /retroalimentación ---

- () Obtiene el color donde se clavó la flecha.

  --- feedback ---

  Not quite. La función get() se puede utilizar para obtener el color.

  --- /feedback ---

- ( ) Dibuja un círculo de tamaño aleatorio.

  --- feedback ---

  Not quite. The circle() function would be used to draw a circle.

  --- /feedback ---

--- /opciones ---

--- /pregunta ---
