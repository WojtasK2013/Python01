print("."*150)

ilość_pytań = int(input("ile chcesz pytań?"))
import random
for i in range(int(ilość_pytań)):
    slowka_polskie = ['biegać','pływać','skakać','pistolet']
    slowka_ang = ['run','swim','jump','pistol']
    p = random.randint(0, len(slowka_ang)-1)
    print( slowka_polskie[p])
    odp = input("   ")
    if odp == slowka_ang[p]:
        print("dobrze")
    else:
        print(f"źle, poprawna odpowiedż to ,,{slowka_ang[p]}''")