# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

student_data = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\6 - Introdução à visualização de dados com o Seaborn\\student_data.csv')


# Create a box plot with subgroups and omit the outliers
# sns.catplot(x='internet', y='G3', kind='box', data=student_data, hue='location', sym="")
sns.catplot(x='internet', y='G3', kind='box', data=student_data, hue='location')

# Show plot
plt.show()