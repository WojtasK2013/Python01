from nicegui import ui,app
def dodaj():
    try:
        wynik.text = str(float(liczba1.value) - float(liczba2.value))
    except ValueError:
        wynik.text = "Błąd: podaj liczby"

ui.label("Dodawanie dwóch liczb")

liczba1 = ui.input("Pierwsza liczba.....")
liczba2 = ui.input("Druga liczba.....")
wynik = ui.label("Wynik pojawi się tutaj")
ui.button("Dodaj", on_click=dodaj)


ui.run(reload=False)