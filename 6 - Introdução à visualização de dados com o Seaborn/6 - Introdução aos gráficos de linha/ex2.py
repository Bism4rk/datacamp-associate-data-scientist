# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd

mpg = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\6 - Introdução à visualização de dados com o Seaborn\\mpg.csv')

# Make the shaded area show the standard deviation
sns.relplot(x="model_year", y="mpg",
            data=mpg, kind="line", ci="sd")

# Show plot
plt.show()

'''
O códgio acima demonstra como alterar o significado da área sombreada de um gráfico de linha gerado pelo Seaborn. normalmente é o intervalo de confiança mas com isso vira o desvio padrão slk meu
'''