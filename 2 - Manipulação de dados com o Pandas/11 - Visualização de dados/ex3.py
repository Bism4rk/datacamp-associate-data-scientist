# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt
import pandas as pd

avocados = pd.read_pickle('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\2 - Manipulação de dados com o Pandas\\11 - Visualização de dados\\avoplotto.pkl')

# Scatter plot of avg_price vs. nb_sold with title
avocados.plot(x="nb_sold", y="avg_price", kind="scatter", title="Number of avocados sold vs. average price")

# Show the plot
plt.show()

'''
O código acima demonstra como criar um gráfico de dispersão (scatter plot) usando o Pandas e Matplotlib para visualizar a relação entre o número de abacates vendidos e o preço médio. Primeiro, os dados são carregados a partir de um arquivo pickle. Em seguida, um gráfico de dispersão é gerado, onde o eixo x representa o número de abacates vendidos e o eixo y representa o preço médio. O gráfico também inclui um título descritivo. Finalmente, o gráfico é exibido na tela.
'''