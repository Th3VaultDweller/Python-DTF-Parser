import requests
from bs4 import BeautifulSoup

# запрос GET на получение html-кода страницы
html = requests.get(
    "https://dtf.ru/games/2311710-dlya-baldur-s-gate-3-vyshel-ogromnyy-pyatyy-patch-v-nem-dobavili-igrabelnyy-epilog-s-3589-strokami-dialogov"
).text

soup = BeautifulSoup(html, "lxml")  # lxml - самый быстрый парсер

# находим все URL-ссылки на странице
links = soup.find_all("a", href=True)

# вывод всех URL-ссылок со страницы
for i, link in enumerate(links):
    url = link.get("href")

    print(f"\n")
    print(i)
    print(f"URL: {url}")
