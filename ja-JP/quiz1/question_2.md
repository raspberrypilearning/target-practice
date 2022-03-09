
--- question ---
---
legend: 質問2/3
---

あなたのプロジェクトでは、`if` , `elif`, `else`条件を使って、矢がどの色に着地したかをチェックしましたね。

このコードを実行すると、出力領域には何が表示されるでしょうか？

--- code ---
---
language: python
---

speed = 6

if speed == 7: 
  print('超高速') 
elif speed == 5: 
  print('かなり速い') 
elif speed == 6: 
  print('非常に速い') 
else: 
  print('速度が認識されない！')

--- /code ---

--- choices ---

- (x)`非常に速い`

  --- feedback ---

  そのとおりです！ **speed**変数に`6`という値が代入され、`speed == 6`という条件が**True**となり、`非常に速い`と表示されます。

  --- /feedback ---

- ( ) `速度が認識されない！`

  --- feedback ---

  ちょっと違います、**speed**変数に割り当てられている値を見てください。

  --- /feedback ---

- ( ) 何も表示されない

  --- feedback ---

  違います、elseステートメントを使用すると、常にtrueになることがあります。 そのため、出力が行われます。

  --- /feedback ---

--- /choices ---

--- /question ---
