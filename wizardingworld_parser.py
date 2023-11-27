import requests
from LxmlSoup import LxmlSoup

# запрос GET на получение html-кода страницы
html = requests.get("https://www.wizardingworld.com/discover/books").text

soup = LxmlSoup(html)

# запрос GET на получение всех ссылок на книги
links = soup.find_all("a", class_="ProductCard_link__z-ZoA")

# вывод названия книги и url-адреса
for i, link in enumerate(links):
    url = link.get("href")
    name = link.text()
    # annotation = soup.find_all('section', class_='ArticleGambit_gambit__1w6yf ArticleGambit_default__3mOC- ArticleGambit_left__qElyK')[i].text()
    print(i)
    print(f"Name: {name}")
    # print(f'Annotation: {annotation}')
    print(f"URL: {url}")
