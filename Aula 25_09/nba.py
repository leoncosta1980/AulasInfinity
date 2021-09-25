from numpy.random.mtrand import permutation
from os import sep
import pandas as pd
import numpy as np
import math as math
from sklearn.neighbors import KNeighborsRegressor

ds = pd.read_csv('nba_2013.csv', sep=',')
# print(ds.head())
# print(ds.info())
# print(ds.isnull().sum())
ds['x3p.'].fillna(0, inplace=True)
ds['ft.'].fillna(0, inplace=True)
ds['x2p.'].fillna(0, inplace=True)
ds['efg.'].fillna(0, inplace=True)
ds['fg.'].fillna(0, inplace=True)
print(ds.isnull().sum())
ds_normalized = ds.select_dtypes('number')
ds_normalized = (ds_normalized - ds_normalized.mean())/ds.std()
print(ds_normalized.head())

#Separar base de teste X treino

#Embaralhar indices para não pegar dados de sequencias
random_index = np.random.permutation(ds_normalized.index)

#Calcular qtde de dados de teste
q_test = math.floor(len(ds_normalized)/4)

#separar a base de testes
test = ds_normalized.loc[random_index[1:q_test]]

#separar a base de treino
train = ds_normalized.loc[random_index[q_test:]]

#Separar o dado da predição
y_column = ds['pts']

#Separar as colunas que irão ajudar a definir o target
ds_temp = ds_normalized.drop(columns =['pts'])
x_columns = ds_temp.columns

knn = KNeighborsRegressor(n_neighbors=3)

knn.fit(train[x_columns], train[y_column])

preditions = knn.predict(test[x_columns])

#Calcular erro medio