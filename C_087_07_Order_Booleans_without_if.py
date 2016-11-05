# worked with Python 2.7.10
# @ by tChatz
# alpha test

'''
ΚΕΦΑΛΑΙΟ 5ο ΚΛΑΣΣΙΚΟΙ ΑΛΓΟΡΙΘΜΟΙ
Δραστηριότητα 7 / σελίδα 89
Ας υποθέσουμε ότι σας δίνεται μια λίστα στην Python η οποία περιέχει λογικές τιμές
True/False εναλλάξ. Επίσης, το πλήθος των True είναι ίσο με το πλήθος των False.
Να γράψετε αλγόριθμο, σε Python, ο οποίος δεδομένης της παραπάνω δομής της
λίστας, θα τοποθετεί τα True πριν από τα False εκτελώντας, τις λιγότερες δυνατές
μετακινήσεις. Δεν επιτρέπεται να κάνετε καμία σύγκριση ούτε να χρησιμοποιήσετε
τη δομή if. Θεωρήστε ότι το πρώτο στοιχείο της λίστας έχει την τιμή True.          
'''

aList = [True, False, True, False, True, False, True, False,
         True, False, True, False, True, False, True, False, True, False,
         True, False, True, False, True, False, True, False, True, False]

def orderBoolean(aList):
    n = len(aList)
    mid = n // 2
    for i in range(1, mid, 2) :
        aList[i], aList[n-i-1] = aList[n-i-1], aList[i]

orderBoolean(aList)
