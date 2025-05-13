print("."*150)
punkty = 0
ilość_pytań = int(input("ile chcesz pytań?"))
import random
for i in range(int(ilość_pytań)):
    slowka_polskie = ['biegać','pływać','skakać','pistolet','auto','drzwi','samolot','szyny','budynek','bank']
    slowka_ang = ['run','swim','jump','pistol','car','door','plane','rails','building','bank']
    p = random.randint(0, len(slowka_ang)-1)
    print( slowka_polskie[p])
    odp = input("   ")
    if odp == slowka_ang[p]:
        print("dobrze")
        punkty =punkty+1
    else:
        print(f"źle, poprawna odpowiedż to ,,{slowka_ang[p]}''")
print(f"zdobyłeś {punkty} na {ilość_pytań} punktów")
ułamek = punkty/ ilość_pytań
procent = ułamek * 100
print(f"czyli {procent:.0f}% poprawnych odpowiedzi")