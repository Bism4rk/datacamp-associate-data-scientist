# Import necessary module
from sqlalchemy import inspect, create_engine

# Create engine: engine
engine = create_engine('sqlite:///C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\11 - Introdução à importação de dados em Python\\Chinook.sqlite')

# # Save the table names to a list: table_names
# table_names = engine.table_names()
# Esse código foi depreciado na versão 1.4 do SQLAlchemy. Use o código abaixo como substituição.

inspector = inspect(engine)
table_names = inspector.get_table_names()

# Print the table names to the shell
print(table_names)

'''
O código acima demonstra como criar um mecanismo de banco de dados SQLite usando SQLAlchemy em Python e como listar os nomes das tabelas presentes no banco de dados. A função create_engine é utilizada para estabelecer a conexão com o banco de dados especificado, que neste caso é um arquivo SQLite chamado "Chinook.sqlite". Em seguida, a função inspect é usada para inspecionar o banco de dados, e o método get_table_names() recupera os nomes das tabelas, que são então armazenados na lista table_names e impressos no console.
'''