
--- question ---
---
legend: Питання 3 з 3
---

За допомогою наступного коду малюється коло:

--- code ---
---
language: python
---

def setup():   
  size(400, 400)   
  fill(0, 255, 0)   
  no_stroke()   
    
def draw():   
  circle(0, 0, 300)    

run()

--- /code ---

На якому з наведених нижче зображень показано правильне положення кола в області виводу результатів?

--- choices ---

- ( ) ![Зелене коло з центром у правому нижньому куті області виводу.](images/bottom-right.png)

  --- feedback ---

  Не зовсім так. Для центрування кола в правому нижньому куті необхідно, щоб його координати збігалися з розміром екрана. У нашому прикладі еліпс матиме такий вигляд: `circle(400, 400, 300)`.

  --- /feedback ---

- ( ) ![Зелене коло з центром посередині в області виводу.](images/centre.png)

  --- feedback ---

  Не зовсім так. Щоб відцентрувати коло посередині, координати повинні бути вдвічі меншими за розмір екрана. У нашому прикладі це було б `circle(200, 200, 300)`.

  --- /feedback ---

- (x) ![Зелене коло з центром у лівому верхньому куті області виводу.](images/top-left.png)

  --- feedback ---

  Правильно! Центр цього кола знаходиться в точці з координатами (0,0) — верхньому лівому куті екрана.

  --- /feedback ---

- ( ) ![Зелене коло з центром у верхньому правому куті області виводу.](images/random-side.png)

  --- feedback ---

  Ні, щоб відцентрувати коло у верхньому правому куті екрана, його код мав би бути `circle(350, 150, 300)`. Координата `x` встановлює позицію еліпса на екрані по горизонталі, а координата `y` встановлює позицію по вертикалі.

  --- /feedback ---

--- /choices ---

--- /question ---
