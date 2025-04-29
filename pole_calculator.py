pierwszy_bok = input('podaj pierwszy bok do obliczenia: ')
drugi_bok = input('podaj drugi bok do obliczenia: ')
pole = float(pierwszy_bok) * float(drugi_bok)
if float(pierwszy_bok) <= 0 or float(drugi_bok)<= 0 :
    print ("nieprawidłowe wymiary.oba boki musazą być liczbami dodatnimi ")
else:
 print(f"pole czworokąta o bokach {pierwszy_bok}cm i {drugi_bok}cm równa się {pole} cm2 ")
