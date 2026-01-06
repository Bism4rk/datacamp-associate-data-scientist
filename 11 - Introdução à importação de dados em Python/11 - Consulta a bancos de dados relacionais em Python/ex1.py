# Import packages
from sqlalchemy import create_engine, text
import pandas as pd

# Create engine: engine
engine = create_engine('sqlite:///C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\11 - Introdução à importação de dados em Python\\Chinook.sqlite')

# Open engine connection: con
con = engine.connect()

# Perform query: rs
rs = con.execute(text('SELECT * FROM Album'))

# Save results of the query to DataFrame: df
df = pd.DataFrame(rs.fetchall())

# Close connection
con.close()

# Print head of DataFrame df
print(df.head())

'''
O código acima demonstra como conectar a um banco de dados SQLite usando SQLAlchemy, executar uma consulta SQL para selecionar todos os registros da tabela "Album", armazenar os resultados em um DataFrame do pandas e imprimir as primeiras linhas do DataFrame. A conexão com o banco de dados é fechada após a execução da consulta.
'''