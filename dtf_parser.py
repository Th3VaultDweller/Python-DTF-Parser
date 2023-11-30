import requests
from bs4 import BeautifulSoup

# запрос GET на получение html-кода страницы
html = requests.get("https://dtf.ru/").text

soup = BeautifulSoup(html, "lxml")

# запрос GET на получение всех ссылок на посты
links = soup.find_all("a", class_="content-link")

# вывод названия поста и url-ссылки
for i, link in enumerate(links):
    # name = link.text()  # название ссылки
    url = link.get("href")  # ссылка
    post_viewers_count = link.find_all(
        "div", class_="post-counters__item"
    )  # кол-во просмотров поста
    likes_count = link.find_all(
        "button", class_="like-button like-button--default like-button--action-like"
    )  # кол-во лайков поста

    print(i)
    # print(f"Name: {name}")
    print(f"URL: {url}")
    print(f"Number of views: {post_viewers_count}")
    print(f"Number of likes: {likes_count}")
