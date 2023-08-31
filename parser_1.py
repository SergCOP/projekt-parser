from bs4 import BeautifulSoup
import requests

url0 = 'https://www.labirint.ru/books/844691/'
HEADERS = ({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.0.2530 Yowser/2.5 Safari/537.36', 
            'Accept-Language': 'ru-RU, en;q=0.5'})
response = requests.get(url0, headers= HEADERS)

soup = BeautifulSoup(response.text, "html.parser")
#with open('output1.html', 'w', encoding="utf-8") as file:    # До востребования
    #file.write(str(soup))                                    # До востребования

book_name = soup.find_all('h1')[0]
description = soup.find_all('p')[0]
availability = soup.find_all('div', attrs={'class':'prodtitle-availibility rang-available'})

with open('book_library/books.json', 'w', encoding="utf-8") as file:
    file.write(f" Name: {str(book_name)}")
    lines = ["\n"]
    file.writelines(lines)
    file.write(f" Description: {str(description)}") 
    lines = ["\n"]
    file.writelines(lines)
    file.write(f" Availability: {str(availability)}") 
    lines = ["\n"]


#print(book_name)                                              # Оставил на время
#print(description)                                            # Оставил на время
#print(availability)                                           # Оставил на время


url1 = 'https://www.labirint.ru/books/954714/' 
HEADERS = ({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.0.2530 Yowser/2.5 Safari/537.36', 
            'Accept-Language': 'ru-RU, en;q=0.5'})
response = requests.get(url1, headers= HEADERS)

soup = BeautifulSoup(response.text, "html.parser")
#with open('output1.html', 'w', encoding="utf-8") as file:    # До востребования
    #file.write(str(soup))                                    # До востребования

book_name = soup.find_all('h1')[0]
description = soup.find_all('p')[0]
availability = soup.find_all('div', attrs={'class':'prodtitle-availibility rang-available'})

with open('book_library/books1.json', 'w', encoding="utf-8") as file:
    file.write(f" Название книги: {str(book_name)}")
    lines = ["\n"]
    file.writelines(lines)
    file.write(f" Описание: {str(description)}") 
    lines = ["\n"]
    file.writelines(lines)
    file.write(f" Наличие: {str(availability)}") 
    lines = ["\n"]


#print(book_name)                                              # Оставил на время
#print(description)                                            # Оставил на время
#print(availability)                                           # Оставил на время


url2 = 'https://www.labirint.ru/books/512950/'
HEADERS = ({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.0.2530 Yowser/2.5 Safari/537.36', 
            'Accept-Language': 'ru-RU, en;q=0.5'})
response = requests.get(url2, headers= HEADERS)

soup = BeautifulSoup(response.text, "html.parser")
#with open('output1.html', 'w', encoding="utf-8") as file:    # До востребования
    #file.write(str(soup))                                    # До востребования

book_name = soup.find_all('h1')[0]
description = soup.find_all('p')[0]
availability = soup.find_all('div', attrs={'class':'prodtitle-availibility rang-available'})

with open('book_library/books2.json', 'w', encoding="utf-8") as file:
    file.write(f" Название книги: {str(book_name)}")
    lines = ["\n"]
    file.writelines(lines)
    file.write(f" Описание: {str(description)}") 
    lines = ["\n"]
    file.writelines(lines)
    file.write(f" Наличие: {str(availability)}") 
    lines = ["\n"]


#print(book_name)                                              # Оставил на время
#print(description)                                            # Оставил на время
#print(availability)                                           # Оставил на время


url3 = 'https://www.labirint.ru/books/846543/'
HEADERS = ({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.0.2530 Yowser/2.5 Safari/537.36', 
            'Accept-Language': 'ru-RU, en;q=0.5'})
response = requests.get(url3, headers= HEADERS)

soup = BeautifulSoup(response.text, "html.parser")
#with open('output1.html', 'w', encoding="utf-8") as file:    # До востребования
    #file.write(str(soup))                                    # До востребования

book_name = soup.find_all('h1')[0]
availability = soup.find_all('div', attrs={'class':'prodtitle-availibility rang-available'})
description = soup.find_all('p')[0]


with open('book_library/books3.json', 'w', encoding="utf-8") as file:
    file.write(f" Название книги: {str(book_name)}")
    lines = ["\n"]
    file.writelines(lines)
    file.write(f" Описание: {str(description)}") 
    lines = ["\n"]
    file.writelines(lines)
    file.write(f" Наличие: {str(availability)}") 
    lines = ["\n"]
 

#print(book_name)                                              # Оставил на время
#print(description)                                            # Оставил на время
#print(availability)                                           # Оставил на время



url4 = 'https://www.labirint.ru/books/632959/'
HEADERS = ({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.0.2530 Yowser/2.5 Safari/537.36', 
            'Accept-Language': 'ru-RU, en;q=0.5'})
response = requests.get(url4, headers= HEADERS)

soup = BeautifulSoup(response.text, "html.parser")
#with open('output1.html', 'w', encoding="utf-8") as file:    # До востребования
    #file.write(str(soup))                                    # До востребования

book_name = soup.find_all('h1')[0]
availability = soup.find_all('div', attrs={'class':'prodtitle-availibility rang-available'})
description = soup.find_all('p')[0]

with open('book_library/books4.json', 'w', encoding="utf-8") as file:
    file.write(f" Название книги: {str(book_name)}")
    lines = ["\n"]
    file.writelines(lines)
    file.write(f" Описание: {str(description)}") 
    lines = ["\n"]
    file.writelines(lines)
    file.write(f" Наличие: {str(availability)}") 
    lines = ["\n"]


#print(book_name)                                              # Оставил на время
#print(description)                                            # Оставил на время
#print(availability)                                           # Оставил на время


url5 = 'https://www.labirint.ru/books/874739/'
HEADERS = ({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.0.2530 Yowser/2.5 Safari/537.36', 
            'Accept-Language': 'ru-RU, en;q=0.5'})
response = requests.get(url5, headers= HEADERS)

soup = BeautifulSoup(response.text, "html.parser")
#with open('output1.html', 'w', encoding="utf-8") as file:    # До востребования
    #file.write(str(soup))                                    # До востребования


book_name = soup.find_all('h1')[0]
availability = soup.find_all('div', attrs={'class':'prodtitle-availibility rang-available'})
description = soup.find_all('p')[0]

with open('book_library/books5.json', 'w', encoding="utf-8") as file:
    file.write(f" Название книги: {str(book_name)}")
    lines = ["\n"]
    file.writelines(lines)
    file.write(f" Описание: {str(description)}") 
    lines = ["\n"]
    file.writelines(lines)
    file.write(f" Наличие: {str(availability)}") 
    lines = ["\n"]


#print(book_name)                                              # Оставил на время
#print(description)                                            # Оставил на время
#print(availability)                                           # Оставил на время


url6 = 'https://www.labirint.ru/books/512884/'
HEADERS = ({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.0.2530 Yowser/2.5 Safari/537.36', 
            'Accept-Language': 'ru-RU, en;q=0.5'})
response = requests.get(url6, headers= HEADERS)

soup = BeautifulSoup(response.text, "html.parser")
#with open('output1.html', 'w', encoding="utf-8") as file:    # До востребования
    #file.write(str(soup))                                    # До востребования

book_name = soup.find_all('h1')[0]
description = soup.find_all('p')[0]
availability = soup.find_all('div', attrs={'class':'prodtitle-availibility rang-available'})

with open('book_library/books6.json', 'w', encoding="utf-8") as file:
    file.write(f" Название книги: {str(book_name)}")
    lines = ["\n"]
    file.writelines(lines)
    file.write(f" Описание: {str(description)}") 
    lines = ["\n"]
    file.writelines(lines)
    file.write(f" Наличие: {str(availability)}") 
    lines = ["\n"]


#print(book_name)                                              # Оставил на время
#print(description)                                            # Оставил на время
#print(availability)                                           # Оставил на время


url7 = 'https://www.labirint.ru/books/601752/'
HEADERS = ({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.0.2530 Yowser/2.5 Safari/537.36', 
            'Accept-Language': 'ru-RU, en;q=0.5'})
response = requests.get(url6, headers= HEADERS)

soup = BeautifulSoup(response.text, "html.parser")
#with open('output1.html', 'w', encoding="utf-8") as file:    # До востребования
    #file.write(str(soup))                                    # До востребования

book_name = soup.find_all('h1')[0]
availability = soup.find_all('div', attrs={'class':'prodtitle-availibility rang-available'})
description = soup.find_all('p')[0]

with open('book_library/books7.json', 'w', encoding="utf-8") as file:
    file.write(f" Название книги: {str(book_name)}")
    lines = ["\n"]
    file.writelines(lines)
    file.write(f" Описание: {str(description)}") 
    lines = ["\n"]
    file.writelines(lines)
    file.write(f" Наличие: {str(availability)}") 
    lines = ["\n"]


#print(book_name)                                              # Оставил на время
#print(description)                                            # Оставил на время
#print(availability)                                           # Оставил на время


url8 = 'https://www.labirint.ru/books/620557/'
HEADERS = ({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.0.2530 Yowser/2.5 Safari/537.36', 
            'Accept-Language': 'ru-RU, en;q=0.5'})
response = requests.get(url8, headers= HEADERS)

soup = BeautifulSoup(response.text, "html.parser")
#with open('output1.html', 'w', encoding="utf-8") as file:    # До востребования
    #file.write(str(soup))                                    # До востребования

book_name = soup.find_all('h1')[0]
availability = soup.find_all('div', attrs={'class':'prodtitle-availibility rang-available'})
description = soup.find_all('p')[0]

with open('book_library/books8.json', 'w', encoding="utf-8") as file:
    file.write(f" Название книги: {str(book_name)}")
    lines = ["\n"]
    file.writelines(lines)
    file.write(f" Описание: {str(description)}") 
    lines = ["\n"]
    file.writelines(lines)
    file.write(f" Наличие: {str(availability)}") 
    lines = ["\n"]


#print(book_name)                                              # Оставил на время
#print(description)                                            # Оставил на время
#print(availability)                                           # Оставил на время


url9 = 'https://www.labirint.ru/books/795012/'
HEADERS = ({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.0.2530 Yowser/2.5 Safari/537.36', 
            'Accept-Language': 'ru-RU, en;q=0.5'})
response = requests.get(url9, headers= HEADERS)

soup = BeautifulSoup(response.text, "html.parser")
#with open('output1.html', 'w', encoding="utf-8") as file:    # До востребования
    #file.write(str(soup))                                    # До востребования

book_name = soup.find_all('h1')[0]
availability = soup.find_all('div', attrs={'class':'prodtitle-availibility rang-available'})
description = soup.find_all('p')[0]

with open('book_library/books9.json', 'w', encoding="utf-8") as file:
    file.write(f" Название книги: {str(book_name)}")
    lines = ["\n"]
    file.writelines(lines)
    file.write(f" Описание: {str(description)}") 
    lines = ["\n"]
    file.writelines(lines)
    file.write(f" Наличие: {str(availability)}") 
    lines = ["\n"]


#print(book_name)                                              # Оставил на время
#print(description)                                            # Оставил на время
#print(availability)                                           # Оставил на время


url10 = 'https://www.labirint.ru/books/630003/'
HEADERS = ({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.0.2530 Yowser/2.5 Safari/537.36', 
            'Accept-Language': 'ru-RU, en;q=0.5'})
response = requests.get(url10, headers= HEADERS)

soup = BeautifulSoup(response.text, "html.parser")
#with open('output1.html', 'w', encoding="utf-8") as file:    # До востребования
    #file.write(str(soup))                                    # До востребования

book_name = soup.find_all('h1')[0]
availability = soup.find_all('div', attrs={'class':'prodtitle-availibility rang-available'})
description = soup.find_all('p')[0]

with open('book_library/books10.json', 'w', encoding="utf-8") as file:
    file.write(f" Название книги: {str(book_name)}")
    lines = ["\n"]
    file.writelines(lines)
    file.write(f" Описание: {str(description)}") 
    lines = ["\n"]
    file.writelines(lines)
    file.write(f" Наличие: {str(availability)}") 
    lines = ["\n"]


#print(book_name)                                              # Оставил на время
#print(description)                                            # Оставил на время
#print(availability)                                           # Оставил на время


url11 = 'https://www.labirint.ru/books/473786/'
HEADERS = ({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.0.2530 Yowser/2.5 Safari/537.36', 
            'Accept-Language': 'ru-RU, en;q=0.5'})
response = requests.get(url11, headers= HEADERS)

soup = BeautifulSoup(response.text, "html.parser")
#with open('output1.html', 'w', encoding="utf-8") as file:    # До востребования
    #file.write(str(soup))                                    # До востребования

book_name = soup.find_all('h1')[0]
availability = soup.find_all('div', attrs={'class':'prodtitle-availibility rang-available'})
description = soup.find_all('p')[0]

with open('book_library/books11.json', 'w', encoding="utf-8") as file:
    file.write(f" Название книги: {str(book_name)}")
    lines = ["\n"]
    file.writelines(lines)
    file.write(f" Описание: {str(description)}") 
    lines = ["\n"]
    file.writelines(lines)
    file.write(f" Наличие: {str(availability)}") 
    lines = ["\n"]
 

#print(book_name)                                              # Оставил на время
#print(description)                                            # Оставил на время
#print(availability)                                           # Оставил на время


url12 = 'https://www.labirint.ru/books/376836/'
HEADERS = ({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.0.2530 Yowser/2.5 Safari/537.36', 
            'Accept-Language': 'ru-RU, en;q=0.5'})
response = requests.get(url12, headers= HEADERS)

soup = BeautifulSoup(response.text, "html.parser")
#with open('output1.html', 'w', encoding="utf-8") as file:    # До востребования
    #file.write(str(soup))                                    # До востребования

book_name = soup.find_all('h1')[0]
availability = soup.find_all('div', attrs={'class':'prodtitle-availibility rang-available'})
description = soup.find_all('p')[0]

with open('book_library/books12.json', 'w', encoding="utf-8") as file:
    file.write(f" Название книги: {str(book_name)}")
    lines = ["\n"]
    file.writelines(lines)
    file.write(f" Описание: {str(description)}") 
    lines = ["\n"]
    file.writelines(lines)
    file.write(f" Наличие: {str(availability)}") 
    lines = ["\n"]


#print(book_name)                                              # Оставил на время
#print(description)                                            # Оставил на время
#print(availability)                                           # Оставил на время


url13 = 'https://www.labirint.ru/books/831913/'
HEADERS = ({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.0.2530 Yowser/2.5 Safari/537.36', 
            'Accept-Language': 'ru-RU, en;q=0.5'})
response = requests.get(url13, headers= HEADERS)

soup = BeautifulSoup(response.text, "html.parser")
#with open('output1.html', 'w', encoding="utf-8") as file:    # До востребования
    #file.write(str(soup))                                    # До востребования

book_name = soup.find_all('h1')[0]
availability = soup.find_all('div', attrs={'class':'prodtitle-availibility rang-available'})
description = soup.find_all('p')[0]

with open('book_library/books13.json', 'w', encoding="utf-8") as file:
    file.write(f" Название книги: {str(book_name)}")
    lines = ["\n"]
    file.writelines(lines)
    file.write(f" Описание: {str(description)}") 
    lines = ["\n"]
    file.writelines(lines)
    file.write(f" Наличие: {str(availability)}") 
    lines = ["\n"]


#print(book_name)                                              # Оставил на время
#print(description)                                            # Оставил на время
#print(availability)                                           # Оставил на время


url14 = 'https://www.labirint.ru/books/853036/'
HEADERS = ({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.0.2530 Yowser/2.5 Safari/537.36', 
            'Accept-Language': 'ru-RU, en;q=0.5'})
response = requests.get(url14, headers= HEADERS)

soup = BeautifulSoup(response.text, "html.parser")
#with open('output1.html', 'w', encoding="utf-8") as file:    # До востребования
    #file.write(str(soup))                                    # До востребования

book_name = soup.find_all('h1')[0]
availability = soup.find_all('div', attrs={'class':'prodtitle-availibility rang-available'})
description = soup.find_all('p')[0]

with open('book_library/books14.json', 'w', encoding="utf-8") as file:
    file.write(f" Название книги: {str(book_name)}")
    lines = ["\n"]
    file.writelines(lines)
    file.write(f" Описание: {str(description)}") 
    lines = ["\n"]
    file.writelines(lines)
    file.write(f" Наличие: {str(availability)}") 
    lines = ["\n"]
 

#print(book_name)                                              # Оставил на время
#print(description)                                            # Оставил на время
#print(availability)                                           # Оставил на время


url15 = 'https://www.labirint.ru/books/818401/'
HEADERS = ({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.0.2530 Yowser/2.5 Safari/537.36', 
            'Accept-Language': 'ru-RU, en;q=0.5'})
response = requests.get(url15, headers= HEADERS)

soup = BeautifulSoup(response.text, "html.parser")
#with open('output1.html', 'w', encoding="utf-8") as file:    # До востребования
    #file.write(str(soup))                                    # До востребования

book_name = soup.find_all('h1')[0]
availability = soup.find_all('div', attrs={'class':'prodtitle-availibility rang-available'})
description = soup.find_all('p')[0]

with open('book_library/books15.json', 'w', encoding="utf-8") as file:
    file.write(f" Название книги: {str(book_name)}")
    lines = ["\n"]
    file.writelines(lines)
    file.write(f" Описание: {str(description)}") 
    lines = ["\n"]
    file.writelines(lines)
    file.write(f" Наличие: {str(availability)}") 
    lines = ["\n"]


#print(book_name)                                              # Оставил на время
#print(description)                                            # Оставил на время
#print(availability)                                           # Оставил на время


url16 = 'https://www.labirint.ru/books/818401/'
HEADERS = ({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.0.2530 Yowser/2.5 Safari/537.36', 
            'Accept-Language': 'ru-RU, en;q=0.5'})
response = requests.get(url16, headers= HEADERS)

soup = BeautifulSoup(response.text, "html.parser")
#with open('output1.html', 'w', encoding="utf-8") as file:    # До востребования
    #file.write(str(soup))                                    # До востребования

book_name = soup.find_all('h1')[0]
availability = soup.find_all('div', attrs={'class':'prodtitle-availibility rang-available'})
description = soup.find_all('p')[0]

with open('book_library/books16.json', 'w', encoding="utf-8") as file:
    file.write(f" Название книги: {str(book_name)}")
    lines = ["\n"]
    file.writelines(lines)
    file.write(f" Описание: {str(description)}") 
    lines = ["\n"]
    file.writelines(lines)
    file.write(f" Наличие: {str(availability)}") 
    lines = ["\n"]


#print(book_name)                                              # Оставил на время
#print(description)                                            # Оставил на время
#print(availability)                                           # Оставил на время


url17 = 'https://www.labirint.ru/books/804737/'
HEADERS = ({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.0.2530 Yowser/2.5 Safari/537.36', 
            'Accept-Language': 'ru-RU, en;q=0.5'})
response = requests.get(url17, headers= HEADERS)

soup = BeautifulSoup(response.text, "html.parser")
#with open('output1.html', 'w', encoding="utf-8") as file:    # До востребования
    #file.write(str(soup))                                    # До востребования

book_name = soup.find_all('h1')[0]
availability = soup.find_all('div', attrs={'class':'prodtitle-availibility rang-available'})
description = soup.find_all('p')[0]

with open('book_library/books17.json', 'w', encoding="utf-8") as file:
    file.write(f" Название книги: {str(book_name)}")
    lines = ["\n"]
    file.writelines(lines)
    file.write(f" Описание: {str(description)}") 
    lines = ["\n"]
    file.writelines(lines)
    file.write(f" Наличие: {str(availability)}") 
    lines = ["\n"]


#print(book_name)                                              # Оставил на время
#print(description)                                            # Оставил на время
#print(availability)                                           # Оставил на время


url18 = 'https://www.labirint.ru/books/834362/'
HEADERS = ({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.0.2530 Yowser/2.5 Safari/537.36', 
            'Accept-Language': 'ru-RU, en;q=0.5'})
response = requests.get(url18, headers= HEADERS)

soup = BeautifulSoup(response.text, "html.parser")
#with open('output1.html', 'w', encoding="utf-8") as file:    # До востребования
    #file.write(str(soup))                                    # До востребования

book_name = soup.find_all('h1')[0]
availability = soup.find_all('div', attrs={'class':'prodtitle-availibility rang-available'})
description = soup.find_all('p')[0]

with open('book_library/books18.json', 'w', encoding="utf-8") as file:
    file.write(f" Название книги: {str(book_name)}")
    lines = ["\n"]
    file.writelines(lines)
    file.write(f" Описание: {str(description)}") 
    lines = ["\n"]
    file.writelines(lines)
    file.write(f" Наличие: {str(availability)}") 
    lines = ["\n"]


#print(book_name)                                              # Оставил на время
#print(description)                                            # Оставил на время
#print(availability)                                           # Оставил на время


url19 = 'https://www.labirint.ru/books/950895/'
HEADERS = ({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.0.2530 Yowser/2.5 Safari/537.36', 
            'Accept-Language': 'ru-RU, en;q=0.5'})
response = requests.get(url19, headers= HEADERS)

soup = BeautifulSoup(response.text, "html.parser")
#with open('output1.html', 'w', encoding="utf-8") as file:    # До востребования
    #file.write(str(soup))                                    # До востребования

book_name = soup.find_all('h1')[0]
availability = soup.find_all('div', attrs={'class':'prodtitle-availibility rang-available'})
description = soup.find_all('p')[0]

with open('book_library/books19.json', 'w', encoding="utf-8") as file:
    file.write(f" Название книги: {str(book_name)}")
    lines = ["\n"]
    file.writelines(lines)
    file.write(f" Описание: {str(description)}") 
    lines = ["\n"]
    file.writelines(lines)
    file.write(f" Наличие: {str(availability)}") 
    lines = ["\n"]


#print(book_name)                                              # Оставил на время
#print(description)                                            # Оставил на время
#print(availability)                                           # Оставил на время


url20 = 'https://www.labirint.ru/books/789634/'
HEADERS = ({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.0.2530 Yowser/2.5 Safari/537.36', 
            'Accept-Language': 'ru-RU, en;q=0.5'})
response = requests.get(url20, headers= HEADERS)

soup = BeautifulSoup(response.text, "html.parser")
#with open('output1.html', 'w', encoding="utf-8") as file:    # До востребования
    #file.write(str(soup))                                    # До востребования

book_name = soup.find_all('h1')[0]
availability = soup.find_all('div', attrs={'class':'prodtitle-availibility rang-available'})
description = soup.find_all('p')[0]

with open('book_library/books20.json', 'w', encoding="utf-8") as file:
    file.write(f" Название книги: {str(book_name)}")
    lines = ["\n"]
    file.writelines(lines)
    file.write(f" Описание: {str(description)}") 
    lines = ["\n"]
    file.writelines(lines)
    file.write(f" Наличие: {str(availability)}") 
    lines = ["\n"]


#print(book_name)                                              # Оставил на время
#print(description)                                            # Оставил на время
#print(availability)                                           # Оставил на время
