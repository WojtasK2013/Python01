import json

with open('programowanie_obiektowe/posłuszność.txt',encoding="utf-8",mode='r') as plik:
    linie = plik.readlines()
    print(linie)

with open('dane/katalog_smaczkow.txt',encoding="utf-8",mode='w') as plik:
    linie.append('\nkość')
    plik.writelines(linie)

with open('dane/zmienne.json',encoding="utf-8",mode='r') as plik:
    
    dane = json.load(plik)
    print(dane)
