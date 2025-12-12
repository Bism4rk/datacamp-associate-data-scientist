# Create a list of categories
flight_categories = ["Short-haul", "Medium", "Long-haul"]

# Create short-haul values
short_flights = "^0h|^1h|^2h|^3h|^4h"

# Create medium-haul values
medium_flights = "^5h|^6h|^7h|^8h|^9h"

# Create long-haul values
long_flights = "^10h|^11h|^12h|^13h|^14h|^15h|^16h"

'''
O código acima demonstra como categorizar voos com base na duração do voo, utilizando expressões regulares para definir intervalos de tempo específicos. As categorias são definidas como "Short-haul" (voos curtos), "Medium" (voos médios) e "Long-haul" (voos longos), com cada categoria associada a um conjunto de padrões de duração de voo. Isso é útil para análise exploratória de dados, permitindo agrupar voos em categorias significativas para facilitar a interpretação e análise dos dados.
'''