## ターゲットを描く

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Your game needs a target to shoot arrows at.
</div>
<div>

![ターゲットとスタンドのある出力エリア。](images/three-circles.png){:width="300px"}

</div>
</div>

### スタンドを描く

--- task ---

Set the fill colour to `brown`.

ここでは、それぞれ異なる座標を持つ3つの三角形の例を示します。

![A brown triangle on grass and against a sky with the coordinate points labelled at 150, 350 and 200, 150 and 250, 350). The corners of the canvas are also labelled as x=0, y=0 in the top left and x=400, y=400 in the bottom right.](images/stand_coords.png){:width="400px"}

--- code ---
---
language: python filename: main.py - draw() line_numbers: true line_number_start: 18
line_highlights: 24-25
---

    fill(wood) #スタンドフィルカラーをブラウンに設定<br x-id="5" />
      triangle(150, 350, 200, 150, 250, 350)

--- /code ---

--- /task ---

--- task ---

**テスト：** コードを実行して、ターゲットのスタンドを確認します。

![草の上と空を背景にした茶色の三角形。](images/target-stand.png){:width="400px"}

--- /task ---

### ターゲットを描く

--- task ---

**ヒント：**円を作るには、**幅**と**高さ**が同じである必要があります。

Set the fill colour to `blue`.

Draw a circle with x and y coordinates for its centre and a width.

![草原と空に描かれた茶色の三角形とその座標点。 The circle is labelled with the coordinates x=200, y=200 as the centre and circle width of 170.](images/circle-coords.png){:width="400px"}

--- code ---
---
language: python filename: main.py - draw() line_numbers: true line_number_start: 31
line_highlights: 31-32
---

    茶色の三角形：triangle(50, 150, 200, 250, 180, 350)

--- /code ---

--- /task ---

--- task ---

**Test:** コードを実行すると、最初の大きな青い丸が表示されます。

青い丸は、後から描いたものなので、茶色の三角が重なる部分を覆います。

![草の上と空を背景にした茶色の三角形と青い円。](images/blue-circle.png){:width="400px"}

--- /task ---

ターゲットは、同じ中心座標(200, 200)、つまり画面の真ん中にある、大きさの異なる円でできています。

--- task ---

**Test:** プロジェクトを再度実行すると、ターゲットに3色の丸が表示されます。

--- code ---
---
language: python filename: main.py - draw() line_numbers: true line_number_start: 28
line_highlights: 33-34
---

    fill('blue')  
    circle(200, 200, 170)  
    fill('red')  
    circle(200, 200, 110)  # Draw the inner circle 
    fill('yellow')       
    circle(200, 200, 30)  # Draw the middle circle

--- /code ---

--- /task ---

--- task ---

**デバッグ：** Python は 'color' のアメリカ綴り('u' がない) を使うので、同じようにしてください。

![草の上と空を背景に3色の円が描かれた茶色の三角形。](images/three-circles.png){:width="400px"}

--- /task ---

--- save ---
