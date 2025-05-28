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
class Kot(ZwierzakDomowy):
    def __init__(self, ksywka):
        super().__init__(ksywka)
    def daj_glos(self):
        print("miau miau")
pies = Pies("Pimpek","Jamnik")
złota_rybka = ZwierzakDomowy('plumek')
kot = Kot("Mruczek")
daj_glos = input('kto ma dać głos?')
if daj_glos == 'pies':
    pies.daj_glos()
if daj_glos == 'kot':
  kot.daj_glos()
  if daj_glos == 'ryba':
    złota_rybka.daj_glos()