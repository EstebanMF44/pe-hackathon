# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# +
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv("world-country-electricity.csv", na_values=("--", "ie"))

df1 = df[(df['Features'] == 'exports ')]

df1['1980']=pd.to_numeric(df1['1980'])
df1['2021']=pd.to_numeric(df1['2021'])


df1['Ratio'] = (df1['2021']-df1['1980'])/(df1['2021'])

df2=df1.sort_values('Ratio', ascending = False)

mask= df2.Ratio != 1.0
df3=df2[mask]

df4=df3.head(3)

df5=df4.iloc[0, 3:-1].tolist()
df6=df4.iloc[1, 3:-1].tolist()
df7=df4.iloc[2, 3:-1].tolist()


X=np.arange(1980, 2022, 1)
Y1=df5
Y2=df6
Y3=df7
plt.plot(X,Y1, label='Argentine')
plt.plot(X,Y2, label='Uruguay')
plt.plot(X,Y3, label='Thaïlande')
plt.legend()
plt.title('Exportation du top 3 entre 1980 et 2021')
plt.show()
# -


