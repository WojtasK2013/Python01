import json

def zapisz_rachunki(rachunki):
    with open('folder_bankowy/rachunki_bankowe.json',encoding="utf-8",mode='w') as plik:
            plik.write(json.dumps(rachunki,indent=4))
            print("zapisano pomyślnie")
def odczytaj_rachunki():
    with open('folder_bankowy/rachunki_bankowe.json',encoding="utf-8",mode='r') as plik:
        return json.load(plik)
rachunki = odczytaj_rachunki()
wyszukaj_konto = input("jakie konto chcesz wyszukać?")
if wyszukaj_konto == 'stwórz':
    nowe_konto = input('jaka ma być nazwa nowego konta')
   
    rachunki[nowe_konto]={"na_koncie ":0} 
zapisz_rachunki(rachunki)
if wyszukaj_konto in rachunki:
    działanie = input("jakie działanie chcesz wykonać")
    if działanie == 'dodać':
        ilość_pieniędzy = int(input('ile pieniędzy chcesz dodać'))
        rachunki[wyszukaj_konto]["na_koncie"] += ilość_pieniędzy
        print(f'{rachunki[wyszukaj_konto]}')
        zapisz_rachunki(rachunki)   
    elif działanie == 'odjąć':
        ilość_pieniędzy = int(input('ile pieniędzy chcesz odjąć'))
        rachunki[wyszukaj_konto]["na_koncie"] -= ilość_pieniędzy
        print(f'{rachunki[wyszukaj_konto]}')
        zapisz_rachunki(rachunki)
    else:
        print("nie znam działania")