wejście = int(input('ile miesięcy hodowałeś króliki farmerze'))

tabela = [1,2]

for i in range(1,wejście-1):
   króliki = tabela[i] + tabela[i - 1]
   tabela.append(króliki)
print(f"bardzo dobry z ciebie farmer, rozmnorzyłeś do {tabela} królików")

