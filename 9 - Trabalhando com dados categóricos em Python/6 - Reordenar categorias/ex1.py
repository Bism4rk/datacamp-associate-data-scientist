import pandas as pd

dogs = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\9 - Trabalhando com dados categóricos em Python\\dogs.csv')

dogs['size'] = dogs['size'].astype('category')

# Print out the current categories of the size variable
print(dogs["size"].cat.categories)

# Reorder the categories, specifying the Series is ordinal, and overwriting the original series
dogs["size"] = dogs["size"].cat.reorder_categories(
    ["small", "medium", "large"],
    ordered=True
)
print(dogs["size"].cat.categories)