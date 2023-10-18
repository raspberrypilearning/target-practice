## Набирай бали

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Гра буде нараховувати бали залежно від того, чи влучить стріла в ціль.
</div>
<div>

![Мішень зі стрілою, що з'являється в різних положеннях, і бали, що з'являються у вигляді тексту під грою.](images/points-scored.gif){:width="300px"}

</div>
</div>

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
We use <span style="color: #0faeb0; font-weight: bold;"> conditions</span> all the time to make decisions. We could say 'if the pencil is blunt, then sharpen it'. Similarly, `if` conditions let us write code that does something different depending on whether a condition is true or false.
</p>

### Відображення балів

--- task ---

Delete ❌ the `print('🎯')` line of code.

--- code ---
---
def draw():
line_highlights: 28
---
# Things to do in every frame
def mouse_pressed():


--- /code ---

--- /task ---

--- task ---

Display a message **if** the `hit_colour` is equal to the `outer` circle colour (blue) 🎯.

Видали ❌ рядок коду `print( red(hit_color), green(hit_color), blue(hit_color) )`.

--- code ---
---
language: python filename: main.py - mouse_pressed() line_numbers: true line_number_start: 7
line_highlights: 9
---

# Функція mouse_pressed викликається тут
def mouse_pressed():     
if hit_colour == Color('blue').hex:  # Like the code in functions, the code in 'if' statements is indented print('You hit the outer circle, 50 points!')

--- /code ---

**Tip:** 💡 If you changed the colour of your outer circle then you will need to replace `'blue'` with the colour name that you have chosen.

--- /task ---

--- task ---

**Test:** 🔄 Run your project. Try to fire the arrow on the blue outer circle to see the message.

**Tip:** 💡 `frame_rate=2`, in `run` at the bottom of your code, controls how fast your game draws. If it's going too fast, set it to a lower number.

![The output area with arrow touching the outer circle. The points message is displayed in the output area.](images/blue-points.png)

def mouse_pressed():     
if hit_color == outer:      
print('Влучення в зовнішнє коло - 50 балів!') # Подібно до функцій, оператори 'if' починаються з абзацного відступу

**Debug:** 🐞 Make sure your code matches exactly and you indented the code inside your `if` statement.

**Debug:** 🐞 Make sure that you have entered the correct colour name you used for **your** outer circle.

--- /task ---

`elif` (else - if) can be used to add more conditions to your `if` statement. These will be read from top to bottom. As soon as a **True** condition is found, it will be actioned. Any remaining conditions will be ignored.

--- task ---

Score points if the arrow lands on the `inner` or `middle` circles 🎯:

--- code ---
---
language: python filename: main.py - mouse_pressed() line_numbers: true line_number_start: 6
line_highlights: 9, 10
---

def mouse_pressed(): if hit_colour == Color('blue').hex:   
print('You hit the outer circle, 50 points!') elif hit_colour == Color('red').hex: print('You hit the inner circle, 200 points!') elif hit_colour == Color('yellow').hex: print('You hit the middle, 500 points!')

--- /code ---

--- /task ---

--- task ---

**Test:** 🔄 Run your project. Try to fire the arrow on the inner and middle circles to see their messages.

![The output area with arrow touching the inner circle. The points message is displayed in the output area.](images/yellow-points.png)

**Debug:** 🐞 Check your indentation matches the example.

**Debug:** 🐞 If you see a message about `hit_colour` being 'not defined', then go back to `draw()` and check that the line declares `hit_colour` as a global variable.

**Debug:** 🐞 Make sure that you have entered the correct colour name for **your** circles.

**Debug:** 🐞 Make sure that you have used the `.hex` string for **your** circle colours.

--- /task ---

### Мимо мішені

There is one more decision you need to make: what happens if the arrow does not land on any of the target circles? ❌

**Налагодження:** 🐞 Якщо ти бачиш повідомлення, що `inner` або `middle` "не визначено", то повернись до `draw()` та перевір, що вони знаходяться в рядку, який визначає змінні як глобальні.

--- task ---

Add code to `print` a message `else` none of the `if` and `elif` statements have been met.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 6
line_highlights: 11, 12, 13, 14
---

def mouse_pressed(): if hit_colour == Color('blue').hex:   
print('You hit the outer circle, 50 points!') elif hit_colour == Color('red').hex: print('You hit the inner circle, 200 points!') elif hit_colour == Color('yellow').hex: print('You hit the middle, 500 points!') else:   
print('You missed! No points!')

--- /code ---

--- /task ---

--- task ---

**Test:** 🔄 Run your project. Fire the arrow in the grass or sky to see the miss message.

**Choose:** 💭 Change the number of points scored for the different colours.

--- /task ---

--- save ---
