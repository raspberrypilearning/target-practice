## Пусти стрілу

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Коли ти будеш натискати або торкатися, стріла буде вистрілювати в місці розташування рухомого круга-мішені.
</div>
<div>

![Мішень з коричневою круговою стрілою, що з'являється в різних положеннях.](images/fire_arrow.gif){:width="300px"}

</div>
</div>

### Намалюй коло для мішені для кожного кадра

--- task ---

Add a function to draw a brown circle at coordinates `200`, `200`.

--- code ---
---
Додай код, щоб випадковим чином з'являвся коричневий кружок всередині мішені:
line_highlights: 10, 11, 12, 13, 14
---
# Функція shoot_arrow викликається тут
def shoot_arrow():   
arrow_x = 200 arrow_y = 200 fill('brown') circle(arrow_x, arrow_y, 15)

--- /code ---

--- /task ---

--- task ---

Call your new `shoot_arrow()`{:.language-python} function at the end of your `draw()`{:.language-python} function.

--- code ---
---
language: python line_numbers: true line_number_start: 33
line_highlights: 44
---

    fill('yellow')      
    circle(200, 200, 30)  
    shoot_arrow()

--- /code ---

--- /task ---

--- task ---

**Test:** Click the **Run** button. You should see the arrow in the centre.


**Test:** Click the **Run** button. You should see the arrow in the centre.

![a brown arrow circle in the centre of the target](images/arrow-centre.png)


--- /task ---

**Тест:** 🔄 Запусти свій код та подивись, як стріла з'являється у випадковому місці в кожному кадрі.


--- task ---

Change the `arrow_x`{:.language-python} and `arrow_y`{:.language-python} variables to choose a random number between 100 and 300.

--- code ---
---
**Тест:** 🔄 Запусти свій код та подивись, як стріла з'являється у випадковому місці в кожному кадрі.
line_highlights: 13
---
def shoot_arrow(): arrow_x = randint(100, 300) arrow_y = randint(100, 300) fill('brown') circle(arrow_x, arrow_y, 15)

--- /code ---

--- /task ---


--- task ---


**Test:** Click the **Run** button. You should see the arrow jump around the target.

![An animation of target with a brown circle arrow appearing in a variety of positions.](images/fire_arrow.gif)

--- /task ---

--- save ---
