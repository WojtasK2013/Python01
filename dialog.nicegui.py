from nicegui import ui
@ui.page('/')
def pokaż_dialog():ef main():
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

ui.run(reload=True)