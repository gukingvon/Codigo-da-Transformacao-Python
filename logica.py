from datetime import datetime

nome = input("Digite seu nome: ");
print(f"olá {nome} bem vindo(a)"); 

horas = datetime.now().strftime("%H:%M:%S")
print(f"{nome} As horas são - {horas} ")

idade = int(input(f"Quantos anos você tem {nome}: "));
if idade >= 18:
    print(f"{nome} Liberado");
elif idade >= 17:
    print(f"Acesso negado {nome}");
else:
    print(f"PROIBIDO A ENTRADA DE MENORES!")
