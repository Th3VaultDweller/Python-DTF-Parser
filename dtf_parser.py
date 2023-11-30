import requests
from bs4 import BeautifulSoup

# запрос GET на получение html-кода страницы
html = requests.get("https://dtf.ru/").text

soup = BeautifulSoup(html, "lxml")  # lxml - самый быстрый парсер

# запрос GET на получение всех ссылок на посты
links = soup.find_all("a", class_="content-link")

# вывод названия поста и url-ссылки
for i, link in enumerate(links):
    name = soup.find(class_="content-container").find_next().text  # название ссылки

    # article_annotation = (
    #     soup.find("div", class_="content-container").find("l-island-a").find_all("p")
    # )

    post_viewers_count = link.find_all(
        "div", class_="post-counters__item"
    )  # кол-во просмотров поста

    likes_count = link.find_all(
        "button", class_="like-button like-button--default like-button--action-like"
    )  # кол-во лайков поста

    url_text = link.text
    url = link.get("href")  # ссылка

    print(f"\n")  # отступ
    print(i)
    print(f"Name: {name}")
    # print(f"Article annotation: {article_annotation}")
    print(f"Number of views: {post_viewers_count}")
    print(f"Number of likes: {likes_count}")
    print(f"URL: {url}")
