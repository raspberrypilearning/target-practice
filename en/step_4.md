## Aim your bow

Archery as a competitive sport dates back to medieval England. Nowadays team and individual Archery events are held at they Olympic Games and Paralympic Games with targets that are 122cm in diameter. 

The object of archery is simple: to shoot arrows as close to the centre of a target as possible. Olympic Archery targets are 122cm in diameter with a series of ten concentric scoring rings, separated into five colours. The inner colour, the gold, scores ten or nine points. (The ‘ten’ measures just 12.2cm in diameter — about the size of an apple). Archers shoot at the target from a distance of 70m (around 230ft) — which is the wingspan of two medium-range planes sat side-by-side.


<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Add an introductory sentence. What will learners achieve by the end of this step?
</div>
<div>
Image, gif or video showing what they will achieve by the end of the step. ![](images/image.png){:width="300px"}
</div>
</div>

<mark>shoot_arrow() function and calling it in the draw() function, color(get()) and also rewrite to draw a small elipse (remove point from code).</mark>

--- task ---

Below the code in `draw()` that creates the target, add 

--- code ---
---
language: python
filename: main.py — draw()
line_numbers: true
line_number_start:  
line_highlights: 10-12
---
  fill(YELLOW)
  ellipse(200, 200, 30, 30)
  
  # Arrow
  fill(WOOD)
  
  shoot_arrow()

--- /code ---

--- /task ---

--- task ---

Create a `shoot_arrow()` function where the comment tells you to

--- code ---
---
language: python
filename: main.py — shoot_arrow()
line_numbers: true
line_number_start:  
line_highlights: 10-12
---

# The shoot_arrow function goes here

def shoot_arrow():
  arrow_x = 200
  arrow_y = 200
  ellipse(arrow_x, arrow_y, 10, 10)

--- /code ---

--- /task ---


--- task ---

Step content... 
Can use:
**Test:**
**Choose:**
**Tip:**

--- /task ---

--- save ---


```python



def shoot_arrow():
  global arrow_x, arrow_y
  global pixel_colour
  arrow_x = randint(100, 300)
  arrow_y = randint(100, 300)
  pixel_colour = color(get(arrow_x, arrow_y))
    
  point(arrow_x, arrow_y)
  

```