#variaveis

valorInicial = float(input("Valor Inicial: "))

taxaDeJuros = float(input("taxa de juros: ")) / 100

periodo = int(input("Insira o periodo em anos: "))

#calculos

total = round(valorInicial*(1+taxaDeJuros)**periodo, 2)

rendimentos = round(total - valorInicial, 2)

print("Você terá: R$" + str(total))

print ("O rendimento foi de: R$" + str(rendimentos))