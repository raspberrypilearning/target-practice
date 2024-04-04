
--- question ---
---
legend: Pytanie 3 z 3
---

Okrąg jest rysowany przy użyciu następującego kodu:

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

Które z poniższych obrazów pokazują prawidłową pozycję tego okręgu w obszarze wyjściowym?

--- choices ---

- ( ) ![Zielone kółko wyśrodkowane w prawym dolnym rogu obszaru wyjściowego.](images/bottom-right.png)

  --- feedback ---

  Nie do końca, aby wyśrodkować okrąg w prawym dolnym rogu, współrzędne musiałyby być takie same jak rozmiar ekranu. W tym przykładzie elipsa byłaby ` circle(400, 400, 300)`.

  --- /feedback ---

- ( ) ![Zielone kółko wyśrodkowane pośrodku obszaru wyjściowego.](images/centre.png)

  --- feedback ---

  Nie do końca, aby wyśrodkować okrąg na środku, współrzędne musiałyby być o połowę mniejsze od rozmiaru ekranu. W tym przykładzie ` circle(200, 200, 300)`.

  --- /feedback ---

- (x) ![Zielone kółko wyśrodkowane w lewym górnym rogu obszaru wyjściowego.](images/top-left.png)

  --- feedback ---

  Zgadza się! Ten okrąg jest wyśrodkowany w współrzędnych (0,0), lewym górnym rogu ekranu.

  --- /feedback ---

- ( ) ![Zielone kółko wyśrodkowane w kierunku prawej górnej części obszaru wyjściowego.](images/random-side.png)

  --- feedback ---

  Nie, to koło będzie miało kod ` circle(350, 150, 300)`, który wyśrodkuje go w kierunku prawego górnego rogu ekranu. Współrzędna ` ` określa odległość elipsy na ekranie, a współrzędna `.` określa odległość ekranu od niego do dołu.

  --- /feedback ---

--- /choices ---

--- /question ---
