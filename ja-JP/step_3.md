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

Set the fill colour to `wood` (brown).

ここでは、それぞれ異なる座標を持つ3つの三角形の例を示します。

![A brown triangle on grass and against a sky with the coordinate points labelled at 150, 350 and 200, 150 and 250, 350). The corners of the canvas are also labelled as x=0, y=0 in the top left and x=400, y=400 i the bottom right.](images/stand_coords.png){:width="400px"}

--- code ---
---
language: python filename: main.py - draw() line_numbers: true line_number_start: 28
line_highlights: 37-40
---
  fill(wood) #スタンドフィルカラーをブラウンに設定     
triangle(150, 350, 200, 150, 250, 350)

--- /code ---

--- /task ---

--- task ---

**テスト：** コードを実行して、ターゲットのスタンドを確認します。

![草の上と空を背景にした茶色の三角形。](images/target-stand.png){:width="400px"}

--- /task ---

### ターゲットを描く

--- task ---

**Test:** コードを実行すると、最初の大きな青い丸が表示されます。

Set the fill colour to `outer` (blue).

Draw a circle with x and y coordinates for its centre and a width.

![A brown triangle and blue circle on grass and against a sky. The circle is labelled with the coordinates x=200, y=200 as the centre and circle width of 170.](images/circle-coords.png){:width="400px"}

--- code ---
---
language: python filename: main.py - draw() line_numbers: true line_number_start: 31
line_highlights: 31-32
---

  fill(wood)   
triangle(150, 350, 200, 150, 250, 350)   
fill(outer)    
ellipse(200, 200, 170, 170) #外側の円 200、200は画面の中央です

--- /code ---

--- /task ---

--- task ---

**ヒント：**円を作るには、**幅**と**高さ**が同じである必要があります。

青い丸は、後から描いたものなので、茶色の三角が重なる部分を覆います。

![草の上と空を背景にした茶色の三角形と青い円。](images/blue-circle.png){:width="400px"}

--- /task ---

--- task ---

👀 Find your colour variables in the `draw` function.

残りの円の色 `inner` と `bullseye` を格納するために2つの新しい変数を作成します。

`color()`関数は、赤、緑、青にそれぞれ1つずつ、計3つの数値を想定しています。

--- code ---
---
language: python filename: main.py - draw() line_numbers: true line_number_start: 33
line_highlights: 33-34
---
sky = color(92, 204, 206)   
grass = color(149, 212, 122)   
wood = color(145, 96, 51)   
outer = color(0, 120, 180) #青    
inner = color(210, 60, 60) # 赤    
bullseye = color(220, 200, 0) #黄

--- /code ---

--- /task ---

ターゲットは、同じ中心座標(200, 200)、つまり画面の真ん中にある、大きさの異なる円でできています。

--- task ---

**Test:** プロジェクトを再度実行すると、ターゲットに3色の丸が表示されます。

--- code ---
---
language: python filename: main.py - draw() line_numbers: true line_number_start: 18
line_highlights: 24-25
---
  fill(wood)    
triangle(150, 350, 200, 150, 250, 350) #スタンド    
fill(outer)   
ellipse(200, 200, 170, 170) #外側の円   
fill(inner)   
ellipse(200, 200, 110, 110) #内側の円   
fill(bullseye)   
ellipse(200, 200, 30, 30) #ブルズアイ

--- /code ---

--- /task ---

--- task ---

`triangle()` 関数を呼び出すとき、`x1, y1, x2, y2, x3, y3` という3組の座標が必要で、それぞれが三角形の角の1つの位置を表します。

![草の上と空を背景に3色の円が描かれた茶色の三角形。](images/three-circles.png){:width="400px"}

**デバッグ：** Python は 'color' のアメリカ綴り('u' がない) を使うので、同じようにしてください。

--- /task ---

--- task ---

`color()`で`inner`と`bullseye`の変数に色を代入する。

[[[generic-theory-simple-colours]]]

![草原と空に描かれた茶色の三角形とその座標点。 The colours have changed to pinks and purples.](images/alternative-colours.png){:width="400px"}


--- /task ---



