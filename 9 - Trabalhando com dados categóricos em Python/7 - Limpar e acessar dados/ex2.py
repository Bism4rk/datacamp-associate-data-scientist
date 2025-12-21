import pandas as pd

dogs = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\9 - Trabalhando com dados categóricos em Python\\dogs.csv')

# Print the category of the coat for ID 23807
print(dogs.loc[23807, "coat"])

# Find the count of male and female dogs who have a "long" coat
print(dogs.loc[dogs["coat"] == "long", "sex"].value_counts())

# Print the mean age of dogs with a breed of "English Cocker Spaniel"
print(dogs.loc[dogs["breed"] == 'English Cocker Spaniel', 'age'].mean())

# Count the number of dogs that have "English" in their breed name
print(dogs[dogs["breed"].str.contains("English", regex=False)].shape[0])

'''
O código acima demmonstra como acessar e analisar dados categóricos em um DataFrame do pandas. Primeiro, ele recupera a categoria do pelo (coat) para um cão específico identificado pelo ID 23807. Em seguida, conta o número de cães machos e fêmeas que possuem um pelo longo (long coat). Depois, calcula a idade média dos cães da raça "English Cocker Spaniel". Finalmente, conta quantos cães têm "English" no nome da raça, utilizando uma busca por substring na coluna breed.
'''