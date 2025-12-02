# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

student_data = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\6 - Introdução à visualização de dados com o Seaborn\\student_data.csv')

# Create a point plot of family relationship vs. absences
sns.catplot(x="famrel", y="absences", data=student_data, kind='point')
            
# Show plot
plt.show()

# Add caps to the confidence interval
sns.catplot(x="famrel", y="absences",
			data=student_data,
            kind="point", capsize=0.2)
        
# Show plot
plt.show()

# Remove the lines joining the points
sns.catplot(x="famrel", y="absences",
			data=student_data,
            kind="point",
            capsize=0.2, join=False)
            
# Show plot
plt.show()

'''
O código acima demonstra como criar gráficos de pontos usando a biblioteca Seaborn em Python. Ele começa importando as bibliotecas necessárias: Matplotlib para visualização, Seaborn para gráficos estatísticos e Pandas para manipulação de dados. Em seguida, os dados dos estudantes são carregados a partir de um arquivo CSV. O primeiro gráfico de pontos é criado para mostrar a relação entre a qualidade do relacionamento familiar (famrel) e o número de ausências (absences) dos estudantes. O segundo gráfico adiciona "caps" (tampas) aos intervalos de confiança para melhorar a visualização. O terceiro gráfico remove as linhas que conectam os pontos, focando apenas nos pontos individuais com seus intervalos de confiança. Cada gráfico é exibido usando plt.show().
'''