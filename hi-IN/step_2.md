## घास बनाएं

--- task ---

[ PLASS Statch starding ](https://editor.raspberrypi.org/en/projects/target-practice-starter){:target="_blank"} प्रोजेक्ट खोलें।

--- /task ---


--- task ---

**Add** code to draw a green rectangle at the bottom of the screen to represent the grass.

![पृष्ठभूमि बनाने के लिए एक घास के रंग के आयत के ऊपर आकाश-रंगीन आयत वाला आउटपुट क्षेत्र। आयत का ऊपरी बायाँ कोना x=0, y=250 के रूप में चिह्नित है यह आयत का मूल है। चौड़ाई 400 और ऊंचाई 150 के रूप में हाइलाइट की गई है। कोड रेक्ट(0, 250, 400, 150) दिखाया गया है।](images/green-grass.png){:width="400px"}

--- code ---
---
language: python line_numbers: true line_number_start: 17
line_highlights: 21-22
---
def draw(): # Things to do in every frame fill('cyan')  
rect(0, 0, 400, 250)  
fill('lightgreen')  
rect(0, 250, 400, 150) --- /code ---

--- /task ---

--- task ---

**Test:** Run your project to view the background.

![पृष्ठभूमि बनाने के लिए एक घास के रंग के आयत के ऊपर आकाश-रंगीन आयत वाला आउटपुट क्षेत्र।](images/background.png){:width="400px"}

--- /task ---

--- save ---
