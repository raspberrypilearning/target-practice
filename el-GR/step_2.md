## Δημιούργησε ένα υπόβαθρο

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Ο ουρανός και το γρασίδι φτιάχνονται γράφοντας κώδικα για να σχεδιάσεις χρωματιστά ορθογώνια.
</div>
<div>

![Η περιοχή εξόδου με ένα ορθογώνιο στο χρώμα του ουρανού πάνω από ένα ορθογώνιο χρώματος γρασιδιού για τη δημιουργία του φόντου.](images/background.png){:width="300px"}

</div>
</div>

### Open the starter project

--- task ---

Άνοιξε το [αρχικό έργο Τοξοβολίας](https://trinket.io/python/1e11252c65){:target="_blank"}.

Εάν έχεις λογαριασμό Trinket, μπορείς να κάνεις κλικ στο κουμπί **Remix** για να αποθηκεύσεις ένα αντίγραφο στη βιβλιοθήκη `My Trinkets`.

--- /task ---

### Edit the sky

--- task ---

[[[p5-processing-library]]]

Click **'Run'** to see a blue filled rectangle drawn from x=`0`, y=`0` (the top of the screen). This `400` x `250` pixels rectangle is the sky.

![A blue rectangle with a black border around it, above a grey rectangle. The top left corner of the canvas is marked as x=0, y=0 this is the origin of the rectangle. The width is highlighted as 400 and the height as 250. The code rect(0, 0, 400, 250) is shown.](images/sky_stroke.png){:width="400px"}

**Tip:** 💡 Coordinates start from (x=0, y=0) in the top left corner. This might be different to other coordinate systems you have used.

--- /task ---

--- task ---

def draw():     
#Πράγματα που θα συμβαίνουν σε κάθε καρέ     
sky = color(92, 204, 206) #Κόκκινο = 92, Πράσινο = 204, Μπλε = 206     
grass = color(149, 212, 122)     
wood = color(145, 96, 51)     
outer = color(0, 120, 180)

fill(sky)

--- code ---
---
language: python filename: main.py — setup() line_numbers: true line_number_start: 11
line_highlights: 25
---
Η κλήση της συνάρτησης `size()` στο `setup()` ορίζει το μέγεθος της οθόνης σε 400 pixel επί 400 pixel.
# Setup your game here
  [[[p5-coordinates]]]

--- /code ---

--- /task ---

--- task ---

**Run** your code again and notice 👀 that the border (stroke) has now disappeared.

--- /task ---

### Draw the grass

--- task ---

**Add** code to draw a green rectangle at the bottom of the screen.

![The output area with a sky-coloured rectangle above a grass-coloured rectangle to create the background. The top left corner of the rectangle is marked as x=0, y=250 this is the origin of the rectangle. The width is highlighted as 400 and the height as 150. The code rect(0, 250, 400, 150) is shown.](images/green-grass.png){:width="400px"}

--- code ---
---
language: python filename: main.py — draw() line_numbers: true line_number_start: 17
line_highlights: 26
---
{:width="300px"}
# Things to do in every frame
  global wood sky = color(92, 204, 206) # Red = 92, Green = 204, Blue = 206 grass = color(149, 212, 122) wood = color(145, 96, 51) outer = color(0, 120, 180)

  fill(sky)     
rect(0, 0, 400, 250)     
fill(grass) # Set the fill color to grass rect(0, 250, 400, 150) # x, y, width, height

--- /code ---

**Tip:** 💡 We have added comments to our code, like `# Set the fill color to grass`, to tell you what it does. You don't need to add these comments to your code, but they can be helpful to remind you what lines of code do.

--- /task ---

--- task ---

outer = color(0, 120, 180)

![The output area with a sky-coloured rectangle above a grass-coloured rectangle to create the background.](images/background.png)no_stroke()   
fill(sky)   
rect(0, 0, 400, 250) #x, y, πλάτος, ύψος

--- /task ---

