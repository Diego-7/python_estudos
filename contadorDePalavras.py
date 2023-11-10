texto = input("Insira o texto: ")

def tratamento(texto):
    return texto.split()

print("Seu texto possui: " + str(len(tratamento(texto))) + " palavras")