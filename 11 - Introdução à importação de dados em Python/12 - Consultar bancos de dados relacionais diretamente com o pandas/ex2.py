# Import packages
from sqlalchemy import create_engine
import pandas as pd

# Create engine: engine
engine = create_engine('sqlite:///C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\11 - Introdução à importação de dados em Python\\Chinook.sqlite')

# Execute query and store records in DataFrame: df
df = pd.read_sql_query('SELECT * FROM Employee WHERE EmployeeId >= 6 ORDER BY BirthDate', engine)

# Print head of DataFrame
print(df.head())

'''
O código acima demonstra uma maneira mais eficiente de consultar um banco de dados SQLite usando SQLAlchemy e pandas. Em vez de criar uma conexão manualmente, ele utiliza a função `pd.read_sql_query`, que gerencia automaticamente a conexão ao banco de dados. A consulta SQL seleciona todos os registros da tabela "Employee" onde o "EmployeeId" é maior ou igual a 6, ordenando os resultados pela data de nascimento ("BirthDate"). Os resultados são então armazenados em um DataFrame do pandas, e as primeiras linhas do DataFrame são impressas na tela.
'''