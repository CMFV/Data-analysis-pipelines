import pandas as pd
import adquisition

def clean_dataset(socioeconomic):
    socioeconomic = socioeconomic.drop(socioeconomic[socioeconomic["year"]<=1970].index)
    socioeconomic['country_year'] = socioeconomic[['country','year']].apply(lambda x : '{} {}'.format(x[0],x[1]), axis=1)
    socioeconomic.sort_values(by=['country_year'], inplace=True)
    socioeconomic_final=socioeconomic.reset_index()
    socioeconomic_final['country_year'].value_counts()
    return socioeconomic_final

def clean_web_scrap(resultado):
    health_index = pd.DataFrame(resultado)
    health_index.drop(['id','1985','2005','2006','2007','2008','2009','2011','2012','2013'], axis=1, inplace=True)
    health_index_melted= pd.melt(health_index, id_vars=['country'], value_vars=['1980', '1990','2000', '2010'], var_name='Year', value_name='health')
    health_index_melted.sort_values(by=['country'], inplace=True)
    health_index_melted['Year'] = health_index_melted['Year'].apply(pd.to_numeric) 
    health_index_melted['country_year'] = health_index_melted[['country','Year']].apply(lambda x : '{} {}'.format(x[0],x[1]), axis=1)
    health_index_melted.sort_values(by=['country_year'], inplace=True)
    health_index_melted.drop(['country','Year'], axis=1, inplace=True)
    health_final=health_index_melted.reset_index()
    lista_health=[]
    for i in health_final.country_year:
        lista_health.append(i.lstrip())
    health_final.country_year=lista_health
    return health_final




