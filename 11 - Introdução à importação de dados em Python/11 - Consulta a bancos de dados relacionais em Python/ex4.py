# Import packages
from sqlalchemy import create_engine, text
import pandas as pd

# Create engine: engine
engine = create_engine('sqlite:///C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\11 - Introdução à importação de dados em Python\\Chinook.sqlite')

# Open engine connection: con
con = engine.connect()

# Open engine in context manager
with engine.connect() as con:
    rs = con.execute(text('SELECT * FROM Employee ORDER BY BirthDate'))
    df = pd.DataFrame(rs.fetchall())

    # Set the DataFrame's column names
    df.columns = rs.keys()  # type: ignore

# Print head of DataFrame
print(df.head())

'''
O código acima demonstra como conectar a um banco de dados SQLite usando SQLAlchemy, executar uma consulta SQL para selecionar todos os registros da tabela "Employee" ordenados por "BirthDate", armazenar os resultados em um DataFrame do pandas e definir os nomes das colunas do DataFrame com base nos nomes das colunas retornadas pela consulta. Finalmente, o código imprime as primeiras linhas do DataFrame resultante.
'''
