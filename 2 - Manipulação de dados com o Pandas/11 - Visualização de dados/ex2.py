# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt
import pandas as pd

avocados = pd.read_pickle('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\2 - Manipulação de dados com o Pandas\\11 - Visualização de dados\\avoplotto.pkl')


# Get the total number of avocados sold on each date
nb_sold_by_date = avocados.groupby('date')['nb_sold'].sum()

# Create a line plot of the number of avocados sold by date
nb_sold_by_date.plot(x="date", y="nb_sold", kind="line")

# Show the plot
plt.show()

'''
O código acima demonstra como criar um gráfico de linha usando o Pandas e Matplotlib para visualizar o número total de abacates vendidos por data. Primeiro, os dados são carregados a partir de um arquivo pickle. Em seguida, os dados são agrupados pela data e o total vendido é calculado. Finalmente, um gráfico de linha é gerado para representar visualmente esses totais ao longo do tempo, e o gráfico é exibido na tela.

'''
