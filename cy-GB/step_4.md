## Saethu

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Nawr mae'n amser ychwanegu saeth sy'n symud ar hap ar draws yr ardal targed.
</div>
<div>

![Y targed, gyda chylch brown, y saeth, yn ymddangos mewn amrywiaeth o safleoedd.](images/fire_arrow.gif){:width="300px"}

</div>
</div>

### Cael y lliw mae'r saeth yn ei daro

--- task ---

Dewch o hyd i'r sylw **#Mae'r swyddogaeth saethu_saeth yn mynd fan hyn** ac ychwanegu cod oddi tano i ddiffinio eich swyddogaeth `saethu_saeth()`.

--- code ---
---
language: python line_numbers: true line_number_start: 8
line_highlights: 11-12
---
# Mae'r swyddogaeth saethu_saeth yn mynd fan hyn
language: python filename: main.py — saethu_saeth() line_numbers: true line_number_start: 10

--- /code ---

--- /task ---

--- task ---

Call your new `shoot_arrow()`{:.language-python} function at the end of your `draw()`{:.language-python} function.

--- code ---
---
language: python line_numbers: true line_number_start: 33
line_highlights: 44-45
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

The arrow needs to move randomly.


--- task ---

Change the `arrow_x`{:.language-python} and `arrow_y`{:.language-python} variables to choose a random number between 100 and 300.

--- code ---
---
language: python line_numbers: true line_number_start: 9
line_number_start: 3
---
def shoot_arrow(): arrow_x = randint(100, 300) arrow_y = randint(100, 300) fill('brown') circle(arrow_x, arrow_y, 15)

--- /code ---

--- /task ---


--- task ---


**Test:** Click the **Run** button. You should see the arrow jump around the target.

![Y targed ar gefndir gyda chylch brown, y saeth, arno.](images/fire_arrow.gif)

--- /task ---

--- save ---
