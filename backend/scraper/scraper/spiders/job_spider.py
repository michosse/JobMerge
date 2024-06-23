import scrapy
from scraper.scraper.items import JobOfferItem
from itemloaders.processors import TakeFirst, Identity, MapCompose
from scraper.scraper.loaders import OfferLoader
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class JobsSpider(scrapy.Spider):
    name = "jobs"

    def start_requests(self):
        start_urls = [
            "https://it.pracuj.pl/praca/gdansk;wp?rd=30&et=1%2C3",
            "https://justjoin.it/trojmiasto/javascript/experience-level_junior",
            "https://justjoin.it/trojmiasto/python/experience-level_junior",
            "https://justjoin.it/trojmiasto/java/experience-level_junior",
            "https://justjoin.it/trojmiasto/net/experience-level_junior",
            "https://justjoin.it/trojmiasto/data/experience-level_junior"
        ]
        for url in start_urls:
            if "justjoin" in url:
                yield SeleniumRequest(url=url, callback=self.parse, wait_time=5, wait_until=EC.presence_of_element_located((By.CSS_SELECTOR,"div.css-1e6xvi3")))
            else:
                yield SeleniumRequest(url=url, callback=self.parse, wait_time=5)


    
    def parse(self, response):
        if 'pracuj.pl' in response.url:
            return self.parse_pracuj(response)
        elif 'justjoin.it' in response.url:
            return self.parse_jjit(response)
    
    def parse_pracuj(self, response):
        for offer in response.css("div.tiles_cd6yyvq"):
            l = OfferLoader(item=JobOfferItem(), selector=offer, response=response)
            l.add_css("title", "a.tiles_o1tnn5os.core_n194fgoq::text")
            l.add_css("company", "h3.tiles_c1rl4c7t.size-caption.core_t1rst47b::text")
            l.add_css("image", "img.core_ia9ocxs::attr(src)")
            l.add_css("tags", "span.tiles_t1eqoqxi::text")
            l.add_css("link", "a.tiles_o1tnn5os.core_n194fgoq::attr(href)")
            yield l.load_item()
    
    def parse_jjit(self, response):
        for offer in response.css("div[data-test-id='virtuoso-item-list'] > div:not([class])"):
            l = OfferLoader(item=JobOfferItem(), selector=offer, response=response)
            l.add_css("title", "h3.css-1gehlh0::text")
            l.add_css("company", "div.css-1mx97sn span::text")
            l.add_css("image", "div.css-5sbskc img::attr(src)")
            l.add_css("tags", "div.css-vzlxkq div.css-1qruno6::text")
            l.add_css("link", "a.offer_list_offer_link.css-3qyn8a::attr(href)", MapCompose(lambda x: f"https://justjoin.it{x}"))
            yield l.load_item()