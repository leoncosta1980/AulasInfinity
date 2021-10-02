import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

ds = pd.read_csv("genres_v2.csv", sep=",")
print(ds.head())
print(ds.info())

ds_normalized = ds.select_dtypes("number")
print(ds_normalized.info())
#print(ds_normalized["Unnamed: 0"].unique())

ds_normalized.drop(columns="Unnamed: 0", axis=1, inplace=True)
print(ds_normalized.head())

sns.boxplot(x=ds_normalized['loudness'])
plt.show()

ds_normalized = (ds_normalized - ds_normalized.mean()) / ds_normalized.std()
print(ds_normalized.head(20))

sns.boxplot(x=ds_normalized['loudness'])
plt.show()