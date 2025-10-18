from nicegui import ui, app
import json
def dopisz_do_systemu(linie):
    with open('folder_bankowy/bank.py',encoding="utf-8",mode='w') as plik:
        linie.append(f' if wyszukaj_konto =={[nowe_konto]}zrób_działanie()')
    plik.writelines(linie)

def odczytaj_rachunki():
    with open('folder_bankowy/rachunki_bankowe.json',encoding="utf-8",mode='r') as plik:
        return json.load(plik)
def zapisz_rachunki(rachunki):
    with open('folder_bankowy/rachunki_bankowe.json',encoding="utf-8",mode='w') as plik:
            plik.write(json.dumps(rachunki,indent=4))
działanie = ui.input("jakie działanie chcesz wykonać")
wyszukaj_konto = ui.input("wyszukaj użytkownika")
   
rachunki = odczytaj_rachunki()
if działanie.value == 'dodać':
        ilość_pieniędzy = ui.input('ile pieniędzy chcesz dodać')
        rachunki[wyszukaj_konto.value]["na_koncie"] += ilość_pieniędzy
        ui.label(f'{rachunki[wyszukaj_konto]}')
        zapisz_rachunki(rachunki)   
elif działanie.value == 'odjąć':
        ilość_pieniędzy = ui.input('ile pieniędzy chcesz odjąć')
        rachunki[wyszukaj_konto]["na_koncie"] -= ilość_pieniędzy.value
        print(f'{rachunki[wyszukaj_konto]}')
        zapisz_rachunki(rachunki)
elif działanie.value == 'odczyt':
        ui.label(rachunki)
        zapisz_rachunki(rachunki)
elif działanie.value == 'dodaj_konto':
        rachunki[wyszukaj_konto] = { "na_koncie":0}
        ui.label(f'{rachunki[wyszukaj_konto]}')
        zapisz_rachunki(rachunki)   
wyszukaj_konto.value = ui.input("jakie konto chcesz wyszukać?")
if wyszukaj_konto.value == 'stwórz':
    @ui.page('/')
    def main():
        rachunki = odczytaj_rachunki()     
def pokaż_dialog():
        with ui.dialog() as dialog, ui.card():
            nowe_konto = ui.input('Podaj nazwę nowego konta')
            nowa_kwota = ui.number('Podaj kwotę początkową', value=0)
            
        def dodaj_konto():
                if nowe_konto.value:
                    rachunki[nowe_konto.value] = {"na_koncie": float(nowa_kwota.value)}
                    zapisz_rachunki(rachunki)
                    ui.notify(f'Utworzono konto: {nowe_konto.value}')
                    dialog.close()
                else:
                    ui.notify('Podaj nazwę konta!', color='red')
            
                with ui.row():
                    ui.button('Dodaj', on_click=dodaj_konto)
                ui.button('Anuluj', on_click=dialog.close)

        ui.button('Stwórz nowe konto', on_click=pokaż_dialog)

        rachunki[nowe_konto]={"na_koncie ":0} 
dopisz_do_systemu([])
zapisz_rachunki(rachunki)



ui.run(reload=True)