import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

planes = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\8 - Análise exploratória de dados em Python\\planes.csv')

# Create a list of categories
flight_categories = ["Short-haul", "Medium", "Long-haul"]

# Create short-haul values
short_flights = "^0h|^1h|^2h|^3h|^4h"

# Create medium-haul values
medium_flights = "^5h|^6h|^7h|^8h|^9h"

# Create long-haul values
long_flights = "^10h|^11h|^12h|^13h|^14h|^15h|^16h"

# Create conditions for values in flight_categories to be created
conditions = [
    planes["Duration"].str.contains(short_flights, na=False),
    planes["Duration"].str.contains(medium_flights, na=False),
    planes["Duration"].str.contains(long_flights, na=False)
]

# Apply the conditions list to the flight_categories
planes["Duration_Category"] = np.select(conditions, 
                                        flight_categories,
                                        default="Extreme duration")

# Plot the counts of each category
sns.countplot(data=planes, x="Duration_Category")
plt.show()

'''
O código acima demonstra como categorizar voos com base na duração do voo, utilizando expressões regulares para definir intervalos de tempo específicos. As categorias são definidas como "Short-haul" (voos curtos), "Medium" (voos médios) e "Long-haul" (voos longos), com cada categoria associada a um conjunto de padrões de duração de voo. Isso é útil para análise exploratória de dados, permitindo agrupar voos em categorias significativas para facilitar a interpretação e análise dos dados.
'''