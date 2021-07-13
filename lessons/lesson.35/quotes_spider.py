import scrapy
from scrapy.http import Response


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        "https://quotes.toscrape.com/page/1/",
        # "https://quotes.toscrape.com/page/2/",
    ]

    def parse(self, response: Response, **kwargs):
        # print("process response", response, "with kwargs", kwargs)
        page = response.url.split("/")[-2]
        page_title = response.css("title::text").get()
        print("process page", page, "title", page_title)

        quotes = response.css("div.quote")
        for quote in quotes:
            text = quote.css("span.text::text").get()
            author = quote.css("small.author::text").get()
            tags = quote.css("div.tags a.tag::text").getall()
            print("text by", author, "with tags", tags)

            yield {
                "text": text,
                "author": author,
                "tags": tags,
            }

        for next_page in response.css("li.next a"):
            yield response.follow(next_page, self.parse)
