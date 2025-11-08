import pandas as pd

licenses = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\3 - Junção de dados com o Pandas\\licenses.csv')
zip_demo = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\3 - Junção de dados com o Pandas\\zip_demo.csv')
wards = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\3 - Junção de dados com o Pandas\\Chicago_wards.csv')

# Merge licenses and zip_demo, on zip; and merge the wards on ward
licenses_zip_ward = licenses.merge(zip_demo, on='zip') \
            			.merge(wards, on='ward')

# Print the results by alderman and show median income
print(licenses_zip_ward.groupby('alderman').agg({'income':'median'}))

'''
O código acima demonstra como mesclar vários DataFrames usando o Pandas e agrupar os dados resultantes para análise. Primeiro, ele lê três conjuntos de dados: licenças, dados demográficos por código postal (zip_demo) e informações sobre bairros (wards) em Chicago. Em seguida, ele mescla os DataFrames de licenças e zip_demo com base na coluna 'zip', e depois mescla o resultado com o DataFrame de wards usando a coluna 'ward'. Após a mesclagem, o código agrupa os dados resultantes pelo nome do vereador ('alderman') e calcula
'''