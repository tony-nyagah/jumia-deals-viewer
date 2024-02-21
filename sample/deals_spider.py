import scrapy
from jumiaDealScraper.jumiaDealScraper.items import JumiadealscraperItem
from scrapy.http import HtmlResponse


class DealsSpider(scrapy.Spider):
    name = "deals"
    #  loop through the pages
    start_urls = [
        f"https://www.jumia.co.ke/catalog/?page={page_number}#catalog-listing"
        for page_number in range(1, 50)
    ]

    def parse(self, response: HtmlResponse):
        for product in response.css("article.prd._fb.col.c-prd"):
            # only get products with an old price listed since those are the ones with ongoing deals
            if product.css("div.info > div.s-prc-w > div.old::text"):
                product_details = JumiadealscraperItem(
                    product_name=product.css("div.info > h3::text").get(),
                    product_price=product.css("div.info > div.prc::text").get(),
                    product_image=product.css("div.img-c > img.img::attr(src)").get(),
                    old_price=product.css(
                        "div.info > div.s-prc-w > div.old::text"
                    ).get(),
                    product_link=f"https://www.jumia.co.ke{product.css('a.core::attr(href)').get()}",
                )
                yield product_details
