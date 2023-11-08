texto = input("Insira o texto: ")

def tratamento(texto):
    texto = texto.replace(" ", ",").split(",")
    return texto
print
print("Seu texto possui: " + str(len(tratamento(texto))) + " palavras")

