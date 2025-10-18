opcja = 0
if str(opcja) == 'odszyfrowanie':
    gotowe_odszyfrowanie = 0
    napis = input("jaka wiadomość?")
    for literka in napis:
        kod = ord(literka) - 3
        odkodowano_odszyfrowanie = chr(kod)
        gotowe_odszyfrowanie = str(gotowe_odszyfrowanie) +str(odkodowano_odszyfrowanie)
    print(gotowe_odszyfrowanie)

    if opcja == 'szyfrowanie':
        gotowe_szyfrowanie = 0
        napis = input("co piszemy?")
        for literka in napis:
            kod = ord(literka) + 3
            odkodowano_szyfrowanie = chr(kod)
            gotowe_odszyfrowanie = str(gotowe_szyfrowanie) + str(odkodowano_szyfrowanie)
    print(gotowe_szyfrowanie)

if opcja == 'kończymy':

    pass