# worked with Python 2.7.10
# @ by tChatz
# alpha test

'''
ΚΕΦΑΛΑΙΟ 6ο ΔΙΑΧΕΙΡΙΣΗ ΑΡΧΕΙΩΝ
Δραστηριότητα 4 / σελίδα 101
Τι πιστεύετε ότι θα συμβεί, όταν θα εκτελεστούν τα παρακάτω σενάρια. Τεκμηριώστε
την άποψή σας.        
'''

my_list = [i**2 for i in range(1,11)]
f = open('output.txt', 'w')
for item in my_list:
    f.write(str(item) + '\n') # δέχεται string όρισμα η write
f.close()
f = open('output.txt', 'r')
print f.readline()
print f.read()
f.close()
    
