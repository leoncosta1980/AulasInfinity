import pandas as pd
import numpy as np

dataset = pd.read_csv('kc_house_data.csv', sep=',')

def categorize(price):
    if price > 500000:
        return 'expensive'
    elif price > 220000:
        return 'fear'
    else:
        return 'cheap'

dataset['cat_price'] = dataset['price'].apply(categorize)
#print(dataset.info())
#print(dataset.head(20))
# print("Qtde de Quartos:",dataset['bedrooms'].unique())
# print(dataset['price'].max())
# print(dataset[dataset['price'] == 7700000.0])
#print(dataset[dataset['bedrooms'] == 33])
#dataset.isnull().sum()

bedrooms = dataset['bedrooms']
bedrooms.dropna(inplace=True)
values = np.array(bedrooms)
print(values.tolist())
sum = 0

#verificar quantos campos nulos temos no datasets
print(dataset.isnull().sum())

for value in values:
    if value !=33:
        sum += value

media = sum / (len(values)-1)
print(media)

#substituir os campos nulos de quartos para a média de quartos do dataset
dataset['bedrooms'].fillna(media, inplace=True)
dataset.dropna(inplace=True)
print(dataset.isnull().sum())