from stuff import gdp, phones, percent_literate
import seaborn as sns
import matplotlib.pyplot as plt

# Create scatter plot with GDP on the x-axis and number of phones on the y-axis
sns.scatterplot(x=gdp, y=phones)

# Show plot
plt.show()

# Change this scatter plot to have percent literate on the y-axis
sns.scatterplot(x=gdp, y=percent_literate)

# Show plot
plt.show()

'''
O código acima demonstra como criar gráficos de dispersão usando a biblioteca Seaborn em Python. Primeiro, ele importa os dados necessários (PIB, número de telefones e percentual de alfabetização) de um módulo chamado "stuff". Em seguida, cria dois gráficos de dispersão: o primeiro com o PIB no eixo x e o número de telefones no eixo y, e o segundo com o PIB no eixo x e o percentual de alfabetização no eixo y. Finalmente, ambos os gráficos são exibidos usando a função plt.show().
'''