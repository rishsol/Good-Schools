import pandas as pd
from bs4 import BeautifulSoup
import requests

url = 'https://en.wikipedia.org/wiki/List_of_municipalities_in_New_Jersey'
parsed_url = requests.get(url)

soup = BeautifulSoup(parsed_url.content, 'html.parser')
soup.prettify()

table = soup.find('table', {'class': 'wikitable sortable'})
#links = table.findAll('a')
print(table.text)

nj_cities = []
nj_cities_df = pd.DataFrame()
#for link in links:
 #  nj_cities.append(link.get('title'))


#nj_cities_df['NJ Cities'] = nj_cities

#print(nj_cities_df)
