import pandas as pd

caminho_do_arquivo = ".\\tabela_excel\\dados.xlsx"
df = pd.read_excel(caminho_do_arquivo)

#Extrai a média aritmética de uma Series numeria
print(df.count())
