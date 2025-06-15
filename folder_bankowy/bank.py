import json

with open('folder_bankowy/rachunki_bankowe.json',encoding="utf-8",mode='r') as plik:
    rachunki = json.load(plik)

wyszukaj_konto = input("jakie konto chcesz wyszukać?")
if wyszukaj_konto == 'stwórz':
    nowe_konto = input('jaka ma być nazwa nowego konta')



with open('folder_bankowy/rachunki_bankowe.json',encoding="utf-8",mode='w') as plik:
    plik.write(json.dumps(rachunki,indent=4))
