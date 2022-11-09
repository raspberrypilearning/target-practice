
--- question ---
---
legend: Ερώτηση 2 από 3
---

Στο έργο σου, χρησιμοποίησες τις συνθήκες `if` , `elif`και `else` για να ελέγξεις σε ποιο χρώμα προσγειώθηκε το βέλος.

In the example below, a variable called `speed` has the number `6` stored in it. When this `if` statement is run, what would be printed in the output area?

--- code ---
---
language: python
---
speed = 6

if speed == 7: print('Υπερβολικά γρήγορα') elif speed == 5: print('Αρκετά γρήγορα') elif speed == 6: print('Πολύ γρήγορα') else: print('Δεν αναγνωρίστηκε η ταχύτητα!')

--- /code ---

--- choices ---

- (x) `Πολύ γρήγορα`

  --- feedback ---

  Αυτό είναι το σωστό! Στη μεταβλητή **speed** έχει δοθεί η τιμή `6`, η οποία κάνει την συνθήκη `speed == 6` **Αληθή** και εμφανίζει το μήνυμα `Πολύ γρήγορα`.

  --- /feedback ---

- ( ) `Δεν αναγνωρίστηκε η ταχύτητα!`

  --- feedback ---

  Όχι ακριβώς, κοίταξε την τιμή που έχει δοθεί στη μεταβλητή **speed**.

  --- /feedback ---

- ( ) Τίποτα δεν εμφανίζεται

  --- feedback ---

  Try again, `else` is used as a final option for when all the above conditions are false. Look through the conditions again, are any of the conditions true?

  --- /feedback ---

--- /choices ---

--- /question ---
