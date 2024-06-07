# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import psycopg2
from scraper.scraper.items import JobOfferItem


class SaveToPostpresPipeline(object):
    def __init__(self) -> None:
      self.create_connection()
    

    def create_connection(self):
        self.connection = psycopg2.connect(
            host = 'localhost',
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

    def process_item(self, item, spider):
       self.store_db(item)
       return item
    
    def store_db(self, item: JobOfferItem):
        try:
          self.cur.execute(""" insert into offer (link, title, company, image, tags) values (%s, %s, %s, %s, %s) ON CONFLICT DO NOTHING""",(
                        item.link,
                        item.title,
                        item.company,
                        item.image,
                        item.tags
                        )
                        )
        except Exception as e:
            print(e)
        self.connection.commit()