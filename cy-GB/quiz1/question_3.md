
--- question ---
---
legend: Cwestiwn 3 o 3
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

- ( ) ![Cylch gwyrdd â'i ganol yng nghornel dde isaf yr ardal allbwn.](images/bottom-right.png)

  --- feedback ---

  Ddim yn hollol. I gael canol y cylch yn y gornel dde isaf, byddai angen i'r cyfesurynnau fod yr un peth â maint y sgrin. In this example, the ellipse would be `circle(400, 400, 300)`.

  --- /feedback ---

- ( ) ![Cylch gwyrdd â'i ganol yng nghanol yr ardal allbwn.](images/centre.png)

  --- feedback ---

  Ddim yn hollol. I gael canol y cylch yn y canol, byddai angen i'r cyfesurynnau fod hanner maint y sgrin. In this example, `circle(200, 200, 300)`.

  --- /feedback ---

- (x) ![Cylch gwyrdd â'i ganol yng nghornel chwith uchaf yr ardal allbwn.](images/top-left.png)

  --- feedback ---

  Cywir! Cyfesurynnau canol y cylch yw (0,0), cornel chwith uchaf y sgrin.

  --- /feedback ---

- ( ) ![Cylch gwyrdd â'i ganol tua chornel dde uchaf yr ardal allbwn.](images/random-side.png)

  --- feedback ---

  No, this circle would have code of `circle(350, 150, 300)` to centre it towards the top-right of the screen. Mae'r cyfesuryn `x` yn dangos pa mor bell ar draws y sgrin mae'r elips, a'r cyfesuryn `y` yw pa mor bell i lawr y sgrin mae'r elips.

  --- /feedback ---

--- /choices ---

--- /question ---
