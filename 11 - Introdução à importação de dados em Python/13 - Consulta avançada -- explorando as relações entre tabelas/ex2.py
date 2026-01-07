# Import packages
from sqlalchemy import create_engine
import pandas as pd

# Create engine: engine
engine = create_engine('sqlite:///C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\11 - Introdução à importação de dados em Python\\Chinook.sqlite')

# Execute query and store records in DataFrame: df
df = pd.read_sql_query('SELECT * FROM PlaylistTrack INNER JOIN Track on PlaylistTrack.TrackID = Track.TrackID WHERE Milliseconds < 250000', engine)

# Print head of DataFrame
print(df.head())

'''
O código acima demonstra como realizar uma consulta SQL que envolve uma junção (JOIN) entre duas tabelas, "PlaylistTrack" e "Track", em um banco de dados SQLite usando SQLAlchemy e pandas. A consulta seleciona todos os registros onde a duração da faixa ("Milliseconds") é menor que 250.000 milissegundos (ou 250 segundos). Os resultados da consulta são armazenados em um DataFrame do pandas, e as primeiras linhas do DataFrame resultante são impressas na tela.
'''