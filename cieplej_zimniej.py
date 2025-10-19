import random

losowa_liczba = int(random.randint(1,100))
i = 0
odpowiedzi = [0]

while True:
    odległość = 0
    odpowiedź = int(input("jaki będzie strzał?"))
    #print(odpowiedzi)
    if odpowiedź == losowa_liczba:
    
        print(f"Brawo, wygrałeś. Kozak z ciebie jak nikt. Uwierz mi,masz w sobie to coś. Ukończyłeś grę w {i} próbach.")
        break
    else:
        print("no przykro mi, spróbuj jescze raz")
        poprzednia_odp = odpowiedzi[-1]
        odległość = abs(losowa_liczba - odpowiedź)
        odpowiedzi.append(odległość)
        if i>0:
            if odległość < poprzednia_odp:
                print("no Cieplej")
            else:
                print("przyłóż się,zimniej")
        i = i + 1

                       