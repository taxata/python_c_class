# worked with Python 2.7.10
# @ by tChatz
# alpha test

'''
ΚΕΦΑΛΑΙΟ 5ο ΚΛΑΣΣΙΚΟΙ ΑΛΓΟΡΙΘΜΟΙ
Δραστηριότητα 10 / σελίδα 89
Να γράψετε ένα πρόγραμμα το οποίο θα διαβάζει από το χρήστη δυο λίστες αριθ-
μών Α και Β και θα ταξινομεί σε αύξουσα σειρά τους αριθμούς της λίστας Α. Στη
συνέχεια θα εμφανίζει πόσοι από τους αριθμούς της λίστας Β εμφανίζονται στην
λίστα Α.
Υπόδειξη: Να θεωρήσετε ότι οι αριθμοί της λίστας Β είναι όλοι διαφορετικοί μεταξύ
τους. Επίσης, να εκμεταλλευτείτε το γεγονός ότι η λίστα Α είναι ταξινομημένη σε
αύξουσα σειρά.     
'''
def fill_a_List():
    aList = []
    item = input('Δώσε έναν ακέραιο=')
    while item != None :
        aList.append(item)
        item = input('Δώσε έναν ακέραιο (None to stop) =')
    return aList

print 'Input LIST A'
A = fill_a_List()
print 'Input LIST B'
B = fill_a_List()

print 'A=',A
print 'B=',B

# Κλασσική Φυσαλίδα
def bubblesort(aList):
    for i in range(len(aList)):
        for j in range(len(aList) - 1, i , -1):
            if aList[j] < aList[j-1] :
                aList[j], aList[j-1] = aList[j-1], aList[j]

# Ταξινόμηση Λίστας Α
bubblesort(A)
# Δυαδική Αναζήτηση
def binarySearch( array, key ) :
    first = 0
    last = len(array)-1
    found = False
    while first <= last and not found :
        mid = ( first + last ) // 2
        if array[ mid ] == key :
            found = True
        elif array[ mid ] < key :
            first = mid + 1
        else :
            last = mid-1
    return found


count = 0
for item in B :
    if binarySearch(A,item) :
        count += 1
print 'Βρήκα %d στοιχεία της λίστας Β να περιέχονται στη λίστα Α ' % count
