﻿# worked with Python 2.7.10
# @ by tChatz
# alpha test


'''
ΚΕΦΑΛΑΙΟ 8ο ΔΟΜΕΣ ΔΕΔΟΜΕΝΩΝ ΙΙ
Δραστηριότητα 1 /σελίδα 151
Να γράψετε ένα πρόγραμμα το οποίο θα διαβάζει μία λέξη και θα εμφανίζει τα γράμ-
ματά της, ένα σε κάθε γραμμή.
'''

word = raw_input('Δώσε μία λέξη=')

# Με διάσχιση
for letter in word:
    print letter

# Με slicing
for i in range(len(word)):
    print word[i]
