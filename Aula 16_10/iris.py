import pandas as pd
from sklearn import datasets
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

iris = datasets.load_iris()

#transformando o Dataset em Dataframe do Pandas
df = pd.DataFrame(iris.data, columns=iris.feature_names)

#conhecendo a base de dados
print(df.head(20))
print(df.info())
print(df.isnull().sum())

#plotar valores p/ saber se tem outliers

# columns = df.columns
# for c in columns:
#     sns.boxplot(x=df[c])
#     plt.show()

#sns.pairplot(df)
#plt.show()

wcss = []
for i in range(1,15):
     kmeans = KMeans(n_clusters=i, init='k-means++')
     kmeans.fit(df)
     wcss.append(kmeans.inertia_)

# print(wcss)
# plt.plot(range(1,15),wcss)
# plt.xlabel('Number of clusters')
# plt.ylabel('WCSS')
# plt.show()

kmeans = KMeans(n_clusters = 3, init='k-means++', n_init = 10, max_iter = 300)
clusters = kmeans.fit_predict(df)
print(clusters)
df['target'] = clusters
print(df.head(25))

sns.pairplot(df, hue='target')
plt.show()