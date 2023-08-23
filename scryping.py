import requests
from bs4 import BeautifulSoup as BS


r = requests.get("https://re.kufar.by/l/belarus/snyat/kvartiru-dolgosrochno?cur=USD&size=30&cursor=eyJ0IjoiYWJzIiwiZiI6dHJ1ZSwicCI6MX0=")
html = BS(r.content, 'html.parser')

for el in html.select(".styles_wrapper__Q06m9"):
    title = el.select(".styles_parameters__7zKlL")
    titles = el.select(".styles_price__byr__lLSfd")
    price = el.select(".styles_price__usd__HpXMa")
    print(title[0].text)
    print(titles[0].text)
    for i in price:
        print(i.text)
    print("_______")
input()
