# Le but de ce code est de renvoyer un tableau contenant le pourcentage représentés par les pertes d'énergie par rapport à la consommation totale d'énergie pour chaque pays sur la période temporelle 1980/2021. Les dernières lignes de codes renvoient le graphe de l'évolution de ce ratio pour le cas de l'Afghanistan.
import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

import seaborn as sns

df = pd.read_csv('world-country-electricity.csv', na_values= ['--' , 'ie'])



df

df['Features'] = df['Features'].str.strip()

df['Country'] = df['Country'].str.strip()













ratio_pertes = df.drop(columns = ['Features' , 'Region'])

ratio_pertes

ratio_pertes.drop_duplicates('Country')



df_pertes_consos = df[df['Features'].isin(['net consumption','distribution losses'])]

years = df_pertes_consos.columns[3::]
years

df_all = df_pertes_consos.pivot_table(columns = ['Country', 'Features'] , values = years)











countries = ratio_pertes.columns

countries

ratio_pertes = ratio_pertes.pivot_table(columns = ['Country'] , values = years)

ratio_pertes

ratio_pertes['Afghanistan'] = df_all['Afghanistan', 'distribution losses']/df_all['Afghanistan', 'net consumption']

ratio_pertes





for i in countries:
    ratio_pertes[i] = df_all[i, 'distribution losses']/df_all[i, 'net consumption']

ratio_pertes

ratio_pertes_epures = ratio_pertes.dropna(axis = 1)

ratio_pertes_epures

x = ratio_pertes_epures['Afghanistan']
plt.figure(figsize=(20, 50))
plt.plot(years, x)
plt.xlabel('Année')
plt.ylabel('Ratio')
plt.show()




