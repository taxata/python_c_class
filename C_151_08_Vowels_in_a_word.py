# worked with Python 2.7.10
# @ by tChatz
# alpha test

'''
ΚΕΦΑΛΑΙΟ 8ο ΔΟΜΕΣ ΔΕΔΟΜΕΝΩΝ ΙΙ
Δραστηριότητα 8 /σελίδα 152
Να γράψετε μια συνάρτηση σε Python η οποία θα δέχεται μια λέξη και θα επιστρέ-
φει το πλήθος των φωνηέντων που έχει. Στη συνέχεια, να γράψετε μια δεύτερη
συνάρτηση, η οποία θα δέχεται μια λίστα από λέξεις και θα επιστρέφει τη λέξη με τα
περισσότερα φωνήεντα.
'''
myText = ''' Either the well was very deep or she fell very slowly for she
had plenty of time as she went down to look about her and to
wonder what was going to happen next  First she tried to look
down and make out what she was coming to but it was too dark to
see anything then she looked at the sides of the well and
noticed that they were filled with cupboards and bookshelves
here and there she saw maps and pictures hung upon pegs  She
took down a jar from one of the shelves as she passed it was
labelled ORANGE MARMALADE but to her great disappointment it
was empty she did not like to drop the jar for fear of killing
somebody so managed to put it into one of the cupboards as she
fell past it'''

words = myText.split()
vowels = 'aoieyu'
# Συνάρτηση καταμέτρησης φωνηέντων σε μία λέξη
def countVowels(word):
    count = 0
    for letter in word :
        if letter.lower() in vowels :
            count += 1
    return count

def maxVowelsWord(words):
    xmax = 0
    xword = ''
    for word in words :
        vowels = countVowels(word)
        if vowels > xmax :
            xmax = vowels
            xword = word
    return xword, xmax

