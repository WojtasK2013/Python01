liczba = int(input('podaj liczbę'))

dzielniki =[]


for dzielnik in range(1, int(liczba) + 1):
 if int(liczba) % dzielnik == 0:
  print(dzielnik)
  dzielniki.append(dzielnik)
print(dzielniki)

if len(dzielniki) == 2:
  print(f"liczba {liczba} jest liczbą pierwszą")

else:
  print(f"liczba {liczba} nie jest liczbą pierwszą") 


dzielniki.pop()

if sum(dzielniki) == liczba:
  print(f"liczba {liczba} jest liczbą doskonałą")

else:
 print(f"liczba {liczba} nie jest liczbą doskonałą")