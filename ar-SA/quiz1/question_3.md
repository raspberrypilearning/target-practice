
--- question ---
---
legend: السؤال 3 من 3
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

- ( ) ![دائرة خضراء متمركزة في الركن الأيمن السفلي من منطقة المخرجات.](images/bottom-right.png)

  --- feedback ---

  ليس تمامًا ، لتوسيط الدائرة في الزاوية اليمنى السفلية ، يجب أن تكون الإحداثيات هي نفس حجم الشاشة. In this example, the ellipse would be `circle(400, 400, 300)`.

  --- /feedback ---

- ( ) ![دائرة خضراء تتمركز في منتصف منطقة المخرجات.](images/centre.png)

  --- feedback ---

  ليس تمامًا ، لتوسيط الدائرة في المنتصف ، يجب أن تكون الإحداثيات نصف حجم الشاشة. In this example, `circle(200, 200, 300)`.

  --- /feedback ---

- (x) ![دائرة خضراء متمركزة في الزاوية العلوية اليسرى من منطقة المخرجات.](images/top-left.png)

  --- feedback ---

  هذا صحيح! تتركز هذه الدائرة عند الإحداثيات (0،0) ، الزاوية العلوية اليسرى من الشاشة.

  --- /feedback ---

- ( ) ![دائرة خضراء متمركزة في الجانب العلوي الأيمن من منطقة المخرجات.](images/random-side.png)

  --- feedback ---

  No, this circle would have code of `circle(350, 150, 300)` to centre it towards the top-right of the screen. الإحداثي `×` هو مدى المسافة بين القطع الناقص عبر الشاشة ، والإحداثي `y` هو مدى المسافة أسفل الشاشة.

  --- /feedback ---

--- /choices ---

--- /question ---
