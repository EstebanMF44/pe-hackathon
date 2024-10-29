# file Alexis 

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

df = pd.read_csv("world-country-electricity.csv", na_values = ["--", "ie"])
df.Features.str.strip
df.Region.str.strip


# Donne la datframe des 5 pays ayant la plus grande croissance en génération
mask = (df["Features"] == "net generation") 
df2 = df[mask]
df2["1980"] = pd.to_numeric(df["1980"])
df2["2021"] = pd.to_numeric(df["2021"])
df2["évolution"] = (df2["2021"]-df2["1980"])/df2["1980"]
df2_sorted = df2.sort_values(by = "évolution", ascending = False)
rise_generation = df2_sorted.iloc[1:6]

# Tracé de l'évolution de la génération de 3 premiers pays au cours du temps 
X = np.arange(1980, 2022)
f1 = rise_generation.iloc[0, 3:-1].tolist()
f2 = rise_generation.iloc[1, 3:-1].tolist()
f3 = rise_generation.iloc[2, 3:-1].tolist()
plt.plot(X, f1, label = rise_generation.iloc[0, 0])
plt.plot(X, f2, label = rise_generation.iloc[1, 0])
plt.plot(X, f3, label = rise_generation.iloc[2,0])
plt.legend()
plt.title('Top 3 des pays ayant eu la plus grande croissnace en terme de production energie')
plt.show()


#même chose mais avec les pays les plus consommateurs 
mask = (df["Features"] == "net consumption") 
df2 = df[mask]
df2["1980"] = pd.to_numeric(df["1980"])
df2["2021"] = pd.to_numeric(df["2021"])
df2["évolution"] = (df2["2021"]-df2["1980"])/df2["1980"]
df2_sorted = df2.sort_values(by = "évolution", ascending = False)
rise_cons = df2_sorted.iloc[1:6]
rise_cons 

# Tracé de l'évolution de la consommation de 3 premiers pays au cours du temps 
X = np.arange(1980, 2022)
f1 = rise_cons.iloc[0, 3:-1].tolist()
f2 = rise_cons.iloc[1, 3:-1].tolist()
f3 = rise_cons.iloc[2, 3:-1].tolist()
plt.plot(X, f1, label = rise_cons.iloc[0, 0])
plt.plot(X, f2, label = rise_cons.iloc[1, 0])
plt.plot(X, f3, label = rise_cons.iloc[2,0])
plt.legend()
plt.title('Top 3 des pays ayant eu la plus grande croissnace en terme de production energie')
plt.show()

# +
X = np.arange(1980, 2022)

# fonction donnant le dataframe des 5 plus grand générateur ou consommateur d'une région 
def tab_par_region(region, feature):
    mask = (df["Features"] == feature)|(df["Region"] == region)
    df2 = df[mask]
    df2["1980"] = pd.to_numeric(df["1980"])
    df2["2021"] = pd.to_numeric(df["2021"])
    df2["évolution"] = (df2["2021"]-df2["1980"])/df2["2021"]
    df2_sorted = df2.sort_values(by = "évolution", ascending = False)
    return df2.iloc[1:6]
    
# Tracé de celui d'Afrique par exemple

df = tab_par_region("Africa","net consumption")
f1 = df.iloc[0, 3:-1].tolist()
f2 = df.iloc[1, 3:-1].tolist()
f3 = df.iloc[2, 3:-1].tolist()
plt.plot(X, f1, label = df.iloc[0, 0])
plt.plot(X, f2, label = df.iloc[1, 0])
plt.plot(X, f3, label = df.iloc[2,0])
plt.legend()
plt.title('Top 3')
plt.show()



