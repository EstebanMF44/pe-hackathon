
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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


# On fait exactement le même travail, mais cette fois-ci sur l'exportation.

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


## Le but de cette partie est de s'intéresser à la consommation totale et la prodution totale par année de chaque continent en kwH 
df = pd.read_csv('world-country-electricity.csv',na_values=("--","ie"))

df_cons = df[df['Features'] == 'net consumption']
df_gen = df[df['Features'] == 'net generation']

Africa_cons = df_cons[df_cons['Region'] == 'Africa']
Africa_gen = df_gen[df_gen['Region'] == 'Africa']

Eurasia_cons = df_cons[df_cons['Region'] == 'Eurasia']
Eurasia_gen = df_gen[df_gen['Region'] == 'Eurasia']

Europe_cons = df_cons[df_cons['Region'] == 'Europe']
Europe_gen = df_gen[df_gen['Region'] == 'Europe']

Asia_Oceania_cons = df_cons[df_cons['Region'] == 'Asia & Oceania']
Asia_Oceania_gen = df_gen[df_gen['Region'] == 'Asia & Oceania']

Middle_East_cons = df_cons[df_cons['Region'] == 'Middle East']
Middle_East_gen = df_gen[df_gen['Region'] == 'Middle East']

North_America_cons = df_cons[df_cons['Region'] == 'North America']
North_America_gen = df_gen[df_gen['Region'] == 'North America']

Central_South_America_cons = df_cons[df_cons['Region'] == 'Central & South America']
Central_South_America_gen = df_gen[df_gen['Region'] == 'Central & South America']



L = []
for i in range (1980,2022,1) : 
    L.append(str(i))


Africa_cons_ok = Africa_cons[L]

Af_cons_sommes_par_annee = Africa_cons_ok.sum(axis=0)

Af_cons_sommes = Af_cons_sommes_par_annee.values.tolist()
X = np.arange(1980,2022,1)
plt.plot(X,Af_cons_sommes,label ='Afrique')

plt.xlabel("Année")
plt.ylabel("Somme")
plt.title("Somme des valeurs de consommation par année")
plt.yticks([])
plt.xticks([1980,1988, 1993, 1998, 2003, 2008, 2013, 2018, 2021])


EUA_cons_ok = Eurasia_cons[L]

EUA_cons_sommes_par_annee = EUA_cons_ok.sum(axis=0)
EUA_cons_sommes = EUA_cons_sommes_par_annee.values.tolist()

plt.plot(X,EUA_cons_sommes, label ='Eurasia')


EU_cons_ok = Europe_cons[L]

EU_cons_sommes_par_annee = EU_cons_ok.sum(axis=0)
EU_cons_sommes = EU_cons_sommes_par_annee.values.tolist()

plt.plot(X,EU_cons_sommes,label ='Europe')

AO_cons_ok = Asia_Oceania_cons[L]

AO_cons_sommes_par_annee = AO_cons_ok.sum(axis=0)
AO_cons_sommes = AO_cons_sommes_par_annee.values.tolist()

#plt.plot(X,AO_cons_sommes,label ='Asie et Oceanie') l'Asie tasse les autres variations donc on choisit ou non de le plot

ME_cons_ok = Middle_East_cons[L]
ME_cons_sommes_par_annee = ME_cons_ok.sum(axis=0)
ME_cons_sommes = ME_cons_sommes_par_annee.values.tolist()

plt.plot(X,ME_cons_sommes,label='Middle East')


NO_cons_ok = North_America_cons[L]
NO_cons_sommes_par_annee = NO_cons_ok.sum(axis=0)
NO_cons_sommes = NO_cons_sommes_par_annee.values.tolist()

plt.plot(X,NO_cons_sommes,label = 'North America')

CS_cons_ok = Central_South_America_cons[L]
CS_cons_sommes_par_annee = CS_cons_ok.sum(axis=0)
CS_cons_sommes = CS_cons_sommes_par_annee.values.tolist()

plt.plot(X,CS_cons_sommes,label='Central South America')
plt.legend()
plt.show()


Africa_gen_ok = Africa_gen[L]

Af_gen_sommes_par_annee = Africa_gen_ok.sum(axis=0)

Af_gen_sommes = Af_gen_sommes_par_annee.values.tolist()
X = np.arange(1980,2022,1)
plt.plot(X,Af_gen_sommes,label ='Afrique')

plt.xlabel("Année")
plt.ylabel("Somme")
plt.title("Somme des valeurs de production par année")
plt.yticks([])
plt.xticks([1980,1988, 1993, 1998, 2003, 2008, 2013, 2018, 2021])


EUA_gen_ok = Eurasia_gen[L]

EUA_gen_sommes_par_annee = EUA_gen_ok.sum(axis=0)
EUA_gen_sommes = EUA_gen_sommes_par_annee.values.tolist()

plt.plot(X,EUA_gen_sommes, label ='Eurasia')


EU_gen_ok = Europe_gen[L]

EU_gen_sommes_par_annee = EU_gen_ok.sum(axis=0)
EU_gen_sommes = EU_gen_sommes_par_annee.values.tolist()

plt.plot(X,EU_gen_sommes,label ='Europe')

AO_gen_ok = Asia_Oceania_gen[L]

AO_gen_sommes_par_annee = AO_gen_ok.sum(axis=0)
AO_gen_sommes = AO_gen_sommes_par_annee.values.tolist()

#plt.plot(X,AO_gen_sommes,label ='Asie et Oceanie') l'Asie tasse les autres variations donc on choisit ou non de le plot

ME_gen_ok = Middle_East_gen[L]
ME_gen_sommes_par_annee = ME_gen_ok.sum(axis=0)
ME_gen_sommes = ME_gen_sommes_par_annee.values.tolist()

plt.plot(X,ME_gen_sommes,label='Middle East')


NO_gen_ok = North_America_gen[L]
NO_gen_sommes_par_annee = NO_gen_ok.sum(axis=0)
NO_gen_sommes = NO_gen_sommes_par_annee.values.tolist()

plt.plot(X,NO_gen_sommes,label = 'North America')

CS_gen_ok = Central_South_America_gen[L]
CS_gen_sommes_par_annee = CS_gen_ok.sum(axis=0)
CS_gen_sommes = CS_gen_sommes_par_annee.values.tolist()

plt.plot(X,CS_gen_sommes,label='Central South America')
plt.legend()
plt.show()

### fin de la partie 

