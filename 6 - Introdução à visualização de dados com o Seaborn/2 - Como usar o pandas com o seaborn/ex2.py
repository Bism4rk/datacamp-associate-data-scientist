# Import Matplotlib, pandas, and Seaborn
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

csv_filepath = 'https://assets.datacamp.com/production/repositories/3996/datasets/ab13162732ae9ca1a9a27e2efd3da923ed6a4e7b/young-people-survey-responses.csv'

# Create a DataFrame from csv file
df = pd.read_csv(csv_filepath)

# Create a count plot with "Spiders" on the x-axis
sns.countplot(x='Spiders', data=df)

# Display the plot
plt.show()

'''
O código acima demonstra como importar as bibliotecas Matplotlib, pandas e Seaborn em Python, ler um arquivo CSV a partir de uma URL e criar um DataFrame com os dados contidos nesse arquivo. Em seguida, ele cria um gráfico de contagem (count plot) usando a coluna "Spiders" do DataFrame no eixo x. Finalmente, o gráfico é exibido utilizando a função plt.show().
'''