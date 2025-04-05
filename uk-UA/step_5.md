## У який колір влучила стріла?

Тепер ти додаси код, який буде визначати колір місця, куди влучила стріла.

### Визнач колір, на який потрапила стріла

--- task ---

Додай нову **глобальну змінну** під назвою `hit_colour` (з англійської «колір, у який влучила стріла»).

Додай код який буде `діставати` (англійською get) колір пікселя з центру стріли та зберігати його у змінній `hit_color`.


--- code ---
---
language: python
line_numbers: true
line_number_start: 9
line_highlights: 10, 13, 14
---
def shoot_arrow():
    global hit_colour  
    arrow_x = randint(100, 300)  
    arrow_y = randint(100, 300) 
    hit_colour = get(arrow_x, arrow_y).hex
    print(hit_colour)
    fill('brown')
    circle(arrow_x, arrow_y, 15)

--- /code ---

**Порада:** код для визначення кольору (`get`) повинен бути **перед** кодом, який малює коло (`circle`). Інакше ти будеш постійно зберігати коричневий колір стріли!

--- /task ---

--- task ---

**Протестуй:** натисни на кнопку **Run**. Ти маєш бачити кольори, що друкуються у **полі для вихідного тексту** у шістнадцятковому форматі.

--- /task ---

### Запускай код, коли натиснута кнопка миші

--- task ---

Додай значок коментаря # перед рядком, який виводить колір. Це означає, що цей рядок не буде виконуватися.


--- code ---
---
language: python
line_numbers: true
line_number_start: 13
line_highlights: 14
---
    hit_colour = get(arrow_x, arrow_y).hex
    # print(hit_colour)
    circle(arrow_x, arrow_y, 15)

--- /code ---

--- /task ---

--- task ---

Додай код, щоб **коли натискалася кнопка миші**, у полі для вихідного тексту виводилось емоджі мішені 🎯.

--- code ---
---
language: python
line_numbers: true
line_number_start: 5
line_highlights: 6-7
---
# Тут буде функція mouse_pressed  
def mouse_pressed():    
    print('🎯')

--- /code ---

--- /task ---

--- task --- 

**Протестуй:** натисни на кнопку **Run**. Ти маєш бачити символ мішені 🎯 щоразу, як клацаєш мишкою на мішені.

![Емоджі мішені виводиться, коли натиснута кнопка миші](images/target_printed.gif)

--- /task ---

--- save ---