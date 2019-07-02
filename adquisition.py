import pandas as pd
import requests
from bs4 import BeautifulSoup



def read(df):
       socioeconomic = pd.read_csv(df, encoding='latin1')
       return socioeconomic

def scrap(url):
       res = requests.get(url)
       soup = BeautifulSoup(res.content,'html.parser')
       rows=soup.select('tr')
       resultado = []
       for i in range(199):
              q=rows[i+1].select('td')
              filas={
                  "id": str(q[0].text),
                  "country":str(q[1].text),
                  "1980": str(q[2].text).strip(),
                  "1985": str(q[3].text).strip(),
                  "1990": str(q[4].text).strip(),
                  "2000": str(q[5].text).strip(),
                  "2005": str(q[6].text).strip(),
                  "2006": str(q[7].text).strip(),
                  "2007": str(q[8].text).strip(),
                  "2008": str(q[9].text).strip(),
                  "2009": str(q[10].text).strip(),
                  "2010": str(q[11].text).strip(),
                  "2011": str(q[12].text).strip(),
                  "2012": str(q[13].text).strip(),
                  "2013": str(q[14].text).strip()
              }
              resultado.append(filas)
       return resultado