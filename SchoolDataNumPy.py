import numpy as np

path = '/Users/rishabsolanki09@gmail.com/Downloads/Sale_Prices_City.csv'
data = np.genfromtxt(path, dtype = str, delimiter= ',')

i = 1
while i < len(data[0]):
    if data[i][2] != 'New Jersey':
        data = np.delete(data, i, 0)
        i -= 1
    else:
        i += 1

#nj_cities = data[1]
#home_price = data[-1]

#important_info = []
#important_info.append(nj_cities)
print(data)
