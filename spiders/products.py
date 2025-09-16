import scrapy


class ProductsSpider(scrapy.Spider):
    name = "products"
    start_urls = ["https://books.toscrape.com/"]

    def parse(self, response):
        for product in response.css("article.product_pod"):
            yield {
                "title": product.css("h3 a::attr(title)").get(),
                "link": response.urljoin(product.css("h3 a::attr(href)").get()),
                "price": product.css("div.product_price p.price_color::text").get(),

            }

        next_page = response.css("li.next a::attr(href)").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
