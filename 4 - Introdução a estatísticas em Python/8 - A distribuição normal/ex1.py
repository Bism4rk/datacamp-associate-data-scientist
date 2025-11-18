import pandas as pd
import matplotlib.pyplot as plt

amir_deals = pd.read_csv('C:\\Users\\reich\\Downloads\\datacamp-associate-data-scientist\\4 - Introdução a estatísticas em Python\\amir_deals.csv', index_col=0)

# Histogram of amount with 10 bins and show plot
amir_deals['amount'].hist(bins=10)
plt.show()

