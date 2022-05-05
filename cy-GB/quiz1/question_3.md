
--- question ---
---
legend: Cwestiwn 3 o 3
---

Mae elips yn cael ei lunio gan ddefnyddio'r cod canlynol:

--- code ---
---
language: python
---

def setup():   
size(400, 400)   
fill(0,255,0)   
no_stroke()

def draw():   
ellipse(0,0,300,300)

run()

--- /code ---

Pa un o'r lluniau isod sy'n dangos safle cywir yr elips yn yr ardal allbwn?

--- choices ---

- ( ) ![Cylch gwyrdd â'i ganol yng nghornel dde isaf yr ardal allbwn.](images/bottom-right.png)

  --- feedback ---

  Ddim yn hollol. I gael canol y cylch yn y gornel dde isaf, byddai angen i'r cyfesurynnau fod yr un peth â maint y sgrin. Yn yr enghraifft hon, byddai'r elips yn `ellipse(400,400,300,300)`.

  --- /feedback ---

- ( ) ![Cylch gwyrdd â'i ganol yng nghanol yr ardal allbwn.](images/centre.png)

  --- feedback ---

  Ddim yn hollol. I gael canol y cylch yn y canol, byddai angen i'r cyfesurynnau fod hanner maint y sgrin. Yn yr enghraifft hon, `ellipse(200,200,300,300)`.

  --- /feedback ---

- (x) ![Cylch gwyrdd â'i ganol yng nghornel chwith uchaf yr ardal allbwn.](images/top-left.png)

  --- feedback ---

  Cywir! Cyfesurynnau canol y cylch yw (0,0), cornel chwith uchaf y sgrin.

  --- /feedback ---

- ( ) ![Cylch gwyrdd â'i ganol tua chornel dde uchaf yr ardal allbwn.](images/random-side.png)

  --- feedback ---

  Na, byddai gan y cylch hwn y cod `ellipse(350,150,300,300)` i'w ganoli tua cornel dde uchaf y sgrin. Mae'r cyfesuryn `x` yn dangos pa mor bell ar draws y sgrin mae'r elips, a'r cyfesuryn `y` yw pa mor bell i lawr y sgrin mae'r elips.

  --- /feedback ---

--- /choices ---

--- /question ---
