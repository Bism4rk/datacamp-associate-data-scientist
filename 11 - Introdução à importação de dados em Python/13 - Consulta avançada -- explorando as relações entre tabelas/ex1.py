# Import packages
from sqlalchemy import create_engine, text
import pandas as pd

# Create engine: engine
engine = create_engine('sqlite:///C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\11 - Introdução à importação de dados em Python\\Chinook.sqlite')

# Open engine in context manager
# Perform query and save results to DataFrame: df
with engine.connect() as con:
    rs = con.execute(text('SELECT Title, Name FROM Album INNER JOIN Artist on Album.ArtistID = Artist.ArtistID'))
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys() # type: ignore

# Print head of DataFrame df
print(df.head())

'''
O código acima demonstra como realizar uma consulta SQL que envolve uma junção (JOIN) entre duas tabelas, "Album" e "Artist", em um banco de dados SQLite usando SQLAlchemy. A consulta seleciona os campos "Title" da tabela "Album" e "Name" da tabela "Artist", combinando os registros com base no campo comum "ArtistID". Os resultados da consulta são armazenados em um DataFrame do pandas, e as colunas do DataFrame são definidas com base nos nomes das colunas retornadas pela consulta. Finalmente, o código imprime as primeiras linhas do DataFrame resultante.
'''