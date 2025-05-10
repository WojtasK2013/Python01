print("."*150)
while True:
    if ilość_py2222222tań.isdigit():
       ilość_pytań = (int(input("ile chcesz pytań?")))
       break
    else:
        print("uwaga!zasady są proste.Musisz zamienić słówko na ekranie z polskiego na angielski")
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