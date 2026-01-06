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
    rs = con.execute(text('SELECT LastName, Title FROM Employee'))
    df = pd.DataFrame(rs.fetchmany(3))
    df.columns = rs.keys() # type: ignore

# Print the length of the DataFrame df
print(len(df))

# Print the head of the DataFrame df
print(df.head())

'''
O código acima expande a funcionalidade de consulta a um banco de dados SQLite usando SQLAlchemy. Ele executa uma consulta SQL para selecionar os campos "LastName" e "Title" da tabela "Employee", recupera apenas os primeiros três registros e os armazena em um DataFrame do pandas. Em seguida, imprime o comprimento do DataFrame e as primeiras linhas. A conexão com o banco de dados é gerenciada automaticamente pelo contexto "with", garantindo que seja fechada corretamente após a execução da consulta.
'''