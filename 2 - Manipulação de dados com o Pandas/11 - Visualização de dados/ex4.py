# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt
import pandas as pd

avocados = pd.read_pickle('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\2 - Manipulação de dados com o Pandas\\11 - Visualização de dados\\avoplotto.pkl')

# Modify bins to 20
avocados[avocados["type"] == "conventional"]["avg_price"].hist(alpha=0.5, bins=20)

# Modify bins to 20
avocados[avocados["type"] == "organic"]["avg_price"].hist(alpha=0.5, bins=20)

# Add a legend
plt.legend(["conventional", "organic"])

# Show the plot
plt.show()

'''
O código acima demonstra como criar histogramas sobrepostos para comparar a distribuição dos preços médios de abacates convencionais e orgânicos usando o Pandas e Matplotlib. Primeiro, os dados são carregados a partir de um arquivo pickle. Em seguida, dois histogramas são gerados: um para abacates convencionais e outro para abacates orgânicos, ambos com 20 bins e transparência ajustada para facilitar a visualização conjunta. Uma legenda é adicionada para identificar cada tipo de abacate, e finalmente, o gráfico é exibido na tela.
'''