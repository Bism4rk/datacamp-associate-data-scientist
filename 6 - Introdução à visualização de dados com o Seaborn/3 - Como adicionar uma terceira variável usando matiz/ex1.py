# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

student_data = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\6 - Introdução à visualização de dados com o Seaborn\\student_data.csv')

# Change the legend order in the scatter plot
sns.scatterplot(x="absences", y="G3", 
                data=student_data, 
                hue="location", hue_order=['Rural', 'Urban'])

# Show plot
plt.show()

'''
O código acima demonstra como criar um gráfico de dispersão (scatter plot) usando a biblioteca Seaborn, onde os pontos são coloridos com base em uma terceira variável categórica (location). A ordem da legenda é personalizada usando o parâmetro hue_order, garantindo que "Rural" apareça antes de "Urban" na legenda do gráfico.
'''