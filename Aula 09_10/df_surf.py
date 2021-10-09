import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt



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

ds.dropna(axis=0, inplace=True)
print(ds.info())
ds_normalized = ds.select_dtypes('number')

wcss = []
for i in range(1,15):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(ds_normalized)
    wcss.append(kmeans.inertia_)

plt.plot(range(1,15),wcss)
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()