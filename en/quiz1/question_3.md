
--- question ---
---
legend: Question 3 of 3
---

A circle is drawn using the following code: 

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

Which of the images below show the correct position of this circle in the output area?

--- choices ---

- ( ) ![A green circle centred in the bottom-right corner of the output area.](images/bottom-right.png)

  --- feedback ---
  
  Not quite, to centre the circle in the bottom-right corner, the coordinates would need to be the same as the screen size. In this example, the ellipse would be `circle(400, 400, 300)`. 

  --- /feedback ---

- ( ) ![A green circle centred in the middle of the output area.](images/centre.png) 

  --- feedback ---

  Not quite, to centre the circle in the middle, the coordinates would need to be half of the screen size. In this example, `circle(200, 200, 300)`. 

  --- /feedback ---

- (x) ![A green circle centred in the top-left corner of the output area.](images/top-left.png)

  --- feedback ---
  
  That's correct! This circle is centred at coordinates (0,0), the top-left corner of the screen. 

  --- /feedback ---

- ( ) ![A green circle centred towards the top-right side of the output area.](images/random-side.png)

  --- feedback ---
  
  No, this circle would have code of `circle(350, 150, 300)` to centre it towards the top-right of the screen. The `x` coordinate is how far across the screen the ellipse is, and the `y` coordinate is how far down the screen it is.

  --- /feedback ---

--- /choices ---

--- /question ---
