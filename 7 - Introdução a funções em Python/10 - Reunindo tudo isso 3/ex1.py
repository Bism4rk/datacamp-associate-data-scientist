# Import pandas
import pandas as pd

tweets_df = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\7 - Introdução a funções em Python\\3 - Reunindo tudo isso\\tweets.csv')

# Select retweets from the Twitter DataFrame: result
result = filter(lambda x: x[0:2] == 'RT', tweets_df['text'])

# Create list from filter object result: res_list
res_list = list(result)

# Print all retweets in res_list
for tweet in res_list:
    print(tweet)

'''
O código acima demonstra o uso da função `filter()` em Python para selecionar tweets que são retweets de um DataFrame do pandas. A função `filter()` é aplicada a uma coluna específica do DataFrame, onde uma função lambda é usada para verificar se os primeiros dois caracteres de cada tweet são "RT", indicando que é um retweet. O resultado da filtragem é então convertido em uma lista e todos os retweets são impressos.
'''