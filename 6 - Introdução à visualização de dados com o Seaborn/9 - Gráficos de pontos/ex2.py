# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

student_data = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\6 - Introdução à visualização de dados com o Seaborn\\student_data.csv')


# Create a point plot that uses color to create subgroups
sns.catplot(x="romantic", y="absences", hue="school", kind="point", data=student_data)

# Show plot
plt.show()

# Turn off the confidence intervals for this plot
sns.catplot(x="romantic", y="absences",
			data=student_data,
            kind="point",
            hue="school", ci=None)

# Show plot
plt.show()

# Import median function from numpy
from numpy import median

# Plot the median number of absences instead of the mean
sns.catplot(x="romantic", y="absences",
			data=student_data,
            kind="point",
            hue="school",
            ci=None, estimator=median)

# Show plot
plt.show()


'''
O código acima demonstra como criar gráficos de pontos usando a biblioteca Seaborn em Python, com foco em subgrupos e diferentes estatísticas. Primeiro, ele importa as bibliotecas necessárias e carrega os dados dos estudantes a partir de um arquivo CSV. O primeiro gráfico de pontos mostra a relação entre o status romântico dos estudantes (romantic) e o número de ausências (absences), diferenciando os dados por escola (school) usando cores. O segundo gráfico desativa os intervalos de confiança para uma visualização mais limpa. O terceiro gráfico utiliza a mediana como estatística central em vez da média, oferecendo uma perspectiva diferente sobre os dados. Cada gráfico é exibido usando plt.show().
'''