wejście = input("Podaj tekst:")

wejście = wejście.lower()

wejście = wejście.replace(' ','')

czysto = wejście[::-1]
poprawnie = czysto

if czysto == wejście:

    print(f'Zgadzam się z tobą w stu procentach, wyraz {wejście} to palindrom')

else:
    print(f'Niestety nie masz racji, wyraz {wejście} to nie palindrom, wyraz ten od tyłu to {poprawnie}')