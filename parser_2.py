from bs4 import BeautifulSoup
import requests
import json

url = 'https://www.labirint.ru/books/844691/'
HEADERS = ({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.0.2530 Yowser/2.5 Safari/537.36', 
            'Accept-Language': 'ru-RU, en;q=0.5'})
response = requests.get(url, headers= HEADERS)


soup = BeautifulSoup(response.text, "html.parser")
#with open('output1.html', 'w', encoding="utf-8") as file:    # Отключил до востребования
    #file.write(str(soup))                                    # Отключил до востребования

book_name = soup.find_all('h1')[0]
description = soup.find_all('p')[0]
availability = soup.find_all("div", class_="prodtitle-availibility rang-available")[0]


python_obj = {'name': str(book_name), 'description': str(description), 'availability': str(availability)}

with open('books1.json', 'w', encoding="utf-8") as file:
    json.dump(python_obj, file)


with open('books1.json', 'r', encoding="utf-8") as f:       #Читка из books1.json
    data = json.load(f)
    #print(json.dumps(data,
                      #sort_keys=False,
                      #indent=4,
                      #ensure_ascii=False,
                      #separators=(',', ': ')))

with open('books1.json', 'a', encoding="utf-8") as file:
    file.write(str(data))

     
