print("."*150)
print("uwaga! pierwsze pytanie")
import random
pytanie = random.randint(1, 1)
if pytanie == 1:
    odp1 = input("jak jest ''biegać,, po angielsku  ")
if odp1 == 'run':
    print("dobrze")
else:
    print("źle")
elif pytanie == 2:
    odp_nr2 = input("jak jest ''pływać,, po angielsku  ")
if odp_nr2 == 'swim':
    print("dobrze")
else:
    print("źle")