## ターゲットを描く
<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
ターゲットスタンドは三角形です。 ターゲットはカラーサークルで作られており、小さいサークルは大きいサークルよりもポイントが高くなります。 
</div>
<div>

![ターゲットとスタンドのある出力エリア。](images/three-circles.png){:width="300px"}

</div>
</div>

図形は、コード行が実行される順序で描画されます。 三角形の木製スタンドは、部分的にターゲットサークルの後ろにあるため、最初に描画する必要があります。

紙からすべての形を切り取ると想像してみてください。 その紙をどう並べ、どう重ねるかによって、最終的な仕上がりは大きく変わってきます。

### スタンドを描く

--- task ---

`triangle()` 関数を呼び出すとき、`x1, y1, x2, y2, x3, y3` という3組の座標が必要で、それぞれが三角形の角の1つの位置を表します。

--- collapse ---
---
title: 三角形の座標
---

  ここでは、それぞれ異なる座標を持つ3つの三角形の例を示します。 それぞれのグリッド位置を見て、`x`と`y`の座標が三角形の角をどのように位置づけているかを確認します。
  + 緑の三角形：triangle(50, 50, 150, 50, 180, 100)
  + 青の三角形：triangle(210, 280, 300, 350, 380, 100)
  + 茶色の三角形：triangle(50, 150, 200, 250, 180, 350)

  ![3つの三角形のある出力領域。](images/triangles-coords.png)

--- /collapse ---

角が (150, 350), (200, 150), (250, 350) にあるスタンドの`triangle()`を描画します。

![草原と空に描かれた茶色の三角形とその座標点。](images/stand_coords.png)

--- code ---
---
language: python 
filename: main.py - draw() 
line_numbers: true 
line_number_start: 28
line_highlights: 31-32
---

  fill(grass)   
  rect(0, 250, 400, 150) #x, y, 幅, 高さ

  fill(wood) #スタンドフィルカラーをブラウンに設定     
  triangle(150, 350, 200, 150, 250, 350)


--- /code ---

**ヒント:** 私たちは、`#スタンドフィルカラーをブラウンに設定
` のように、コードにコメントを追加して、それが何をするものなのかを説明しています。 これらのコメントをコードに追加する必要はありませんが、コードの行が何を行っているかを思い出すのに便利です。

--- /task ---

--- task ---

**テスト：** コードを実行して、ターゲットのスタンドを確認します。

![草の上と空を背景にした茶色の三角形。](images/target-stand.png)

--- /task ---

### ターゲットを描く

--- task ---

ターゲットの一番大きな部分は、`ellipse ()` 関数を使って作った青い**円**になります。 楕円は、片側に角のない形状です。 楕円のようにつぶれてもいいし、円のように完全に丸くなってもいい。

楕円は、`x`と`y`の座標、幅、高さが必要です。 楕円の`x`と`y`の座標が中心位置となります。

青い丸は、後から描いたものなので、茶色の三角が重なる部分を覆います。

**ヒント：**円を作るには、**幅**と**高さ**が同じである必要があります。

--- code ---
---
language: python 
filename: main.py - draw() 
line_numbers: true 
line_number_start: 31
line_highlights: 33-34
---

  fill(wood)   
  triangle(150, 350, 200, 150, 250, 350)   
  fill(outer)    
  ellipse(200, 200, 170, 170) #外側の円 200、200は画面の中央です

--- /code ---

--- /task ---

--- task ---

**Test:** コードを実行すると、最初の大きな青い丸が表示されます。

![草の上と空を背景にした茶色の三角形と青い円。](images/blue-circle.png)

--- /task ---

--- task ---

残りの円の色 `inner` と `bullseye` を格納するために2つの新しい変数を作成します。

`color()`で`inner`と`bullseye`の変数に色を代入する。

`color()`関数は、赤、緑、青にそれぞれ1つずつ、計3つの数値を想定しています。

私たちは、伝統的なアーチェリーの的の色を示す数字を使いましたが、互いに異なる色であれば、好きな色を使うことができます。

[[[generic-theory-simple-colours]]]

--- code ---
---
language: python 
filename: main.py - draw() 
line_numbers: true 
line_number_start: 18
line_highlights: 24-25
---

def draw():   
#全てのフレームで行うこと

  sky = color(92, 204, 206)   
  grass = color(149, 212, 122)   
  wood = color(145, 96, 51)   
  outer = color(0, 120, 180) #青    
  inner = color(210, 60, 60) # 赤    
  bullseye = color(220, 200, 0) #黄

--- /code ---

--- /task ---

--- task ---

ターゲットは、同じ中心座標(200, 200)、つまり画面の真ん中にある、大きさの異なる円でできています。

さらに2つの円を追加して、内側の円とブルズアイを表現します。 各円を描く前に`fill()`を変更します。

--- code ---
---
language: python 
filename: main.py - draw() 
line_numbers: true 
line_number_start: 33
line_highlights: 37-40
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

**Test:** プロジェクトを再度実行すると、ターゲットに3色の丸が表示されます。 納得がいくまで色を変えてみてください。

![草の上と空を背景に3色の円が描かれた茶色の三角形。](images/three-circles.png)

**デバッグ：** Python は 'color' のアメリカ綴り('u' がない) を使うので、同じようにしてください。

--- /task ---

--- save ---

