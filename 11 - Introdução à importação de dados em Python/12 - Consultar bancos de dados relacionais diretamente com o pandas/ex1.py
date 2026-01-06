# Import packages
from sqlalchemy import create_engine, text
import pandas as pd

# Create engine: engine
engine = create_engine('sqlite:///C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\11 - Introdução à importação de dados em Python\\Chinook.sqlite')

# Execute query and store records in DataFrame: df
df = pd.read_sql_query('SELECT * FROM Album', engine)

# Print head of DataFrame
print(df.head())

# Open engine in context manager and store query result in df1
with engine.connect() as con:
    rs = con.execute(text("SELECT * FROM Album"))
    df1 = pd.DataFrame(rs.fetchall())
    df1.columns = rs.keys() # type: ignore

# Confirm that both methods yield the same result
print(df.equals(df1))

'''
O código acima demonstra como conectar a um banco de dados SQLite usando SQLAlchemy, executar uma consulta SQL para selecionar todos os registros da tabela "Album" e armazenar os resultados em um DataFrame do pandas. Ele também mostra duas abordagens diferentes para realizar essa tarefa: usando a função `pd.read_sql_query` e utilizando um gerenciador de contexto para abrir a conexão e executar a consulta manualmente. Finalmente, o código verifica se ambos os DataFrames resultantes são iguais.
'''