## अपने तीर को चलाये

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
जब आप क्लिक या टैप करते हैं, तो एक तीर चलती हुई लक्ष्य सर्कल की स्थिति में आ जाएगा। 
</div>
<div>

![लक्ष्य, एक भूरे वृत्त तीर के साथ विभिन्न स्थानों में दिखाई देता है।](images/fire_arrow.gif){:width="300px"}

</div>
</div>

### हर फ्रेम में एक लक्ष्य सर्कल बनाएं

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;"> कंप्यूटर एक के बाद एक कई छवियों को दिखाकर गतिविधि का प्रभाव बनाते हैं। प्रत्येक चित्र को एक <span style="color: #0faeb0; font-weight: bold;"> फ्रेम </span> कहा जाता है।   
</p>

--- task ---

अपने ` debrase_arrow()` फ़ंक्शन को टिप्पणी **# के तहत परिभाषित करें शूट_arrow फ़ंक्शन > ** जाता है।

एक लक्ष्य क्षेत्र के अंदर एक भूरे वृत्त को यादृच्छिक रूप से खींचने के लिए कोड जोड़ें:

![एक आयत जो एक अर्ध पारदर्शी आयत में लक्ष्य क्षेत्र निर्देशांक दिखाता है। लक्ष्य क्षेत्र x=100 और y=100 से x=300 और y=300 के बीच है इसलिए पूरा लक्ष्य और चौड़ा कवर करता है।](images/target_area.png)

--- code ---
---
भाषा: Python फ़ाइल नाम: main.py - Shoot_arrow() line_number: True line_number_start: 7
line_highlights: 8-12
---
# shoot_arrow फ़ंक्शन यहाँ जाता है
def movt_arrow():   
row_x = randint(100, 300) # 100 और >     
के बीच एक यादृच्छिक संख्या स्टोर करें row_y = randint(100, 300) # 100 और >     
के बीच एक यादृच्छिक संख्या स्टोर करें fill('sienna') # रंग भरने के लिए तीर को भूरे रंग    
पर सेट करें circle(row_x, row_y, 15) # random coordinates पर एक छोटा वृत्त बनाएं

--- /code ---

--- /task ---

--- task ---

` > ` फ़ंक्शन पर जाएं और अपने नए ` >_arm> ` फ़ंक्शन को कॉल करें।

--- code ---
---
भाषा: Python फ़ाइल नाम: main.py — draway() line_number: True line_number_start: 31
line_highlights: 33
---

    fill('yellow') # सर्कल भरण के लिए रंग को पीले रंग में सेट करें circle(200, 200, 30) # x, y, width shoot_arrow() का उपयोग करके मध्य वृत्त बनाएं

--- /code ---

--- /task ---

--- task ---

** >:** ? अपना कोड चलाएँ और देखें कि प्रत्येक फ्रेम यादृच्छिक स्थिति में तीर दिखाई देता है।

![भूरे वृत्त तीर के साथ लक्ष्य का एक एनीमेशन विभिन्न स्थानों में दिखाई दे रहा है।](images/fire_arrow.gif)

पुराने तीर के ऊपर पृष्ठभूमि और लक्ष्य बनाया जाएगा। इसका अर्थ है कि आपको एक बार में केवल एक तीर दिखाई देता है।

--- /task ---

### तीर से रंग को हिट करें

` >()` फ़ंक्शन एक पिक्सेल का रंग देता है।

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
चित्र तत्व के लिए छोटा, एक <span style="color: #0faeb0; font-weight: bold;"> > > </span>, एक चित्र के अंदर एक रंगीन डॉट है। चित्र बहुत सारे रंगीन पिक्सलों से बने होते हैं।
</p>

--- task ---

एक ** > variabrass ** जोड़ें जिसे ` >_PLASS ` कहा जाता है जो आपके पूरे कोड में उपयोग किया जा सकता है।

` > ` में कोड जोड़ें तीर के केंद्र में पिक्सेल का रंग और इसे ` >_Pastes ` वेरिएबल में संग्रहीत करें। In order to compare the colours, we need to use the hexadecimal code. This can be done with the `.hex` string.

--- code ---
---
भाषा: Python फ़ाइल नाम: main.py - Shoot_arrow() line_number: True line_number_start: 7
line_highlights: 9, 12
---
# move_arrow फ़ंक्शन यहाँ जाता है
def shoot_arrow(): global heat_color # का उपयोग अन्य functiaceae   
में किया जा सकता है row_x = randint(100, 300) # 100 और >     
के बीच एक यादृच्छिक संख्या स्टोर करें row_y = randint(100, 300) # 100 और 300 के बीच एक यादृच्छिक संख्या स्टोर करें tag_color = get(row_x, row_y).हेक्स # get the heat >      
fill('sienna') # रंग भरने के लिए तीर को भूरे रंग    
पर सेट करें circle(row_x, row_y, 15) # random coordinates पर एक छोटा वृत्त बनाएं

--- /code ---

** >:** ? ` > ` का कोड, रंग ** > ** होना आवश्यक है ` > ampions ` बनाने के लिए कोड हो अन्यथा आप हमेशा तीर के लकड़ी के रंग को बचा लेंगे!

--- /task ---

### जब माउस दबाया जाता है तो रंग प्रिंट करें

कुछ घटनाओं के लिए 'सुनता है' ` debrates 5 ` library, इनमें से एक है press of the mouse button। जब यह पता लगाता है कि बटन दबाया गया है, तो यह ` >_` फ़ंक्शन में दिया गया कोड जो भी कोड चलेगा।

--- task ---

अपने ` Campions_powed()` फ़ंक्शन को टिप्पणी **# के तहत परिभाषित करें mouse_powed फ़ंक्शन > ** जाता है।

लक्ष्य इमोजी प्रिंट करने के लिए कोड जोड़ें? जब माउस पर क्लिक किया जाता है।

--- code ---
---
language: python फ़ाइल नाम: main.py - mouse_powed() line_number: True line_number_start: 5
line_highlights: 6
---

# mouse_powed फ़ंक्शन यहाँ जाता है
def mouse_powed():    
print('?')

--- /code ---

--- /task ---

--- task ---

** >:** ? अपना प्रोजेक्ट चलाएँ।

प्रोजेक्ट मुद्रित होता है? हर बार जब तीर को फिर से बनाया जाता है।

![भूरे वृत्त तीर के साथ लक्ष्य का एक एनीमेशन विभिन्न स्थानों में दिखाई दे रहा है।](images/fire_arrow.gif)

** > blockबग:** ? यदि आप ` >_current ` के बारे में एक संदेश 'परिभाषित नहीं' देख रहे हैं, तो ` >_robow()` पर वापस जाएं और जांचें कि आपने ` Petting_currs ` लाइन को शामिल किया है।

** > blockबग:** ? अल्पविराम और कोष्ठकों के लिए ` > ` लाइन को वास्तव में ध्यान से देखें।

--- /task ---

--- save ---
