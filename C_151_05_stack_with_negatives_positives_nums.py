# worked with Python 2.7.10
# @ by tChatz
# alpha test

'''
ΚΕΦΑΛΑΙΟ 8ο ΔΟΜΕΣ ΔΕΔΟΜΕΝΩΝ ΙΙ
Δραστηριότητα 5 /σελίδα 151
Να γράψετε ένα πρόγραμμα το οποίο θα διαβάζει αριθμούς από το πληκτρολόγιο,
μέχρι να δοθεί ο αριθμός 0. Κάθε φορά που θα διαβάζει έναν θετικό αριθμό, θα τον
προσθέτει σε μια στοίβα. Όταν διαβάζει έναν αρνητικό αριθμό θα αφαιρεί τόσους
αριθμούς από τη στοίβα, όσο είναι η τιμή του αριθμού. Ο αλγόριθμος θα τερματίζει
όταν αδειάσει η στοίβα.
'''
# ή όταν δοθεί ο αριθμός 0 μηδέν

stack = []

# Βασικές λειτουργίες στοίβας
def push(stack, item) :
    stack.append(item)
    return stack

def pop(stack) :
    return stack.pop()

def isEmpty(stack) :
    return len(stack) == 0

num = input('Δώσε έναν θετικό ακέραιο αριθμό=')
while num <=0 :
    num = input('Δώσε έναν θετικό ακέραιο αριθμό=')
push(stack,num)

while num != 0 and len(stack) != 0:
    num = input('Δώσε έναν ακέραιο αριθμό=')    
    if num > 0 :
        push(stack,num)
    elif num < 0 :
        if len(stack) >= abs(num):
            for i in range(abs(num)):
                item = pop(stack)
                print item,
        else :
            print 'Not enough items in stack poping the items left'
            for i in range(len(stack)):
                item = pop(stack)
                print item,
        print  
    print stack

