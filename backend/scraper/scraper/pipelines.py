# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import os
import re
import psycopg2
from scraper.scraper.items import JobOfferItem

HOST = os.getenv('DATABASE_HOST','localhost')
class SaveToPostpresPipeline(object):
    def __init__(self) -> None:
      self.create_connection()
    

    def create_connection(self):
        self.connection = psycopg2.connect(
            host = HOST,
            user = 'postgres',
            password = 'admin',
            database = 'jobs',
            port = '5432'
        )
        self.cur = self.connection.cursor()
        self.cur.execute("""CREATE TABLE IF NOT EXISTS offer(
                         link varchar,
                         title varchar,
                         company varchar,
                         image varchar,
                         tags varchar[],
                         PRIMARY KEY (title, company)
        )""")
        self.cur.execute("""TRUNCATE TABLE offer;""")

    def process_item(self, item, spider):
       self.store_db(item)
       return item
    
    def store_db(self, item: JobOfferItem):
        try:
          image = f"https{item.image.split('https')[-1]}"
          self.cur.execute(""" insert into offer (link, title, company, image, tags) values (%s, %s, %s, %s, %s) ON CONFLICT DO NOTHING""",(
                        item.link,
                        item.title,
                        item.company,
                        image,
                        item.tags
                        )
                        )
        except Exception as e:
            print(e)
        self.connection.commit()