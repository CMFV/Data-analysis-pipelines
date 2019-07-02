import pandas as pd
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
import os

import adquisition
import clean
import analysis

def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    csv_name=dir_path+'/GLOB.SES.csv'
    socioeconomic=adquisition.read(csv_name)
    url='http://hdr.undp.org/en/content/health-index'
    resultado=adquisition.scrap(url)
    socioeconomic_final= clean.clean_dataset(socioeconomic)
    health_final=clean.clean_web_scrap(resultado)
    socioeconomic_health=analysis.merging_dataframes(socioeconomic_final, health_final)
    correl_matrix=analysis.correlation_calc(socioeconomic_health)
    analysis.plot_correlation(correl_matrix)
    analysis.plot_SES_yrseduc_health(socioeconomic_health)
    analysis.plot_SES_country_health(socioeconomic_health)
    analysis.plot_SES_yrseduc_SES(socioeconomic_health)

if __name__=="__main__":
    main()