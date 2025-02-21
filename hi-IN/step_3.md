## अपना लक्ष्य बनाएँ

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
आपके गेम को पर तीर चलाने के लिए एक लक्ष्य की आवश्यकता है।
</div>
<div>

![लक्ष्य और स्टैंड वाला आउटपुट क्षेत्र।](images/three-circle.png){:width="300px"}

</div>
</div>

### एक त्रिकोणीय स्टैंड बनाएं

--- task ---

Set the fill colour to `brown`.

प्रत्येक कोनों के लिए x और y निर्देशांक का उपयोग करके एक त्रिकोण बनाएं।

![घास पर एक भूरा त्रिकोण और एक आकाश के खिलाफ 150, 350 और 200, 150 और 250, 350 पर लेबल निर्देशांक बिंदुओं के साथ)। कैनवास के कोने भी ऊपर बाएँ x=0, y=0 और नीचे दाईं ओर x=400, y=400 के रूप में लेबल किए गए हैं।](images/stand_coords.png){:width="400px"}

--- code ---
---
language: python line_numbers: true line_number_start: 21
line_highlights: 23-24
---

    fill('lightgreen')  
    rect(0, 250, 400, 150)  
    fill('brown') 
    triangle(150, 350, 200, 150, 250, 350)

--- /code ---

--- /task ---

--- task ---

**Test:** Run your code to see the stand for your target:

![घास पर एक भूरा त्रिकोण और एक आकाश के खिलाफ।](images/target-stand.png){:width="400px"}

--- /task ---

### लक्ष्य वृत्त बनाएं

--- task ---

लक्ष्य का सबसे बड़ा भाग एक नीला ** अपलोड ** है।

भरण रंग को ` > ` पर सेट करें।

इसके केंद्र और चौड़ाई के लिए x और y निर्देशांक के साथ एक वृत्त बनाएं।

![एक भूरा त्रिकोण और घास पर नीला घेरा और एक आकाश के खिलाफ। वृत्त को निर्देशांक x=200, y=200 के साथ केंद्र के रूप में और 170 की वृत्त चौड़ाई के साथ लेबल किया गया है।](images/circle-coords.png){:width="400px"}

--- code ---
---
language: python line_numbers: true line_number_start: 23
line_highlights: 25-26
---

    fill('brown')  
    triangle(150, 350, 200, 150, 250, 350)  
    fill('blue')  
    circle(200, 200, 170)

--- /code ---

--- /task ---

--- task ---

** >:** पहला बड़ा नीला वृत्त देखने के लिए अपना कोड चलाता है।

नीले घेरे को स्टैंड के बाद खींचा गया था इसलिए यह सामने है।

![एक भूरा त्रिकोण और घास पर नीला घेरा और एक आकाश के खिलाफ।](images/blue-circle.png){:width="400px"}

--- /task ---

लक्ष्य एक ही केंद्र निर्देशांक (200, 200) के साथ अलग-अलग आकार के वृत्तों से बना होता है।

--- task ---

लक्ष्य के भीतरी और मध्य भागों के लिए ** > ** रंगीन घेरे।

--- code ---
---
language: python line_numbers: true line_number_start: 25
line_highlights: 27-30
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

**Test:** Run your project to see the target with three coloured circles.

![एक भूरा त्रिकोण जिसमें तीन रंगीन घेरे घास पर और एक आकाश के खिलाफ हैं।](images/three-circles.png){:width="400px"}

--- /task ---

--- save ---
