import pandas as pd

# From previous steps
airline_bumping = pd.read_csv("C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\2 - Manipulação de dados com o Pandas\\14 - Leitura e gravação de CSVs\\airline_bumping.csv")
print(airline_bumping.head())
airline_totals = airline_bumping.groupby("airline")[["nb_bumped", "total_passengers"]].sum()
airline_totals["bumps_per_10k"] = airline_totals["nb_bumped"] / airline_totals["total_passengers"] * 10000

# Print airline_totals
print(airline_totals)

'''
O código acima demonstra como ler um arquivo CSV usando o Pandas, agrupar os dados por uma coluna específica (neste caso, "airline"), somar os valores de outras colunas ("nb_bumped" e "total_passengers") e calcular uma nova métrica ("bumps_per_10k") que representa o número de passageiros retirados por 10.000 passageiros totais. Finalmente, o DataFrame resultante é impresso para visualização.
'''