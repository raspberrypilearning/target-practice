## What colour did you hit?

Next, you will add some code to get the colour at the location of the arrow.

### Get the colour hit by the arrow

--- task ---

**Debuggen:** 🐞 Als je een bericht ziet over `raak_kleur` die 'niet gedefinieerd' is, ga dan terug naar `draw()` en controleer de regel waarin `raak_kleur` als globale variabele gedeclareerd is.

Add code to `get` the colour at the centre of the arrow ,and store it in the `hit_colour` variable.


--- code ---
---
language: python line_numbers: true line_number_start: 9
line_highlights: 10, 13, 14
---
def shoot_arrow(): global hit_colour  
arrow_x = randint(100, 300)  
arrow_y = randint(100, 300) hit_colour = get(arrow_x, arrow_y).hex print(hit_colour) fill('brown') circle(arrow_x, arrow_y, 15)

--- /code ---

**Debug:** 🐞 Zorg ervoor dat je de `.hex` string hebt gebruikt voor **jouw** cirkelkleuren.

--- /task ---

--- task ---

**Test:** 🔄 Voer je project uit. **Debuggen:** 🐞 Zorg ervoor dat je de juiste kleurnaam hebt ingevoerd voor **jouw** cirkels.

--- /task ---

### Run code when the mouse is pressed

--- task ---

Comment out the line that prints the colour. This means it will not run.

--- code ---
---
language: python line_numbers: true line_number_start: 13
line_highlights: 14
---

    hit_colour = get(arrow_x, arrow_y).hex
    # print(hit_colour)
    circle(arrow_x, arrow_y, 15)

--- /code ---

--- /task ---

--- task ---

Add code to print the target emoji 🎯 **when the mouse is clicked**.

--- code ---
---
language: python line_numbers: true line_number_start: 5
line_highlights: 6-7
---
# De mouse_pressed functie komt hier
def mouse_pressed():    
print('🎯')

--- /code ---

--- /task ---

**Test:** 🔄 Voer je project uit. You should see the 🎯 character printed when you click the mouse on the target.

![target emoji printed when mouse clicked](images/target_printed.gif) --- /task ---

--- save ---