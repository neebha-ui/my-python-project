import requests
from bs4 import BeautifulSoup
import pandas as pd

response = requests.get("https://books.toscrape.com/")

#print(response)

soup = BeautifulSoup(response.content,'html.parser')
#print(soup)

names = soup.find_all('a',title = True)
#print(names)

name = []
for i in names[0:10]:
    result = i["title"]
    name.append(result)
#print(name)
prices = soup.find_all("p","price_color")
#print(prices)

price =[]
for i in prices[0:10]:
    result = i.get_text()
    price.append(result)

#print(price)

result = [float(i.replace("£",""))for i in price]
#print(result)  


images = soup.find_all("img",class_= "thumbnail")
#print(images)

image = []
for i in images[0:10]:
    data = i['src']
    image.append(data)
#print(image) 


sample = "https://books.toscrape.com/"
result_2 = [sample+i for i in image]
#print(result)

df = pd.DataFrame()
print(df)

df["Names"] = name
df["Prices"] = result
df["Images"] = result_2

print(df)

df.to_csv("books.csv")