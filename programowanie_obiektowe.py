class ZwierzakDomowy:
    def __init__(self,ksywka):
        self.ksywka = ksywka
    def daj_glos(self):
        print("nie umiem mówić")
class Pies(ZwierzakDomowy):
    def __init__(self, ksywka,rasa):
        super().__init__(ksywka)
        self.rasa = rasa
    def daj_glos(self):
        print("hau hau")
    def turlaj_się(self):
       print('pies się turla')
class Kot(ZwierzakDomowy):
    def __init__(self, ksywka):
        super().__init__(ksywka)
    def daj_glos(self):
        print("miau miau")
        def turlaj_się(self):
            print('kot się turla')
class Ptaszek(ZwierzakDomowy):
    def __init__(self, ksywka):
        super().__init__(ksywka)
    def daj_glos(self):
        print("ćwir ćwir")
    def turlaj_się(self):
        print ('nie umiem się turlać')
class Rybka(ZwierzakDomowy)
    def __init__(self, ksywka):
        super().__init__(ksywka)
    def daj_glos(self):
        print("nie umiem mówić")
    def turlaj_się(self):
        print ('rybka turla się pod wodą')
pies = Pies("Pimpek","Jamnik")
ptaszek = Ptaszek('papuga')
złota_rybka = ZwierzakDomowy('plumek')
kot = Kot("Mruczek")
komenda = input('jaka   ma być komęda?')
if komenda == 'daj głos':
        daj_glos =  input("kto ma dać głos ")
if daj_glos == 'pies':
    pies.daj_glos()
if daj_glos == 'kot':
    kot.daj_glos()
if daj_glos == 'ryba':
    złota_rybka.daj_glos()
if daj_glos == ptaszek:
    ptaszek.daj_glos
if komenda == 'turlaj się':
 turlaj_się = input("kto ma się turlać")
if turlaj_się == 'pies':