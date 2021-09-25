import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

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

bedrooms = pd.DataFrame(values)
bedrooms.columns = ['bedrooms']
#Aplicação do ZScore para eliminar Outliers
#Verificar a existênc ade Outlier

# sns.boxplot(x=dataset['bedrooms'])
# plt.show()

#Utilizar o Zscore
# z = np.abs(stats.zscore(bedrooms))
# z_bedrooms = bedrooms[(z<3).all(axis=1)]
# sns.boxplot(x=z_bedrooms['bedrooms'])
# plt.show()

#Aplicando o IQR 
Q1 = bedrooms.quantile(0.25)
Q3 = bedrooms.quantile(0.75)
IQR = Q3 -Q1
q_highest_bedrooms = Q3 + 1.5 * IQR
q_lowest_bedrooms = Q1 - 1.5 * IQR
print("Maior: ",q_highest_bedrooms)
print("Menor: ",q_lowest_bedrooms)

IQR_bedrooms = bedrooms[~((bedrooms>q_highest_bedrooms)|(bedrooms<q_lowest_bedrooms)).any(axis=1)]
sns.boxplot(x=IQR_bedrooms['bedrooms'])
plt.show()