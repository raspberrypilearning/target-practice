## What colour did you hit?

Next, you will add some code to get the colour at the location of the arrow.

### Get the colour hit by the arrow

--- task ---

يستخدم من أجل **تخصيص** - مثل `arrow_x = 200` لتعيين قيمة متغير

Add code to `get` the colour at the centre of the arrow ,and store it in the `hit_colour` variable.


--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 9
line_highlights: 28
---
def mouse_pressed():    
if hit_color == outer:    
print('You hit the outer circle, 50 points!')    
elif hit_color == inner:    
print('You hit the inner circle, 200 points!')   
elif hit_color == bullseye:    
print('You hit the bullseye, 500 points!')

--- /code ---

يستخدم لاختبار **تكافؤ** - مثل `hit_color == bullseye` - إذا كانت الأشياء على كلا الجانبين لها نفس القيمة ، فإن الاختبار هو `True`، وإلا فهو `False`

--- /task ---

--- task ---

**اختبار:** قم بتشغيل مشروعك. You should see colours being printed in the **Text output**, in hexadecimal format.

--- /task ---

### Run code when the mouse is pressed

--- task ---

Comment out the line that prints the colour. This means it will not run.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 26
line_highlights: 10-11
---

    def mouse_pressed():<br x-id="5" />
      if hit_color == outer:<br x-id="6" />
        print('You hit the outer circle, 50 points!')

--- /code ---

--- /task ---

--- task ---

Add code to print the target emoji 🎯 **when the mouse is clicked**.

--- code ---
---
language: python filename: main.py - mouse_pressed() line_numbers: true line_number_start: 8
line_highlights: 12-15
---
# The mouse_pressed function goes here
def mouse_pressed():    
print('🎯')

--- /code ---

--- /task ---

**اختبار:** قم بتشغيل مشروعك. You should see the 🎯 character printed when you click the mouse on the target.

![target emoji printed when mouse clicked](images/target_printed.gif) --- /task ---

--- save ---