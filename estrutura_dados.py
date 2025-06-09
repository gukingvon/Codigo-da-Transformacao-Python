nomes = []
for i in range(3):
    nome = input("Digite o nome da pessoa: ")
    nomes.append(nome)
print("Pessoas cadastradas:")
for nome in nomes:
    print("-", nome)
