from functools import reduce

#variaveis
num = 8
name = "Diego"
lista = ["gol", "tiggo", "uno", "saveiro", "compass"]

#funções

#adiciona novo item no fim da lista
#def adicionar_item(lista):
#    novo = input("Insira o item: ")
#    lista.append(novo)
#adicionar_item(lista)    
#print(lista)

#Soma todos os numeros da lista
def add_num(a,b):
    return a+b
a = [1, 2, 3, 10]
#print(reduce(add_num, a))
#for i in range(5, 15, 3):
 #   print(i) 

#Retorna o indice e o item da lista
#for indice, item in enumerate(lista):
 #   print(f"índice {indice}: {item}")

#executa a função até a variavel num atingir o valor desejado
while num < 20:
    num += 1
    print(num)
