
--- question ---
---
legend: 3 प्रश्नों में तीसरा
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

- ( ) ![आउटपुट क्षेत्र के निचले-दाएँ कोने में केंद्रित एक हरा वृत्त।](images/bottom-right.png)

  --- feedback ---

  नहीं, निचले-दाएँ कोने में वृत्त को केंद्र में लाने के लिए, निर्देशांक स्क्रीन के आकार के समान होने चाहिए। In this example, the ellipse would be `circle(400, 400, 300)`.

  --- /feedback ---

- ( ) ![आउटपुट क्षेत्र के मध्य में केंद्रित एक हरा वृत्त।](images/centre.png)

  --- feedback ---

  बिल्कुल नहीं, मध्य में वृत्त को केंद्रित करने के लिए, निर्देशांक स्क्रीन के आकार का आधा होना चाहिए। In this example, `circle(200, 200, 300)`.

  --- /feedback ---

- (x) ![आउटपुट क्षेत्र के ऊपरी-बाएँ कोने में केंद्रित एक हरा वृत्त।](images/top-left.png)

  --- feedback ---

  यह सही है! यह वृत्त निर्देशांक (0,0) पर केंद्रित है, जो स्क्रीन का ऊपरी-बायाँ कोना है।

  --- /feedback ---

- ( ) ![आउटपुट क्षेत्र के ऊपरी-दाईं ओर केंद्रित एक हरा वृत्त।](images/random-side.png)

  --- feedback ---

  No, this circle would have code of `circle(350, 150, 300)` to centre it towards the top-right of the screen. `x` निर्देशांक यह है कि कितनी दूर स्क्रीन पर दीर्घवृत्त है, और `y` निर्देशांक है कि स्क्रीन कितनी नीचे है।

  --- /feedback ---

--- /choices ---

--- /question ---
