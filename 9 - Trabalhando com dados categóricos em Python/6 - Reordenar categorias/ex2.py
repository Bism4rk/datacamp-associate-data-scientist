import pandas as pd

dogs = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\9 - Trabalhando com dados categóricos em Python\\dogs.csv')

dogs['size'] = dogs['size'].astype('category')


# Previous code
dogs["size"] = dogs["size"].cat.reorder_categories(
    ["small", "medium", "large"],
    ordered=True
)

# How many Male/Female dogs are available of each size?
print(dogs.groupby('size')['sex'].value_counts())

# Do larger dogs need more room to roam?
print(dogs.groupby('size')['keep_in'].value_counts())