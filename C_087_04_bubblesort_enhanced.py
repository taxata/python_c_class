﻿# worked with Python 2.7.10
# @ by tChatz
# alpha test


'''
ΚΕΦΑΛΑΙΟ 5ο ΚΛΑΣΣΙΚΟΙ ΑΛΓΟΡΙΘΜΟΙ
Δραστηριότητα 4 / Σελίδα 87 (βελτιωμένη φυσαλίδα)
Να δώσετε τη βελτιωμένη έκδοση του αλγορίθμου ταξινόμησης ευθείας ανταλλαγής
η οποία τερματίζει, όταν διαπιστώσει ότι η λίστα είναι ταξινομημένη, ώστε να απο-
φεύγονται περιττές συγκρίσεις.
Υπόδειξη: Χρησιμοποιήστε μια λογική μεταβλητή η οποία θα αλλάζει τιμή, αν υπάρ-
χουν τουλάχιστον δύο στοιχεία τα οποία δεν βρίσκονται στην επιθυμητή σειρά, κα-
θώς η “φυσαλίδα ανεβαίνει στην επιφάνεια”.
'''
# Κλασσική Φυσαλίδα
def bubblesort(aList):
    for i in range(len(aList)):
        for j in range(len(aList) - 1, i , -1):
            if aList[j] < aList[j-1] :
                aList[j], aList[j-1] = aList[j-1], aList[j]
                

# Βελτιωμένη Φυσαλίδα
def shortBubblesort(aList):
        done = False
        i = 0
        while i < len(aList) - 1  and done == False :
            done = True
            for j in range(len(aList) - 1, i , -1):
                if aList[j] < aList[j-1] :
                    aList[j], aList[j-1] = aList[j-1], aList[j]
                    done = False
                
