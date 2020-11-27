"""
scrapy runspider myspider.py
scrapy runspider myspider.py -O quotes.jl
scrapy runspider myspider.py -o quotes.jl
"""

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
        # 'http://quotes.toscrape.com/page/3/',
        # 'http://quotes.toscrape.com/page/4/',
    ]

    def parse(self, response, **kwargs):
        page = response.url.split("/")[-2]
        print(page, response.css("title::text").getall())

        for quote in response.css("div.quote"):
            text = quote.css("span.text::text").get()
            author = quote.css("small.author::text").get()
            # print("- text by", author, text)
            yield {
                "text": text,
                "author": author,
                "tags": quote.css("div.tags a.tag::text").getall(),
            }
