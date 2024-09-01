# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class DealScraperPipeline:
    def __init__(self):
        # create/connect to a database
        self.connection = sqlite3.connect("deals.db")

        # create cursor, used to execute commands
        self.cursor = self.connection.cursor()

        # create quotes table if none exists
        self.cursor.execute(
            """
        CREATE TABLE IF NOT EXISTS deals(
            product_name TEXT,
            product_price TEXT,
            product_image TEXT,
            old_price TEXT,
            product_link TEXT        
        )
        """
        )

    def process_item(self, item, spider):

        # check to see if item  is already in the db
        self.cursor.execute(
            "SELECT * FROM deals WHERE product_link = ?", (item["product_link"],)
        )
        result = self.cursor.fetchone()

        # if it is in the db, create a log message
        if result:
            spider.logger.warn(f"Product already in database: {item['product_link']}")
        else:
            # define insert statement
            self.cursor.execute(
                """INSERT INTO deals (product_name, product_price, product_image, old_price, product_link) VALUES (?, ?, ?, ?, ?)""",
                (
                    item["product_name"],
                    item["product_price"],
                    item["product_image"],
                    item["old_price"],
                    item["product_link"],
                ),
            )
            # insert data into the database
            self.connection.commit()

        return item
