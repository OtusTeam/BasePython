import requests
from bs4 import BeautifulSoup


URL_TO_PARSE = "https://otus.ru/nest/post/703/"


response = requests.get(URL_TO_PARSE)

soup = BeautifulSoup(response.text, "html.parser")

print(soup.title)
print(soup.title.text)

print(soup.h1)
print(soup.h1.text)
print(soup.h1["class"])

h1s = soup.find_all("h1")
print(h1s)

h2s = soup.find_all("h2")
print(h2s)

h1s_and_h2s = soup.find_all(["h1", "h2"])
print(h1s_and_h2s)

tiles = soup.select("div.blog__tile")
for i, tile in enumerate(tiles, start=1):
    print(i)
    # print(tile)
    print(tile.text)

author_block = soup.select_one("#author_block")
print(author_block)

author_name = author_block.select_one(".post-info__author")
print(author_name.text)

posts_links = soup.find_all("a", attrs={"class": "blog-tile__item-title"})
for post_link in posts_links:
    print(post_link.text.strip(), post_link.get("href"))

SIMILAR_POSTS_SELECTOR = "body > div.body-wrapper > div > div.blog.js-blog > div.blog__content > div > div > div.container__col.container__col_8.container__col_md-12 > div.blog-tile-wrapper"

print(soup.select_one(SIMILAR_POSTS_SELECTOR))

SIMILAR_POSTS_HEADER_SELECTOR = "body > div.body-wrapper > div > div.blog.js-blog > div.blog__content > div > div > div.container__col.container__col_8.container__col_md-12 > div.blog-tile-wrapper > div > div.blog-tile__item.blog-tile__item_no-padding-bottom.blog-tile__item_last > div"

similar_posts_header = soup.select_one(SIMILAR_POSTS_HEADER_SELECTOR)

print(similar_posts_header.text)
print(similar_posts_header.parent)
print(similar_posts_header.parent.parent)

similar_posts_links = similar_posts_header.parent.parent.find_all("a", attrs={"class": "blog-tile__item-title"})
for link in similar_posts_links:
    print(link["title"], link["href"])
