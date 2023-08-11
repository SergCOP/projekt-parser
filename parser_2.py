from bs4 import BeautifulSoup
import requests


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

with open("book1.json", 'w', encoding="utf-8") as file:
    file.write(f" Name: {str(book_name)}")
    lines = ["\n"]
    file.writelines(lines)
    file.write(f" Description: {str(description)}") 
    lines = ["\n"]
    file.writelines(lines)
    file.write(f" Availability: {str(availability)}") 
    lines = ["\n"]


#print(book_name)                                            # Оставил на время
#print(description)                                          # Оставил на время
#print(availability)                                         # Оставил на время


     
