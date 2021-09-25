import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

base = np.array([10,11,11,13,15,17,15,18,16,15,16,18,15,11,10,15,12,80,82,86,88,85,84,83,81,82,84,80,82,85,86,88,89])
ds = pd.DataFrame(base)
ds.columns = ['dado']
sns.boxplot(x=ds['dado'])
plt.show()
