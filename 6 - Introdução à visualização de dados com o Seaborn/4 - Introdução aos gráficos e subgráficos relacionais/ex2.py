# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

student_data = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\6 - Introdução à visualização de dados com o Seaborn\\student_data.csv')

# Create a scatter plot of G1 vs. G3
sns.relplot(x='G1', y='G3', data=student_data, kind='scatter')

# Show plot
plt.show()

# Adjust to add subplots based on school support
sns.relplot(x="G1", y="G3", 
            data=student_data,
            kind="scatter", col='schoolsup', col_order=['yes', 'no'])

# Show plot
plt.show()

# Adjust further to add subplots based on family support
sns.relplot(x="G1", y="G3", 
            data=student_data,
            kind="scatter", 
            col="schoolsup",
            col_order=["yes", "no"],
            row='famsup', row_order=['yes', 'no'])

# Show plot
plt.show()

'''
O código acima demonstra como criar gráficos relacionais usando a biblioteca Seaborn em Python. Primeiro, um gráfico de dispersão simples é criado para visualizar a relação entre as notas G1 e G3 dos estudantes. Em seguida, o gráfico é ajustado para incluir subgráficos baseados no suporte escolar (schoolsup), dividindo os dados em duas colunas: uma para estudantes com suporte escolar e outra para aqueles sem. Finalmente, o gráfico é ainda mais detalhado ao adicionar subgráficos baseados no suporte familiar (famsup), criando uma grade de gráficos que mostra as combinações de suporte escolar e familiar. Cada etapa do processo é seguida pela exibição do gráfico resultante.
'''