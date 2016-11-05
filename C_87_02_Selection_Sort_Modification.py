
# worked with Python 2.7.10
# @ by tChatz
# alpha test
'''
ΚΕΦΑΛΑΙΟ 5ο ΚΛΑΣΣΙΚΟΙ ΑΛΓΟΡΙΘΜΟΙ

Δραστηριότητα 2 / Σελίδα 87
Να τροποποιήσετε τον αλγόριθμο της ταξινόμησης με επιλογή, ώστε να ταξινομεί
μια λίστα ακεραίων σε φθίνουσα σειρά. Υπάρχει τρόπος να το πετύχετε, χωρίς να
κάνετε καμία απολύτως αλλαγή στον κύριο αλγόριθμο που δίνεται σε αυτή την ενό-
τητα; Σε τι οφείλεται αυτό;
'''
## Αρχικός αλγόριθμος ταξινόμησης με επιλογή
# Εύρεση της θέσης του μικρότερου στοιχείου μιας λίστας
# μεταξύ των θέσεων start & end

def findMinPosition(start, end, List):
    position = start
    for i in range(start, end):
        if List[i] < List[position] :
            position = i
    return position

# Αλγόριθμος ταξινόμησης selection sort
def selectionSortAscending(List):
    position = None
    n = len(List)
    for i in range(0,n):
        position = findMinPosition(i, n, List)
        List[i], List[position] = List[position], List [i]
    return List

# Η λύση στην άσκηση μπορεί να δοθεί με τους εξής τρόπους:
# 1ος Pythonic Way με μικροαλλαγή στον αρχικό κώδικα της ταξινόμησης
def selectionSortDescending(List):
    position = None
    n = len(List)
    for i in range(0,n):
        position = findMinPosition(i, n, List)
        List[i], List[position] = List[position], List [i]
    List = List.reverse()
    return List

# 2ος χωρίς αλλαγή στον αρχικό κώδικα της ταξινόμησης
def findMinMaxPosition(start, end, List, AscDesc):
    # Τροποποίηση της εύρεσης θέσης του min ώστε να βρίσκει και τη θέση του max
    # ανάλογα αν επιθυμούμε αύξουσα (Ascending) ή φθίνουσα (Descending) ταξινόμηση
    position = start
    for i in range(start, end):
        if AscDesc.lower()=='a':
            if List[i] < List[position] :
                position = i
        elif AscDesc.lower()=='d' :
            if List[i] > List[position] :
                position = i
    return position

def selectionSort2(List,AscDesc):
    # Προσθήκη ακόμας μίας παραμέτρου στη συνάρτηση
    position = None
    n = len(List)
    for i in range(0,n):
        position = findMinMaxPosition(i, n, List,AscDesc)
        List[i], List[position] = List[position], List [i]
    return List
