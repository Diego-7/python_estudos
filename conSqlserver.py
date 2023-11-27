# Importar o módulo pyodbc
import pyodbc

# Criar a string de conexão com os dados do banco de dados SQL Server
server = 'server'
database = 'database'
username = 'user'
password = 'password'
connection_string = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}; TrustServerCertificate=yes'

# Criar a conexão com o banco de dados
conn = pyodbc.connect(connection_string)

# Criar um objeto cursor para executar consultas SQL
cursor = conn.cursor()

# Definir a consulta SQL para obter os dados da tabela desejada
sql_query = 'SELECT * FROM produtos'

# Executar a consulta SQL e obter os resultados
cursor.execute(sql_query)
records = cursor.fetchall()

# Imprimir os resultados
for r in records:
    print(r)

# Fechar a conexão com o banco de dados
conn.close()