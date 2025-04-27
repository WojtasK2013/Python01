print('hello')
import random

liczby = input('ile liczb chcesz zgadnąć? ')
liczby = int(liczby)
for i in range(liczby):
    a = random.randint(1, 10)
    print (f'zgadnij liczbe od 1 do 10: ')
    podana_liczba = int(input('zgadnij liczbę: '))
    if podana_liczba == a:
        print('zgadłeś')
pass
print('koniec gry')