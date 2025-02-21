## Створення фону

--- task ---

Відкрий стартовий проєкт [Стрільба по мішені](https://trinket.io/python/ba27b1e043){:target="_blank"}.

--- /task ---

--- task ---

**Add** code to draw a green rectangle at the bottom of the screen to represent the grass.

![Область виводу з прямокутником небесного кольору, над прямокутником зеленого кольору, які створюють фон. Верхній лівий кут прямокутника позначено як x=0, y=250 - це початок прямокутника. Ширина виділена як 400, а висота - як 150. Показано код rect(0, 250, 400, 150).](images/green-grass.png){:width="400px"}

--- code ---
---
language: python line_numbers: true line_number_start: 17
line_highlights: 15
---
def draw(): # Things to do in every frame fill('cyan')  
rect(0, 0, 400, 250)  
fill('lightgreen')  
rect(0, 250, 400, 150)

--- /code ---

--- /task ---

--- task ---

Небо обведено чорною рамкою (обведенням).

![The output area with a sky-coloured rectangle above a grass-coloured rectangle to create the background.](images/background.png){:width="400px"}

--- /task ---

--- save ---
