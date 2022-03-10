## 背景を作成する

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
空と草は、色付きの長方形を描くコードを書くことによって作られています。
</div>
<div>

![草色の長方形の上に空色の長方形がある出力領域で、背景を作成する。](images/background.png){:width="300px"}

</div>
</div>

--- task ---

[アーチェリースターター](https://trinket.io/python/cbf88a8458){:target="_blank"}プロジェクトを開く。

Trinketアカウントをお持ちの方は、**Remix**ボタンをクリックすると、`My Trinkets`ライブラリにコピーを保存することができます。

--- /task ---

スタータープロジェクトには、`p5` ライブラリをインポートするためのコードがすでに書かれており、このライブラリを使ってアーチェリーゲームを構築することになります。

[[[p5-processing-library]]]

--- task ---

`fill()`関数は、図形の内側の色を設定します。 スタータープロジェクトには、これを行うために使用できるRGBカラーがすでにいくつか含まれています。

`draw()`関数を見つけ、`fill()`色を`sky`に設定するコードをインデントして、空を描く準備をします。

--- code ---
---
language: python 
filename: main.py — draw() 
line_numbers: true 
line_number_start: 18
line_highlights: 25
---

def draw():     
  #すべてのフレームで行うこと     
  sky = color(92, 204, 206) #赤 = 92, 緑 = 204, 青 = 206     
  grass = color(149, 212, 122)     
  wood = color(145, 96, 51)     
  outer = color(0, 120, 180)

  fill(sky)

--- /code ---

--- /task ---

`setup()`内の`size()`関数呼び出しで、画面サイズを400ピクセル×400ピクセルに設定しています。

[[[p5-coordinates]]]

--- task ---

`fill()`のコードの後に、`rect()`を左上の座標(`0`,`0`) に合わせて、幅`400`、高さ`250`で描画します。

![灰色の長方形の上に、上部の角から始まる空の長方形の位置を示す座標グリッドが描かれた青色の長方形。](images/sky_coords.png)

--- code ---
---
language: python 
filename: main.py — draw() 
line_numbers: true 
line_number_start: 25
line_highlights: 26
---

  fill(sky) 
  rect(0, 0, 400, 250) #開始 x, 開始 y, 幅, 高さ

--- /code ---

--- /task ---

--- task ---

**テスト：** コードを実行して、結果を確認します。 `p5`ライブラリでは、`run()`関数が`setup()`関数を一度呼び出し、その後`draw()`関数を繰り返し呼び出すことを覚えておいてください。

![灰色の長方形の上に、周囲に黒い境界線がある青い長方形。](images/sky_stroke.png){:width="300px"}

ちょっと不思議な感じですね：あなたの空の周りに黒い線があります！ これは、プログラムが起動するときに、描画するものの周りに**ストローク** という黒い枠を自動的に設定するからです。

--- /task ---

--- task ---

空を描画する前に`no_stroke()`を追加して、ストロークをオフにします。

--- code ---
---
language: python 
filename: main.py — draw() 
line_numbers: true 
line_number_start: 23
line_highlights: 25
---

  outer = color(0, 120, 180)

  no_stroke()   
  fill(sky)   
  rect(0, 0, 400, 250) #x, y, 幅, 高さ

--- /code ---

--- /task ---

--- task ---

**テスト：** プロジェクトを再度実行して、ストロークがなくなったことを確認します。

--- /task ---

--- task ---

`fill()`は、`fill()`が新しい色で再度呼ばれるまで、描画されたすべての図形の塗りつぶしの色を変更します。

`fill()`の色を`grass`に変更し、さらに`rect(x, y, 幅, 高さ)`を追加します。

この長方形は、画面の下部から始まるように、空の下の座標(0, 250) に配置する必要があります。

--- code ---
---
language: python 
filename: main.py — draw() 
line_numbers: true 
line_number_start: 23
line_highlights: 28-29
---

  outer = color(0, 120, 180)

  no_stroke()     
  fill(sky)     
  rect(0, 0, 400, 250) #x, y, 幅, 高さ    
  fill(grass)    
  rect(0, 250, 400, 150)

--- /code ---

--- /task ---

--- task ---

**テスト：** プロジェクトを再度実行して、完成した背景を表示します。

--- /task ---

--- save ---
