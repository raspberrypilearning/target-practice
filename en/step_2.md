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

The next step in setting up our game window is to draw the sky and grass backdrop. We will do this by creating two rectangles with the ```draw``` function and colouring them blue and green.

--- task ---
Under the ```setup function```, leave a blank line by pressing Enter and **remove the indent** so that your cursor is all the way against the left edge of the coding window, ready to start defining a new function.

--- collapse ---
---
title: Indentation in python
---
Indentation refers to the spaces at the beginning of a code line, which are usually in blocks of **four spaces**. You can create an indent by pressing the ```Tab``` key on your keyboard while typing in the code window.

In other programming languages the indentation in code is for making it easier to read, but in Python, the indentation is very important as Python uses indentation to indicate a 'block' of code.

Everything which is indented in the block above is part of the ```setup``` function. Once the indentation ends, so does the function. 
--- /collapse ---

On this line type ```def draw():``` and press Enter. You'll see that an indentation is provided for your function again.

--- /task ---

The ```draw()``` function is the second function called by ```run()``` after ```setup()```. It tells the program what to create in the window we just coded. 

Now we need to create some colour variables. This will allow us to use the colour names to draw them rather than complicated **tuples**.

--- task ---
On the next line, type ``` global SKY_BLUE,``` and press Enter. This line creates the global variable for our sky colour, ```SKY_BLUE```.
--- /task ---

--- task ---
Now type ```SKY_BLUE = color(92, 204, 206)``` and press Enter. This line sets our new ```SKY_BLUE``` variable using a colour tuple. 

--- collapse ---
---
title: Colour tuples in python
---
All the colours you can see on your computer screen are made by combining different levels of Red, Blue and Green. 

These levels can be set to any value from ```0``` to ```255```, and combining different levels of these three colours can make up to 16 million different variations! 

To define the colours in python we use **tuples**, or sets of three numbers in brackets separated by commas. The first number in the tuple represents the Red value, the second is the Green value and the third value is for Blue - this is why we call it an **RGB** colour palette.

The colour we have created above is a light blue colour. It has much less red than blue and green, which we can see from the tuple: Red = 92
Green = 204
Blue = 206 

You can see a whole list of RGB colour values [here](https://image-color.com/color-picker#5CCCCE).

--- /collapse ---

--- save ---