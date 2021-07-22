## Set up your screen

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
In this step you will code the window which will display your game by drawing the background sky and grass. 
</div>
<div>
Image, gif or video showing what they will achieve by the end of the step. ![](images/image.png){:width="300px"}
</div>
</div>

<mark>define SKY_BLUE constant, Draw sky and run(), color theory (collapse), coordinates (collapse) for rect</mark>
--- task ---

Open the [Python archery starter](https://trinket.io/python/06ee0e5643) project. Trinket will open in another browser tab.

[[[working-offline]]]

--- /task ---

The first line of the script ```#!/bin/python3``` tells Trinket that you are using Python 3 (the latest version). The import lines tell Python that you are going to use some code you didn’t write, by importing **modules** of code that you can call upon to do specific things.

Here, we are importing **everything** from the p5 library and the math library by using the ```*``` symbol. This is sometimes called a **wildcard** and it pretty much just means 'all'. So, we are asking python to import **all** from the p5 and math libraries for use in our code. We are only importing one part of the ```time``` module, the **package** called ```sleep``` which allows us to put timed breaks in our code. 

--- task ---
In the main.py file of your Trinket, on the last line, type:
```def setup():``` and hit enter.

You should see the cursor move down a line and leave a small gap or **indent** at the beginning of the next. **Don't remove the indent!** It's very important to the structure of our code!

--- /task ---

With this line, we have started to **define a function** called ```setup```. This function is always called first in python processing by the final command of every script: ```run()```. The ```setup``` function usually contains all the things the script needs to do to prepare the context for your code to run. Things like set the **framerate** for animations, or create a game window that is 400x400 pixels. 

--- task ---
Leaving the indent created by Trinket, type ```frame_rate(5)``` and hit Enter. You should see Trinket keep the same level of **indentation** as the previous line. 

This line sets how many **frames** per second our animation will contain. The higher the number, the more frames. More frames means a smoother and **faster** animation. 

We are using ```5``` as our value because we want our player to be able to have a chance of firing their arrow at the right time. We could increase the framerate, but it would mean our 'arrow' would be moving much more quickly (and make it nearly impossible to be accurate). With this value, they will have 1/5th of a second to fire while the arrow is still.
--- /task ---

--- task ---
Leaving the indent created, type ```size(400, 400)``` and hit Enter. You should see Trinket keep the same level of **indentation** as the previous line. 

This line defines how big our game window will be. In this instance it will create a window with the dimensions of 400 pixels by 400 pixels. 
--- /task ---

--- task ---
Leaving the indent created, type ```global shoot``` and hit Enter. You should see Trinket keep the same level of **indentation** as the previous line, and the word ```global``` should turn purple. 

This line has created a **global variable** called ```shoot```. In python, a variable is used to store values. 
--- /task ---

Normally, when you create a variable inside a function as we have done here, that variable is **local** and can **only be used inside that function**.

To create a **global variable** inside a function, you can use the ```global``` keyword. If you create a variable using this keyword, the variable has global **scope**. Which means it is available **everywhere in your script**.

--- task ---
Leaving the indent created, type ```shoot = False``` and hit Enter. You should see Trinket keep the same level of **indentation** as the previous line, and the word ```False``` will turn purple.

This line has set the value of our global variable to be ```False```. 

--- collapse ---
---
title: ```False``` keyword and Boolean
---
The Boolean data type has only two values: **true** or **false**. These values are used to control the flow of the execution of programs. 

In python, we use the values ```True``` and ```False```. The ```False``` keyword is the same as ```0``` or ```off```. The ```True``` keyword is the same as ```1``` or ```on```.
--- /collapse ---

--- /task ---

The code you have just typed is the ```setup``` function for our game. When the program runs, it will now set the animation frame rate to 5 frames per second, create a window 400 pixels wide by 400 pixels high, create a global variable called shoot (which we will need later) and set it to False. 




--- save ---