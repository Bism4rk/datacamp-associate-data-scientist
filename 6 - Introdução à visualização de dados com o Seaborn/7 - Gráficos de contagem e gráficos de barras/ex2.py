# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd

survey_data = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\6 - Introdução à visualização de dados com o Seaborn\\survey_data.csv')

# Create a bar plot of interest in math, separated by gender
sns.catplot(x='Gender', y='Interested in Math', data=survey_data, kind='bar')

# Show plot
plt.show()

