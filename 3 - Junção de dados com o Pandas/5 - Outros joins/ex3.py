import pandas as pd

iron_1_actors = pd.DataFrame({
    'character': ['Tony Stark', 'Steve Rogers', 'Bruce Banner', 'Natasha Romanoff'],
    'id': [1, 2, 3, 4],
    'name': ['Robert Downey Jr.', 'Chris Evans', 'Mark Ruffalo', 'Scarlett Johansson']
})

iron_2_actors = pd.DataFrame({
    'character': ['Tony Stark', 'Steve Rogers', 'Thor Odinson', 'Clint Barton'],
    'id': [1, 2, 5, 6],
    'name': ['Robert Downey Jr.', 'Chris Evans', 'Chris Hemsworth', 'Jeremy Renner']
})

# iron_1_actors and iron_2_actors aren't the actual dataframes from the exercise, i made them using dictionaries to allow you to run the code

# Merge iron_1_actors to iron_2_actors on id with outer join using suffixes
iron_1_and_2 = iron_1_actors.merge(iron_2_actors,
                                     how='outer',
                                     on='id',
                                     suffixes=('_1', '_2'))

# Create an index that returns true if name_1 or name_2 are null
m = ((iron_1_and_2['name_1'].isnull()) | 
     (iron_1_and_2['name_2'].isnull()))

# Print the first few rows of iron_1_and_2
print(iron_1_and_2[m].head())

'''
O código acima demonstra como usar um outer join para combinar dois DataFrames do Pandas com base em uma coluna comum ('id'). Ele também mostra como identificar linhas onde uma das colunas de nome ('name_1' ou 'name_2') é nula, indicando que o ator estava presente em apenas um dos filmes.
'''