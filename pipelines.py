# importar a biblioteca pandas
import pandas as pd

# criar um dataframe de exemplo
df = pd.DataFrame({'nome': ['Ana', 'Bia', 'Carlos'], 'idade': [25, 32, 18]})

# definir uma função para calcular a média de idade por grupo
def media_idade_por_grupo(dataframe, coluna):
    # agrupa os dados por uma coluna e retorna a média de idade por grupo
    return dataframe.groupby(coluna).mean()

# definir uma função para converter os nomes das colunas para maiúsculas
def maiuscula_nome_coluna(dataframe):
    # converte todos os nomes das colunas para maiúsculas
    dataframe.columns = dataframe.columns.str.upper()
    # e retorna o dataframe
    return dataframe

# criar um pipeline que aplica as duas funções criadas acima
pipeline = df.pipe(media_idade_por_grupo, coluna='nome').pipe(maiuscula_nome_coluna)

# mostrar o resultado do pipeline
# print(pipeline)
