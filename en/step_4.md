## Add an arrow

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Add an even smaller circle to represent an arrow.
</div>
<div>

![The target, with a brown circle arrow appearing in a variety of positions.](images/fire_arrow.gif){:width="300px"}

</div>
</div>

### Where will you shoot?

--- task ---

Add a function to draw a brown circle at coordinates `200`, `200`. 

--- code ---
---
language: python
line_numbers: true
line_number_start: 8
line_highlights: 9-13
---
# The shoot_arrow function goes here    
def shoot_arrow():   
    arrow_x = 200
    arrow_y = 200
    fill('brown')
    circle(arrow_x, arrow_y, 15)

--- /code ---

--- /task ---

--- task ---

Call your new `shoot_arrow()`{:.language-python} function at the end of your `draw()`{:.language-python} function. 

--- code ---
---
language: python
line_numbers: true
line_number_start: 33
line_highlights: 35
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
language: python
line_numbers: true
line_number_start: 9
line_highlights: 10-11
---
def shoot_arrow():
    arrow_x = randint(100, 300)
    arrow_y = randint(100, 300)
    fill('brown')
    circle(arrow_x, arrow_y, 15)

--- /code ---

--- /task ---


--- task ---


**Test:** Click the **Run** button. You should see the arrow jump around the target.

![An animation of target with a brown circle arrow appearing in a variety of positions.](images/fire_arrow.gif)

--- /task ---

--- save ---
