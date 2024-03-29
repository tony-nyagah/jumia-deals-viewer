from jumiaDealScraper.jumiaDealScraper.spiders.deals_spider import DealsSpider
from scrapy.crawler import CrawlerProcess


def run_spider_and_export_json():
    process = CrawlerProcess(
        settings={
            "FEEDS": {"deals.jsonl": {"format": "jsonlines", "overwrite": True}},
        }
    )
    process.crawl(DealsSpider)
    process.start()


if __name__ == "__main__":
    run_spider_and_export_json()
