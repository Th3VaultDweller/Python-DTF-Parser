import requests
from bs4 import BeautifulSoup

# запрос GET на получение html-кода страницы
html = requests.get("https://dtf.ru/").text

soup = BeautifulSoup(html, "lxml")

# запрос GET на получение всех ссылок на книги
links = soup.find_all("a", class_="content-link")

# вывод названия книги и url-ссылки
for i, link in enumerate(links):
    # name = link.text()  # название ссылки
    url = link.get("href")  # ссылка
    post_viewers_count = link.find_all(
        "span", class_="post-counters__item"
    )  # кол-во просмотров поста
    likes_count = link.find_all(
        "span", class_="like-button__count"
    )  # кол-во лайков поста

    print(i)
    # print(f"Name: {name}")
    print(f"URL: {url}")
    print(f"Number of views: {post_viewers_count}")
    print(f"Number of likes: {likes_count}")
