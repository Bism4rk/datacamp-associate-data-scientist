import pandas as pd

dict1 = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'city': ['New York', 'Los Angeles', 'Chicago']
}

pd1 = pd.DataFrame(dict1)

dict2 = {
    'name': ['David', 'Eva', 'Frank'],
    'age': [28, 22, 33],
    'city': ['Miami', 'Seattle', 'Boston']
}

pd2 = pd.DataFrame(dict2)

pd_concat = pd.concat([pd1, pd2], ignore_index=True)
print(pd_concat)


