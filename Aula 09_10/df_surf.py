import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



def classify_board_adequate(board_adequate):
    if board_adequate == 'Very inadequate':
        return 0
    if board_adequate == 'Inadequate':
        return 1
    if board_adequate == 'More or less':
        return 2
    if board_adequate == 'Suitable':
        return 3
    if board_adequate == 'Very suitable':
        return 4
    

    
ds = pd.read_csv('df_surf.csv', sep=',')
print(ds.head(20))
print(ds.info())
print(ds['board_adequate'].unique())

#substituir a coluna board_adequate como uma classificação numérica

ds['board_adequate'] = ds['board_adequate'].apply(classify_board_adequate)
ds.drop(columns=['surfer_weight_distribution','board_tail_rocker','board_nose_rocker'],axis=1, inplace=True)
#print(ds.info())
ds = ds.select_dtypes('number')
#ds.dropna(axis=0, inplace=True)
print(ds.info())
ds[ds['board_how_many']==60] = 6.0
ds[ds['board_how_many']==10] = 1.0

#criando uma função para aplicar nas colunas
def remove_na(column_name):
    column = ds[column_name]
    column.dropna(inplace=True)
    column = column.tolist()
    #print(column)
    sum = 0
    for d in column:
        sum = sum + d
        media = sum / len(column)
        ds[column_name].fillna(media, inplace=True)
    print('Média da coluna {}: {}'.format(column_name, media))
#termina aqui

#substituindo em todas as colunas

for column in ds.columns:
    remove_na(column)
print(ds.info())


# wcss = []
# for i in range(1,15):
#     kmeans = KMeans(n_clusters=i, init='k-means++')
#     kmeans.fit(ds)
#     wcss.append(kmeans.inertia_)

# print(wcss)
# plt.plot(range(1,15),wcss)
# plt.xlabel('Number of clusters')
# plt.ylabel('WCSS')
# plt.show()

#dropando os indices para n influencia o algoritmo
ds.drop(columns='Unnamed: 0', inplace=True)
kmeans = KMeans(n_clusters = 3, init='k-means++', n_init = 10, max_iter = 300)
clusters = kmeans.fit_predict(ds)
print(clusters)
ds['cluster'] = clusters
print(ds.head(25))

sns.pairplot(ds, x_vars=['cluster'],y_vars=['board_length'])
plt.show()