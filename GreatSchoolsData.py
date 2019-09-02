import pandas as pd
from bs4 import BeautifulSoup
import requests
from pandas.io.html import read_html

url = 'https://en.wikipedia.org/wiki/List_of_municipalities_in_New_Jersey'

data = pd.read_html(url, attrs= {'class': 'wikitable sortable'})

nj_cities_table = data[0]
nj_cities = nj_cities_table['Municipality']

print(nj_cities)

