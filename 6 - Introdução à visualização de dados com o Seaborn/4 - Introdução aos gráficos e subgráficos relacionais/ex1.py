# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

student_data = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\6 - Introdução à visualização de dados com o Seaborn\\student_data.csv')


# Change to make subplots based on study time
sns.relplot(x="absences", y="G3", 
            data=student_data,
            kind="scatter", col='study_time')

# Show plot
plt.show()

# Change this scatter plot to arrange the plots in rows instead of columns
sns.relplot(x="absences", y="G3", 
            data=student_data,
            kind="scatter", 
            row="study_time")

# Show plot
plt.show()

'''
O código acima demonstra como criar gráficos de dispersão (scatter plots) usando a biblioteca Seaborn, organizando-os em subgráficos (subplots) com base na variável "study_time". No primeiro gráfico, os subgráficos são dispostos em colunas, enquanto no segundo gráfico, eles são organizados em linhas. Isso permite uma visualização clara de como a relação entre "absences" e "G3" varia conforme o tempo de estudo dos estudantes.
'''