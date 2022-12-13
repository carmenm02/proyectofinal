import pandas as pd
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import pylab as plt
import pickle

df1 = pd.read_csv('csv_limpio.csv', delimiter= ',')

ss = StandardScaler()
df_transformado = ss.fit_transform(df1)
print(df_transformado)
x_tran = df_transformado[:, 0]
y_tran = df_transformado[:, 1]
sns.scatterplot(x_tran, y_tran)
plt.show()

with open('datos.pickle', 'wb') as f:
    pickle.dump(df_transformado,f)