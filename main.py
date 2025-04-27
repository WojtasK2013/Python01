print('hello')
import random

try:
    liczby = int(input('ile liczb chcesz zgadnąć? '))
    if liczby <= 0:
        print('Liczba prób musi być większa od 0.')
    else:
        for i in range(liczby):
            a = random.randint(1, 10)
            print(f'zgadnij liczbe od 1 do 10: ')
            try:
                podana_liczba = int(input('zgadnij liczbę: '))
                if podana_liczba < 1 or podana_liczba > 10:
                    print('Liczba musi być z przedziału od 1 do 10.')
                if podana_liczba == a:
                    print('zgadłeś')
                else:
                    print('nie zgadłeś')
            except ValueError:
                print('Podana wartość nie jest liczbą całkowitą! Spróbuj ponownie.')
except ValueError:
    print('Podana wartość nie jest liczbą całkowitą! Uruchom program ponownie i podaj poprawną liczbę.')
    pass
print('koniec gry')
