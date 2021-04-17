import scrapy
from scrapy.http.response import Response


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        "https://quotes.toscrape.com/page/1/",
        # "https://quotes.toscrape.com/page/2/",
        # "https://quotes.toscrape.com/page/3/",
    ]

    def parse(self, response: Response, **kwargs):
        page = response.url.split("/")[-2]
        print("quotes page", page, response.css("title::text").get())

        for quote in response.css("div.quote"):
            text = quote.css("span.text::text").get()
            author = quote.css("small.author::text").get()
            tags = quote.css("div.tags a.tag::text").getall()
            print("text by", author, text, "tags:", tags)

            yield {
                "text": text,
                "author": author,
                "tags": tags,
            }

        for next_page in response.css('li.next a'):
            yield response.follow(next_page, self.parse)
