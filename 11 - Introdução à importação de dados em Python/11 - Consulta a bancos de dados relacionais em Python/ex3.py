# Import packages
from sqlalchemy import create_engine, text
import pandas as pd

# Create engine: engine
engine = create_engine('sqlite:///C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\11 - Introdução à importação de dados em Python\\Chinook.sqlite')

# Open engine connection: con
con = engine.connect()

# Open engine in context manager
# Perform query and save results to DataFrame: df
with engine.connect() as con:
    rs = con.execute(text('SELECT * FROM Employee WHERE EmployeeID >= 6'))
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()  # type: ignore


# Print the head of the DataFrame df
print(df.head())

'''
O código acima realiza uma consulta a um banco de dados SQLite usando SQLAlchemy para selecionar todos os registros da tabela "Employee" onde o "EmployeeID" é maior ou igual a 6. Os resultados da consulta são armazenados em um DataFrame do pandas, e as colunas do DataFrame são definidas com base nos nomes das colunas retornadas pela consulta. Finalmente, o código imprime as primeiras linhas do DataFrame resultante.
'''