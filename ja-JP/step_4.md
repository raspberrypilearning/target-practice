## 矢を放つ

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
次に、ターゲット領域をランダムに移動する矢を追加します。
</div>
<div>

![茶色の丸い矢が様々な位置に現れるターゲット。](images/fire_arrow.gif){:width="300px"}

</div>
</div>

--- task ---

コメント **# shoot_arrow関数はここにあります ** を探し、その下に `shoot_arrow()` 関数を定義するコードを追加してください。

画面中央に小さな`ellipse()`を追加し、矢を表現します。

--- code ---
---
language: python filename: main.py — shoot_arrow() line_numbers: true line_number_start: 10
line_highlights: 11-12
---

# shoot_arrow関数はここにあります
def shoot_arrow():   
ellipse(200, 200, 15, 15)

--- /code ---

--- /task ---

--- task ---

ターゲットを作成する `draw()`コードに移動して、`fill()`を `wood `に設定するコードを最後に追加し、新しい `shoot_arrow()` 関数を呼び出します。

--- code ---
---
language: python filename: main.py — draw() line_numbers: true line_number_start: 41
line_highlights: 44-45
---

  fill(bullseye)    
ellipse(200, 200, 30, 30)

  fill(wood)   
shoot_arrow()

--- /code ---

--- /task ---

--- task ---

**テスト:**コードを実行し、矢がブルズアイに表示されることを確認します。

![背景のターゲットに茶色の丸い矢印が描かれている。](images/arrow-middle.png)

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;"> コンピュータゲーム、ビデオ、アニメーションは、たくさんの画像を次々に表示することで、動きの効果を生み出します。 各画像は<span style="color: #0faeb0; font-weight: bold;">フレーム</span>と呼ばれます。 画像が変化する速さを<span style="color: #800080;">フレームレート</span>といい、<span style="color: #800080;">fps</span>またはフレーム/秒の単位で示されます。  
</p>

`setup()` の `frame_rate(2)` 行で、フレームレートを2フレーム/秒に設定します。

`draw()`関数は1フレームごとに呼び出されます。 `draw()`が呼ばれるたびにランダムな位置に矢を描画することになります。

背景とターゲットは、古い矢の上に描画されます。 これは、一度に1つの矢しか表示されないことを意味します。

--- task ---

コードの先頭で`import`ステートメントを見つけ、`random`ライブラリから`randint`を使用します。

--- code ---
---
language: python filename: main.py line_numbers: true
line_number_start: 3
---

# ライブラリコードをインポートする
from p5 import *    
from math import *    
from random import randint

--- /code ---

--- /task ---

--- task ---

`shoot_arrow()`関数に行き、`arrow_x`と`arrow_y`の2つの新しい変数を追加して、`100`から`300`までの乱数を格納します。

これによって、一部のショットが的を外れても、端に行くことはなくなります。

`ellipse()` を変更して、新しい変数を使用して矢を配置します。

![半透明の長方形でターゲット領域の座標を示す長方形。](images/target_area.png)

--- code ---
---
language: python filename: main.py — shoot_arrow() line_numbers: true line_number_start: 10
line_highlights: 12-14
---

# shoot_arrow関数はここにあります
def shoot_arrow():    
arrow_x = randint(100, 300)   
arrow_y = randint(100, 300)    
ellipse(arrow_x, arrow_y, 15, 15) #ランダム座標へのアップデイト

--- /code ---

--- /task ---

### 矢が当たった色を取得する

`get()`関数は、ピクセルの色を返します。

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
<span style="color: #0faeb0; font-weight: bold;">ピクセル</span>は、ピクチャーエレメントの略で、画像の中にある1つの色のついた点のことです。 画像は、たくさんの色のついたピクセルで構成されています。
</p>

--- task ---

その上に矢を描く前に、矢が狙っている色を保存する必要があります。

`hit_color`を格納するコードを追加します。 `get()`関数で、`arrow_x`と`arrow_y`座標（矢の中心）のピクセルの色を取得することができます。

--- code ---
---
language: python filename: main.py — shoot_arrow() line_numbers: true line_number_start: 10
line_highlights: 14
---

# shoot_arrow関数はここにあります
def shoot_arrow():    
arrow_x = randint(100, 300)    
arrow_y = randint(100, 300)    
hit_color = get(arrow_x, arrow_y) #矢印を描く前に色を保存する   
ellipse(arrow_x, arrow_y, 15, 15)

--- /code ---

**ヒント：** 色を取得して保存するコードは、楕円を描くコードの**前**にある必要があります。そうしないと、常に矢印の木の色が保存されます!

--- /task ---

`p5` ライブラリは、特定のイベントを「リッスン」します。これらの1つは、マウスボタンを押すことです。 マウスボタンが押されたことを検知すると、`mouse_pressed()`関数で指定されたコードを実行します。

--- task ---

コメント **# mouse_pressed関数はここにあります ** を探し、その下に `mouse_pressed()` 関数を定義するコードを追加します。

矢が当たったピクセルの赤、緑、青の量を表示するコードを追加します。

--- code ---
---
language: python filename: main.py - mouse_pressed() line_numbers: true line_number_start: 8
line_highlights: 9-10
---

# mouse_pressed関数はここにあります
def mouse_pressed():    
print( red(hit_color), green(hit_color), blue(hit_color) )

--- /code ---

--- /task ---

--- task ---

2つの関数 `shoot_arrow()` と `mouse_pressed()` を定義していますが、これらの関数は両方とも `hit_color` 変数を使用する必要があります。

プログラム全体で使用する必要のある変数は、 **グローバル変数**と呼ばれます。 `shoot_arrow()` 関数にコードを追加して、 ` hit_color ` をグローバル変数にします。

--- code ---
---
language: python filename: main.py - shoot_arrow() line_numbers: true line_number_start: 12
line_highlights: 14
---

# shoot_arrow関数はここにあります
def shoot_arrow():    
global hit_color #他の機能でも使用可能     
arrow_x = randint(100, 300)     
arrow_y = randint(100, 300)     
hit_color = get(arrow_x, arrow_y) #矢を描く前に色を保存する     
ellipse(arrow_x, arrow_y, 15, 15)

--- /code ---

--- /task ---

--- task ---

**テスト：** プロジェクトを実行します。 矢印はランダムな座標で再描画されます。

プロジェクトでは、矢印が再描画されるたびに`hit_color`を取得し、ターゲットの下の出力エリアにその色の値を表示します。

![さまざまな位置に茶色の円の矢印が表示されているターゲット。](images/fire_arrow.gif)

**デバッグ：** 「`hit_colour` being 'not defined'」というメッセージが表示された場合は、 `shoot_arrow()` に戻り、 `のグローバル` 行があることを確認します。

**デバッグ：** `print` 行にカンマや括弧がないか、本当に注意深くチェックしてください。

--- /task ---

--- save ---

