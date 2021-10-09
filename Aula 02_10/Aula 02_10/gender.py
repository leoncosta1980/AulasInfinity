import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier


ds = pd.read_csv('gender.csv', sep=',')

print(ds.info())
print(ds.head(20))

#sns.boxplot(x=ds['forehead_width_cm'])
#plt.show()

X = ds.drop(columns='Male', axis = 1)
y = ds['Male']


x_train, x_test, y_train, Y_test = train_test_split(X,y, test_size=0.25, random_state=50)

print("Tamanho da base de teste: ", len(x_test))
print("Tamanho da base de teste: ", len(x_train))

knn = KNeighborsClassifier()

k_values = dict(n_neighbors=[1,2,3,4,5,6])

gridSearch = GridSearchCV(knn, k_values, scoring = 'accuracy')

gs = gridSearch.fit(x_train, y_train)


print("Acuracia para o valor de {} é: {}".format(gs.best_params_, gs.best_score_)) 