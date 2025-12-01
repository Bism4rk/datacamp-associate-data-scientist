# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd

survey_data = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\6 - Introdução à visualização de dados com o Seaborn\\survey_data.csv')

# Create count plot of internet usage
sns.catplot(x="Internet usage", data=survey_data, kind='count')

# Show plot
plt.show()

# Change the orientation of the plot
sns.catplot(y="Internet usage", data=survey_data,
            kind="count")

# Show plot
plt.show()

# Separate into column subplots based on age category
sns.catplot(y="Internet usage", data=survey_data,
            kind="count", col='Age Category')

# Show plot
plt.show()

