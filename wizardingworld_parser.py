import requests
from bs4 import BeautifulSoup

# запрос GET на получение html-кода страницы
html = requests.get("https://www.wizardingworld.com/discover/books").text

soup = BeautifulSoup(html, "lxml")

# запрос GET на получение всех ссылок на книги
links = soup.find_all("a", class_="ProductCard_link__z-ZoA")

# вывод названия книги и url-ссылки
for i, link in enumerate(links):
    url = link.get("href")  # ссылка
    name = link.text()  # название ссылки
    print(i)
    print(f"Name: {name}")
    print(f"URL: {url}")
