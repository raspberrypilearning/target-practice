
--- question ---
---
legend: 質問3/3
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

- ( ) ![出力領域の右下隅の中央にある緑色の円。](images/bottom-right.png)

  --- feedback ---

  ちょっと違います、右下の円を中央に配置するには、画面サイズと同じ座標にする必要があります。 In this example, the ellipse would be `circle(400, 400, 300)`.

  --- /feedback ---

- ( ) ![出力領域の中央にある緑色の円。](images/centre.png)

  --- feedback ---

  ちょっと違います、円を中央に配置するためには、座標が画面サイズの半分になる必要があるのです。 In this example, `circle(200, 200, 300)`.

  --- /feedback ---

- (x) ![出力領域の左上隅の中央にある緑色の円。](images/top-left.png)

  --- feedback ---

  そのとおりです！ この円の中心は、画面の左上隅の座標(0,0) です。

  --- /feedback ---

- ( ) ![出力領域の右上に向かって中央に配置された緑色の円。](images/random-side.png)

  --- feedback ---

  No, this circle would have code of `circle(350, 150, 300)` to centre it towards the top-right of the screen. `x`座標は楕円が画面の横方向にどれだけあるか、`y`座標は画面の下方向にどれだけあるかを示しています。

  --- /feedback ---

--- /choices ---

--- /question ---
