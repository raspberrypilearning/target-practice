## 背景を作成する

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Your game needs a colourful background.
</div>
<div>

![草色の長方形の上に空色の長方形がある出力領域で、背景を作成する。](images/background.png){:width="300px"}

</div>
</div>

### Open the starter project

--- task ---

Open the [Target practice starter](https://editor.raspberrypi.org/en/projects/target-practice-starter){:target="_blank"} project. The code editor will open in another browser tab.

If you have a Raspberry Pi account, you can click on the **Save** button to save a copy to your **Projects**.

--- /task ---

### Edit the sky

--- task ---

The starter project has some code already written for you.

Click **'Run'** to see a blue filled rectangle drawn from x=`0`, y=`0` (the top of the screen). This `400` x `250` pixels rectangle is the sky.

![灰色の長方形の上に、周囲に黒い境界線がある青い長方形。 The top left corner of the canvas is marked as x=0, y=0 this is the origin of the rectangle. The width is highlighted as 400 and the height as 250. The code rect(0, 0, 400, 250) is shown.](images/sky_stroke.png)`fill()`のコードの後に、`rect()`を左上の座標(`0`,`0`) に合わせて、幅`400`、高さ`250`で描画します。

**Tip:** 💡 Coordinates start from (x=0, y=0) in the top left corner. This might be different to other coordinate systems you have used.

--- /task ---

--- task ---

The sky has been drawn with a black border (stroke).

空を描画する前に`no_stroke()`を追加して、ストロークをオフにします。

--- code ---
---
language: python filename: main.py — draw() line_numbers: true line_number_start: 23
line_highlights: 25
---
def setup():
# Setup your game here

    size(400, 400)  # Width and height of screen
    no_stroke()

--- /code ---

--- /task ---

--- task ---

`fill()`の色を`grass`に変更し、さらに`rect(x, y, 幅, 高さ)`を追加します。

**テスト：** プロジェクトを再度実行して、ストロークがなくなったことを確認します。

--- /task ---

### Draw the grass

--- task ---

**Add** code to draw a green rectangle at the bottom of the screen.

![The output area with a sky-coloured rectangle above a grass-coloured rectangle to create the background. The top left corner of the rectangle is marked as x=0, y=250 this is the origin of the rectangle. The width is highlighted as 400 and the height as 150. The code rect(0, 250, 400, 150) is shown.](images/green-grass.png)`setup()`内の`size()`関数呼び出しで、画面サイズを400ピクセル×400ピクセルに設定しています。

--- code ---
---
language: python filename: main.py — draw() line_numbers: true line_number_start: 18
line_highlights: 26
---
def draw():
# Things to do in every frame

    fill('cyan')  # Set the fill colour for the sky to cyan
    rect(0, 0, 400, 250)  # Draw a rectangle for the sky with these values for x, y, width, height
    fill('lightgreen')  # Set the fill colour for the grass to light green
    rect(0, 250, 400, 150)  # Draw a rectangle for the grass with these values for x, y, width, height

--- /code ---

**テスト：** コードを実行して、結果を確認します。 You don't need to add comments to your code, but they are helpful to remind you what lines of code do.

--- /task ---

--- task ---

**テスト：** プロジェクトを再度実行して、完成した背景を表示します。

![The output area with a sky-coloured rectangle above a grass-coloured rectangle to create the background.](images/background.png){:width="300px"}

--- /task ---

--- save ---
