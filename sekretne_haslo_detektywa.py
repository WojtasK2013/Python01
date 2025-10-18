def wyjscie():
        exit()
def szyfrowanie():
    gotowe_szyfrowanie = 0
    napis = input("co piszemy?")
    for literka in napis:
        kod = ord(literka) + 3
        odkodowano_szyfrowanie = chr(kod)
        gotowe_szyfrowanie = str(gotowe_szyfrowanie) + str(odkodowano_szyfrowanie)
    print(gotowe_szyfrowanie)


opcja = input('co dzisiaj robimy mistrzu?')
if str(opcja) == '1':
    gotowe_odszyfrowanie = 0
    napis = input("jaka wiadomość?")
    for literka in napis:
        kod = ord(literka) - 3
        odkodowano_odszyfrowanie = chr(kod)
        gotowe_odszyfrowanie = str(gotowe_odszyfrowanie) +str(odkodowano_odszyfrowanie)
    print(gotowe_odszyfrowanie)
elif opcja == '2':
    szyfrowanie()
elif opcja == '3':
    wyjscie()