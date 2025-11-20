import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load the dataset
world_happiness = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\4 - Introdução a estatísticas em Python\\world_happiness.csv')

# Create a scatterplot of happiness_score vs. life_exp and show
sns.scatterplot(x="life_exp", y="happiness_score", data=world_happiness)

# Show plot
plt.show()

# Create scatterplot of happiness_score vs life_exp with trendline
sns.lmplot(x="life_exp", y="happiness_score", data=world_happiness, ci=None)

# Show plot
plt.show()

# Correlation between life_exp and happiness_score
cor = world_happiness['life_exp'].corr(world_happiness['happiness_score'])

print(cor)

'''
O código acima demonstra como criar gráficos de dispersão e linhas de tendência usando a biblioteca Seaborn em Python, além de calcular a correlação entre duas variáveis: expectativa de vida (life_exp) e índice de felicidade (happiness_score). Ele começa carregando um conjunto de dados sobre felicidade mundial a partir de um arquivo CSV. Em seguida, cria um gráfico de dispersão para visualizar a relação entre a expectativa de vida e o índice de felicidade. Depois, adiciona uma linha de tendência ao gráfico para ajudar a identificar a direção e a força da relação entre as duas variáveis. Finalmente, calcula e imprime o coeficiente de correlação entre essas variáveis, fornecendo uma medida quantitativa da relação entre elas.
'''