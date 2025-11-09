import pandas as pd

taglines = pd.read_pickle('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\3 - Junção de dados com o Pandas\\taglines.pkl')
toy_story = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\3 - Junção de dados com o Pandas\\toy_story.csv')

# Print column names of both DataFrames to check
print("Toy Story columns:", toy_story.columns.tolist())
print("Taglines columns:", taglines.columns.tolist())


# Merge the toy_story and taglines tables with a left join
toystory_tag = toy_story.merge(taglines, on='id', how='left')

# Print the rows and shape of toystory_tag
print(toystory_tag)
print(toystory_tag.shape)

# Merge the toy_story and taglines tables with a inner join
toystory_tag_inner = toy_story.merge(taglines, on='id')

# Print the rows and shape of toystory_tag
print(toystory_tag_inner)
print(toystory_tag_inner.shape)

'''
O código acima demonstra as diferenças entre uma junção à esquerda (left join) e uma junção interna (inner join) usando os DataFrames toy_story e taglines. Na junção à esquerda, todas as linhas do DataFrame toy_story são mantidas, e as informações correspondentes do DataFrame taglines são adicionadas quando há uma correspondência no campo 'id'. Se não houver correspondência, os valores das colunas do DataFrame taglines serão preenchidos com NaN. Na junção interna, apenas as linhas que possuem correspondências em ambos os DataFrames são mantidas. Isso resulta em um DataFrame menor, pois todas as linhas sem correspondência são descartadas.
'''