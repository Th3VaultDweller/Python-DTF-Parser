import requests
from bs4 import BeautifulSoup

# запрос GET на получение html-кода страницы
html = requests.get(
    "https://dtf.ru/games/2311710-dlya-baldur-s-gate-3-vyshel-ogromnyy-pyatyy-patch-v-nem-dobavili-igrabelnyy-epilog-s-3589-strokami-dialogov"
).text

soup = BeautifulSoup(html, "lxml")  # lxml - самый быстрый парсер

# находим название статьи и аннотацию
article_title = soup.title
article_annotation = soup.find("div", class_="content content--full").find("p").text
print(article_title.text)
print(article_annotation)

print(f"\n")

# находим кол-во комментариев, показов и открытий статьи
views_and_opens = soup.find(class_="post-counters")  # показы и открытия
print(views_and_opens.text.strip())
# сomments_count = soup.find(class_="content-info content-info--full l-island-a")
# print(сomments_count.text.strip())

# находим все URL-ссылки на странице
links = soup.find_all("a", href=True)

# вывод всех URL-ссылок со страницы и их названий
for i, link in enumerate(links):
    link_text = link.text  # название ссылки
    url = link.get("href")  # ссылка

    print(f"\n")
    print(i)
    print(f"{link_text.strip()}: {url}")

# находим все картинки на странице
all_img = soup.find_all("img")
print(all_img)

# вывод всех источников картинок со страницы
for i, image in enumerate(all_img):
    img_src = image.get("data-image-src")
    print(f"\n")
    print(i)
    print(f"Image source: {img_src}")
