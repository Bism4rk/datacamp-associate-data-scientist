import pandas as pd
from list import list_of_occupations

# Create a Series, default dtype
series1 = pd.Series(list_of_occupations)

# Print out the data type and number of bytes for series1
print("series1 data type:", series1.dtype)
print("series1 number of bytes:", series1.nbytes)

# Create a Series, "category" dtype
series2 = pd.Series(list_of_occupations, dtype="category")

# Print out the data type and number of bytes for series2
print("series2 data type:", series2.dtype)
print("series2 number of bytes:", series2.nbytes)

'''
O código acima demonstra um dos benefícios do uso de dados categóricos em pandas: a economia de memória. Ao converter uma Series de strings para o tipo "category", o uso de memória pode ser significativamente reduzido, especialmente quando há muitas repetições dos mesmos valores na Series.
'''