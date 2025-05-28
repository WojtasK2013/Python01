def print_wojtka(tekst='bążur',znak='-',znak2='-'):   
    """Funkcja wojtka wyswietlajaca tekst miedzy belkami"""
    print(znak*150)
    print(tekst)
    print(znak2*150)
def print_wojtka2(nic=''):
    nic = input('podaj nic')
    return nic
if __name__ == '__main__':
    print_wojtka("cześć","-=","+")
    print_wojtka("witamy w grze","=+","*")
    print_wojtka()
    a = print_wojtka2()
    if a == "klik": 
        print("")
    else:
        print("coś napewno")