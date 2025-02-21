## Draw the grass

--- task ---

[アーチェリースターター](https://trinket.io/python/cbf88a8458){:target="_blank"}プロジェクトを開く。

--- /task ---

--- task ---

**Add** code to draw a green rectangle at the bottom of the screen to represent the grass.

![The output area with a sky-coloured rectangle above a grass-coloured rectangle to create the background. The top left corner of the rectangle is marked as x=0, y=250 this is the origin of the rectangle. The width is highlighted as 400 and the height as 150. The code rect(0, 250, 400, 150) is shown.](images/green-grass.png)`fill()`のコードの後に、`rect()`を左上の座標(`0`,`0`) に合わせて、幅`400`、高さ`250`で描画します。

--- code ---
---
language: python filename: main.py — draw() line_numbers: true line_number_start: 18
line_highlights: 25
---
def draw(): # Things to do in every frame fill('cyan')  
rect(0, 0, 400, 250)  
fill('lightgreen')  
rect(0, 250, 400, 150)

--- /code ---

--- /task ---

--- task ---

**テスト：** プロジェクトを再度実行して、完成した背景を表示します。

![![草色の長方形の上に空色の長方形がある出力領域で、背景を作成する。](images/background.png)`setup()`内の`size()`関数呼び出しで、画面サイズを400ピクセル×400ピクセルに設定しています。

--- /task ---

--- save ---
