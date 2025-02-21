## Δημιούργησε ένα υπόβαθρο

--- task ---

Άνοιξε το [αρχικό έργο Τοξοβολίας](https://trinket.io/python/1e11252c65){:target="_blank"}.

--- /task ---

--- task ---

Το αρχικό έργο έχει ήδη έτοιμο κώδικα για να εισαγάγεις τη βιβλιοθήκη `p5`, θα χρησιμοποιήσεις αυτήν τη βιβλιοθήκη για να δημιουργήσεις το παιχνίδι τοξοβολίας σου.

![The output area with a sky-coloured rectangle above a grass-coloured rectangle to create the background. The top left corner of the rectangle is marked as x=0, y=250 this is the origin of the rectangle. The width is highlighted as 400 and the height as 150. The code rect(0, 250, 400, 150) is shown.](images/green-grass.png){:width="400px"}

--- code ---
---
language: python line_numbers: true line_number_start: 17
line_highlights: 25
---
def draw(): # Things to do in every frame fill('cyan')  
rect(0, 0, 400, 250)  
fill('lightgreen')  
rect(0, 250, 400, 150)

--- /code ---

--- /task ---

--- task ---

def draw():     
#Πράγματα που θα συμβαίνουν σε κάθε καρέ     
sky = color(92, 204, 206) #Κόκκινο = 92, Πράσινο = 204, Μπλε = 206     
grass = color(149, 212, 122)     
wood = color(145, 96, 51)     
outer = color(0, 120, 180)

![The output area with a sky-coloured rectangle above a grass-coloured rectangle to create the background.](images/background.png){:width="400px"}

--- /task ---

--- save ---
