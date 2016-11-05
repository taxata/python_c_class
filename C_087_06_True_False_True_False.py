# worked with Python 2.7.10
# @ by tChatz
# alpha test

'''
ΚΕΦΑΛΑΙΟ 5ο ΚΛΑΣΣΙΚΟΙ ΑΛΓΟΡΙΘΜΟΙ
Δραστηριότητα 6 / σελίδα 89
Να γράψετε ένα πρόγραμμα σε Python το οποίο θα δέχεται μια λίστα με λογικές
τιμές True/False και στη συνέχεια θα καλεί την συνάρτηση του προηγούμενου ερω-
τήματος, ώστε να τοποθετηθούν τα True πριν από τα False. Στη συνέχεια θα τοπο-
θετεί τις τιμές αυτές εναλλάξ, δηλαδή True, False, True, False, κλπ, εκτελώντας τις
λιγότερες δυνατές συγκρίσεις.
'''

def orderBooleans(aList):
        i, j, n = 0, 0, len(aList) - 1
        while j <= n:
            if aList[j] > False:
                aList[i], aList[j] = aList[j], aList[i] 
                i += 1
                j += 1
            else:
                j += 1

aList = []
item = input('Δωσε λογικές τιμές 1=True, 0=False =')
while item != None :
    aList.append(item)
    item = input('Δωσε λογικές τιμές 1=True, 0=False, None=Stop =')

orderBooleans(aList)
print aList

# Βρες τη θέση του 1ου False
pos = 0
for item in aList:
    if item == 1 :
        pos += 1
    else :
        break
    
# Βάλε ενναλάξ τα στοιχεία 0 & 1
j = 1
for i in range(pos, len(aList)):
    aList[j], aList[i] = aList[i], aList[j]
    j += 2

print aList
