import json

def dopisz_do_systemu(linie):
    with open('folder_bankowy/bank.py',encoding="utf-8",mode='w') as plik:
        linie.append(f' if wyszukaj_konto =={[nowe_konto]}zrób_działanie()')
    plik.writelines(linie)
def zapisz_rachunki(rachunki):
    with open('folder_bankowy/rachunki_bankowe.json',encoding="utf-8",mode='w') as plik:
            plik.write(json.dumps(rachunki,indent=4))
            print("zapisano pomyślnie")
def odczytaj_rachunki():
    with open('folder_bankowy/rachunki_bankowe.json',encoding="utf-8",mode='r') as plik:
        return json.load(plik)
def zrób_działanie(wyszukaj_konto):
    print("Dostępne działania i ich komendy:")
    print("  'dodać'        - dodaje pieniądze do wybranego konta")
    print("  'odjąć'        - odejmuje pieniądze z wybranego konta")
    print("  'odczyt'       - wyświetla wszystkie rachunki")
    print("  'dodaj_konto'  - dodaje nowe konto o podanej nazwie")

    rachunki = odczytaj_rachunki()
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
    elif działanie == 'odczyt':
        print(rachunki)
        zapisz_rachunki(rachunki)
    elif działanie == 'dodaj_konto':
        rachunki[wyszukaj_konto] = { "na_koncie":0}
        print(f'{rachunki[wyszukaj_konto]}')
        zapisz_rachunki(rachunki)   
    else:
        print("nie znam działania")

rachunki = odczytaj_rachunki()
wyszukaj_konto = input("jakie konto chcesz wyszukać?")
if wyszukaj_konto == 'stwórz':
    nowe_konto = input('jaka ma być nazwa nowego konta')
    rachunki[nowe_konto]={"na_koncie ":0} 
    dopisz_do_systemu()
zapisz_rachunki(rachunki)
zrób_działanie(wyszukaj_konto)
