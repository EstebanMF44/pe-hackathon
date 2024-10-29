

# +
# L'objet de cette partie est de trouver les pays qui ont eu les plus grosses explosions en terme d'importation / exportation depuis 1980,
# et de représenter cette évolution. Calculer simplement le ratio entre importation (ou exportation) entre 2021 et 1980 a donné des résultats
# non significatifs, valorisant des pays dont l'importation (ou l'exportation) était pratiquement nulle au départ et qui a connu une légère
# augmentation. 
# Pour pallier ce problème et avoir un résultat plus parlant, nous décidons de retenir l'écart type 
# à savoir [ (importation en 2021 - importation en 1980 )/ importation en 2021 ] à la place (et de même avec l'exportation)

# Dans un premier temps, nous nous focalisons sur l'étude de l'importation.

df = pd.read_csv("world-country-electricity.csv", na_values=("--", "ie")) 

df1 = df[(df['Features'] == 'imports ')] #on met un masque pour garder uniquement les statistiques liées à l'importation

df1['1980']=pd.to_numeric(df1['1980'])
df1['2021']=pd.to_numeric(df1['2021']) #les valeurs du tableau sont de type str...


df1['Ratio'] = (df1['2021']-df1['1980'])/(df1['2021']) #on crée une nouvelle colonne qui calcul l'écart relatif entre l'importation entre 
#1980 et 2021

df2=df1.sort_values('Ratio', ascending = False) #on la trie pour pouvoir récupérer le top 3

mask= df2.Ratio != 1.0 #certains pays n'importaient rien en 1980 (souvent pour des raisons politiques, type embargo etc.) Nous avons décidé 
#de ne pas retenir ces pays d'où la condition écrite

df3=df2[mask]

df4=df3.head(3) #on retient le top 3 

df5=df4.iloc[0, 3:-1].tolist()
df6=df4.iloc[1, 3:-1].tolist()
df7=df4.iloc[2, 3:-1].tolist() #on transforme les dataframes en listes pour faciliter le tracé du graphe


X=np.arange(1980, 2022, 1)
Y1=df5
Y2=df6
Y3=df7
plt.plot(X,Y1, label='Inde')
plt.plot(X,Y2, label='Royaume-Uni')
plt.plot(X,Y3, label='Argentine')
plt.legend()
plt.title('Importation du top 3 entre 1980 et 2021')
plt.show()

# +
#on fait exactement le même travail, mais cette fois-ci sur l'exportation

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


