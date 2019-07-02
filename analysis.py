import matplotlib.pyplot as plt
import seaborn as sns
import clean
import adquisition
import pandas as pd


def merging_dataframes(socioeconomic_final, health_final):
    socioeconomic_health = socioeconomic_final.merge(health_final, how='outer', on=['country_year'])
    socioeconomic_health=socioeconomic_health.dropna()
    socioeconomic_health.drop(['index_x', 'unid', 'wbid', 'index_y', 'country_year', 'popshare'], axis=1, inplace=True)
    socioeconomic_health[["SES","health","yrseduc"]] = socioeconomic_health[["SES", "health","yrseduc"]].apply(pd.to_numeric)
    socioeconomic_health.set_index('country')
    return socioeconomic_health


def correlation_calc(socioeconomic_health):
    correl_matrix = socioeconomic_health.corr()
    return correl_matrix

def plot_correlation(correl_matrix):
    sns.heatmap(correl_matrix, 
        xticklabels=correl_matrix.columns,
        yticklabels=correl_matrix.columns)
    plt.show()

def plot_SES_yrseduc_health(socioeconomic_health):
    socioeconomic_health.plot.scatter(x='SES', y='yrseduc', s=socioeconomic_health['health'] * 200)
    plt.show()

def plot_SES_country_health(socioeconomic_health):
    socioeconomic_health.groupby("country")[['health']].mean().plot.barh( figsize=(25,100), stacked=True)
    plt.show()

def plot_SES_yrseduc_SES(socioeconomic_health):
    socioeconomic_health[['yrseduc','SES']].plot(figsize=(25,10), stacked=True)
    plt.show()