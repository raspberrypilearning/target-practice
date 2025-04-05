## Додай стрілу

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Додайте найменше коло — це буде стріла.
</div>
<div>

![Мішень з коричневою круговою стрілою, що з'являється в різних положеннях.](images/fire_arrow.gif){:width="300px"}

</div>
</div>

### Куди ти поцілиш?

--- task ---

Додай функцію, яка малюватиме коричневе коло з координатами `200`, `200`.

--- code ---
---
language: python line_numbers: true line_number_start: 8
line_highlights: 9-13
---
# The shoot_arrow function goes here
def shoot_arrow():   
arrow_x = 200 arrow_y = 200 fill('brown') circle(arrow_x, arrow_y, 15)

--- /code ---

--- /task ---

--- task ---

Виклич цю нову функцію `shoot_arrow()`{:.language-python} (з англійської «пустити стрілу») наприкінці своєї функції `draw()`{:.language-python} (з англійської «малювати»).

--- code ---
---
language: python line_numbers: true line_number_start: 33
line_highlights: 35
---

    fill('yellow')      
    circle(200, 200, 30)  
    shoot_arrow()

--- /code ---

--- /task ---

--- task ---

**Протестуй:** натисни на кнопку **Run**. Ти маєш побачити стрілу в центрі.

![Коричневе коло стріли в центрі мішені](images/arrow-centre.png)


--- /task ---

Стріла повинна рухатися випадковим чином.


--- task ---

Зміни код так, щоб змінні `arrow_x`{:.language-python} і `arrow_y`{:.language-python} вибирали випадкове число від 100 до 300.

--- code ---
---
language: python line_numbers: true line_number_start: 9
line_highlights: 10-11
---
def shoot_arrow(): arrow_x = randint(100, 300) arrow_y = randint(100, 300) fill('brown') circle(arrow_x, arrow_y, 15)

--- /code ---

--- /task ---


--- task ---


**Протестуй:** натисни на кнопку **Run**. Ти маєш побачити, як стріла рухається навколо цілі.

![Анімація, на якій коричневе коло стріли зʼявляється у різних положеннях.](images/fire_arrow.gif)

--- /task ---

--- save ---
