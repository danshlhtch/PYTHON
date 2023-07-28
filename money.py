'''
import requests
data = requests.get('https://free.currconv.com/api/v7/convert?apiKey=YOUR_API_KEY&q=USD_RUB&compact=ultra').json()
print (data['USD_RUB'])
'''

import random
a = 1
for a in range (1,1000000):
    print(a)
    if a == 807000:
        break
print("_________Программа успешно запущена_________")