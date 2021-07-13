from pprint import pprint

import requests
from bs4 import BeautifulSoup

URL_TO_PARSE = "https://otus.ru/nest/post/703/"

response = requests.get(URL_TO_PARSE)

soup = BeautifulSoup(response.text, "html.parser")

print("soup.title")
print(soup.title)

print("soup.title.text")
print(soup.title.text)

print("soup.h1")
print(soup.h1)

print("soup.h1.text")
print(soup.h1.text)

print('soup.h1["class"]')
print(soup.h1["class"])


h1s = soup.find_all("h1")
print("h1s", h1s)


h2s = soup.find_all("h2")
pprint("h2s")
pprint(h2s)


h1s_and_h2s = soup.find_all(["h1", "h2"])
pprint("h1s_and_h2s")
pprint(h1s_and_h2s)

tile = soup.select_one("div.blog__tile")
print("tile:", tile)
print("tile.text:", tile.text)


author_block = soup.select_one("#author_block")
print("author_block")
print(author_block)

author_name = author_block.select_one(".post-info__author")

print("Author:", author_name.text)


def print_posts_links(sp):
    posts_links = sp.find_all("a", {"class": "blog-tile__item-title"})
    print("posts links")
    for post_link in posts_links:
        print(post_link.text.strip(), post_link.get("href"))


SIMILAR_POSTS_SELECTOR = (
    "body > div.body-wrapper > div > div.blog.js-blog "
    "> div.blog__content > div > div "
    "> div.container__col.container__col_8.container__col_md-12 "
    "> div.blog-tile-wrapper"
)

similar_posts_block = soup.select_one(SIMILAR_POSTS_SELECTOR)

print(similar_posts_block)
print_posts_links(similar_posts_block)

SIMILAR_POSTS_HEADER_SELECTOR = (
    "body > div.body-wrapper > div > div.blog.js-blog "
    "> div.blog__content > div > div "
    "> div.container__col.container__col_8.container__col_md-12 "
    "> div.blog-tile-wrapper "
    "> div "
    "> div.blog-tile__item.blog-tile__item_no-padding-bottom.blog-tile__item_last "
    "> div"
)

similar_posts_header = soup.select_one(SIMILAR_POSTS_HEADER_SELECTOR)
print("similar_posts_block.parent.parent links:")
print_posts_links(similar_posts_block.parent)


print("similar_posts_block.parent")
print(similar_posts_block.parent)
