import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

ds = pd.read_csv("genres_v2.csv", sep=",")
print(ds.head())
print(ds.info())
ds.drop(columns='Unnamed: 0', axis = 1, inplace=True)
ds.drop(columns='title', axis = 1, inplace=True)

#Normalizando o DS
ds_normalized = ds.select_dtypes("number")
print(ds_normalized.info())
#print(ds_normalized["Unnamed: 0"].unique())

#ds_normalized.drop(columns="Unnamed: 0", axis=1, inplace=True)
print(ds_normalized.head())

#sns.boxplot(x=ds_normalized['loudness'])
#plt.show()

ds_normalized = (ds_normalized - ds_normalized.mean()) / ds_normalized.std()

print(ds_normalized.head(20))

#sns.boxplot(x=ds_normalized['loudness'])
#plt.show()

#Aplicar o PCA
pca = PCA(n_components=8)
pca.fit(ds_normalized)
print(pca.explained_variance_ratio_)

percent = 0

for component in pca.explained_variance_ratio_:
    percent += component

print("Total de cobertura dos dados na nossa base: {:.2f}%".format(percent*100))

#Aplicando o PCA depois da análise realizada
pca = PCA(n_components=8).fit_transform(ds_normalized)

#Rodar o algoritmo k-means em cima da base de dados com PCA
kmeans = KMeans(n_clusters=6)
kmeans.fit(pca)
print(kmeans.labels_)

#Pegar os valores dos label e colocar uma nova coluna e colocar dentro do DS original

ds['cluster'] = kmeans.labels_
print(ds.head(30))

print(ds['cluster']==0)

print(pd.value_counts(ds['cluster']))