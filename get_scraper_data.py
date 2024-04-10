from scrapy.crawler import CrawlerProcess

from jumiaScraper.spiders.deals_spider import DealsSpider


def run_spider():
    process = CrawlerProcess()
    process.crawl(DealsSpider)
    process.start()


if __name__ == "__main__":
    run_spider()
