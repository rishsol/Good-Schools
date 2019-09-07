import numpy as np

def scientificToStandard(str):
    index = str.index('e')
    significand = int(str[0: index], 10)
    order_of_magnitude = int(str[index + 1:] , 10)

    return significand * (10**order_of_magnitude)


path = '/Users/rishabsolanki09@gmail.com/Downloads/Sale_Prices_City.csv'
data = np.genfromtxt(path, dtype = str, delimiter= ',')

i = 1
while i < len(data[0]):
    if data[i][2] != 'New Jersey':
        data = np.delete(data, i, 0)
        i -= 1
    else:
        i += 1

all_info = data[:, [1, -3]]

for num in np.nditer(all_info[:, 1], op_flags = ['readwrite']):
    try:
        num[...] = int(num)
    except ValueError:
        if str(num) == '':
            num[...] = 0
        else:
            num[...] = scientificToStandard(str(num))

print(all_info)