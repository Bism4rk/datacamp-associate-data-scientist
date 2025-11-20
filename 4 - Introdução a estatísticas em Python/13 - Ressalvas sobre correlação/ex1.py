import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load the dataset
world_happiness = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\4 - Introdução a estatísticas em Python\\world_happiness.csv')

# Scatterplot of gdp_per_cap and life_exp
sns.scatterplot(x="gdp_per_cap", y="life_exp", data=world_happiness)

# Show plot
plt.show()
  
# Correlation between gdp_per_cap and life_exp
cor = world_happiness['gdp_per_cap'].corr(world_happiness['life_exp'])

print(cor)

'''
O código acima demonstra duas variáveis com uma relação não linear. Primeiro, ele cria um gráfico de dispersão (scatterplot) para visualizar a relação entre o PIB per capita (gdp_per_cap) e a expectativa de vida (life_exp) usando a biblioteca Seaborn em Python. Em seguida, calcula o coeficiente de correlação entre essas duas variáveis. Devido à natureza não linear da relação, o coeficiente de correlação pode não refletir com precisão a força ou a direção da relação entre as variáveis, destacando uma limitação do uso da correlação de Pearson em tais casos.
'''