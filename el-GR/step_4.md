## Ρίξε το βέλος σου

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Τώρα ήρθε η ώρα να προσθέσεις ένα βέλος που κινείται τυχαία στην περιοχή του στόχου.
</div>
<div>

![Ο στόχος, με ένα καφέ κυκλικό βέλος να εμφανίζεται σε διάφορες θέσεις.](images/fire_arrow.gif){:width="300px"}

</div>
</div>

--- task ---

Βρες το σχόλιο **#Η συνάρτηση shoot_arrow πηγαίνει εδώ** και από κάτω πρόσθεσε κώδικα για να ορίσεις τη συνάρτηση `shoot_arrow()`.

Πρόσθεσε μία μικρή έλλειψη με τη συνάρτηση `ellipse()` στο κέντρο της οθόνης για να απεικονίσει το βέλος.

--- code ---
---
language: python 
filename: main.py — shoot_arrow() 
line_numbers: true 
line_number_start: 10
line_highlights: 11-12
---

#Η συνάρτηση shoot_arrow πηγαίνει εδώ
def shoot_arrow():   
  ellipse(200, 200, 15, 15)

--- /code ---

--- /task ---

--- task ---

Πήγαινε στον κώδικα `draw()` που δημιουργεί τον στόχο και πρόσθεσε κώδικα στο τέλος για να ορίσεις τη συνάρτηση `fill()` ως `wood` (ξύλο, άρα χρώμα καφέ), και μετά κάλεσε τη νέα σου συνάρτηση `shoot_arrow()`.

--- code ---
---
language: python 
filename: main.py — draw() 
line_numbers: true 
line_number_start: 41
line_highlights: 44-45
---

  fill(bullseye)    
  ellipse(200, 200, 30, 30)

  fill(wood)   
  shoot_arrow()

--- /code ---

--- /task ---

--- task ---

**Δοκιμή:** Εκτέλεσε τον κώδικά σου και δες το βέλος να εμφανίζεται στο κέντρο του στόχου.

![Ο στόχος στο φόντο με ένα καφέ κυκλικό βέλος πάνω του.](images/arrow-middle.png)

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;"> Παιχνίδια στον υπολογιστή, βίντεο και κινούμενα σχέδια δημιουργούν το εφέ της κίνησης προβάλλοντας πολλές εικόνες τη μία μετά την άλλη. Κάθε εικόνα ονομάζεται <span style="color: #0faeb0; font-weight: bold;"> καρέ </span>. Η ταχύτητα με την οποία αλλάζει η εικόνα ονομάζεται <span style="color: #800080;"> ρυθμός καρέ </span> και μετριέται σε <span style="color: #800080;">fps</span> ή καρέ ανά δευτερόλεπτο.  
</p>

Η γραμμή `frame_rate(2)` στη συνάρτηση `setup()` ορίζει τον ρυθμό καρέ σε 2 καρέ ανά δευτερόλεπτο.

Η συνάρτηση `draw()` καλείται σε κάθε καρέ. Θα σχεδιάζεις το βέλος σε τυχαία θέση κάθε φορά που καλείται η συνάρτηση `draw()`.

Το υπόβαθρο και ο στόχος θα σχεδιάζονται πάνω από το παλιό βέλος. Αυτό σημαίνει ότι βλέπεις μόνο ένα βέλος κάθε φορά.

--- task ---

Βρες τις δηλώσεις εισαγωγής `import`, στην αρχή του κώδικά σου, θα χρησιμοποιήσεις το `randint` από τη βιβλιοθήκη `random`.

--- code ---
---
language: python 
filename: main.py 
line_numbers: true
line_number_start: 3
---

#Εισαγωγή του κώδικα της βιβλιοθήκης
from p5 import *    
from math import *    
from random import randint

--- /code ---

--- /task ---

--- task ---

Πήγαινε στη συνάρτηση `shoot_arrow()` και πρόσθεσε δύο νέες μεταβλητές `arrow_x` και `arrow_y` για να αποθηκεύσεις τυχαίους αριθμούς μεταξύ `100` και `300`.

Αυτό θα κάνει μερικές βολές να χάσουν τον στόχο, αλλά να βρίσκονται εντός των ορίων του παιχνιδιού σου.

Άλλαξε την `ellipse()` για να χρησιμοποιήσεις τις νέες μεταβλητές για να τοποθετήσεις το βέλος σου.

![Ένα ορθογώνιο που δείχνει τις συντεταγμένες της περιοχής στόχου σε ένα ημιδιαφανές ορθογώνιο.](images/target_area.png)

--- code ---
---
language: python 
filename: main.py — shoot_arrow() 
line_numbers: true 
line_number_start: 10
line_highlights: 12-14
---

#Η συνάρτηση shoot_arrow πηγαίνει εδώ
def shoot_arrow():    
  arrow_x = randint(100, 300)   
  arrow_y = randint(100, 300)    
  ellipse(arrow_x, arrow_y, 15, 15) #Ενημέρωσε με τυχαίες συντεταγμένες

--- /code ---

--- /task ---

### Μάθε το χρώμα που χτυπά το βέλος

Η συνάρτηση `get()` επιστρέφει το χρώμα ενός εικονοστοιχείου.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Ένα <span style="color: #0faeb0; font-weight: bold;">pixel</span>, συντομογραφία (στα αγγλικά) για το στοιχείο εικόνας (picture element) και στα ελληνικά εικονοστοιχείο, είναι μια μονή έγχρωμη κουκκίδα μέσα σε μια εικόνα. Οι εικόνες αποτελούνται από πολλά έγχρωμα εικονοστοιχεία.
</p>

--- task ---

Πρέπει να αποθηκεύσεις το χρώμα στο οποίο στοχεύει το βέλος πριν σχεδιάσεις ένα βέλος πάνω του.

Πρόσθεσε κώδικα για να αποθηκεύσεις το `hit_color`. Χρησιμοποίησε τη συνάρτηση `get()`, για να λάβεις το χρώμα του εικονοστοιχείου στις συντεταγμένες `arrow_x` και `arrow_y` — το κέντρο του βέλους.

--- code ---
---
language: python 
filename: main.py — shoot_arrow() 
line_numbers: true 
line_number_start: 10
line_highlights: 14
---

#Η συνάρτηση shoot_arrow πηγαίνει εδώ
def shoot_arrow():    
  arrow_x = randint(100, 300)    
  arrow_y = randint(100, 300)    
  hit_color = get(arrow_x, arrow_y) #Αποθήκευσε το χρώμα πριν σχεδιάσεις το βέλος   
  ellipse(arrow_x, arrow_y, 15, 15)

--- /code ---

**Συμβουλή:** Ο κώδικας για να μάθεις το χρώμα και να το αποθηκεύσεις πρέπει να βρίσκεται **πριν από** τον κώδικα που σχεδιάζει την έλλειψη, διαφορετικά θα αποθηκεύεις πάντα το χρώμα του ξύλου του βέλους!

--- /task ---

Η βιβλιοθήκη `p5` «ακούει» ορισμένα συμβάντα, ένα από αυτά είναι το πάτημα του κουμπιού του ποντικιού. Όταν εντοπίσει ότι το κουμπί έχει πατηθεί, θα εκτελέσει όποιον κώδικα έχει δοθεί στη συνάρτηση `mouse_pressed()`.

--- task ---

Βρες το σχόλιο **#Η συνάρτηση mouse_pressed πηγαίνει εδώ** και από κάτω πρόσθεσε κώδικα για να ορίσεις τη συνάρτηση `mouse_pressed()`.

Πρόσθεσε κώδικα για να εμφανίσεις τις ποσότητες κόκκινου, πράσινου και μπλε στο εικονοστοιχείο στο οποίο προσγειώνεται το βέλος.

--- code ---
---
language: python 
filename: main.py - mouse_pressed() 
line_numbers: true 
line_number_start: 8
line_highlights: 9-10
---

#Η συνάρτηση mouse_pressed πηγαίνει εδώ
def mouse_pressed():    
  print( red(hit_color), green(hit_color), blue(hit_color) )

--- /code ---

--- /task ---

--- task ---

Έχεις ορίσει δύο συναρτήσεις `shoot_arrow()` και `mouse_pressed()`, και οι δύο αυτές συναρτήσεις πρέπει να χρησιμοποιούν τη μεταβλητή `hit_color`.

Μια μεταβλητή που χρειάζεται να χρησιμοποιείται σε ολόκληρη την έκταση ενός προγράμματος είναι γνωστή ως **καθολική μεταβλητή** (global). Πρόσθεσε κώδικα στη συνάρτηση `shoot_arrow()` για να μετατρέψεις το `hit_color` σε καθολική μεταβλητή:

--- code ---
---
language: python 
filename: main.py - shoot_arrow() 
line_numbers: true 
line_number_start: 12
line_highlights: 14
---

#Η συνάρτηση shoot_arrow πηγαίνει εδώ
def shoot_arrow():    
  global hit_color #Μπορεί να χρησιμοποιηθεί και σε άλλες συναρτήσεις     
  arrow_x = randint(100, 300)     
  arrow_y = randint(100, 300)     
  hit_color = get(arrow_x, arrow_y) #Σώσε το χρώμα πριν σχεδιάσεις το βέλος     
  ellipse(arrow_x, arrow_y, 15, 15)

--- /code ---

--- /task ---

--- task ---

**Δοκιμή:** Τρέξε το έργο σου. Το βέλος σχεδιάζεται ξανά σε τυχαίες συντεταγμένες.

Το έργο λαμβάνει το `hit_color` κάθε φορά που επανασχεδιάζεται το βέλος κι εμφανίζει την τιμή χρώματος στην περιοχή εξόδου κάτω από τον στόχο.

![Ο στόχος, με ένα καφέ κυκλικό βέλος να εμφανίζεται σε διάφορες θέσεις.](images/fire_arrow.gif)

**Εντοπισμός σφαλμάτων:** Εάν βλέπεις ένα μήνυμα σχετικά με το ότι το `hit_colour` δεν έχει οριστεί, τότε πρέπει να επστρέψεις στο `shoot_arrow()` και να ελέγξεις ότι έχεις την γραμμή `global hit_color`.

**Εντοπισμός σφαλμάτων:** Έλεγξε πολύ προσεκτικά τη γραμμή `print` για κόμματα και παρενθέσεις.

--- /task ---

--- save ---

