print("."*150)
ilość_pytań = input("ile chcesz pytań?")
print("uwaga! pierwsze pytanie")
import random
for i in range(int(ilość_pytań)):
 pytanie = random.randint(1, 2)
if pytanie == 1:
    odp = input("jak jest ''biegać,, po angielsku  ")
if odp == 'run':
    print("dobrze")
else:
    print("źle")
if pytanie == 2:
    odp = input("jak jest ''pływać,, po angielsku  ")
if odp == 'swim':
    print("dobrze")
else:
    print("źle")